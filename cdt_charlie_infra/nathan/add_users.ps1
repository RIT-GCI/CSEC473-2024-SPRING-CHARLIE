# Username and Password
$username = "LazyUser"
$password = ConvertTo-SecureString "LazyAdminPwd123!" -AsPlainText -Force  # Super strong plane text password here (yes this isn't secure at all)

# Creating the user
New-LocalUser -Name "$username" -Password $password -FullName "$username" -Description "Lazy Test user"
