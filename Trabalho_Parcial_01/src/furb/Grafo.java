package furb;

/**
 *
 * @author Rodrigo Fernandes
 */

public class Grafo {

	private int vertice;
	private int[][] custo;
	private final int maximo = 99999;

	public Grafo(int vertices, int[][] custos) {
		this.vertice = vertices;
		this.custo = custos;
	}

	public int calcularRota(int inicial, int fim) {
		int result = floydWarshall()[inicial - 1][fim - 1];
		return (result == this.maximo) ? -1 : result;
	}

	private int[][] floydWarshall() {
		int[][] distancia = this.inicializar();

		for (int k = 0; k < vertice; k++) {
			for (int i = 0; i < vertice; i++) {
				for (int j = 0; j < vertice; j++) {
					if (distancia[i][k] + distancia[k][j] < distancia[i][j]) {
						distancia[i][j] = distancia[i][k] + distancia[k][j];
					}
				}
			}
		}
		return distancia;
	}

	private int[][] inicializar() {
		int[][] v = new int[vertice][vertice];
		for (int i = 0; i < vertice; i++) {
			for (int j = 0; j < vertice; j++) {
				if ((this.custo[i][j] == 0) && (i != j)) {
					v[i][j] = this.maximo;
				} else {
					v[i][j] = this.custo[i][j];
				}
			}
		}
		return v;
	}
}
