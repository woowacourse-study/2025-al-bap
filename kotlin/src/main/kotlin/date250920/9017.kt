package date250920

// 코스는 4 - 12
// 상위 4명 주자의 점수 합하여
// 한 팀에 6명
// 가장 낮은 점수를 얻은 팀 승리
// 동점인 경우는 다섯 번째 주자가 더 빨리 들어온 팀

fun main() {
    val times = readln().toInt()
    val answer = mutableListOf<Int>()

    for (i in 0 until times) {
        readln()
        answer.add(solve(readln().split(" ").map { it.toInt() }))
    }

    answer.forEach { println(it) }
}

fun solve(a: List<Int>): Int {
    val teams = a.toSet()
    var members = a.toMutableList()
    val scores = mutableListOf<Pair<Int, Int>>()
    val fifth: MutableMap<Int, Int> = mutableMapOf()

    teams.forEach { team ->
        if (members.count { it == team } != 6) {
            scores.add(team to Int.MAX_VALUE)
            members = members.filter { it != team }.toMutableList()
        }
    }

    teams.forEach { team ->
        if (members.contains(team)) {
            var score = 0
            var prev = -1
            var count = 0
            for (i in 0 until members.size) {
                if (members[i] == team && prev != i) {
                    count++
                    if (count <= 4) score += i + 1
                    prev = i
                    if (count == 5) {
                        fifth[team] = i
                    }
                }
            }
            scores.add(team to score)
        }
    }
    val answer = scores.minOf { it.second }
    return if (scores.count { it.second == answer } > 1) {
        val list = scores.filter { it.second == answer }
        var temp: Pair<Int, Int> = 0 to Int.MAX_VALUE

        list.forEach {
            if (temp.second > fifth[it.first]!!) {
                temp = it.first to fifth[it.first]!!
            }
        }

        temp.first
    } else {
        scores.find { it.second == answer }?.first ?: 0
    }
}