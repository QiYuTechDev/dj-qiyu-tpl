if (!globalThis.genHtmlCustomElement) {
    /**
     * 生成一个新的 Div Custom Node
     *
     * @param {string[]} css_files 添加 css_files 到这个 shadow dom
     * @param {ShadowRootMode} mode
     * @return {typeof HTMLDivElement}
     */
    globalThis.genHtmlCustomElement = function (css_files, mode = "open") {
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
}

if (!globalThis.registerHtmlCustomElements) {
    /**
     * @param {string} name
     * @param {string[]} css_files
     * @param {ShadowRootMode} mode
     */
    globalThis.registerHtmlCustomElements = function (name, css_files, mode = 'open') {
        const cls = customElements.get(name)
        if (cls) {
            return
        }

        const newCls = genHtmlCustomElement(css_files, mode)
        customElements.define(name, newCls, {extends: 'div'})
    }
}
