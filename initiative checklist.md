# Initiative Tracker Implementation Checklist

## Phase 1: Data Model & Persistence

### Step 1: Create Encounter ORM Model
- [ ] Open `systems/initiative_backend.py`
- [ ] Import `Base` from `systems/players_backend.py`
- [ ] Import `Column`, `Integer`, `String`, `DateTime`, `relationship` from sqlalchemy
- [ ] Create `Encounter` class inheriting from `Base`
- [ ] Add `__tablename__ = "encounters"`
- [ ] Add `id` column (Integer, Primary Key)
- [ ] Add `user_id` column (String, NOT NULL) - match type used in Player model
- [ ] Add `name` column (String, NOT NULL)
- [ ] Add `last_updated` column (DateTime, defaults to current time, updates on change)
- [ ] Add `combatants` relationship: `relationship("Combatant", back_populates="encounter")`

### Step 2: Create Combatant ORM Model
- [ ] In `systems/initiative_backend.py`, create `Combatant` class inheriting from `Base`
- [ ] Add `__tablename__ = "combatants"`
- [ ] Add `id` column (Integer, Primary Key)
- [ ] Add `encounter_id` column (Integer, Foreign Key to encounters.id, NOT NULL)
- [ ] Add `name` column (String, NOT NULL)
- [ ] Add `is_player` column (Boolean, NOT NULL - tracks if player or creature)
- [ ] Add `player_id` column (Integer/UUID, nullable, Foreign Key to players.id)
- [ ] Add `creature_name` column (String, nullable - name of creature from JSON)
- [ ] Add `initiative` column (Integer, NOT NULL)
- [ ] Add `current_hp` column (Integer, NOT NULL)
- [ ] Add `max_hp` column (Integer, NOT NULL)
- [ ] Add `ac` column (Integer, NOT NULL)
- [ ] Add `speed` column (String, NOT NULL - e.g., "30 ft.")
- [ ] Add `status` column (JSON/array type, nullable - conditions like ["poisoned", "prone"])
- [ ] Add `encounter` relationship: `relationship("Encounter", back_populates="combatants")`

### Step 3: Set up SQLAlchemy Schema Creation
- [ ] In `streamlit_app.py`, import the engine from `systems/players_backend.py`
- [ ] Import `Base` from `systems/initiative_backend.py`
- [ ] Add call to `Base.metadata.create_all(engine)` at app startup (after Supabase connection)
- [ ] This will auto-create `encounters` and `combatants` tables in PostgreSQL

## Phase 2: Backend Logic (Core Mechanics)

### Step 4: Implement Initiative Backend Functions
- [ ] Open `systems/initiative_backend.py`
- [ ] Import `Session` from sqlalchemy.orm
- [ ] Import `random` (already imported)
- [ ] Implement `roll_initiative(dex_modifier: int) -> int`
  - [ ] Returns `random.randint(1, 20) + dex_modifier`
- [ ] Implement `create_encounter(session: Session, user_id: str, encounter_name: str) -> Encounter`
  - [ ] Create new Encounter row with user_id and name
  - [ ] Commit to DB
  - [ ] Return the encounter
- [ ] Implement `add_combatants_to_encounter(session: Session, encounter_id: int, combatants_list: List[dict], players_db: dict, creatures_json: dict) -> List[Combatant]`
  - [ ] Input format: `[{"type": "player", "player_id": 123}, {"type": "creature", "creature_name": "Goblin", "count": 3}]`
  - [ ] For each player in list: fetch from DB, get dex_mod, roll initiative, create Combatant row
  - [ ] For each creature in list: fetch from creatures_json, get dex_mod, roll initiative once per unique creature name, create Combatant rows
  - [ ] Commit all to DB
  - [ ] Return list of created Combatant objects
- [ ] Implement `get_encounter_with_sorted_combatants(session: Session, encounter_id: int) -> Encounter`
  - [ ] Query Encounter by ID
  - [ ] Fetch its combatants
  - [ ] Sort by initiative DESC
  - [ ] Return encounter with sorted combatants
- [ ] Implement `update_combatant_hp(session: Session, combatant_id: int, new_hp: int) -> Combatant`
  - [ ] Query Combatant by ID
  - [ ] Clamp new_hp to [0, max_hp]
  - [ ] Update current_hp
  - [ ] Commit
  - [ ] Return combatant
- [ ] Implement `update_combatant_status(session: Session, combatant_id: int, statuses: List[str]) -> Combatant`
  - [ ] Query Combatant by ID
  - [ ] Update status column with new statuses array (e.g., ["poisoned", "prone"])
  - [ ] Commit
  - [ ] Return combatant
- [ ] Implement `delete_encounter(session: Session, encounter_id: int) -> bool`
  - [ ] Query Encounter by ID
  - [ ] Delete all related Combatants
  - [ ] Delete Encounter
  - [ ] Commit
  - [ ] Return True on success

## Phase 3: UI Layer (Streamlit Page)

### Step 5: Redesign Initiative Page - Encounter Selection/Creation
- [ ] Open `pages/01initiative.py`
- [ ] Add section header "Encounter Management"
- [ ] Add dropdown to display all encounters for current user (fetch from DB using session.query)
- [ ] Add text input for new encounter name
- [ ] Add button "Create New Encounter" that calls create_encounter() and updates dropdown
- [ ] Add "Delete Current Encounter" button that removes selected encounter
- [ ] Store selected encounter ID in `st.session_state.selected_encounter_id`

### Step 6: Redesign Initiative Page - Add Combatants Section
- [ ] Add section header "Add Combatants to Encounter"
- [ ] Add multiselect for Players
  - [ ] Show list of current user's players from DB
  - [ ] Display format: "Character Name (Level X Class)"
  - [ ] Allow selecting multiple
  - [ ] Store in `st.session_state.selected_players`
- [ ] Add multiselect for Creatures
  - [ ] Load from creatures_json from session_state
  - [ ] Display format: "Creature Name (CR X)"
  - [ ] Allow selecting multiple (same creature can be selected twice for separate entries)
  - [ ] Store in `st.session_state.selected_creatures`
- [ ] Add button "Roll Initiative & Add to Encounter"
  - [ ] Calls `add_combatants_to_encounter()` with selected players + creatures
  - [ ] Clears multiselect selections after adding
  - [ ] Refreshes display

### Step 7: Redesign Initiative Page - Combat Display
- [ ] Add section header "Combat Order"
- [ ] Add turn tracker (simple text showing "Current Turn: [Name]")
- [ ] Add button "Advance Turn" to move to next combatant
- [ ] Create table/list of combatants sorted by initiative DESC with columns:
  - [ ] Initiative (number)
  - [ ] Name (player or creature name)
  - [ ] HP (current/max, with edit button or input field)
  - [ ] AC (display only)
  - [ ] Speed (display only)
  - [ ] Status (display conditions, with button to add/remove)
  - [ ] Delete button (remove from encounter)
- [ ] For each combatant row:
  - [ ] Add input field to edit HP (triggers `update_combatant_hp()` on change)
  - [ ] Add status chips/tags showing current conditions
  - [ ] Add button to add new status condition
  - [ ] Add button to remove individual status
  - [ ] Add delete button to remove combatant from encounter

### Step 8: Session State Management
- [ ] In `pages/01initiative.py`, ensure these session state keys are initialized:
  - [ ] `st.session_state.selected_encounter_id` — current encounter being edited
  - [ ] `st.session_state.selected_players` — multiselect values (cleared after adding)
  - [ ] `st.session_state.selected_creatures` — multiselect values (cleared after adding)
  - [ ] `st.session_state.current_turn_index` — track whose turn (initialize to 0)

## Phase 4: Integration & Polish

### Step 9: Load Creature Data at App Startup
- [ ] Open `streamlit_app.py`
- [ ] At the beginning of the app (after auth check), load creatures from `data/monsters.json`
- [ ] Store in `st.session_state.creatures` so it's available across all pages
- [ ] Pass creature dict to initiative page functions

### Step 10: Fix Existing Bug
- [ ] Open `systems/players_backend.py`
- [ ] Find Player model and locate int_mod and wis_mod columns
- [ ] Check if they reference the wrong ability scores (currently wis_mod references int, int_mod references wis)
- [ ] Swap the references to fix the bug

### Step 11: Add Data Validation
- [ ] In `systems/initiative_backend.py`, update `update_combatant_hp()` to clamp HP to [0, max_hp]
- [ ] In all backend functions that modify encounters, verify user_id ownership before allowing changes
- [ ] Add error handling for invalid encounter IDs or combatant IDs

### Step 12: End-to-End Testing
- [ ] Create new encounter
- [ ] Add 2 players + 1 creature
- [ ] Verify all 3 appear in sorted list by initiative DESC
- [ ] Edit HP on one combatant
- [ ] Reload page
- [ ] Verify HP change persisted to DB
- [ ] Add status "poisoned" to one combatant
- [ ] Reload page
- [ ] Verify status persisted
- [ ] Delete encounter
- [ ] Verify it no longer appears in dropdown
- [ ] Test with multiple identical creatures (e.g., 3x Goblins) to confirm they have same initiative

---

## Notes
- **Parallel work allowed**: Phase 2 and Phase 3 can be done in parallel
- **Database**: Tables auto-created by SQLAlchemy via `Base.metadata.create_all(engine)`
- **User isolation**: All functions filter by user_id to ensure multi-user safety
- **Tied initiatives**: Display order for tied initiatives (stable sort or alphabetical secondary sort) - clarify behavior during Step 7