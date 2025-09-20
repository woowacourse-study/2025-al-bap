package date250919

fun main() {
    val count: Int = readln().toIntOrNull() ?: return
    val channels: MutableList<String> = mutableListOf()
    for (i in 0 until count) {
        val input = readln()
        channels.add(input)
    }
    println(solve(channels))
}

fun solve(list: MutableList<String>):String {
    var answer: String = ""
    val pos1: Int = list.indexOf("KBS1")

    for (i in 0 until pos1) {
        answer += "1"
    }
    for (i in 0 until pos1) {
        answer += "4"
    }
    list.removeAt(pos1)
    list.add(0, "KBS1")

    val pos2: Int = list.indexOf("KBS2")

    for (i in 0 until pos2) {
        answer += "1"
    }
    for (i in 0 until pos2 - 1) {
        answer += "4"
    }

    return answer
}
