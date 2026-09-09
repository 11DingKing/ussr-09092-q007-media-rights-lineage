class Asset
  attr_reader :digest, :parent_digest

  def initialize(digest:, parent_digest: nil)
    @digest = digest
    @parent_digest = parent_digest
  end
end
