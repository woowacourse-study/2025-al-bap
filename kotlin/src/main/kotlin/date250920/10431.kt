package date250920

fun main() {
    val count = readln().toInt()
    val answer: MutableList<Pair<Int, Int>> = mutableListOf()

    for (i in 0 until count) {
        val students = readln().split(" ").map { it.toInt() }.toMutableList()
        val line = students.removeFirst()

        answer.add(solve(line, students))
    }

    answer.forEach {
        println("${it.first} ${it.second}")
    }
}

fun solve(line: Int, students: List<Int>): Pair<Int, Int> {
    var count: Int = 0
    val current: MutableList<Int> = mutableListOf()

    students.forEach { student ->
        val bigger = current.find { it > student }
        if (bigger == null) {
            current.add(student)
        } else {
            val index = current.indexOf(bigger)
            count += current.size - index
            current.add(index, student)
        }
    }

    return Pair(line, count)
}