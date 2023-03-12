import numpy

frontamplitude = 3
frontfrequency = 1
frontphaseOffset = 0

backamplitude = numpy.pi/10
backfrequency = 8
backphaseOffset = 0

steps = 1000
OldRange = (1 - -1)
NewRange = (numpy.pi/4 - -numpy.pi/4)
numberofGenerations = 10

populationSize = 2

numoflinks = 4

numSensorNeurons = numoflinks + 2
numMotorNeurons = numoflinks + 1
motorJointRange = .45

names = ["Aardvark", "Abacus", "Abbey", "Abdomen", "Abode", "Abolishment", "Abroad", "Abstinence", "Abstract", 
         "Abundance", "Acacia", "Academic", "Accelerant", "Accelerator", "Accent", "Acceptance", "Access", "Accessory", 
         "Accident", "Acclaim", "Accommodation", "Accompaniment", "Accord", "Account", "Accumulation", "Accuracy", "Accusation", 
         "Acetate", "Acid", "Acorn", "Acoustics", "Acquaintance", "Acquisition", "Acrobat", "Acrylic", "Act", "Action", "Activation", 
         "Activity", "Actor", "Actress", "Acute", "Ad", "Adage", "Adaptation", "Adapter", "Addiction", "Addition", "Address", "Adjective",
        "Adjustment", "Administration", "Administrator", "Admiral", "Admiration", "Admission", "Adobe", "Adolescence", "Adrenaline", "Adulation", 
        "Adult", "Adulthood", "Advance", "Advancement", "Advantage", "Advertisement", "Advertising", "Advice", "Advocate", "Affect", "Affidavit", 
        "Affinity", "Affirmation", "Affliction", "Affluence", "Affront", "Aftermath", "Afternoon", "Aftershock", "Afterthought", "Agate", "Age", "Agency",
          "Agenda", "Agent", "Agglomeration", "Aggression", "Aglet", "Agony", "Agreement", "Agriculture", "Aid", "Aide", "Aim", "Air", "Airbag", "Airbus", 
          "Airfare", "Airfield", "Airforce", "Airline", "Airmail", "Airplane", "Airport", "Airstrip", "Aisle", "Alarm", "Albatross", "Alchemy", "Alcohol", 
          "Alcove", "Ale", "Alert", "Algae", "Alien", "Allegation", "Allergist", "Alley", "Alligator", "Allocation", "Allowance", "Alloy", "Almanac", "Almond", 
          "Alpaca", "Alphabet", "Alpine", "Altar", "Alteration", "Alternate", "Alternative", "Altitude", "Alto", "Aluminium", "Aluminum", "Amalgam", "Amazement", 
          "Ambassador", "Ambiguity", "Ambition", "Ambulance", "Amendment", "Amenity", "Amethyst", "Amnesty", "Amount", "Amphibian", "Amplifier", "Amplitude", 
          "Amulet", "Amusement", "Anaconda", "Anaesthesia", "Anagram", "Analgesic", "Analog", "Analogue", "Analogy", "Analysis", "Analyst", "Anarchist", "Anatomy", 
          "Ancestor", "Ancestry", "Anchor", "Anecdote", "Angel", "Anger", "Angina", "Angle", "Angler", "Angling", "Angora", "Anguish", "Animal", "Animation", "Ankle", 
          "Anklet", "Anniversary", "Announcement", "Annoyance", "Annual","Baby", "Babysitter", "Back", "Backbone", "Background", "Backpack", "Bacon", "Bacteria", "Badge", "Badger", "Bag", "Bagel", "Baggage", "Bail",
           "Bait", "Bake", "Baker", "Bakery", "Balance", "Balcony", "Ball", "Ballet", "Balloon", "Ballot", "Bamboo", "Banana", "Band", "Bandage", "Bandana", 
           "Banjo", "Bank", "Banker", "Bankruptcy", "Banner", "Banquet", "Bar", "Barbecue", "Barber", "Barbershop", "Bargain", "Barge", "Barley", "Barn", "Barometer",
             "Barracks", "Barrel", "Barrier", "Base", "Baseball", "Basement", "Basil", "Basket", "Basketball", "Bass", "Bassinet", "Bastard", "Bat", "Bath", "Bather",
               "Bathrobe", "Bathroom", "Bathtub", "Battery", "Battle", "Battleship", "Bay", "Bayou", "Beach", "Bead", "Beak", "Beam", "Bean", "Bear", "Beard", 
               "Beast", "Beat", "Beater", "Beautician", "Beauty", "Beaver", "Bed", "Bedbug", "Bedroom", "Bee", "Beech", "Beef", "Beer", "Beet", "Beetle", "Beggar", 
               "Beginner", "Beginning", "Beheading", "Behest", "Behavior", "Beige", "Belief", "Bell", "Belt", "Bench", "Bend", "Benefactor", "Beneficiary", "Benefit", 
               "Beret", "Berry", "Bestseller", "Bet", "Beverage", "Bewilderment", "Bible", "Bicycle", "Bid", "Bidder", "Bidding", "Bifocals", "Bight", "Bike", 
               "Bikini", "Bill", "Billboard", "Billionaire", "Bin", "Binder", "Binding", "Binoculars", "Biochemistry", "Biology", "Biplane", "Bird", "Birth",
                 "Birthday", "Biscuit", "Bishop", "Bite", "Bitterness", "Black", "Blackberry", "Blackboard", "Blackout", "Bladder", "Blame", "Blank", "Blanket", 
                 "Blast", "Blazer", "Bleach", "Blemish", "Blend", "Blessing", "Blind", "Blister", "Blizzard", "Block", "Blockade", "Blonde", "Blood", "Bloom", 
                 "Blossom", "Blouse", "Blow", "Blowgun", "Blue", "Blueberry", "Bluff", "Blunder", "Blush", "Board", "Boat", "Bobbin", "Bobsled", "Body", "Bog", 
                 "Bogie", "Boil", "Boiler", "Bolt", "Bomb", "Bomber", "Bombing", "Bond", "Bonding", "Bondsman", "Bone", "Bongo", "Bonnet", "Bonus", "Book"]

names1 = ["Cab", "Cabaret", "Cabbage", "Cabin", "Cabinet", "Cable", "Caboose", "Cacao", "Cache", "Cackle", "Cactus", "Cadence", "Cadet", "Cafeteria", "Caffeine", 
          "Cage", "Cake", "Calamity", "Calcification", "Calculation", "Calculator", "Calendar", "Calf", "Caliber", "Calibre", "Calibration", "Calibre", "Calm", 
          "Calorie", "Camaraderie", "Camber", "Cameo", "Camera", "Camouflage", "Camp", "Campaign", "Camper", "Campus", "Can", "Canal", "Cancel", "Cancellation",
            "Cancer", "Candelabrum", "Candidacy", "Candidate", "Candle", "Candy", "Cane", "Cannon", "Canoe", "Canopy", "Cantaloupe", "Canvas", "Canyon", "Cap", 
            "Capability", "Capacity", "Cape", "Capital", "Capitalism", "Capitalist", "Capitol", "Capitulation", "Capon", "Cappuccino", "Caprice", "Capstan", 
            "Capsule", "Captain", "Caption", "Captivity", "Capture", "Car", "Carapace", "Caravan", "Carbon", "Carburetor", "Carcass", "Card", "Cardboard", 
            "Cardinal", "Cards", "Care", "Career", "Caregiver", "Caretaker", "Cargo", "Caribou", "Caricature", "Carnation", "Carnival", "Carnivore", "Carousel", 
            "Carouse", "Carp", "Carpenter", "Carpet", "Carport", "Carriage", "Carrier", "Carrot", "Cart", "Cartilage", "Cartographer", "Cartoon", "Cartoonist", 
            "Cartouche", "Cartridge", "Carve", "Cascade", "Case", "Casement", "Casework", "Cash", "Cashew", "Cashier", "Casino", "Casket", "Cassava", "Casserole", 
            "Cassette", "Cast", "Caste", "Castle", "Castor", "Castanet", "Castaway", "Caste", "Casualty", "Cat", "Cataclysm", "Catalogue", "Catalyst", "Catastrophe", 
            "Catch", "Catchment", "Catchphrase", "Catechism", "Category", "Caterpillar", "Cathedral", "Catholic", "Catsup", "Cattle", "Caucus", "Caution", 
            "Cave", "Caveman", "Cavity", "Cayenne", "Cayuse", "Ceasefire", "Cedar", "Ceiling", "Celebration", "Celebrity", "Celerity", "Celery", "Cell", "Cellar",
              "Cellist", "Cello", "Celsius", "Cement", "Cemetery", "Censor", "Censorship", "Census", "Cent", "Center", "Centimetre", "Central", "Centre", 
              "Centrifuge", "Century", "Cereal", "Certificate", "Certification", "Certainty", "Certification", "Cessation","Daffodil", "Dagger", "Daily", "Dairy", "Daisy", "Dale", "Damage", "Dame", "Dance", "Dancer", "Dandelion", "Danger", "Danish", "Dare", "Dark", "Darn",
          "Dart", "Dartboard", "Database", "Date", "Daughter", "Dawn", "Day", "Daybed", "Daybreak", "Daydream", "Daylight", "Days", "Daytime", "Dazzle", "Deacon",
            "Dead", "Deadline", "Deadlock", "Deaf", "Deal", "Dealer", "Dealing", "Dearest", "Death", "Debate", "Debris", "Debt", "Debtor", "Decade", "Decadence", 
            "Decay", "Deceit", "Deception", "December", "Decency", "Decibel", "Deciduous", "Decimal", "Decision", "Deck", "Declaration", "Decline", "Decor", 
            "Decoration", "Decoy", "Decrease", "Decryption", "Dedication", "Deduction", "Deed", "Deem", "Deep", "Deer", "Defeat", "Defendant", "Defense", "Deficiency",
              "Deficit", "Definition", "Deforestation", "Deformity", "Degree", "Dehydration", "Deity", "Delay", "Delegation", "Delicacy", "Delight", "Delinquent", 
              "Delirium", "Deliverance", "Delivery", "Delta", "Demand", "Demise", "Democracy", "Demolition", "Demon", "Demonstration", "Den", "Denial", "Dent", 
              "Dentist", "Deodorant", "Department", "Departure", "Dependency", "Dependent", "Depiction", "Deposition", "Depression", "Deprivation", "Depth", "Deputy",
                "Derailment", "Derby", "Deregulation", "Dereliction", "Derision", "Dermatitis", "Dermatologist", "Descent", "Description", "Desert", "Design", 
                "Designation", "Designer", "Desire", "Desk", "Desktop", "Despair", "Desperation", "Destination", "Destiny", "Destroyer", "Destruction", "Detail",
                  "Detection", "Detective", "Detention", "Detergent", "Determination", "Detour", "Detroit", "Development", "Deviation", "Device", "Devil", "Devotion",
                    "Dew", "Dexterity", "Diabetes", "Diagnosis", "Diagram", "Dial", "Dialect", "Dialogue", "Diameter", "Diamond", "Diaper", "Diaphragm", "Diary",
                      "Dice", "Dictator", "Dictatorship", "Dictionary", "Dictionnaire", "Didgeridoo", "Die", "Diesel", "Diet", "Difference", "Difficulty", 
                      "Diffraction", "Digestion", "Dignity", "Dilemma", "Dill", "Dime", "Dimension", "Dimple", "Diner", "Dinghy", "Dining", "Dinner", "Dinosaur", 
                      "Diploma", "Diplomacy", "Director", "Directory", "Dirge", "Dirt"]

names2 = ["Eager", "Eagle", "Ear", "Earache", "Eardrum", "Earlobe", "Early", "Earn", "Earnest", "Earring", "Earshot", "Earth", "Earthquake", "Ease", "Easel", "East",
           "Easter", "Easy", "Eat", "Eave", "Eavesdrop", "Ebb", "Ebonite", "Ebony", "Eccentric", "Echo", "Eclair", "Eclipse", "Economic", "Economist", "Ecosystem", 
           "Edge", "Edible", "Edict", "Edifice", "Edit", "Edition", "Editor", "Educate", "Education", "Educator", "Eel", "Eerie", "Effect", "Efficiency", "Effort",
             "Egg", "Egghead", "Ego", "Eject", "Ejection", "Elaborate", "Elapse", "Elastic", "Elbow", "Elder", "Elderly", "Elect", "Election", "Electric", 
             "Electrical", "Electrician", "Electrify", "Electrode", "Electron", "Electronic", "Electronics", "Elegance", "Elegant", "Element", "Elementary", 
             "Elephant", "Elevate", "Elevation", "Elevator", "Elf", "Eliminate", "Elite", "Elixir", "Elk", "Ellipse", "Ellipsis", "Elliptical", "Elm", "Elocution", 
             "Eloquence", "Else", "Elsewhere", "Elucidate", "Elude", "Elusive", "Emaciate", "Email", "Emanate", "Embalm", "Embargo", "Embark", "Embarrass", "Embassy", 
             "Embed", "Embellish", "Embezzle", "Emblazon", "Embody", "Emboss", "Embrace", "Embroider", "Embroil", "Emerald", "Emergency", "Emerge", "Emergence", 
             "Emigrate", "Emigration", "Eminent", "Emirate", "Emotion", "Emotional", "Empathize", "Emperor", "Emphasis", "Emphasize", "Empire", "Employ", "Employee",
               "Employer", "Empower", "Empress", "Empty", "Emulate", "Enable", "Enact", "Enamel", "Enamored", "Encapsulate", "Encase", "Enchant", "Encircle",
                 "Enclose", "Encode", "Encompass", "Encounter", "Encourage", "Encroach", "Encumber", "End", "Endanger", "Endear", "Endeavor", "Endemic", "Endless",
                 "Endorse", "Endow", "Endurance", "Endure", "Enemy", "Energy", "Enforce", "Engage", "Engender", "Engine", "Engineer", "England", "English", 
                 "Enhance", "Enjoy", "Enlarge", "Enlighten", "Enlist", "Enmity", "Enormous", "Enough", "Enquire", "Enrage", "Enrich", "Enroll", "Ensemble", "Ensure", 
                 "Entail", "Enter", "Enterprise", "Entertain", "Enthusiasm", "Entice", "Entire","Fabulous", "Facetious", "Facility", "Factor", "Factory", "Faculty", "Fade", "Faint", "Fair", "Fairground", "Fairway", "Fairy", "Faith", "Falcon",
          "Fall", "Fallacy", "Falling", "Fame", "Familiar", "Family", "Famine", "Fan", "Fanatic", "Fancy", "Fanfare", "Fang", "Fantasy", "Farce", "Fare",
            "Farewell", "Farm", "Farmer", "Farming", "Farmland", "Fascination", "Fashion", "Fast", "Fastener", "Fat", "Fatal", "Fate", "Father", "Fatigue",
              "Faucet", "Fault", "Favor", "Favorite", "Fawn", "Fax", "Fear", "Feast", "Feather", "Feature", "February", "Federal", "Fee", "Feeble", "Feed", 
              "Feedback", "Feel", "Feeling", "Fellow", "Felon", "Female", "Feminine", "Fence", "Fencing", "Fender", "Ferry", "Fertilizer", "Festival", "Fetch", 
              "Fever", "Few", "Fiance", "Fiancee", "Fibre", "Fiction", "Fiddle", "Field", "Fiend", "Fierce", "Fiesta", "Fifth", "Fifty", "Fig", "Fight", 
              "Figure", "Filing", "Fill", "Fillet", "Filling", "Film", "Filter", "Filtration", "Fin", "Final", "Finance", "Financial", "Financing", "Find", 
              "Finder", "Fine", "Finger", "Fingernail", "Finish", "Finite", "Fire", "Firearm", "Fireman", "Fireplace", "Firework", "Firm", "First", "Fish", 
              "Fisherman", "Fishing", "Fishmonger", "Fist", "Fit", "Fitness", "Five", "Fix", "Fixture", "Flag", "Flair", "Flake", "Flame", "Flank", "Flannel", 
              "Flap", "Flare", "Flash", "Flask", "Flat", "Flattery", "Flavor", "Flavour", "Fleck", "Fleece", "Flesh", "Flicker", "Flight", "Flint", "Flip", 
              "Flock", "Flood", "Floor", "Floppy", "Flora", "Flour", "Flow", "Flower", "Fluctuation", "Flue", "Fluent", "Fluid", "Fluke", "Flute", "Fly", "Flyer", 
              "Foal", "Foam", "Fob", "Focus", "Fodder", "Foe", "Fog", "Fold", "Folder", "Foliage", "Folk", "Follow", "Folly", "Fond", "Food", "Fool", "Foot", 
              "Football", "Footpath", "Footprint", "Footstep", "Foray", "Forbearance", "Forbid", "Force", "Forecast", "Forefather", "Forefinger", "Foreigner",
                "Foreman", "Forest", "Forgery", "Forgiveness", "Form", "Format", "Formation", "Formula", "Fort"]