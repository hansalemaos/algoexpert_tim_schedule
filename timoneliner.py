import pandas as pd
cal1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
cal2 = [['10:00', '11:00'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
bound1 = [['8:00', '18:30']]
bound2 = [['10:00', '20:30']]
min_meeting_time = 30
result = (
[x[1].iloc[[0, -1]].drop(columns=['minabs', 'freetime']).reset_index(drop=True).rename(index={0: 'start', 1: 'end'})
 for x in pd.DataFrame(range(60 * 24)).apply(lambda x: divmod(x[0], 60), result_type='expand', axis=1).drop(
    [k for k in range(0, 60 * 24) if k not in list(set.union(*[set.union(*[set.union(*[set(list(
        range(*[sum([(z * 60) if ini == 0 else z for ini, z in enumerate((map(int, y.split(':'))))]) for y in x])))
        for x in cal]) for cal in [bound2]])]))] + [k for k in range(0, 60 * 24) if
                                                    k not in list(set.union(*[set.union(*[set.union(*[
                                                        set(list(range(*[sum([(z * 60) if ini == 0 else z for ini, z in
                                                                              enumerate((map(int, y.split(':'))))]) for
                                                                         y in x])))
                                                        for x in cal]) for cal in [bound1]])]))] + list(
        set.union(*list(((set.union(*[
            set(list(range(
                *[sum([(z * 60) if ini == 0 else z for ini, z in enumerate((map(int, y.split(':'))))]) for y in x])))
            for x in cal]) for cal in [cal1, cal2])))))).reset_index().rename(
    columns={0: 'hour', 1: 'min', 'index': 'minabs'})
     .assign(freetime=lambda x: x.minabs.diff().gt(min_meeting_time).cumsum() + min_meeting_time).groupby('freetime',
                                                                                                          as_index=False)
 if x[1].iloc[[0, -1]].minabs.diff().dropna().iloc[0] + 1 >= min_meeting_time])
for date in result:
    print(date)