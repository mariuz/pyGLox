varying vec3 normal, lightDir;
varying vec3 vertex, vv;

void main(void)
{
	vec3 cc = vec3(cos(vertex.x*vertex.z)+abs(vertex.y),vertex.y,0);
	//cc.y = 0;
	//cc.z = 0;
	
	vec4 color = vec4(cc,1) * vec4(0.4,0.4,0.4,1) + 0.26;

	float NdotL = max(dot(normalize(normal), normalize(lightDir)), 0.0);
	if(NdotL > 0.0)
	{
		color *= NdotL;
		//vec3 hv = normalize(normalize(lightDir) + normalize(vv));
		//color += pow(dot(normalize(normal),hv),32);
	}
	
	gl_FragColor = color * 1.4;
}
