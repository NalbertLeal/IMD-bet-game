all:
	@echo "Select a options: \n make install \n make run \n make clean"
install:
	@sudo apt-get install python-numpy
run:
	@python IMD_bet_game.py
clean:
	@rm output.csv
