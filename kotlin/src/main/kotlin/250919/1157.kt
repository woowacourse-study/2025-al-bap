package `250919`

fun main() {
    println(solve(readln()))
}

fun solve(a: String): String {
    val matrix = mutableMapOf<String, Int>()
    val list = a.toList().map { it.uppercase() }
    list.forEach {
        matrix[it] = (matrix[it] ?: 0) + 1
    }
    if (matrix.keys.size == 1) return matrix.keys.first()
    val results = matrix.values
    val sorted = results.sortedBy { -it }
    val max = sorted.first()
    if (max == sorted[1]) return "?"
    val idx = results.indexOf(max)
    return matrix.keys.toList()[idx]
}
