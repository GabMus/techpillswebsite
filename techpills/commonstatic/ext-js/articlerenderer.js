
function isUrl(s) {
    var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
    return regexp.test(s);
}

function isPic(s) {
    return(s.match(/\.(jpeg|jpg|gif|png|tiff|svg)$/) != null);
}

function renderText(s, cont) {
    $(
        "<p>"+
        s.replace(/\n/g, '<br />')
        .replace(/\[b\]/g, '<strong>')
        .replace(/\[\/b\]/g, '</strong>')
        .replace(/\[u\]/g, '<u>')
        .replace(/\[\/u\]/g, '</u>')
        .replace(/\[i\]/g, '<em>')
        .replace(/\[\/i\]/g, '</em>')
        .replace(/\[url\]/g, '<a href=\"')
        .replace(/\[\/url\]/g, '\">')
        .replace(/\[\/\/url\]/g, '</a>')+
        "</p>"
    ).appendTo(cont);
}

function hasTag(s) {
    return (s.match(/^\[(img|cod)\]/) != null);
}

var renderByTag= {
    '[img]': function(s, cont) {
        if (isUrl(s) && isPic(s)) {
            s=s.substring(5);
            $(
                "<div style=\"text-align: center; margin: auto;\">"+
                "<img style=\"width: 90%; margin: auto;\" src=\""+
                    s+
                "\" /></div>"
            ).appendTo(cont);
        } else {renderText(s, cont);}
    },
    '[cod]': function(s, cont) {
        s=s.substring(5);
        $(
            "<pre><code style=\"font-family: DejaVu Sans Mono, monospace; text-wrap: nowrap; background-color: #faf8f0; text-align: left !important; display: block; padding: 0.5em 1em; border: 1px solid #bebab0; overflow: scroll;\">"+
                s+
            "</code></pre>"
        ).appendTo(cont);
    }
}

function renderArticle(content, container) {
    if (content == undefined) { return; }
    var splitCont=content.split('\n\n');
    for (var par in splitCont) {
        var row=splitCont[par].trim();
        if (hasTag(row)) {
            var tag=row.substring(0,5);
            renderByTag[tag](row, container);
        }
        else {
            renderText(row, container);
        }
    }
}
