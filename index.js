const R = require("ramda");

const data = require('./data.json');

const getPlayer = (name, data) => data.players.find(player => player.nickname == name);

// const calcAvgRoundsPlayers = players => {
//   R.sum(R.filter(player => player.stats.Rounds, players))/R.length(players);
// }

const x = R.sum(R.filter(player => player.stats.Rounds));

// // const getRating = data => {

// // }

people_online = [
  getPlayer("redrails", data),
  getPlayer("paintboy55", data),
  getPlayer("Lingy", data),
  getPlayer("G_Dez", data),
  getPlayer("j_dez", data),
  getPlayer("Das_Panda", data),
  getPlayer("PerfectMex", data),
  getPlayer("KingChico", data),
  getPlayer("ADAX_", data),
  getPlayer("ZeD4nnY", data)
]

console.log(x(people_online));


// ```
// [top_half, bottom_half] = order(avg_kills)[::num_players/2] minus 25% rounds played penalty
// for i in 4:
//   pick_random(top_half) to array Team_1
//   pick_random(bottom_half) to array Team_2
//   pick_random(top_half) to array Team_1
//   pick_random(top_half) to array Team_2

// random.randrange(1,2) from remaining_players and assign to Team_1
// assign last to Team_2
// ```