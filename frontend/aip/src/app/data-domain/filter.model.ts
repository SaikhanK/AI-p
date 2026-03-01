export type Filter = ChoicesFilter

export type ChoicesFilter = {
    key: string,
    value?: string,
    choices?: string[]
}

export type CombiendFilter = {
    [key: string]: Filter[]
}

export const combiendfilter: CombiendFilter = {
    product: [{
        key: 'product_category',
        choices: ['true', 'false']
    },
    {
        key: 'product_brand',
        choices: ['Apple', 'Samsung', 'Mercedes']
    },
    {
        key: 'product_color',
        choices: ['Blue', 'Red', 'Green']
    }
    ]
}