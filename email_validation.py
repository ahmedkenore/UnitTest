#Fonction qui permet de valider une adresse mail 
#   -Paramètre d'entrée : l'adresse à valider
#   -Donnée retour      : true si l'adresse mail est bien validée
def validate_email(address):
      if '@' not in address:
            return False
 
      parts = address.split('@')
      if len(parts) != 2:
            return False
 
      local = parts[0]
      domain_name_parts = parts[1].split(".")
      if len(domain_name_parts) != 2:
            return False
 
      hostname = domain_name_parts[0]
      domain = domain_name_parts[0]
 
      if len(local)<1 or len(hostname)<2 or len(domain)<2:
            return False
 
      if not (local.isalnum() and hostname.isalnum() and domain.isalnum()):
            return False
 
      return True
