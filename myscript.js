let totalCount = 0;
let multiplier = 1;

function onLoadCall()
{
    updateCurrency();
    updateMultiplier();
}

function countup()
{
    totalCount += (1 * multiplier);
    updateCurrency();
}

function resetCount()
{
    totalCount = 0;
    multiplier = 1;
    updateCurrency();    
    updateMultiplier();
}

function setMultiplier(value)
{
    if(totalCount >= value*100)
    {
        multiplier = value;
        deductCurrency(value*100);
        updateMultiplier();
    }
    else
    {
        alert("cannot afford it!");
    }
}

function deductCurrency(value)
{
    totalCount -= value;
    updateCurrency();
}

function updateCurrency()
{
    document.getElementById("count").innerHTML = "Click currency : " + totalCount;
}

function updateMultiplier()
{
    document.getElementById("multiplier").innerHTML = "Multipler : x"+ multiplier;
}

function getCookieJar()
{
    return totalCount;
}