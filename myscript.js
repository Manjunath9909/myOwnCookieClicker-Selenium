let totalCount = 0;
let multiplier = 1;

function onLoadCall()
{
    document.getElementById("count").innerHTML = "Click count : " + totalCount;
    document.getElementById("multiplier").innerHTML = "Multipler : x"+ multiplier;
}

function countup()
{
    totalCount += (1 * multiplier);
    document.getElementById("count").innerHTML = "Click count : " + totalCount;
}

function resetCount()
{
    totalCount = 0;
    multiplier = 1;
    document.getElementById("count").innerHTML = "Click count : " + totalCount;
    document.getElementById("multiplier").innerHTML = "Multipler : x"+ multiplier;
}

function setMultiplier(value)
{
    multiplier = value;
    document.getElementById("multiplier").innerHTML = "Multipler : x"+ multiplier;
}