import pandas as pandas

xl_file = "C:/Users/<username>/Downloads/LicenseLog.xlsx"
df = pd.read_excel(xl_file)
usernamelist = df['User ID'].tolist()
domain = @domain.com'
usernamelist = [id + domain for id in usernamelist]
print(*usernamelist, sep = '; ')
