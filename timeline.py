events = [("1914-06-28", "Assassination of Archduke Franz Ferdinand of Austria"),
          ("1914-07-28", "Austria-Hungary declares war on Serbia"),
          ("1914-08-04", "Germany declares war on Belgium"),
          ("1914-08-04", "Great Britain declares war on Germany"),
          ("1915-02-05", "Germany declares unrestricted submarine warfare"),
          ("1917-04-06", "United States declares war on Germany"),
          ("1918-11-11", "Armistice signed, ending World War 1")]

for event in events:
    date, description = event
    print(f"{date}: {description}")
