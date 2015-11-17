class UnlockEsp8266Action < BaseAction
  def execute(con)
    s = TCPSocket.new con[:host], con[:port]
  end
end
