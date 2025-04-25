export function parseStructure(lines: any): {
    structure: {
        nodes: {
            line: any;
            id: any;
            pos: {
                x: any;
                y: any;
            };
            const: {
                x: any;
                y: any;
            };
            isXConstraint(): any;
            isYConstraint(): any;
            isXYConstraint(): any;
            loads: any[];
        }[];
        nodesById: Map<any, {
            line: any;
            id: any;
            pos: {
                x: any;
                y: any;
            };
            const: {
                x: any;
                y: any;
            };
            isXConstraint(): any;
            isYConstraint(): any;
            isXYConstraint(): any;
            loads: any[];
        }>;
        bars: {
            id: any;
            line: any;
            startNodeId: any;
            endNodeId: any;
            section: number;
            young: number;
        }[];
    };
    errors: ({
        line: number;
        message: any;
    } | {
        line: any;
        message: string;
    })[];
};
