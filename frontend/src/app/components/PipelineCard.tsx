type Props = {

  title: string

  data: any
}

export default function PipelineCard({

  title,

  data

}: Props) {

  return (

    <div
      className="
        bg-white/5
        border border-white/10
        rounded-3xl
        p-6
        backdrop-blur-lg
        overflow-auto
      "
    >

      <h2
        className="
          text-2xl
          font-bold
          mb-4
          text-cyan-400
        "
      >
        {title}
      </h2>

      <pre
        className="
          text-sm
          text-zinc-300
          whitespace-pre-wrap
        "
      >
        {
          JSON.stringify(
            data,
            null,
            2
          )
        }
      </pre>

    </div>
  )
}
