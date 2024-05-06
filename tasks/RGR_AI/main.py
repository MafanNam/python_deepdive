import pandas as pd


def reaction_type(group, atr):
    def _get_reaction_type(row):
        stress_levels = [row[atr] for _, row in group.iterrows()]
        if (abs(stress_levels[0] - stress_levels[1]) <= stress_levels[0] * 0.1 and
                abs(stress_levels[1] - stress_levels[2]) <= stress_levels[0] * 0.1):
            return 'Type 5'
        elif stress_levels[0] < stress_levels[1] and stress_levels[1] > stress_levels[2]:
            return 'Type 1'
        elif stress_levels[0] > stress_levels[1] and stress_levels[1] < stress_levels[2]:
            return 'Type 2'
        elif stress_levels[0] < stress_levels[1] < stress_levels[2]:
            return 'Type 3'
        elif stress_levels[0] > stress_levels[1] > stress_levels[2]:
            return 'Type 4'
        else:
            return 'Not Type'

    group['Reaction Type'] = group.apply(_get_reaction_type, axis=1)

    return group[['PATNAME', 'STRESS', atr, 'Reaction Type']]


file_path = 'Data.xlsx'
df = pd.read_excel(file_path)

grouped_df = df.groupby('PATNAME', sort=False)

df_with_reaction_types_attr1 = grouped_df.apply(reaction_type, atr="attr1")
df_with_reaction_types_attr3 = grouped_df.apply(reaction_type, atr="attr3")
df_with_reaction_types_attr9 = grouped_df.apply(reaction_type, atr="attr9")

new_file_path = 'Data1.xlsx'
with pd.ExcelWriter(new_file_path) as writer:
    df_with_reaction_types_attr1.to_excel(writer, sheet_name='attr1', index=False)
    df_with_reaction_types_attr3.to_excel(writer, sheet_name='attr3', index=False)
    df_with_reaction_types_attr9.to_excel(writer, sheet_name='attr9', index=False)

print("DataFrame з реакціями збережено в новий Excel-файл.")
