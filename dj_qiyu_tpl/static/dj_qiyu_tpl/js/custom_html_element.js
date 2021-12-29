/**
 * 生成一个新的 Div Custom Node
 *
 * @param {string[]} css_files 添加 css_files 到这个 shadow dom
 * @param {ShadowRootMode} mode
 * @return {typeof HTMLDivElement}
 */
function genHtmlCustomElement(css_files, mode = "open") {
    return class extends HTMLDivElement {
        constructor() {
            super();

            const shadow = this.attachShadow({mode: mode});

            shadow.innerHTML = this.innerHTML;

            css_files.forEach(function (href) {
                let style = document.createElement("link");
                style.rel = "stylesheet";
                style.type = "text/css";
                style.href = href;
                shadow.appendChild(style);
            });
        }
    }
}
