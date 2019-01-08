from whichbins.schedule import Schedule

def test_schedule_has_collections():
    schedule = Schedule()
    assert len(schedule.schedule.items()) == 0

def test_schedule_can_be_queried_by_date():
    schedule = Schedule()
    assert schedule.onDate('2019-01-01') == None

def test_schedule_can_have_entries_added():
    schedule = Schedule()
    schedule.add('2019-01-01', { "black": True, "green": True })
    expectedCollection = { 
        "black": True, 
        "green": True, 
        "brown": False, 
        "blue": False 
    }
    assert schedule.onDate('2019-01-01') == expectedCollection
    assert len(schedule.schedule.items()) == 1
