# SNMP MIB module (CTRON-SSR-L3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-SSR-L3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:48 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

l3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 600)
)
if mibBuilder.loadTexts:
    l3MIB.setRevisions(
        ("1999-09-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SSRProtocols(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hopopt", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ggp", 3),
          ("ipip", 4),
          ("stream", 5),
          ("tcp", 6),
          ("cbt", 7),
          ("egp", 8),
          ("igp", 9),
          ("bbnrccmon", 10),
          ("nvpii", 11),
          ("pup", 12),
          ("argus", 13),
          ("emcon", 14),
          ("xnet", 15),
          ("chaos", 16),
          ("udp", 17),
          ("mux", 18),
          ("dcn", 19),
          ("hmp", 20),
          ("prm", 21),
          ("xnsidp", 22),
          ("trunk1", 23),
          ("trunk2", 24),
          ("leaf1", 25),
          ("leaf2", 26),
          ("rdp", 27),
          ("irtp", 28),
          ("isotp4", 29),
          ("netblt", 30),
          ("mfe", 31),
          ("meritInp", 32),
          ("sep", 33),
          ("tpc", 34),
          ("idpr", 35),
          ("xtp", 36),
          ("ddp", 37),
          ("idprCmtp", 38),
          ("tppp", 39),
          ("il", 40),
          ("ipv6", 41),
          ("sdrp", 42),
          ("ipv6r", 43),
          ("ipv6f", 44),
          ("idrp", 45),
          ("rsvp", 46),
          ("gre", 47),
          ("mhrp", 48),
          ("bna", 49),
          ("esp", 50),
          ("ah", 51),
          ("inlsp", 52),
          ("swipe", 53),
          ("narp", 54),
          ("mobile", 55),
          ("tlsp", 56),
          ("skip", 57),
          ("ipv6Icmp", 58),
          ("ipv6Nonxt", 59),
          ("ipv6Opts", 60),
          ("hostInternal", 61),
          ("cftp", 62),
          ("any", 63),
          ("satExpak", 64),
          ("kryptolan", 65),
          ("rvd", 66),
          ("ippc", 67),
          ("adfs", 68),
          ("satMon", 69),
          ("visa", 70),
          ("ipcv", 71),
          ("cpnx", 72),
          ("cphb", 73),
          ("wsn", 74),
          ("pvp", 75),
          ("brSatMon", 76),
          ("sunNd", 77),
          ("wbMon", 78),
          ("wbExpak", 79),
          ("isoIp", 80),
          ("vmtp", 81),
          ("secureVmtp", 82),
          ("vines", 83),
          ("ttp", 84),
          ("nsfnetIgp", 85),
          ("dgp", 86),
          ("tcf", 87),
          ("eigrp", 88),
          ("ospfigp", 89),
          ("spriteRpc", 90),
          ("larp", 91),
          ("mtp", 92),
          ("ax25", 93),
          ("ipipep", 94),
          ("micp", 95),
          ("sccSp", 96),
          ("etherip", 97),
          ("encap", 98),
          ("anyEncrpyt", 99),
          ("gmtp", 100),
          ("ifmp", 101),
          ("pnni", 102),
          ("pim", 103),
          ("aris", 104),
          ("scps", 105),
          ("qnx", 106),
          ("an", 107),
          ("ippcp", 108),
          ("snp", 109),
          ("cpqP", 110),
          ("ipxIp", 111),
          ("vrrp", 112),
          ("reserved", 255))
    )



# MIB Managed Objects in the order of their OIDs

_L3Group_ObjectIdentity = ObjectIdentity
l3Group = _L3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3)
)
_L3FlowTable_Object = MibTable
l3FlowTable = _L3FlowTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1)
)
if mibBuilder.loadTexts:
    l3FlowTable.setStatus("obsolete")
_L3FlowEntry_Object = MibTableRow
l3FlowEntry = _L3FlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1)
)
l3FlowEntry.setIndexNames(
    (0, "CTRON-SSR-L3-MIB", "l3FlowIndex"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowFilterId"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowPortOfEntry"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowSrcIpAddress"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowDstIpAddress"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowTOS"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowProtocol"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowSrcPort"),
    (0, "CTRON-SSR-L3-MIB", "l3FlowDstPort"),
)
if mibBuilder.loadTexts:
    l3FlowEntry.setStatus("obsolete")


class _L3FlowIndex_Type(Integer32):
    """Custom type l3FlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_L3FlowIndex_Type.__name__ = "Integer32"
_L3FlowIndex_Object = MibTableColumn
l3FlowIndex = _L3FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 1),
    _L3FlowIndex_Type()
)
l3FlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowIndex.setStatus("obsolete")


class _L3FlowFilterId_Type(Integer32):
    """Custom type l3FlowFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_L3FlowFilterId_Type.__name__ = "Integer32"
_L3FlowFilterId_Object = MibTableColumn
l3FlowFilterId = _L3FlowFilterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 2),
    _L3FlowFilterId_Type()
)
l3FlowFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowFilterId.setStatus("obsolete")


class _L3FlowPortOfEntry_Type(Integer32):
    """Custom type l3FlowPortOfEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_L3FlowPortOfEntry_Type.__name__ = "Integer32"
_L3FlowPortOfEntry_Object = MibTableColumn
l3FlowPortOfEntry = _L3FlowPortOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 3),
    _L3FlowPortOfEntry_Type()
)
l3FlowPortOfEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowPortOfEntry.setStatus("obsolete")
_L3FlowSrcIpAddress_Type = IpAddress
_L3FlowSrcIpAddress_Object = MibTableColumn
l3FlowSrcIpAddress = _L3FlowSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 4),
    _L3FlowSrcIpAddress_Type()
)
l3FlowSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowSrcIpAddress.setStatus("obsolete")
_L3FlowDstIpAddress_Type = IpAddress
_L3FlowDstIpAddress_Object = MibTableColumn
l3FlowDstIpAddress = _L3FlowDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 5),
    _L3FlowDstIpAddress_Type()
)
l3FlowDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowDstIpAddress.setStatus("obsolete")


class _L3FlowTOS_Type(Integer32):
    """Custom type l3FlowTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_L3FlowTOS_Type.__name__ = "Integer32"
_L3FlowTOS_Object = MibTableColumn
l3FlowTOS = _L3FlowTOS_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 6),
    _L3FlowTOS_Type()
)
l3FlowTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowTOS.setStatus("obsolete")
_L3FlowProtocol_Type = SSRProtocols
_L3FlowProtocol_Object = MibTableColumn
l3FlowProtocol = _L3FlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 7),
    _L3FlowProtocol_Type()
)
l3FlowProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowProtocol.setStatus("obsolete")


class _L3FlowSrcPort_Type(Integer32):
    """Custom type l3FlowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FlowSrcPort_Type.__name__ = "Integer32"
_L3FlowSrcPort_Object = MibTableColumn
l3FlowSrcPort = _L3FlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 8),
    _L3FlowSrcPort_Type()
)
l3FlowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowSrcPort.setStatus("obsolete")


class _L3FlowDstPort_Type(Integer32):
    """Custom type l3FlowDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FlowDstPort_Type.__name__ = "Integer32"
_L3FlowDstPort_Object = MibTableColumn
l3FlowDstPort = _L3FlowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 9),
    _L3FlowDstPort_Type()
)
l3FlowDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowDstPort.setStatus("obsolete")
_L3FlowPkts_Type = Counter32
_L3FlowPkts_Object = MibTableColumn
l3FlowPkts = _L3FlowPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 10),
    _L3FlowPkts_Type()
)
l3FlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowPkts.setStatus("obsolete")
_L3FlowOctets_Type = Counter32
_L3FlowOctets_Object = MibTableColumn
l3FlowOctets = _L3FlowOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 11),
    _L3FlowOctets_Type()
)
l3FlowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3FlowOctets.setStatus("obsolete")
_L3FlowPriorityTable_Object = MibTable
l3FlowPriorityTable = _L3FlowPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2)
)
if mibBuilder.loadTexts:
    l3FlowPriorityTable.setStatus("obsolete")
_L3FlowPriorityEntry_Object = MibTableRow
l3FlowPriorityEntry = _L3FlowPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1)
)
l3FlowPriorityEntry.setIndexNames(
    (0, "CTRON-SSR-L3-MIB", "l3FlowPriorityIndex"),
)
if mibBuilder.loadTexts:
    l3FlowPriorityEntry.setStatus("obsolete")


class _L3FlowPriorityIndex_Type(Integer32):
    """Custom type l3FlowPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_L3FlowPriorityIndex_Type.__name__ = "Integer32"
_L3FlowPriorityIndex_Object = MibTableColumn
l3FlowPriorityIndex = _L3FlowPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 1),
    _L3FlowPriorityIndex_Type()
)
l3FlowPriorityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityIndex.setStatus("obsolete")


class _L3FlowPriorityName_Type(OctetString):
    """Custom type l3FlowPriorityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_L3FlowPriorityName_Type.__name__ = "OctetString"
_L3FlowPriorityName_Object = MibTableColumn
l3FlowPriorityName = _L3FlowPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 2),
    _L3FlowPriorityName_Type()
)
l3FlowPriorityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityName.setStatus("obsolete")
_L3FlowPrioritySrcIpAddress_Type = IpAddress
_L3FlowPrioritySrcIpAddress_Object = MibTableColumn
l3FlowPrioritySrcIpAddress = _L3FlowPrioritySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 3),
    _L3FlowPrioritySrcIpAddress_Type()
)
l3FlowPrioritySrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPrioritySrcIpAddress.setStatus("obsolete")


class _L3FlowPrioritySrcPort_Type(Integer32):
    """Custom type l3FlowPrioritySrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FlowPrioritySrcPort_Type.__name__ = "Integer32"
_L3FlowPrioritySrcPort_Object = MibTableColumn
l3FlowPrioritySrcPort = _L3FlowPrioritySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 4),
    _L3FlowPrioritySrcPort_Type()
)
l3FlowPrioritySrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPrioritySrcPort.setStatus("obsolete")
_L3FlowPriorityDstIpAddress_Type = IpAddress
_L3FlowPriorityDstIpAddress_Object = MibTableColumn
l3FlowPriorityDstIpAddress = _L3FlowPriorityDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 5),
    _L3FlowPriorityDstIpAddress_Type()
)
l3FlowPriorityDstIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityDstIpAddress.setStatus("obsolete")


class _L3FlowPriorityDstPort_Type(Integer32):
    """Custom type l3FlowPriorityDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FlowPriorityDstPort_Type.__name__ = "Integer32"
_L3FlowPriorityDstPort_Object = MibTableColumn
l3FlowPriorityDstPort = _L3FlowPriorityDstPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 6),
    _L3FlowPriorityDstPort_Type()
)
l3FlowPriorityDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityDstPort.setStatus("obsolete")


class _L3FlowPriorityTOS_Type(Integer32):
    """Custom type l3FlowPriorityTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_L3FlowPriorityTOS_Type.__name__ = "Integer32"
_L3FlowPriorityTOS_Object = MibTableColumn
l3FlowPriorityTOS = _L3FlowPriorityTOS_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 7),
    _L3FlowPriorityTOS_Type()
)
l3FlowPriorityTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityTOS.setStatus("obsolete")
_L3FlowPriorityProtocol_Type = SSRProtocols
_L3FlowPriorityProtocol_Object = MibTableColumn
l3FlowPriorityProtocol = _L3FlowPriorityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 8),
    _L3FlowPriorityProtocol_Type()
)
l3FlowPriorityProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityProtocol.setStatus("obsolete")


class _L3FlowPriorityInterface_Type(OctetString):
    """Custom type l3FlowPriorityInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L3FlowPriorityInterface_Type.__name__ = "OctetString"
_L3FlowPriorityInterface_Object = MibTableColumn
l3FlowPriorityInterface = _L3FlowPriorityInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 9),
    _L3FlowPriorityInterface_Type()
)
l3FlowPriorityInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriorityInterface.setStatus("obsolete")


class _L3FlowPriority_Type(Integer32):
    """Custom type l3FlowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("control", 4))
    )


_L3FlowPriority_Type.__name__ = "Integer32"
_L3FlowPriority_Object = MibTableColumn
l3FlowPriority = _L3FlowPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 10),
    _L3FlowPriority_Type()
)
l3FlowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FlowPriority.setStatus("obsolete")
_L3Conformance_ObjectIdentity = ObjectIdentity
l3Conformance = _L3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2)
)
_L3Compliances_ObjectIdentity = ObjectIdentity
l3Compliances = _L3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 1)
)
_L3Groups_ObjectIdentity = ObjectIdentity
l3Groups = _L3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 2)
)

# Managed Objects groups

l3ConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 2, 1)
)
l3ConfGroupV10.setObjects(
      *(("CTRON-SSR-L3-MIB", "l3FlowIndex"),
        ("CTRON-SSR-L3-MIB", "l3FlowFilterId"),
        ("CTRON-SSR-L3-MIB", "l3FlowPortOfEntry"),
        ("CTRON-SSR-L3-MIB", "l3FlowSrcIpAddress"),
        ("CTRON-SSR-L3-MIB", "l3FlowDstIpAddress"),
        ("CTRON-SSR-L3-MIB", "l3FlowTOS"),
        ("CTRON-SSR-L3-MIB", "l3FlowProtocol"),
        ("CTRON-SSR-L3-MIB", "l3FlowSrcPort"),
        ("CTRON-SSR-L3-MIB", "l3FlowDstPort"),
        ("CTRON-SSR-L3-MIB", "l3FlowPkts"),
        ("CTRON-SSR-L3-MIB", "l3FlowOctets"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityIndex"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityName"),
        ("CTRON-SSR-L3-MIB", "l3FlowPrioritySrcIpAddress"),
        ("CTRON-SSR-L3-MIB", "l3FlowPrioritySrcPort"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityDstIpAddress"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityDstPort"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityTOS"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityProtocol"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriorityInterface"),
        ("CTRON-SSR-L3-MIB", "l3FlowPriority"))
)
if mibBuilder.loadTexts:
    l3ConfGroupV10.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

l3ComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 2, 1, 1)
)
l3ComplianceV10.setObjects(
    ("CTRON-SSR-L3-MIB", "l3ConfGroupV10")
)
if mibBuilder.loadTexts:
    l3ComplianceV10.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-L3-MIB",
    **{"SSRProtocols": SSRProtocols,
       "l3Group": l3Group,
       "l3FlowTable": l3FlowTable,
       "l3FlowEntry": l3FlowEntry,
       "l3FlowIndex": l3FlowIndex,
       "l3FlowFilterId": l3FlowFilterId,
       "l3FlowPortOfEntry": l3FlowPortOfEntry,
       "l3FlowSrcIpAddress": l3FlowSrcIpAddress,
       "l3FlowDstIpAddress": l3FlowDstIpAddress,
       "l3FlowTOS": l3FlowTOS,
       "l3FlowProtocol": l3FlowProtocol,
       "l3FlowSrcPort": l3FlowSrcPort,
       "l3FlowDstPort": l3FlowDstPort,
       "l3FlowPkts": l3FlowPkts,
       "l3FlowOctets": l3FlowOctets,
       "l3FlowPriorityTable": l3FlowPriorityTable,
       "l3FlowPriorityEntry": l3FlowPriorityEntry,
       "l3FlowPriorityIndex": l3FlowPriorityIndex,
       "l3FlowPriorityName": l3FlowPriorityName,
       "l3FlowPrioritySrcIpAddress": l3FlowPrioritySrcIpAddress,
       "l3FlowPrioritySrcPort": l3FlowPrioritySrcPort,
       "l3FlowPriorityDstIpAddress": l3FlowPriorityDstIpAddress,
       "l3FlowPriorityDstPort": l3FlowPriorityDstPort,
       "l3FlowPriorityTOS": l3FlowPriorityTOS,
       "l3FlowPriorityProtocol": l3FlowPriorityProtocol,
       "l3FlowPriorityInterface": l3FlowPriorityInterface,
       "l3FlowPriority": l3FlowPriority,
       "l3MIB": l3MIB,
       "l3Conformance": l3Conformance,
       "l3Compliances": l3Compliances,
       "l3Groups": l3Groups,
       "l3ConfGroupV10": l3ConfGroupV10,
       "l3ComplianceV10": l3ComplianceV10}
)
