import Attack

if __name__ == "__main__":

	#Various slashes.
	slashAttack = Attack.Slash()
	fireElementSlashAttack = Attack.FireElement(Attack.Slash())
	increasedDamageSlashAttack = Attack.IncreasedDamage(Attack.Slash())
	increasedDamageFireElementSlashAttack = Attack.IncreasedDamage(Attack.FireElement(Attack.Slash()))

	print(slashAttack.Attack())
	print(fireElementSlashAttack.Attack())
	print(increasedDamageSlashAttack.Attack())
	print(increasedDamageFireElementSlashAttack.Attack())

	#Various Spells.
	spellAttack = Attack.Spell()
	fireElementSpellAttack = Attack.FireElement(Attack.Spell())
	increasedDamageSpellAttack = Attack.IncreasedDamage(Attack.Spell())
	increasedDamageFireElementSpellAttack = Attack.IncreasedDamage(Attack.FireElement(Attack.Spell()))

	print(spellAttack.Attack())
	print(fireElementSpellAttack.Attack())
	print(increasedDamageSpellAttack.Attack())
	print(increasedDamageFireElementSpellAttack.Attack())