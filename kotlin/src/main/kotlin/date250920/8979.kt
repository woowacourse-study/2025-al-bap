package date250920

data class Country(
    val id: Int,
    val gold: Int,
    val silver: Int,
    val copper: Int,
)

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    val countries = mutableListOf<Country>()
    var target: Country = Country(0,0,0,0)

    for (i in 0 until input[0]) {
        val country = readln().split(" ").map { it.toInt() }
        val a = Country(country[0], country[1], country[2], country[3])
        countries.add(a)
        if (country[0] == input[1]) target = a
    }

    println(solve(target, countries))
}

fun solve(target: Country, countries: List<Country>): Int {
    var count = 1
    count += countries.count { it.gold > target.gold }
    count += countries.count { it.gold == target.gold && it.silver > target.silver }
    count += countries.count { it.gold == target.gold && it.silver == target.silver && it.copper > target.copper }
    return count
}