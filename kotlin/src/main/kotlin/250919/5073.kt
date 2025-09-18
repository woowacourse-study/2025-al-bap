package `250919`

fun main() {
    val answers: MutableList<String> = mutableListOf()
    while(true) {
        val a = readln().split(" ").map { it.toInt() }
        if (a[0] == 0) break
        answers.add(solve(a[0], a[1], a[2]))
    }
    answers.forEach {
        println(it)
    }
}

fun solve(a: Int, b: Int, c: Int): String {
    val input = listOf(a, b, c).sorted()
    if (input[2] >= input[0] + input[1]) return "Invalid"

    return when {
        a == b && b == c -> "Equilateral"
        a == b || b == c || c == a -> "Isosceles"
        else -> "Scalene"
    }
}
