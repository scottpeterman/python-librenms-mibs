# SNMP MIB module (CM-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-ENTITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:03 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmIntervalType,
 OperationalState,
 RestartType,
 SecondaryState,
 TDMFrequencySourceType,
 UsbOperationalMode,
 VlanId) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmIntervalType",
    "OperationalState",
    "RestartType",
    "SecondaryState",
    "TDMFrequencySourceType",
    "UsbOperationalMode",
    "VlanId")

(CmAutoProvMode,) = mibBuilder.importSymbols(
    "CM-SYSTEM-MIB",
    "CmAutoProvMode")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3)
)
if mibBuilder.loadTexts:
    cmEntityMIB.setRevisions(
        ("2021-01-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NeProvAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("decline", 2))
    )



class NetworkElementType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              57)
        )
    )
    namedValues = NamedValues(
        *(("onerackunit", 1),
          ("hubshelf", 2),
          ("cle", 3),
          ("aggregation", 4),
          ("cpmr", 5),
          ("ccge101", 6),
          ("ccge206", 7),
          ("ccge201", 8),
          ("ccge201se", 9),
          ("ccge206f", 10),
          ("ccge112", 11),
          ("ccge114", 12),
          ("ccge206v", 13),
          ("ccxg210", 14),
          ("cct1804", 15),
          ("cct3204", 16),
          ("ccsyncprobe", 17),
          ("ccge114h", 18),
          ("ccge114ph", 19),
          ("ccge114sh", 20),
          ("ccge114s", 21),
          ("sh1pcs", 22),
          ("ccosa5411", 23),
          ("ccge112pro", 24),
          ("ccge112proM", 25),
          ("ccge114pro", 26),
          ("ccge114proC", 27),
          ("ccge114proSH", 28),
          ("ccge114proCSH", 29),
          ("ccge114proHE", 30),
          ("ccge112proH", 31),
          ("ccxg210c", 32),
          ("ccosa5420", 33),
          ("ccosa5421", 34),
          ("ccge114g", 35),
          ("ccge114proVmH", 36),
          ("ccge114proVmCH", 37),
          ("ccge114proVmCSH", 38),
          ("ccge101pro", 39),
          ("ccgo102ProS", 40),
          ("ccgo102ProSP", 41),
          ("cccx101Pro30A", 42),
          ("cccx102Pro30A", 43),
          ("ccxg116pro", 44),
          ("ccxg120pro", 45),
          ("ccge112proVm", 46),
          ("ccosa5430", 47),
          ("ccosa5440", 48),
          ("ge102proh", 49),
          ("ge102proefmh", 50),
          ("ccxg116proH", 51),
          ("ccgo102ProSM", 52),
          ("ccxg118proSH", 53),
          ("ccxg118proacSH", 54),
          ("ccge114proVmSH", 55),
          ("ccge104", 56),
          ("ccxg120proSH", 57))
    )



class SlotType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("scu", 1),
          ("psu", 2),
          ("fan", 3),
          ("generic", 4),
          ("lag", 5),
          ("nemi", 6),
          ("stu", 7),
          ("swf-140g", 8),
          ("ami", 9),
          ("sti", 10))
    )



class ShelfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              59)
        )
    )
    namedValues = NamedValues(
        *(("onerackunit", 1),
          ("hubshelf", 2),
          ("cle", 3),
          ("aggregation", 4),
          ("cpmr", 5),
          ("onerackunit-ge101", 6),
          ("onerackunit-ge206", 7),
          ("onerackunit-ge201", 8),
          ("onerackunit-ge201se", 9),
          ("onerackunit-ge206f", 10),
          ("onerackunit-ge112", 11),
          ("onerackunit-ge114", 12),
          ("onerackunit-ge206v", 13),
          ("onerackunit-xg210", 14),
          ("onerackunit-t1804", 15),
          ("onerackunit-t3204", 16),
          ("onerackunit-syncprobe", 17),
          ("onerackunit-ge114h", 18),
          ("onerackunit-ge114ph", 19),
          ("onerackunit-ge114sh", 20),
          ("onerackunit-ge114s", 21),
          ("onerackunit-sh1pcs", 22),
          ("onerackunit-osa5411", 23),
          ("onerackunitGe112Pro", 24),
          ("ge112ProM", 25),
          ("onerackunitGe114Pro", 26),
          ("onerackunitGe114ProC", 27),
          ("onerackunitGe114ProSH", 28),
          ("onerackunitGe114ProCSH", 29),
          ("onerackunitGe114ProHE", 30),
          ("onerackunitGe112ProH", 31),
          ("onerackunit-xg210c", 32),
          ("onerackunit-osa5420", 33),
          ("onerackunit-osa5421", 34),
          ("onerackunit-ge114g", 35),
          ("onerackunitGe114ProVmH", 36),
          ("onerackunitGe114ProVmCH", 37),
          ("onerackunitGe114ProVmCSH", 38),
          ("ge101pro", 39),
          ("go102proS", 40),
          ("go102proSP", 41),
          ("onerackunit-cx101pro30A", 42),
          ("onerackunit-cx102pro30A", 43),
          ("onerackunit-xg116pro", 44),
          ("onerackunit-xg120pro", 45),
          ("onerackunitGe112ProVm", 46),
          ("osa5401", 47),
          ("osa5405", 48),
          ("onerackunit-osa5430", 49),
          ("threerackunit-osa5440", 50),
          ("ge102proh", 51),
          ("ge102proefmh", 52),
          ("onerackunit-xg116proH", 53),
          ("go102proSM", 54),
          ("onerackunit-xg118proSH", 55),
          ("onerackunit-xg118proacSH", 56),
          ("onerackunitGe114ProVmSH", 57),
          ("onerackunitGe104", 58),
          ("onerackunit-xg120proSH", 59))
    )



class ShelfAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initiateLampTest", 1),
          ("initiateACO", 2),
          ("coldRestart", 3))
    )



class PsuType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ac", 1),
          ("dc", 2))
    )



class CardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("psu", 2),
          ("fan", 3),
          ("nemi", 4),
          ("scu", 5),
          ("eth-10-100-1000-ntu", 6),
          ("eth-cpmr", 7),
          ("eth-ge-101", 8),
          ("eth-ge-206", 9),
          ("eth-ge-201", 10),
          ("eth-ge-201se", 11),
          ("eth-10-100-1000-nte", 12),
          ("scu-t", 13),
          ("eth-ge-206f", 14),
          ("eth-xg-1x", 15),
          ("swf-140g", 16),
          ("stu", 17),
          ("eth-ge-10s", 18),
          ("ami", 19),
          ("sti", 20),
          ("eth-ge-112", 21),
          ("eth-ge-114", 22),
          ("eth-ge-206v", 23),
          ("eth-ge-4e-cc", 24),
          ("eth-ge-4s-cc", 25),
          ("eth-xg-210", 26),
          ("eth-xg-1x-cc", 27),
          ("eth-xg-1s-cc", 28),
          ("stm1-4-et", 29),
          ("pwe3-ocnstm", 30),
          ("pwe3-e1t1", 31),
          ("eth-xg-1x-h", 32),
          ("eth-ge-10s-h", 33),
          ("eth-t1804", 34),
          ("eth-t3204", 35),
          ("eth-ge-syncprobe", 36),
          ("eth-ge-8s-cc", 37),
          ("eth-ge-114h", 38),
          ("eth-ge-114ph", 39),
          ("eth-fe-36e", 40),
          ("eth-ge-114sh", 41),
          ("eth-ge-114s", 42),
          ("sti-h", 43),
          ("stu-h", 44),
          ("eth-ge-8e-cc", 45),
          ("eth-sh1pcs", 46),
          ("eth-osa5411", 47),
          ("ethGe112Pro", 48),
          ("ethGe112ProM", 49),
          ("ethGe114Pro", 50),
          ("ethGe114ProC", 51),
          ("ethGe114ProSH", 52),
          ("ethGe114ProCSH", 53),
          ("ethGe114ProHE", 54),
          ("ethGe112ProH", 55),
          ("eth-xg-210c", 56),
          ("eth-ge-8sc-cc", 57),
          ("eth-osa5420", 58),
          ("eth-osa5421", 59),
          ("bits-x16", 60),
          ("eth-ge-114g", 61),
          ("ethGe114ProVmH", 62),
          ("ethGe114ProVmCH", 63),
          ("ethGe114ProVmCSH", 64),
          ("serverCard", 65),
          ("eth-ptpv2-osa", 66),
          ("gnss-osa", 67),
          ("thc-osa", 68),
          ("sgc-osa", 69),
          ("pps-x16", 70),
          ("clk-x16", 71),
          ("todAndPps-x16", 72),
          ("eth-ge-101pro", 73),
          ("ethgo102proS", 74),
          ("ethgo102proSP", 75),
          ("ethcx101pro30A", 76),
          ("ethcx102pro30A", 77),
          ("osa-ge-4s", 78),
          ("eth-xg-116pro", 79),
          ("eth-xg-120pro", 80),
          ("ethGe112ProVm", 81),
          ("eth-osa5401", 82),
          ("eth-osa5405", 83),
          ("eth-csm", 84),
          ("aux-osa", 85),
          ("bits-x16-enhanced", 86),
          ("osa-ge-4s-protected", 87),
          ("eth-ge-102pro-h", 88),
          ("eth-ge-102pro-efmh", 89),
          ("eth-xg-116pro-h", 90),
          ("ethgo102proSM", 91),
          ("eth-xg-118pro-sh", 92),
          ("eth-xg-118proac-sh", 93),
          ("ethGe114ProVmSH", 94),
          ("ethGe104", 95),
          ("eth-xg-120pro-sh", 96),
          ("irig", 97),
          ("mb-gnss", 98),
          ("composite-clock", 99))
    )



class CmCPMRLinkLossFwdMode(TextualConvention, Integer32):
    status = "current"
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
        *(("llfmode-none", 1),
          ("llfmode-acc2acc", 2),
          ("llfmode-net2acc", 3),
          ("llfmode-both", 4))
    )



class PWE3OCNSTMCardMode(TextualConvention, Integer32):
    status = "current"
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
        *(("stm4", 1),
          ("oc12", 2),
          ("stm1", 3),
          ("oc3", 4))
    )



class PWE3E1T1CardMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1-16", 1),
          ("e1-16", 2))
    )



class PSNEncapsulationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )



class LLDPEnableAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enableLLDP", 1),
          ("disableLLDP", 2),
          ("enableLLDPTxOnly", 3),
          ("enableLLDPRxOnly", 4))
    )



class LedControlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("normal", 1),
          ("status-led-only", 2),
          ("all-disabled", 3))
    )



class ResyncType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("resync-to-pps", 2))
    )



class StorageStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("formatting", 1),
          ("empty", 2),
          ("ready", 3),
          ("unformatted", 4),
          ("unmounted", 5))
    )



class SwitchPortAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("switch", 1))
    )



class PortCarrierType(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("t1", 1),
          ("e1", 2),
          ("t3", 3),
          ("e3", 4),
          ("oc3", 5),
          ("oc12", 6),
          ("stm1", 7),
          ("stm4", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CmEntityObjects_ObjectIdentity = ObjectIdentity
cmEntityObjects = _CmEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1)
)
_NetworkElementTable_Object = MibTable
networkElementTable = _NetworkElementTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    networkElementTable.setStatus("current")
_NetworkElementEntry_Object = MibTableRow
networkElementEntry = _NetworkElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1)
)
networkElementEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
)
if mibBuilder.loadTexts:
    networkElementEntry.setStatus("current")
_NeIndex_Type = Integer32
_NeIndex_Object = MibTableColumn
neIndex = _NeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 1),
    _NeIndex_Type()
)
neIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neIndex.setStatus("current")


class _NeName_Type(DisplayString):
    """Custom type neName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeName_Type.__name__ = "DisplayString"
_NeName_Object = MibTableColumn
neName = _NeName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 2),
    _NeName_Type()
)
neName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neName.setStatus("current")
_NeType_Type = NetworkElementType
_NeType_Object = MibTableColumn
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 3),
    _NeType_Type()
)
neType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neType.setStatus("current")


class _NeContact_Type(DisplayString):
    """Custom type neContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeContact_Type.__name__ = "DisplayString"
_NeContact_Object = MibTableColumn
neContact = _NeContact_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 4),
    _NeContact_Type()
)
neContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neContact.setStatus("current")


class _NeLocation_Type(DisplayString):
    """Custom type neLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeLocation_Type.__name__ = "DisplayString"
_NeLocation_Object = MibTableColumn
neLocation = _NeLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 5),
    _NeLocation_Type()
)
neLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neLocation.setStatus("current")


class _NeDescription_Type(DisplayString):
    """Custom type neDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeDescription_Type.__name__ = "DisplayString"
_NeDescription_Object = MibTableColumn
neDescription = _NeDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 6),
    _NeDescription_Type()
)
neDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neDescription.setStatus("current")


class _NeCmdPromptPrefix_Type(DisplayString):
    """Custom type neCmdPromptPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NeCmdPromptPrefix_Type.__name__ = "DisplayString"
_NeCmdPromptPrefix_Object = MibTableColumn
neCmdPromptPrefix = _NeCmdPromptPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 7),
    _NeCmdPromptPrefix_Type()
)
neCmdPromptPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neCmdPromptPrefix.setStatus("current")
_NeAccepted_Type = TruthValue
_NeAccepted_Object = MibTableColumn
neAccepted = _NeAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 8),
    _NeAccepted_Type()
)
neAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAccepted.setStatus("current")
_NeFromPort_Type = VariablePointer
_NeFromPort_Object = MibTableColumn
neFromPort = _NeFromPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 9),
    _NeFromPort_Type()
)
neFromPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neFromPort.setStatus("current")
_NeProvAction_Type = NeProvAction
_NeProvAction_Object = MibTableColumn
neProvAction = _NeProvAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 10),
    _NeProvAction_Type()
)
neProvAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neProvAction.setStatus("current")
_NeStorageType_Type = StorageType
_NeStorageType_Object = MibTableColumn
neStorageType = _NeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 11),
    _NeStorageType_Type()
)
neStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neStorageType.setStatus("current")
_NeRowStatus_Type = RowStatus
_NeRowStatus_Object = MibTableColumn
neRowStatus = _NeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 12),
    _NeRowStatus_Type()
)
neRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neRowStatus.setStatus("current")
_NeAutoProvMode_Type = CmAutoProvMode
_NeAutoProvMode_Object = MibTableColumn
neAutoProvMode = _NeAutoProvMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 13),
    _NeAutoProvMode_Type()
)
neAutoProvMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neAutoProvMode.setStatus("current")
_NeFineGrainedPmInterval_Type = CmPmIntervalType
_NeFineGrainedPmInterval_Object = MibTableColumn
neFineGrainedPmInterval = _NeFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 1, 1, 14),
    _NeFineGrainedPmInterval_Type()
)
neFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neFineGrainedPmInterval.setStatus("current")
_ShelfTable_Object = MibTable
shelfTable = _ShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2)
)
if mibBuilder.loadTexts:
    shelfTable.setStatus("current")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1)
)
shelfEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("current")
_ShelfIndex_Type = Integer32
_ShelfIndex_Object = MibTableColumn
shelfIndex = _ShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 1),
    _ShelfIndex_Type()
)
shelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIndex.setStatus("current")
_ShelfEntityIndex_Type = PhysicalIndex
_ShelfEntityIndex_Object = MibTableColumn
shelfEntityIndex = _ShelfEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 2),
    _ShelfEntityIndex_Type()
)
shelfEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfEntityIndex.setStatus("current")
_ShelfType_Type = ShelfType
_ShelfType_Object = MibTableColumn
shelfType = _ShelfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 3),
    _ShelfType_Type()
)
shelfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfType.setStatus("current")


class _ShelfbackplaneRev_Type(DisplayString):
    """Custom type shelfbackplaneRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfbackplaneRev_Type.__name__ = "DisplayString"
_ShelfbackplaneRev_Object = MibTableColumn
shelfbackplaneRev = _ShelfbackplaneRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 4),
    _ShelfbackplaneRev_Type()
)
shelfbackplaneRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfbackplaneRev.setStatus("current")
_ShelfbackplaneDOM_Type = DateAndTime
_ShelfbackplaneDOM_Object = MibTableColumn
shelfbackplaneDOM = _ShelfbackplaneDOM_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 5),
    _ShelfbackplaneDOM_Type()
)
shelfbackplaneDOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfbackplaneDOM.setStatus("current")


class _ShelfbackplaneSerialNo_Type(DisplayString):
    """Custom type shelfbackplaneSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ShelfbackplaneSerialNo_Type.__name__ = "DisplayString"
_ShelfbackplaneSerialNo_Object = MibTableColumn
shelfbackplaneSerialNo = _ShelfbackplaneSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 6),
    _ShelfbackplaneSerialNo_Type()
)
shelfbackplaneSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfbackplaneSerialNo.setStatus("current")
_ShelfAction_Type = ShelfAction
_ShelfAction_Object = MibTableColumn
shelfAction = _ShelfAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 7),
    _ShelfAction_Type()
)
shelfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfAction.setStatus("current")
_ShelfAdminState_Type = AdminState
_ShelfAdminState_Object = MibTableColumn
shelfAdminState = _ShelfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 8),
    _ShelfAdminState_Type()
)
shelfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfAdminState.setStatus("current")
_ShelfOperationalState_Type = OperationalState
_ShelfOperationalState_Object = MibTableColumn
shelfOperationalState = _ShelfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 9),
    _ShelfOperationalState_Type()
)
shelfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfOperationalState.setStatus("current")
_ShelfSecondaryState_Type = SecondaryState
_ShelfSecondaryState_Object = MibTableColumn
shelfSecondaryState = _ShelfSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 10),
    _ShelfSecondaryState_Type()
)
shelfSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSecondaryState.setStatus("current")


class _ShelfMfgSite_Type(DisplayString):
    """Custom type shelfMfgSite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfMfgSite_Type.__name__ = "DisplayString"
_ShelfMfgSite_Object = MibTableColumn
shelfMfgSite = _ShelfMfgSite_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 11),
    _ShelfMfgSite_Type()
)
shelfMfgSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfMfgSite.setStatus("current")


class _ShelfOscillatorType_Type(DisplayString):
    """Custom type shelfOscillatorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfOscillatorType_Type.__name__ = "DisplayString"
_ShelfOscillatorType_Object = MibTableColumn
shelfOscillatorType = _ShelfOscillatorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 12),
    _ShelfOscillatorType_Type()
)
shelfOscillatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfOscillatorType.setStatus("current")
_ShelfLedControl_Type = LedControlType
_ShelfLedControl_Object = MibTableColumn
shelfLedControl = _ShelfLedControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 2, 1, 13),
    _ShelfLedControl_Type()
)
shelfLedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfLedControl.setStatus("current")
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1)
)
slotEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("current")
_SlotEntityIndex_Type = PhysicalIndex
_SlotEntityIndex_Object = MibTableColumn
slotEntityIndex = _SlotEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 2),
    _SlotEntityIndex_Type()
)
slotEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotEntityIndex.setStatus("current")
_SlotType_Type = SlotType
_SlotType_Object = MibTableColumn
slotType = _SlotType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 3),
    _SlotType_Type()
)
slotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotType.setStatus("current")
_SlotCardType_Type = CardType
_SlotCardType_Object = MibTableColumn
slotCardType = _SlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 4),
    _SlotCardType_Type()
)
slotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardType.setStatus("current")


class _SlotCardUnitName_Type(DisplayString):
    """Custom type slotCardUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlotCardUnitName_Type.__name__ = "DisplayString"
_SlotCardUnitName_Object = MibTableColumn
slotCardUnitName = _SlotCardUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 5),
    _SlotCardUnitName_Type()
)
slotCardUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardUnitName.setStatus("current")


class _SlotCardFormatVersion_Type(DisplayString):
    """Custom type slotCardFormatVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SlotCardFormatVersion_Type.__name__ = "DisplayString"
_SlotCardFormatVersion_Object = MibTableColumn
slotCardFormatVersion = _SlotCardFormatVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 6),
    _SlotCardFormatVersion_Type()
)
slotCardFormatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFormatVersion.setStatus("current")


class _SlotCardCLEICode_Type(DisplayString):
    """Custom type slotCardCLEICode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlotCardCLEICode_Type.__name__ = "DisplayString"
_SlotCardCLEICode_Object = MibTableColumn
slotCardCLEICode = _SlotCardCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 7),
    _SlotCardCLEICode_Type()
)
slotCardCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardCLEICode.setStatus("current")


class _SlotCardPartNumber_Type(DisplayString):
    """Custom type slotCardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlotCardPartNumber_Type.__name__ = "DisplayString"
_SlotCardPartNumber_Object = MibTableColumn
slotCardPartNumber = _SlotCardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 8),
    _SlotCardPartNumber_Type()
)
slotCardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardPartNumber.setStatus("current")


class _SlotCardHwRev_Type(DisplayString):
    """Custom type slotCardHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlotCardHwRev_Type.__name__ = "DisplayString"
_SlotCardHwRev_Object = MibTableColumn
slotCardHwRev = _SlotCardHwRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 9),
    _SlotCardHwRev_Type()
)
slotCardHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardHwRev.setStatus("current")


class _SlotCardSwRev_Type(DisplayString):
    """Custom type slotCardSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlotCardSwRev_Type.__name__ = "DisplayString"
_SlotCardSwRev_Object = MibTableColumn
slotCardSwRev = _SlotCardSwRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 10),
    _SlotCardSwRev_Type()
)
slotCardSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardSwRev.setStatus("current")


class _SlotCardSerialNum_Type(DisplayString):
    """Custom type slotCardSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlotCardSerialNum_Type.__name__ = "DisplayString"
_SlotCardSerialNum_Object = MibTableColumn
slotCardSerialNum = _SlotCardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 11),
    _SlotCardSerialNum_Type()
)
slotCardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardSerialNum.setStatus("current")


class _SlotCardMfgName_Type(DisplayString):
    """Custom type slotCardMfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlotCardMfgName_Type.__name__ = "DisplayString"
_SlotCardMfgName_Object = MibTableColumn
slotCardMfgName = _SlotCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 12),
    _SlotCardMfgName_Type()
)
slotCardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardMfgName.setStatus("current")
_SlotCardMfgDate_Type = DateAndTime
_SlotCardMfgDate_Object = MibTableColumn
slotCardMfgDate = _SlotCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 13),
    _SlotCardMfgDate_Type()
)
slotCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardMfgDate.setStatus("current")


class _SlotCardMfgSite_Type(DisplayString):
    """Custom type slotCardMfgSite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlotCardMfgSite_Type.__name__ = "DisplayString"
_SlotCardMfgSite_Object = MibTableColumn
slotCardMfgSite = _SlotCardMfgSite_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 14),
    _SlotCardMfgSite_Type()
)
slotCardMfgSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardMfgSite.setStatus("current")
_SlotSecondaryState_Type = SecondaryState
_SlotSecondaryState_Object = MibTableColumn
slotSecondaryState = _SlotSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 15),
    _SlotSecondaryState_Type()
)
slotSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSecondaryState.setStatus("current")


class _SlotCardPhysicalAddress_Type(DisplayString):
    """Custom type slotCardPhysicalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlotCardPhysicalAddress_Type.__name__ = "DisplayString"
_SlotCardPhysicalAddress_Object = MibTableColumn
slotCardPhysicalAddress = _SlotCardPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 3, 1, 16),
    _SlotCardPhysicalAddress_Type()
)
slotCardPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardPhysicalAddress.setStatus("current")
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1)
)
psuEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")
_PsuEntityIndex_Type = PhysicalIndex
_PsuEntityIndex_Object = MibTableColumn
psuEntityIndex = _PsuEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 1),
    _PsuEntityIndex_Type()
)
psuEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuEntityIndex.setStatus("current")
_PsuType_Type = PsuType
_PsuType_Object = MibTableColumn
psuType = _PsuType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 2),
    _PsuType_Type()
)
psuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuType.setStatus("current")
_PsuAdminState_Type = AdminState
_PsuAdminState_Object = MibTableColumn
psuAdminState = _PsuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 3),
    _PsuAdminState_Type()
)
psuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psuAdminState.setStatus("current")
_PsuOperationalState_Type = OperationalState
_PsuOperationalState_Object = MibTableColumn
psuOperationalState = _PsuOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 4),
    _PsuOperationalState_Type()
)
psuOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuOperationalState.setStatus("current")
_PsuSecondaryState_Type = SecondaryState
_PsuSecondaryState_Object = MibTableColumn
psuSecondaryState = _PsuSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 5),
    _PsuSecondaryState_Type()
)
psuSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuSecondaryState.setStatus("current")
_PsuOutputVoltage_Type = Integer32
_PsuOutputVoltage_Object = MibTableColumn
psuOutputVoltage = _PsuOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 6),
    _PsuOutputVoltage_Type()
)
psuOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuOutputVoltage.setStatus("current")
_PsuTemperature_Type = Integer32
_PsuTemperature_Object = MibTableColumn
psuTemperature = _PsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 7),
    _PsuTemperature_Type()
)
psuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuTemperature.setStatus("current")
_PsuOutputCurrent_Type = Integer32
_PsuOutputCurrent_Object = MibTableColumn
psuOutputCurrent = _PsuOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 8),
    _PsuOutputCurrent_Type()
)
psuOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuOutputCurrent.setStatus("current")
_PsuStorageType_Type = StorageType
_PsuStorageType_Object = MibTableColumn
psuStorageType = _PsuStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 9),
    _PsuStorageType_Type()
)
psuStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    psuStorageType.setStatus("current")
_PsuRowStatus_Type = RowStatus
_PsuRowStatus_Object = MibTableColumn
psuRowStatus = _PsuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 4, 1, 10),
    _PsuRowStatus_Type()
)
psuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    psuRowStatus.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1)
)
fanEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanEntityIndex_Type = PhysicalIndex
_FanEntityIndex_Object = MibTableColumn
fanEntityIndex = _FanEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1, 1),
    _FanEntityIndex_Type()
)
fanEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanEntityIndex.setStatus("current")
_FanAdminState_Type = AdminState
_FanAdminState_Object = MibTableColumn
fanAdminState = _FanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1, 2),
    _FanAdminState_Type()
)
fanAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanAdminState.setStatus("current")
_FanOperationalState_Type = OperationalState
_FanOperationalState_Object = MibTableColumn
fanOperationalState = _FanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1, 3),
    _FanOperationalState_Type()
)
fanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanOperationalState.setStatus("current")
_FanSecondaryState_Type = SecondaryState
_FanSecondaryState_Object = MibTableColumn
fanSecondaryState = _FanSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1, 4),
    _FanSecondaryState_Type()
)
fanSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSecondaryState.setStatus("current")
_FanStorageType_Type = StorageType
_FanStorageType_Object = MibTableColumn
fanStorageType = _FanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1, 5),
    _FanStorageType_Type()
)
fanStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fanStorageType.setStatus("current")
_FanRowStatus_Type = RowStatus
_FanRowStatus_Object = MibTableColumn
fanRowStatus = _FanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 5, 1, 6),
    _FanRowStatus_Type()
)
fanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fanRowStatus.setStatus("current")
_ScuTable_Object = MibTable
scuTable = _ScuTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6)
)
if mibBuilder.loadTexts:
    scuTable.setStatus("current")
_ScuEntry_Object = MibTableRow
scuEntry = _ScuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1)
)
scuEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    scuEntry.setStatus("current")
_ScuEntityIndex_Type = PhysicalIndex
_ScuEntityIndex_Object = MibTableColumn
scuEntityIndex = _ScuEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 1),
    _ScuEntityIndex_Type()
)
scuEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuEntityIndex.setStatus("current")
_ScuAdminState_Type = AdminState
_ScuAdminState_Object = MibTableColumn
scuAdminState = _ScuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 2),
    _ScuAdminState_Type()
)
scuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scuAdminState.setStatus("current")
_ScuOperationalState_Type = OperationalState
_ScuOperationalState_Object = MibTableColumn
scuOperationalState = _ScuOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 3),
    _ScuOperationalState_Type()
)
scuOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuOperationalState.setStatus("current")
_ScuSecondaryState_Type = SecondaryState
_ScuSecondaryState_Object = MibTableColumn
scuSecondaryState = _ScuSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 4),
    _ScuSecondaryState_Type()
)
scuSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuSecondaryState.setStatus("current")
_ScuVoltage_Type = Integer32
_ScuVoltage_Object = MibTableColumn
scuVoltage = _ScuVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 5),
    _ScuVoltage_Type()
)
scuVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuVoltage.setStatus("current")
_ScuTemperature_Type = Integer32
_ScuTemperature_Object = MibTableColumn
scuTemperature = _ScuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 6),
    _ScuTemperature_Type()
)
scuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuTemperature.setStatus("current")
_ScuRestartAction_Type = RestartType
_ScuRestartAction_Object = MibTableColumn
scuRestartAction = _ScuRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 7),
    _ScuRestartAction_Type()
)
scuRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scuRestartAction.setStatus("current")
_ScuStorageType_Type = StorageType
_ScuStorageType_Object = MibTableColumn
scuStorageType = _ScuStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 8),
    _ScuStorageType_Type()
)
scuStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scuStorageType.setStatus("current")
_ScuRowStatus_Type = RowStatus
_ScuRowStatus_Object = MibTableColumn
scuRowStatus = _ScuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 9),
    _ScuRowStatus_Type()
)
scuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scuRowStatus.setStatus("current")
_ScuFlashModelNum_Type = DisplayString
_ScuFlashModelNum_Object = MibTableColumn
scuFlashModelNum = _ScuFlashModelNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 10),
    _ScuFlashModelNum_Type()
)
scuFlashModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuFlashModelNum.setStatus("current")
_ScuFlashFirmwareRev_Type = DisplayString
_ScuFlashFirmwareRev_Object = MibTableColumn
scuFlashFirmwareRev = _ScuFlashFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 11),
    _ScuFlashFirmwareRev_Type()
)
scuFlashFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuFlashFirmwareRev.setStatus("current")
_ScuFlashSerialNum_Type = DisplayString
_ScuFlashSerialNum_Object = MibTableColumn
scuFlashSerialNum = _ScuFlashSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 6, 1, 12),
    _ScuFlashSerialNum_Type()
)
scuFlashSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuFlashSerialNum.setStatus("current")
_NemiTable_Object = MibTable
nemiTable = _NemiTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7)
)
if mibBuilder.loadTexts:
    nemiTable.setStatus("current")
_NemiEntry_Object = MibTableRow
nemiEntry = _NemiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1)
)
nemiEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    nemiEntry.setStatus("current")
_NemiEntityIndex_Type = PhysicalIndex
_NemiEntityIndex_Object = MibTableColumn
nemiEntityIndex = _NemiEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 1),
    _NemiEntityIndex_Type()
)
nemiEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiEntityIndex.setStatus("current")
_NemiAdminState_Type = AdminState
_NemiAdminState_Object = MibTableColumn
nemiAdminState = _NemiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 2),
    _NemiAdminState_Type()
)
nemiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nemiAdminState.setStatus("current")
_NemiOperationalState_Type = OperationalState
_NemiOperationalState_Object = MibTableColumn
nemiOperationalState = _NemiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 3),
    _NemiOperationalState_Type()
)
nemiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiOperationalState.setStatus("current")
_NemiSecondaryState_Type = SecondaryState
_NemiSecondaryState_Object = MibTableColumn
nemiSecondaryState = _NemiSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 4),
    _NemiSecondaryState_Type()
)
nemiSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiSecondaryState.setStatus("current")
_NemiVoltage_Type = Integer32
_NemiVoltage_Object = MibTableColumn
nemiVoltage = _NemiVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 5),
    _NemiVoltage_Type()
)
nemiVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiVoltage.setStatus("current")
_NemiTemperature_Type = Integer32
_NemiTemperature_Object = MibTableColumn
nemiTemperature = _NemiTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 6),
    _NemiTemperature_Type()
)
nemiTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiTemperature.setStatus("current")
_NemiRestartAction_Type = RestartType
_NemiRestartAction_Object = MibTableColumn
nemiRestartAction = _NemiRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 7),
    _NemiRestartAction_Type()
)
nemiRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nemiRestartAction.setStatus("current")
_NemiStorageType_Type = StorageType
_NemiStorageType_Object = MibTableColumn
nemiStorageType = _NemiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 8),
    _NemiStorageType_Type()
)
nemiStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nemiStorageType.setStatus("current")
_NemiRowStatus_Type = RowStatus
_NemiRowStatus_Object = MibTableColumn
nemiRowStatus = _NemiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 9),
    _NemiRowStatus_Type()
)
nemiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nemiRowStatus.setStatus("current")
_NemiForceOffLineAction_Type = TruthValue
_NemiForceOffLineAction_Object = MibTableColumn
nemiForceOffLineAction = _NemiForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 10),
    _NemiForceOffLineAction_Type()
)
nemiForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nemiForceOffLineAction.setStatus("current")
_NemiFlashModelNum_Type = DisplayString
_NemiFlashModelNum_Object = MibTableColumn
nemiFlashModelNum = _NemiFlashModelNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 11),
    _NemiFlashModelNum_Type()
)
nemiFlashModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiFlashModelNum.setStatus("current")
_NemiFlashFirmwareRev_Type = DisplayString
_NemiFlashFirmwareRev_Object = MibTableColumn
nemiFlashFirmwareRev = _NemiFlashFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 12),
    _NemiFlashFirmwareRev_Type()
)
nemiFlashFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiFlashFirmwareRev.setStatus("current")
_NemiFlashSerialNum_Type = DisplayString
_NemiFlashSerialNum_Object = MibTableColumn
nemiFlashSerialNum = _NemiFlashSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 7, 1, 13),
    _NemiFlashSerialNum_Type()
)
nemiFlashSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemiFlashSerialNum.setStatus("current")
_EthernetNTUCardTable_Object = MibTable
ethernetNTUCardTable = _EthernetNTUCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ethernetNTUCardTable.setStatus("current")
_EthernetNTUCardEntry_Object = MibTableRow
ethernetNTUCardEntry = _EthernetNTUCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1)
)
ethernetNTUCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTUCardEntry.setStatus("current")
_EthernetNTUCardEntityIndex_Type = PhysicalIndex
_EthernetNTUCardEntityIndex_Object = MibTableColumn
ethernetNTUCardEntityIndex = _EthernetNTUCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 1),
    _EthernetNTUCardEntityIndex_Type()
)
ethernetNTUCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTUCardEntityIndex.setStatus("current")
_EthernetNTUCardAdminState_Type = AdminState
_EthernetNTUCardAdminState_Object = MibTableColumn
ethernetNTUCardAdminState = _EthernetNTUCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 2),
    _EthernetNTUCardAdminState_Type()
)
ethernetNTUCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTUCardAdminState.setStatus("current")
_EthernetNTUCardOperationalState_Type = OperationalState
_EthernetNTUCardOperationalState_Object = MibTableColumn
ethernetNTUCardOperationalState = _EthernetNTUCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 3),
    _EthernetNTUCardOperationalState_Type()
)
ethernetNTUCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTUCardOperationalState.setStatus("current")
_EthernetNTUCardSecondaryState_Type = SecondaryState
_EthernetNTUCardSecondaryState_Object = MibTableColumn
ethernetNTUCardSecondaryState = _EthernetNTUCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 4),
    _EthernetNTUCardSecondaryState_Type()
)
ethernetNTUCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTUCardSecondaryState.setStatus("current")
_EthernetNTUCardVoltage_Type = Integer32
_EthernetNTUCardVoltage_Object = MibTableColumn
ethernetNTUCardVoltage = _EthernetNTUCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 5),
    _EthernetNTUCardVoltage_Type()
)
ethernetNTUCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTUCardVoltage.setStatus("current")
_EthernetNTUCardTemperature_Type = Integer32
_EthernetNTUCardTemperature_Object = MibTableColumn
ethernetNTUCardTemperature = _EthernetNTUCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 6),
    _EthernetNTUCardTemperature_Type()
)
ethernetNTUCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTUCardTemperature.setStatus("current")
_EthernetNTUCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTUCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTUCardSnmpDyingGaspEnabled = _EthernetNTUCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 7),
    _EthernetNTUCardSnmpDyingGaspEnabled_Type()
)
ethernetNTUCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTUCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTUCardRestartAction_Type = RestartType
_EthernetNTUCardRestartAction_Object = MibTableColumn
ethernetNTUCardRestartAction = _EthernetNTUCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 8),
    _EthernetNTUCardRestartAction_Type()
)
ethernetNTUCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTUCardRestartAction.setStatus("current")
_EthernetNTUCardStorageType_Type = StorageType
_EthernetNTUCardStorageType_Object = MibTableColumn
ethernetNTUCardStorageType = _EthernetNTUCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 9),
    _EthernetNTUCardStorageType_Type()
)
ethernetNTUCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTUCardStorageType.setStatus("current")
_EthernetNTUCardRowStatus_Type = RowStatus
_EthernetNTUCardRowStatus_Object = MibTableColumn
ethernetNTUCardRowStatus = _EthernetNTUCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 8, 1, 10),
    _EthernetNTUCardRowStatus_Type()
)
ethernetNTUCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTUCardRowStatus.setStatus("current")
_EthernetCPMRCardTable_Object = MibTable
ethernetCPMRCardTable = _EthernetCPMRCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9)
)
if mibBuilder.loadTexts:
    ethernetCPMRCardTable.setStatus("current")
_EthernetCPMRCardEntry_Object = MibTableRow
ethernetCPMRCardEntry = _EthernetCPMRCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1)
)
ethernetCPMRCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetCPMRCardEntry.setStatus("current")
_EthernetCPMRCardEntityIndex_Type = PhysicalIndex
_EthernetCPMRCardEntityIndex_Object = MibTableColumn
ethernetCPMRCardEntityIndex = _EthernetCPMRCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 1),
    _EthernetCPMRCardEntityIndex_Type()
)
ethernetCPMRCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardEntityIndex.setStatus("current")
_EthernetCPMRCardAdminState_Type = AdminState
_EthernetCPMRCardAdminState_Object = MibTableColumn
ethernetCPMRCardAdminState = _EthernetCPMRCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 2),
    _EthernetCPMRCardAdminState_Type()
)
ethernetCPMRCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCPMRCardAdminState.setStatus("current")
_EthernetCPMRCardOperationalState_Type = OperationalState
_EthernetCPMRCardOperationalState_Object = MibTableColumn
ethernetCPMRCardOperationalState = _EthernetCPMRCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 3),
    _EthernetCPMRCardOperationalState_Type()
)
ethernetCPMRCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardOperationalState.setStatus("current")
_EthernetCPMRCardSecondaryState_Type = SecondaryState
_EthernetCPMRCardSecondaryState_Object = MibTableColumn
ethernetCPMRCardSecondaryState = _EthernetCPMRCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 4),
    _EthernetCPMRCardSecondaryState_Type()
)
ethernetCPMRCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardSecondaryState.setStatus("current")
_EthernetCPMRCardVoltage_Type = Integer32
_EthernetCPMRCardVoltage_Object = MibTableColumn
ethernetCPMRCardVoltage = _EthernetCPMRCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 5),
    _EthernetCPMRCardVoltage_Type()
)
ethernetCPMRCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardVoltage.setStatus("current")
_EthernetCPMRCardTemperature_Type = Integer32
_EthernetCPMRCardTemperature_Object = MibTableColumn
ethernetCPMRCardTemperature = _EthernetCPMRCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 6),
    _EthernetCPMRCardTemperature_Type()
)
ethernetCPMRCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardTemperature.setStatus("current")
_EthernetCPMRCardRestartAction_Type = RestartType
_EthernetCPMRCardRestartAction_Object = MibTableColumn
ethernetCPMRCardRestartAction = _EthernetCPMRCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 7),
    _EthernetCPMRCardRestartAction_Type()
)
ethernetCPMRCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCPMRCardRestartAction.setStatus("current")
_EthernetCPMRCardPSU1State_Type = OperationalState
_EthernetCPMRCardPSU1State_Object = MibTableColumn
ethernetCPMRCardPSU1State = _EthernetCPMRCardPSU1State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 8),
    _EthernetCPMRCardPSU1State_Type()
)
ethernetCPMRCardPSU1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardPSU1State.setStatus("current")
_EthernetCPMRCardPSU2State_Type = OperationalState
_EthernetCPMRCardPSU2State_Object = MibTableColumn
ethernetCPMRCardPSU2State = _EthernetCPMRCardPSU2State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 9),
    _EthernetCPMRCardPSU2State_Type()
)
ethernetCPMRCardPSU2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardPSU2State.setStatus("current")
_EthernetCPMRCardFAN1State_Type = OperationalState
_EthernetCPMRCardFAN1State_Object = MibTableColumn
ethernetCPMRCardFAN1State = _EthernetCPMRCardFAN1State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 10),
    _EthernetCPMRCardFAN1State_Type()
)
ethernetCPMRCardFAN1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardFAN1State.setStatus("current")
_EthernetCPMRCardFAN2State_Type = OperationalState
_EthernetCPMRCardFAN2State_Object = MibTableColumn
ethernetCPMRCardFAN2State = _EthernetCPMRCardFAN2State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 11),
    _EthernetCPMRCardFAN2State_Type()
)
ethernetCPMRCardFAN2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardFAN2State.setStatus("current")
_EthernetCPMRCardPsuType_Type = PsuType
_EthernetCPMRCardPsuType_Object = MibTableColumn
ethernetCPMRCardPsuType = _EthernetCPMRCardPsuType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 12),
    _EthernetCPMRCardPsuType_Type()
)
ethernetCPMRCardPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardPsuType.setStatus("current")
_EthernetCPMRCardLLFMode_Type = CmCPMRLinkLossFwdMode
_EthernetCPMRCardLLFMode_Object = MibTableColumn
ethernetCPMRCardLLFMode = _EthernetCPMRCardLLFMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 13),
    _EthernetCPMRCardLLFMode_Type()
)
ethernetCPMRCardLLFMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCPMRCardLLFMode.setStatus("current")
_EthernetCPMRCardLLFModeAction_Type = CmCPMRLinkLossFwdMode
_EthernetCPMRCardLLFModeAction_Object = MibTableColumn
ethernetCPMRCardLLFModeAction = _EthernetCPMRCardLLFModeAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 9, 1, 14),
    _EthernetCPMRCardLLFModeAction_Type()
)
ethernetCPMRCardLLFModeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCPMRCardLLFModeAction.setStatus("current")
_EthernetNTEGE101CardTable_Object = MibTable
ethernetNTEGE101CardTable = _EthernetNTEGE101CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ethernetNTEGE101CardTable.setStatus("current")
_EthernetNTEGE101CardEntry_Object = MibTableRow
ethernetNTEGE101CardEntry = _EthernetNTEGE101CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1)
)
ethernetNTEGE101CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE101CardEntry.setStatus("current")
_EthernetNTEGE101CardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE101CardEntityIndex_Object = MibTableColumn
ethernetNTEGE101CardEntityIndex = _EthernetNTEGE101CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 1),
    _EthernetNTEGE101CardEntityIndex_Type()
)
ethernetNTEGE101CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardEntityIndex.setStatus("current")
_EthernetNTEGE101CardAdminState_Type = AdminState
_EthernetNTEGE101CardAdminState_Object = MibTableColumn
ethernetNTEGE101CardAdminState = _EthernetNTEGE101CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 2),
    _EthernetNTEGE101CardAdminState_Type()
)
ethernetNTEGE101CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardAdminState.setStatus("current")
_EthernetNTEGE101CardOperationalState_Type = OperationalState
_EthernetNTEGE101CardOperationalState_Object = MibTableColumn
ethernetNTEGE101CardOperationalState = _EthernetNTEGE101CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 3),
    _EthernetNTEGE101CardOperationalState_Type()
)
ethernetNTEGE101CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardOperationalState.setStatus("current")
_EthernetNTEGE101CardSecondaryState_Type = SecondaryState
_EthernetNTEGE101CardSecondaryState_Object = MibTableColumn
ethernetNTEGE101CardSecondaryState = _EthernetNTEGE101CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 4),
    _EthernetNTEGE101CardSecondaryState_Type()
)
ethernetNTEGE101CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardSecondaryState.setStatus("current")
_EthernetNTEGE101CardVoltage_Type = Integer32
_EthernetNTEGE101CardVoltage_Object = MibTableColumn
ethernetNTEGE101CardVoltage = _EthernetNTEGE101CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 5),
    _EthernetNTEGE101CardVoltage_Type()
)
ethernetNTEGE101CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardVoltage.setStatus("current")
_EthernetNTEGE101CardTemperature_Type = Integer32
_EthernetNTEGE101CardTemperature_Object = MibTableColumn
ethernetNTEGE101CardTemperature = _EthernetNTEGE101CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 6),
    _EthernetNTEGE101CardTemperature_Type()
)
ethernetNTEGE101CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardTemperature.setStatus("current")
_EthernetNTEGE101CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE101CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE101CardSnmpDyingGaspEnabled = _EthernetNTEGE101CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 7),
    _EthernetNTEGE101CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE101CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE101CardRestartAction_Type = RestartType
_EthernetNTEGE101CardRestartAction_Object = MibTableColumn
ethernetNTEGE101CardRestartAction = _EthernetNTEGE101CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 10, 1, 8),
    _EthernetNTEGE101CardRestartAction_Type()
)
ethernetNTEGE101CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101CardRestartAction.setStatus("current")
_EthernetNTEGE206CardTable_Object = MibTable
ethernetNTEGE206CardTable = _EthernetNTEGE206CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11)
)
if mibBuilder.loadTexts:
    ethernetNTEGE206CardTable.setStatus("current")
_EthernetNTEGE206CardEntry_Object = MibTableRow
ethernetNTEGE206CardEntry = _EthernetNTEGE206CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1)
)
ethernetNTEGE206CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE206CardEntry.setStatus("current")
_EthernetNTEGE206CardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE206CardEntityIndex_Object = MibTableColumn
ethernetNTEGE206CardEntityIndex = _EthernetNTEGE206CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 1),
    _EthernetNTEGE206CardEntityIndex_Type()
)
ethernetNTEGE206CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardEntityIndex.setStatus("current")
_EthernetNTEGE206CardAdminState_Type = AdminState
_EthernetNTEGE206CardAdminState_Object = MibTableColumn
ethernetNTEGE206CardAdminState = _EthernetNTEGE206CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 2),
    _EthernetNTEGE206CardAdminState_Type()
)
ethernetNTEGE206CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardAdminState.setStatus("current")
_EthernetNTEGE206CardOperationalState_Type = OperationalState
_EthernetNTEGE206CardOperationalState_Object = MibTableColumn
ethernetNTEGE206CardOperationalState = _EthernetNTEGE206CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 3),
    _EthernetNTEGE206CardOperationalState_Type()
)
ethernetNTEGE206CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardOperationalState.setStatus("current")
_EthernetNTEGE206CardSecondaryState_Type = SecondaryState
_EthernetNTEGE206CardSecondaryState_Object = MibTableColumn
ethernetNTEGE206CardSecondaryState = _EthernetNTEGE206CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 4),
    _EthernetNTEGE206CardSecondaryState_Type()
)
ethernetNTEGE206CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardSecondaryState.setStatus("current")
_EthernetNTEGE206CardVoltage_Type = Integer32
_EthernetNTEGE206CardVoltage_Object = MibTableColumn
ethernetNTEGE206CardVoltage = _EthernetNTEGE206CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 5),
    _EthernetNTEGE206CardVoltage_Type()
)
ethernetNTEGE206CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardVoltage.setStatus("current")
_EthernetNTEGE206CardTemperature_Type = Integer32
_EthernetNTEGE206CardTemperature_Object = MibTableColumn
ethernetNTEGE206CardTemperature = _EthernetNTEGE206CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 6),
    _EthernetNTEGE206CardTemperature_Type()
)
ethernetNTEGE206CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardTemperature.setStatus("current")
_EthernetNTEGE206CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE206CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE206CardSnmpDyingGaspEnabled = _EthernetNTEGE206CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 7),
    _EthernetNTEGE206CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE206CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE206CardRestartAction_Type = RestartType
_EthernetNTEGE206CardRestartAction_Object = MibTableColumn
ethernetNTEGE206CardRestartAction = _EthernetNTEGE206CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 8),
    _EthernetNTEGE206CardRestartAction_Type()
)
ethernetNTEGE206CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardRestartAction.setStatus("current")
_EthernetNTEGE206CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE206CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE206CardFineGrainedPmInterval = _EthernetNTEGE206CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 11, 1, 9),
    _EthernetNTEGE206CardFineGrainedPmInterval_Type()
)
ethernetNTEGE206CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206CardFineGrainedPmInterval.setStatus("current")
_PseudoWireE3CardTable_Object = MibTable
pseudoWireE3CardTable = _PseudoWireE3CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12)
)
if mibBuilder.loadTexts:
    pseudoWireE3CardTable.setStatus("obsolete")
_PseudoWireE3CardEntry_Object = MibTableRow
pseudoWireE3CardEntry = _PseudoWireE3CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1)
)
pseudoWireE3CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    pseudoWireE3CardEntry.setStatus("obsolete")
_PseudoWireE3CardEntityIndex_Type = PhysicalIndex
_PseudoWireE3CardEntityIndex_Object = MibTableColumn
pseudoWireE3CardEntityIndex = _PseudoWireE3CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 1),
    _PseudoWireE3CardEntityIndex_Type()
)
pseudoWireE3CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE3CardEntityIndex.setStatus("obsolete")
_PseudoWireE3CardAdminState_Type = AdminState
_PseudoWireE3CardAdminState_Object = MibTableColumn
pseudoWireE3CardAdminState = _PseudoWireE3CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 2),
    _PseudoWireE3CardAdminState_Type()
)
pseudoWireE3CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardAdminState.setStatus("obsolete")
_PseudoWireE3CardOperationalState_Type = OperationalState
_PseudoWireE3CardOperationalState_Object = MibTableColumn
pseudoWireE3CardOperationalState = _PseudoWireE3CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 3),
    _PseudoWireE3CardOperationalState_Type()
)
pseudoWireE3CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE3CardOperationalState.setStatus("obsolete")
_PseudoWireE3CardSecondaryState_Type = SecondaryState
_PseudoWireE3CardSecondaryState_Object = MibTableColumn
pseudoWireE3CardSecondaryState = _PseudoWireE3CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 4),
    _PseudoWireE3CardSecondaryState_Type()
)
pseudoWireE3CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE3CardSecondaryState.setStatus("obsolete")
_PseudoWireE3CardIpAddress_Type = IpAddress
_PseudoWireE3CardIpAddress_Object = MibTableColumn
pseudoWireE3CardIpAddress = _PseudoWireE3CardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 5),
    _PseudoWireE3CardIpAddress_Type()
)
pseudoWireE3CardIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardIpAddress.setStatus("obsolete")
_PseudoWireE3CardIpNetmask_Type = IpAddress
_PseudoWireE3CardIpNetmask_Object = MibTableColumn
pseudoWireE3CardIpNetmask = _PseudoWireE3CardIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 6),
    _PseudoWireE3CardIpNetmask_Type()
)
pseudoWireE3CardIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardIpNetmask.setStatus("obsolete")
_PseudoWireE3CardIpGateway_Type = IpAddress
_PseudoWireE3CardIpGateway_Object = MibTableColumn
pseudoWireE3CardIpGateway = _PseudoWireE3CardIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 7),
    _PseudoWireE3CardIpGateway_Type()
)
pseudoWireE3CardIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardIpGateway.setStatus("obsolete")
_PseudoWireE3CardDhcpEnabled_Type = TruthValue
_PseudoWireE3CardDhcpEnabled_Object = MibTableColumn
pseudoWireE3CardDhcpEnabled = _PseudoWireE3CardDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 8),
    _PseudoWireE3CardDhcpEnabled_Type()
)
pseudoWireE3CardDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardDhcpEnabled.setStatus("obsolete")
_PseudoWireE3CardMgmtVlanId_Type = VlanId
_PseudoWireE3CardMgmtVlanId_Object = MibTableColumn
pseudoWireE3CardMgmtVlanId = _PseudoWireE3CardMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 9),
    _PseudoWireE3CardMgmtVlanId_Type()
)
pseudoWireE3CardMgmtVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardMgmtVlanId.setStatus("obsolete")
_PseudoWireE3CardTimeOfDay_Type = DateAndTime
_PseudoWireE3CardTimeOfDay_Object = MibTableColumn
pseudoWireE3CardTimeOfDay = _PseudoWireE3CardTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 10),
    _PseudoWireE3CardTimeOfDay_Type()
)
pseudoWireE3CardTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardTimeOfDay.setStatus("obsolete")
_PseudoWireE3CardRestartAction_Type = RestartType
_PseudoWireE3CardRestartAction_Object = MibTableColumn
pseudoWireE3CardRestartAction = _PseudoWireE3CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 12, 1, 11),
    _PseudoWireE3CardRestartAction_Type()
)
pseudoWireE3CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE3CardRestartAction.setStatus("obsolete")
_ScuTTable_Object = MibTable
scuTTable = _ScuTTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13)
)
if mibBuilder.loadTexts:
    scuTTable.setStatus("current")
_ScuTEntry_Object = MibTableRow
scuTEntry = _ScuTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1)
)
scuTEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    scuTEntry.setStatus("current")
_ScuTEntityIndex_Type = PhysicalIndex
_ScuTEntityIndex_Object = MibTableColumn
scuTEntityIndex = _ScuTEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 1),
    _ScuTEntityIndex_Type()
)
scuTEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuTEntityIndex.setStatus("current")
_ScuTAdminState_Type = AdminState
_ScuTAdminState_Object = MibTableColumn
scuTAdminState = _ScuTAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 2),
    _ScuTAdminState_Type()
)
scuTAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scuTAdminState.setStatus("current")
_ScuTOperationalState_Type = OperationalState
_ScuTOperationalState_Object = MibTableColumn
scuTOperationalState = _ScuTOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 3),
    _ScuTOperationalState_Type()
)
scuTOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuTOperationalState.setStatus("current")
_ScuTSecondaryState_Type = SecondaryState
_ScuTSecondaryState_Object = MibTableColumn
scuTSecondaryState = _ScuTSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 4),
    _ScuTSecondaryState_Type()
)
scuTSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuTSecondaryState.setStatus("current")
_ScuTVoltage_Type = Integer32
_ScuTVoltage_Object = MibTableColumn
scuTVoltage = _ScuTVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 5),
    _ScuTVoltage_Type()
)
scuTVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuTVoltage.setStatus("current")
_ScuTTemperature_Type = Integer32
_ScuTTemperature_Object = MibTableColumn
scuTTemperature = _ScuTTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 6),
    _ScuTTemperature_Type()
)
scuTTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scuTTemperature.setStatus("current")
_ScuTRestartAction_Type = RestartType
_ScuTRestartAction_Object = MibTableColumn
scuTRestartAction = _ScuTRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 7),
    _ScuTRestartAction_Type()
)
scuTRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scuTRestartAction.setStatus("current")
_ScuTStorageType_Type = StorageType
_ScuTStorageType_Object = MibTableColumn
scuTStorageType = _ScuTStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 8),
    _ScuTStorageType_Type()
)
scuTStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scuTStorageType.setStatus("current")
_ScuTRowStatus_Type = RowStatus
_ScuTRowStatus_Object = MibTableColumn
scuTRowStatus = _ScuTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 13, 1, 9),
    _ScuTRowStatus_Type()
)
scuTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scuTRowStatus.setStatus("current")
_EthernetNTECardTable_Object = MibTable
ethernetNTECardTable = _EthernetNTECardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14)
)
if mibBuilder.loadTexts:
    ethernetNTECardTable.setStatus("current")
_EthernetNTECardEntry_Object = MibTableRow
ethernetNTECardEntry = _EthernetNTECardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1)
)
ethernetNTECardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTECardEntry.setStatus("current")
_EthernetNTECardEntityIndex_Type = PhysicalIndex
_EthernetNTECardEntityIndex_Object = MibTableColumn
ethernetNTECardEntityIndex = _EthernetNTECardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 1),
    _EthernetNTECardEntityIndex_Type()
)
ethernetNTECardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECardEntityIndex.setStatus("current")
_EthernetNTECardAdminState_Type = AdminState
_EthernetNTECardAdminState_Object = MibTableColumn
ethernetNTECardAdminState = _EthernetNTECardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 2),
    _EthernetNTECardAdminState_Type()
)
ethernetNTECardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECardAdminState.setStatus("current")
_EthernetNTECardOperationalState_Type = OperationalState
_EthernetNTECardOperationalState_Object = MibTableColumn
ethernetNTECardOperationalState = _EthernetNTECardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 3),
    _EthernetNTECardOperationalState_Type()
)
ethernetNTECardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECardOperationalState.setStatus("current")
_EthernetNTECardSecondaryState_Type = SecondaryState
_EthernetNTECardSecondaryState_Object = MibTableColumn
ethernetNTECardSecondaryState = _EthernetNTECardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 4),
    _EthernetNTECardSecondaryState_Type()
)
ethernetNTECardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECardSecondaryState.setStatus("current")
_EthernetNTECardVoltage_Type = Integer32
_EthernetNTECardVoltage_Object = MibTableColumn
ethernetNTECardVoltage = _EthernetNTECardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 5),
    _EthernetNTECardVoltage_Type()
)
ethernetNTECardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECardVoltage.setStatus("current")
_EthernetNTECardTemperature_Type = Integer32
_EthernetNTECardTemperature_Object = MibTableColumn
ethernetNTECardTemperature = _EthernetNTECardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 6),
    _EthernetNTECardTemperature_Type()
)
ethernetNTECardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECardTemperature.setStatus("current")
_EthernetNTECardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTECardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTECardSnmpDyingGaspEnabled = _EthernetNTECardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 7),
    _EthernetNTECardSnmpDyingGaspEnabled_Type()
)
ethernetNTECardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTECardRestartAction_Type = RestartType
_EthernetNTECardRestartAction_Object = MibTableColumn
ethernetNTECardRestartAction = _EthernetNTECardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 8),
    _EthernetNTECardRestartAction_Type()
)
ethernetNTECardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECardRestartAction.setStatus("current")
_EthernetNTECardStorageType_Type = StorageType
_EthernetNTECardStorageType_Object = MibTableColumn
ethernetNTECardStorageType = _EthernetNTECardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 9),
    _EthernetNTECardStorageType_Type()
)
ethernetNTECardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTECardStorageType.setStatus("current")
_EthernetNTECardRowStatus_Type = RowStatus
_EthernetNTECardRowStatus_Object = MibTableColumn
ethernetNTECardRowStatus = _EthernetNTECardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 14, 1, 10),
    _EthernetNTECardRowStatus_Type()
)
ethernetNTECardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTECardRowStatus.setStatus("current")
_EthernetNTEGE201CardTable_Object = MibTable
ethernetNTEGE201CardTable = _EthernetNTEGE201CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15)
)
if mibBuilder.loadTexts:
    ethernetNTEGE201CardTable.setStatus("current")
_EthernetNTEGE201CardEntry_Object = MibTableRow
ethernetNTEGE201CardEntry = _EthernetNTEGE201CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1)
)
ethernetNTEGE201CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE201CardEntry.setStatus("current")
_EthernetNTEGE201CardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE201CardEntityIndex_Object = MibTableColumn
ethernetNTEGE201CardEntityIndex = _EthernetNTEGE201CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 1),
    _EthernetNTEGE201CardEntityIndex_Type()
)
ethernetNTEGE201CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardEntityIndex.setStatus("current")
_EthernetNTEGE201CardAdminState_Type = AdminState
_EthernetNTEGE201CardAdminState_Object = MibTableColumn
ethernetNTEGE201CardAdminState = _EthernetNTEGE201CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 2),
    _EthernetNTEGE201CardAdminState_Type()
)
ethernetNTEGE201CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardAdminState.setStatus("current")
_EthernetNTEGE201CardOperationalState_Type = OperationalState
_EthernetNTEGE201CardOperationalState_Object = MibTableColumn
ethernetNTEGE201CardOperationalState = _EthernetNTEGE201CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 3),
    _EthernetNTEGE201CardOperationalState_Type()
)
ethernetNTEGE201CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardOperationalState.setStatus("current")
_EthernetNTEGE201CardSecondaryState_Type = SecondaryState
_EthernetNTEGE201CardSecondaryState_Object = MibTableColumn
ethernetNTEGE201CardSecondaryState = _EthernetNTEGE201CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 4),
    _EthernetNTEGE201CardSecondaryState_Type()
)
ethernetNTEGE201CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardSecondaryState.setStatus("current")
_EthernetNTEGE201CardVoltage_Type = Integer32
_EthernetNTEGE201CardVoltage_Object = MibTableColumn
ethernetNTEGE201CardVoltage = _EthernetNTEGE201CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 5),
    _EthernetNTEGE201CardVoltage_Type()
)
ethernetNTEGE201CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardVoltage.setStatus("current")
_EthernetNTEGE201CardTemperature_Type = Integer32
_EthernetNTEGE201CardTemperature_Object = MibTableColumn
ethernetNTEGE201CardTemperature = _EthernetNTEGE201CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 6),
    _EthernetNTEGE201CardTemperature_Type()
)
ethernetNTEGE201CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardTemperature.setStatus("current")
_EthernetNTEGE201CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE201CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE201CardSnmpDyingGaspEnabled = _EthernetNTEGE201CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 7),
    _EthernetNTEGE201CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE201CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE201CardRestartAction_Type = RestartType
_EthernetNTEGE201CardRestartAction_Object = MibTableColumn
ethernetNTEGE201CardRestartAction = _EthernetNTEGE201CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 8),
    _EthernetNTEGE201CardRestartAction_Type()
)
ethernetNTEGE201CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardRestartAction.setStatus("current")
_EthernetNTEGE201CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE201CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE201CardFineGrainedPmInterval = _EthernetNTEGE201CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 15, 1, 9),
    _EthernetNTEGE201CardFineGrainedPmInterval_Type()
)
ethernetNTEGE201CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE201SyncECardTable_Object = MibTable
ethernetNTEGE201SyncECardTable = _EthernetNTEGE201SyncECardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16)
)
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardTable.setStatus("current")
_EthernetNTEGE201SyncECardEntry_Object = MibTableRow
ethernetNTEGE201SyncECardEntry = _EthernetNTEGE201SyncECardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1)
)
ethernetNTEGE201SyncECardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardEntry.setStatus("current")
_EthernetNTEGE201SyncECardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE201SyncECardEntityIndex_Object = MibTableColumn
ethernetNTEGE201SyncECardEntityIndex = _EthernetNTEGE201SyncECardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 1),
    _EthernetNTEGE201SyncECardEntityIndex_Type()
)
ethernetNTEGE201SyncECardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardEntityIndex.setStatus("current")
_EthernetNTEGE201SyncECardAdminState_Type = AdminState
_EthernetNTEGE201SyncECardAdminState_Object = MibTableColumn
ethernetNTEGE201SyncECardAdminState = _EthernetNTEGE201SyncECardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 2),
    _EthernetNTEGE201SyncECardAdminState_Type()
)
ethernetNTEGE201SyncECardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardAdminState.setStatus("current")
_EthernetNTEGE201SyncECardOperationalState_Type = OperationalState
_EthernetNTEGE201SyncECardOperationalState_Object = MibTableColumn
ethernetNTEGE201SyncECardOperationalState = _EthernetNTEGE201SyncECardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 3),
    _EthernetNTEGE201SyncECardOperationalState_Type()
)
ethernetNTEGE201SyncECardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardOperationalState.setStatus("current")
_EthernetNTEGE201SyncECardSecondaryState_Type = SecondaryState
_EthernetNTEGE201SyncECardSecondaryState_Object = MibTableColumn
ethernetNTEGE201SyncECardSecondaryState = _EthernetNTEGE201SyncECardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 4),
    _EthernetNTEGE201SyncECardSecondaryState_Type()
)
ethernetNTEGE201SyncECardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardSecondaryState.setStatus("current")
_EthernetNTEGE201SyncECardVoltage_Type = Integer32
_EthernetNTEGE201SyncECardVoltage_Object = MibTableColumn
ethernetNTEGE201SyncECardVoltage = _EthernetNTEGE201SyncECardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 5),
    _EthernetNTEGE201SyncECardVoltage_Type()
)
ethernetNTEGE201SyncECardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardVoltage.setStatus("current")
_EthernetNTEGE201SyncECardTemperature_Type = Integer32
_EthernetNTEGE201SyncECardTemperature_Object = MibTableColumn
ethernetNTEGE201SyncECardTemperature = _EthernetNTEGE201SyncECardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 6),
    _EthernetNTEGE201SyncECardTemperature_Type()
)
ethernetNTEGE201SyncECardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardTemperature.setStatus("current")
_EthernetNTEGE201SyncECardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE201SyncECardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE201SyncECardSnmpDyingGaspEnabled = _EthernetNTEGE201SyncECardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 7),
    _EthernetNTEGE201SyncECardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE201SyncECardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE201SyncECardRestartAction_Type = RestartType
_EthernetNTEGE201SyncECardRestartAction_Object = MibTableColumn
ethernetNTEGE201SyncECardRestartAction = _EthernetNTEGE201SyncECardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 8),
    _EthernetNTEGE201SyncECardRestartAction_Type()
)
ethernetNTEGE201SyncECardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardRestartAction.setStatus("current")
_EthernetNTEGE201SyncECardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE201SyncECardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE201SyncECardFineGrainedPmInterval = _EthernetNTEGE201SyncECardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 16, 1, 9),
    _EthernetNTEGE201SyncECardFineGrainedPmInterval_Type()
)
ethernetNTEGE201SyncECardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE201SyncECardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE206FCardTable_Object = MibTable
ethernetNTEGE206FCardTable = _EthernetNTEGE206FCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17)
)
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardTable.setStatus("current")
_EthernetNTEGE206FCardEntry_Object = MibTableRow
ethernetNTEGE206FCardEntry = _EthernetNTEGE206FCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1)
)
ethernetNTEGE206FCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardEntry.setStatus("current")
_EthernetNTEGE206FCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE206FCardEntityIndex_Object = MibTableColumn
ethernetNTEGE206FCardEntityIndex = _EthernetNTEGE206FCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 1),
    _EthernetNTEGE206FCardEntityIndex_Type()
)
ethernetNTEGE206FCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardEntityIndex.setStatus("current")
_EthernetNTEGE206FCardAdminState_Type = AdminState
_EthernetNTEGE206FCardAdminState_Object = MibTableColumn
ethernetNTEGE206FCardAdminState = _EthernetNTEGE206FCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 2),
    _EthernetNTEGE206FCardAdminState_Type()
)
ethernetNTEGE206FCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardAdminState.setStatus("current")
_EthernetNTEGE206FCardOperationalState_Type = OperationalState
_EthernetNTEGE206FCardOperationalState_Object = MibTableColumn
ethernetNTEGE206FCardOperationalState = _EthernetNTEGE206FCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 3),
    _EthernetNTEGE206FCardOperationalState_Type()
)
ethernetNTEGE206FCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardOperationalState.setStatus("current")
_EthernetNTEGE206FCardSecondaryState_Type = SecondaryState
_EthernetNTEGE206FCardSecondaryState_Object = MibTableColumn
ethernetNTEGE206FCardSecondaryState = _EthernetNTEGE206FCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 4),
    _EthernetNTEGE206FCardSecondaryState_Type()
)
ethernetNTEGE206FCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardSecondaryState.setStatus("current")
_EthernetNTEGE206FCardVoltage_Type = Integer32
_EthernetNTEGE206FCardVoltage_Object = MibTableColumn
ethernetNTEGE206FCardVoltage = _EthernetNTEGE206FCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 5),
    _EthernetNTEGE206FCardVoltage_Type()
)
ethernetNTEGE206FCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardVoltage.setStatus("current")
_EthernetNTEGE206FCardTemperature_Type = Integer32
_EthernetNTEGE206FCardTemperature_Object = MibTableColumn
ethernetNTEGE206FCardTemperature = _EthernetNTEGE206FCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 6),
    _EthernetNTEGE206FCardTemperature_Type()
)
ethernetNTEGE206FCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardTemperature.setStatus("current")
_EthernetNTEGE206FCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE206FCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE206FCardSnmpDyingGaspEnabled = _EthernetNTEGE206FCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 7),
    _EthernetNTEGE206FCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE206FCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE206FCardRestartAction_Type = RestartType
_EthernetNTEGE206FCardRestartAction_Object = MibTableColumn
ethernetNTEGE206FCardRestartAction = _EthernetNTEGE206FCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 8),
    _EthernetNTEGE206FCardRestartAction_Type()
)
ethernetNTEGE206FCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardRestartAction.setStatus("current")
_EthernetNTEGE206FCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE206FCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE206FCardFineGrainedPmInterval = _EthernetNTEGE206FCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 17, 1, 9),
    _EthernetNTEGE206FCardFineGrainedPmInterval_Type()
)
ethernetNTEGE206FCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206FCardFineGrainedPmInterval.setStatus("current")
_Ethernet1x10GCardTable_Object = MibTable
ethernet1x10GCardTable = _Ethernet1x10GCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18)
)
if mibBuilder.loadTexts:
    ethernet1x10GCardTable.setStatus("current")
_Ethernet1x10GCardEntry_Object = MibTableRow
ethernet1x10GCardEntry = _Ethernet1x10GCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1)
)
ethernet1x10GCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernet1x10GCardEntry.setStatus("current")
_Ethernet1x10GCardEntityIndex_Type = PhysicalIndex
_Ethernet1x10GCardEntityIndex_Object = MibTableColumn
ethernet1x10GCardEntityIndex = _Ethernet1x10GCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 1),
    _Ethernet1x10GCardEntityIndex_Type()
)
ethernet1x10GCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GCardEntityIndex.setStatus("current")
_Ethernet1x10GCardAdminState_Type = AdminState
_Ethernet1x10GCardAdminState_Object = MibTableColumn
ethernet1x10GCardAdminState = _Ethernet1x10GCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 2),
    _Ethernet1x10GCardAdminState_Type()
)
ethernet1x10GCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GCardAdminState.setStatus("current")
_Ethernet1x10GCardOperationalState_Type = OperationalState
_Ethernet1x10GCardOperationalState_Object = MibTableColumn
ethernet1x10GCardOperationalState = _Ethernet1x10GCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 3),
    _Ethernet1x10GCardOperationalState_Type()
)
ethernet1x10GCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GCardOperationalState.setStatus("current")
_Ethernet1x10GCardSecondaryState_Type = SecondaryState
_Ethernet1x10GCardSecondaryState_Object = MibTableColumn
ethernet1x10GCardSecondaryState = _Ethernet1x10GCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 4),
    _Ethernet1x10GCardSecondaryState_Type()
)
ethernet1x10GCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GCardSecondaryState.setStatus("current")
_Ethernet1x10GCardTemperature_Type = Integer32
_Ethernet1x10GCardTemperature_Object = MibTableColumn
ethernet1x10GCardTemperature = _Ethernet1x10GCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 5),
    _Ethernet1x10GCardTemperature_Type()
)
ethernet1x10GCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GCardTemperature.setStatus("current")
_Ethernet1x10GCardSnmpDyingGaspEnabled_Type = TruthValue
_Ethernet1x10GCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernet1x10GCardSnmpDyingGaspEnabled = _Ethernet1x10GCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 6),
    _Ethernet1x10GCardSnmpDyingGaspEnabled_Type()
)
ethernet1x10GCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GCardSnmpDyingGaspEnabled.setStatus("current")
_Ethernet1x10GCardRestartAction_Type = RestartType
_Ethernet1x10GCardRestartAction_Object = MibTableColumn
ethernet1x10GCardRestartAction = _Ethernet1x10GCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 7),
    _Ethernet1x10GCardRestartAction_Type()
)
ethernet1x10GCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GCardRestartAction.setStatus("current")
_Ethernet1x10GCardStorageType_Type = StorageType
_Ethernet1x10GCardStorageType_Object = MibTableColumn
ethernet1x10GCardStorageType = _Ethernet1x10GCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 8),
    _Ethernet1x10GCardStorageType_Type()
)
ethernet1x10GCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet1x10GCardStorageType.setStatus("current")
_Ethernet1x10GCardRowStatus_Type = RowStatus
_Ethernet1x10GCardRowStatus_Object = MibTableColumn
ethernet1x10GCardRowStatus = _Ethernet1x10GCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 9),
    _Ethernet1x10GCardRowStatus_Type()
)
ethernet1x10GCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet1x10GCardRowStatus.setStatus("current")
_Ethernet1x10GCardForceOffLineAction_Type = TruthValue
_Ethernet1x10GCardForceOffLineAction_Object = MibTableColumn
ethernet1x10GCardForceOffLineAction = _Ethernet1x10GCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 18, 1, 10),
    _Ethernet1x10GCardForceOffLineAction_Type()
)
ethernet1x10GCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GCardForceOffLineAction.setStatus("current")
_Ethernet10x1GCardTable_Object = MibTable
ethernet10x1GCardTable = _Ethernet10x1GCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19)
)
if mibBuilder.loadTexts:
    ethernet10x1GCardTable.setStatus("current")
_Ethernet10x1GCardEntry_Object = MibTableRow
ethernet10x1GCardEntry = _Ethernet10x1GCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1)
)
ethernet10x1GCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernet10x1GCardEntry.setStatus("current")
_Ethernet10x1GCardEntityIndex_Type = PhysicalIndex
_Ethernet10x1GCardEntityIndex_Object = MibTableColumn
ethernet10x1GCardEntityIndex = _Ethernet10x1GCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 1),
    _Ethernet10x1GCardEntityIndex_Type()
)
ethernet10x1GCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GCardEntityIndex.setStatus("current")
_Ethernet10x1GCardAdminState_Type = AdminState
_Ethernet10x1GCardAdminState_Object = MibTableColumn
ethernet10x1GCardAdminState = _Ethernet10x1GCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 2),
    _Ethernet10x1GCardAdminState_Type()
)
ethernet10x1GCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GCardAdminState.setStatus("current")
_Ethernet10x1GCardOperationalState_Type = OperationalState
_Ethernet10x1GCardOperationalState_Object = MibTableColumn
ethernet10x1GCardOperationalState = _Ethernet10x1GCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 3),
    _Ethernet10x1GCardOperationalState_Type()
)
ethernet10x1GCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GCardOperationalState.setStatus("current")
_Ethernet10x1GCardSecondaryState_Type = SecondaryState
_Ethernet10x1GCardSecondaryState_Object = MibTableColumn
ethernet10x1GCardSecondaryState = _Ethernet10x1GCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 4),
    _Ethernet10x1GCardSecondaryState_Type()
)
ethernet10x1GCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GCardSecondaryState.setStatus("current")
_Ethernet10x1GCardTemperature_Type = Integer32
_Ethernet10x1GCardTemperature_Object = MibTableColumn
ethernet10x1GCardTemperature = _Ethernet10x1GCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 5),
    _Ethernet10x1GCardTemperature_Type()
)
ethernet10x1GCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GCardTemperature.setStatus("current")
_Ethernet10x1GCardSnmpDyingGaspEnabled_Type = TruthValue
_Ethernet10x1GCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernet10x1GCardSnmpDyingGaspEnabled = _Ethernet10x1GCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 6),
    _Ethernet10x1GCardSnmpDyingGaspEnabled_Type()
)
ethernet10x1GCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GCardSnmpDyingGaspEnabled.setStatus("current")
_Ethernet10x1GCardRestartAction_Type = RestartType
_Ethernet10x1GCardRestartAction_Object = MibTableColumn
ethernet10x1GCardRestartAction = _Ethernet10x1GCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 7),
    _Ethernet10x1GCardRestartAction_Type()
)
ethernet10x1GCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GCardRestartAction.setStatus("current")
_Ethernet10x1GCardStorageType_Type = StorageType
_Ethernet10x1GCardStorageType_Object = MibTableColumn
ethernet10x1GCardStorageType = _Ethernet10x1GCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 8),
    _Ethernet10x1GCardStorageType_Type()
)
ethernet10x1GCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet10x1GCardStorageType.setStatus("current")
_Ethernet10x1GCardRowStatus_Type = RowStatus
_Ethernet10x1GCardRowStatus_Object = MibTableColumn
ethernet10x1GCardRowStatus = _Ethernet10x1GCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 9),
    _Ethernet10x1GCardRowStatus_Type()
)
ethernet10x1GCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet10x1GCardRowStatus.setStatus("current")
_Ethernet10x1GCardForceOffLineAction_Type = TruthValue
_Ethernet10x1GCardForceOffLineAction_Object = MibTableColumn
ethernet10x1GCardForceOffLineAction = _Ethernet10x1GCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 19, 1, 10),
    _Ethernet10x1GCardForceOffLineAction_Type()
)
ethernet10x1GCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GCardForceOffLineAction.setStatus("current")
_EthernetSWFCardTable_Object = MibTable
ethernetSWFCardTable = _EthernetSWFCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20)
)
if mibBuilder.loadTexts:
    ethernetSWFCardTable.setStatus("current")
_EthernetSWFCardEntry_Object = MibTableRow
ethernetSWFCardEntry = _EthernetSWFCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1)
)
ethernetSWFCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetSWFCardEntry.setStatus("current")
_EthernetSWFCardEntityIndex_Type = PhysicalIndex
_EthernetSWFCardEntityIndex_Object = MibTableColumn
ethernetSWFCardEntityIndex = _EthernetSWFCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 1),
    _EthernetSWFCardEntityIndex_Type()
)
ethernetSWFCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetSWFCardEntityIndex.setStatus("current")
_EthernetSWFCardAdminState_Type = AdminState
_EthernetSWFCardAdminState_Object = MibTableColumn
ethernetSWFCardAdminState = _EthernetSWFCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 2),
    _EthernetSWFCardAdminState_Type()
)
ethernetSWFCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetSWFCardAdminState.setStatus("current")
_EthernetSWFCardOperationalState_Type = OperationalState
_EthernetSWFCardOperationalState_Object = MibTableColumn
ethernetSWFCardOperationalState = _EthernetSWFCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 3),
    _EthernetSWFCardOperationalState_Type()
)
ethernetSWFCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetSWFCardOperationalState.setStatus("current")
_EthernetSWFCardSecondaryState_Type = SecondaryState
_EthernetSWFCardSecondaryState_Object = MibTableColumn
ethernetSWFCardSecondaryState = _EthernetSWFCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 4),
    _EthernetSWFCardSecondaryState_Type()
)
ethernetSWFCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetSWFCardSecondaryState.setStatus("current")
_EthernetSWFCardTemperature_Type = Integer32
_EthernetSWFCardTemperature_Object = MibTableColumn
ethernetSWFCardTemperature = _EthernetSWFCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 5),
    _EthernetSWFCardTemperature_Type()
)
ethernetSWFCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetSWFCardTemperature.setStatus("current")
_EthernetSWFCardRestartAction_Type = RestartType
_EthernetSWFCardRestartAction_Object = MibTableColumn
ethernetSWFCardRestartAction = _EthernetSWFCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 6),
    _EthernetSWFCardRestartAction_Type()
)
ethernetSWFCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetSWFCardRestartAction.setStatus("current")
_EthernetSWFCardStorageType_Type = StorageType
_EthernetSWFCardStorageType_Object = MibTableColumn
ethernetSWFCardStorageType = _EthernetSWFCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 7),
    _EthernetSWFCardStorageType_Type()
)
ethernetSWFCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetSWFCardStorageType.setStatus("current")
_EthernetSWFCardRowStatus_Type = RowStatus
_EthernetSWFCardRowStatus_Object = MibTableColumn
ethernetSWFCardRowStatus = _EthernetSWFCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 8),
    _EthernetSWFCardRowStatus_Type()
)
ethernetSWFCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetSWFCardRowStatus.setStatus("current")
_EthernetSWFCardForceOffLineAction_Type = TruthValue
_EthernetSWFCardForceOffLineAction_Object = MibTableColumn
ethernetSWFCardForceOffLineAction = _EthernetSWFCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 20, 1, 9),
    _EthernetSWFCardForceOffLineAction_Type()
)
ethernetSWFCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetSWFCardForceOffLineAction.setStatus("current")
_StuCardTable_Object = MibTable
stuCardTable = _StuCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21)
)
if mibBuilder.loadTexts:
    stuCardTable.setStatus("current")
_StuCardEntry_Object = MibTableRow
stuCardEntry = _StuCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1)
)
stuCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    stuCardEntry.setStatus("current")
_StuCardEntityIndex_Type = PhysicalIndex
_StuCardEntityIndex_Object = MibTableColumn
stuCardEntityIndex = _StuCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 1),
    _StuCardEntityIndex_Type()
)
stuCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCardEntityIndex.setStatus("current")
_StuCardAdminState_Type = AdminState
_StuCardAdminState_Object = MibTableColumn
stuCardAdminState = _StuCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 2),
    _StuCardAdminState_Type()
)
stuCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuCardAdminState.setStatus("current")
_StuCardOperationalState_Type = OperationalState
_StuCardOperationalState_Object = MibTableColumn
stuCardOperationalState = _StuCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 3),
    _StuCardOperationalState_Type()
)
stuCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCardOperationalState.setStatus("current")
_StuCardSecondaryState_Type = SecondaryState
_StuCardSecondaryState_Object = MibTableColumn
stuCardSecondaryState = _StuCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 4),
    _StuCardSecondaryState_Type()
)
stuCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCardSecondaryState.setStatus("current")
_StuCardTemperature_Type = Integer32
_StuCardTemperature_Object = MibTableColumn
stuCardTemperature = _StuCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 5),
    _StuCardTemperature_Type()
)
stuCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCardTemperature.setStatus("current")
_StuCardRestartAction_Type = RestartType
_StuCardRestartAction_Object = MibTableColumn
stuCardRestartAction = _StuCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 6),
    _StuCardRestartAction_Type()
)
stuCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuCardRestartAction.setStatus("current")
_StuCardStorageType_Type = StorageType
_StuCardStorageType_Object = MibTableColumn
stuCardStorageType = _StuCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 7),
    _StuCardStorageType_Type()
)
stuCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuCardStorageType.setStatus("current")
_StuCardRowStatus_Type = RowStatus
_StuCardRowStatus_Object = MibTableColumn
stuCardRowStatus = _StuCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 8),
    _StuCardRowStatus_Type()
)
stuCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuCardRowStatus.setStatus("current")
_StuCardForceOffLineAction_Type = TruthValue
_StuCardForceOffLineAction_Object = MibTableColumn
stuCardForceOffLineAction = _StuCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 21, 1, 9),
    _StuCardForceOffLineAction_Type()
)
stuCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuCardForceOffLineAction.setStatus("current")
_AmiTable_Object = MibTable
amiTable = _AmiTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22)
)
if mibBuilder.loadTexts:
    amiTable.setStatus("current")
_AmiEntry_Object = MibTableRow
amiEntry = _AmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1)
)
amiEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    amiEntry.setStatus("current")
_AmiEntityIndex_Type = PhysicalIndex
_AmiEntityIndex_Object = MibTableColumn
amiEntityIndex = _AmiEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1, 1),
    _AmiEntityIndex_Type()
)
amiEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiEntityIndex.setStatus("current")
_AmiAdminState_Type = AdminState
_AmiAdminState_Object = MibTableColumn
amiAdminState = _AmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1, 2),
    _AmiAdminState_Type()
)
amiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amiAdminState.setStatus("current")
_AmiOperationalState_Type = OperationalState
_AmiOperationalState_Object = MibTableColumn
amiOperationalState = _AmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1, 3),
    _AmiOperationalState_Type()
)
amiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiOperationalState.setStatus("current")
_AmiSecondaryState_Type = SecondaryState
_AmiSecondaryState_Object = MibTableColumn
amiSecondaryState = _AmiSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1, 4),
    _AmiSecondaryState_Type()
)
amiSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiSecondaryState.setStatus("current")
_AmiTemperature_Type = Integer32
_AmiTemperature_Object = MibTableColumn
amiTemperature = _AmiTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1, 5),
    _AmiTemperature_Type()
)
amiTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiTemperature.setStatus("current")
_AmiRestartAction_Type = RestartType
_AmiRestartAction_Object = MibTableColumn
amiRestartAction = _AmiRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 22, 1, 6),
    _AmiRestartAction_Type()
)
amiRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amiRestartAction.setStatus("current")
_StiTable_Object = MibTable
stiTable = _StiTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23)
)
if mibBuilder.loadTexts:
    stiTable.setStatus("current")
_StiEntry_Object = MibTableRow
stiEntry = _StiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1)
)
stiEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    stiEntry.setStatus("current")
_StiEntityIndex_Type = PhysicalIndex
_StiEntityIndex_Object = MibTableColumn
stiEntityIndex = _StiEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 1),
    _StiEntityIndex_Type()
)
stiEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiEntityIndex.setStatus("current")
_StiAdminState_Type = AdminState
_StiAdminState_Object = MibTableColumn
stiAdminState = _StiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 2),
    _StiAdminState_Type()
)
stiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiAdminState.setStatus("current")
_StiOperationalState_Type = OperationalState
_StiOperationalState_Object = MibTableColumn
stiOperationalState = _StiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 3),
    _StiOperationalState_Type()
)
stiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiOperationalState.setStatus("current")
_StiSecondaryState_Type = SecondaryState
_StiSecondaryState_Object = MibTableColumn
stiSecondaryState = _StiSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 4),
    _StiSecondaryState_Type()
)
stiSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiSecondaryState.setStatus("current")
_StiTemperature_Type = Integer32
_StiTemperature_Object = MibTableColumn
stiTemperature = _StiTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 5),
    _StiTemperature_Type()
)
stiTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiTemperature.setStatus("current")
_StiStorageType_Type = StorageType
_StiStorageType_Object = MibTableColumn
stiStorageType = _StiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 6),
    _StiStorageType_Type()
)
stiStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiStorageType.setStatus("current")
_StiRowStatus_Type = RowStatus
_StiRowStatus_Object = MibTableColumn
stiRowStatus = _StiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 23, 1, 7),
    _StiRowStatus_Type()
)
stiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiRowStatus.setStatus("current")
_F3UsbHostTable_Object = MibTable
f3UsbHostTable = _F3UsbHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24)
)
if mibBuilder.loadTexts:
    f3UsbHostTable.setStatus("current")
_F3UsbHostEntry_Object = MibTableRow
f3UsbHostEntry = _F3UsbHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1)
)
f3UsbHostEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-ENTITY-MIB", "f3UsbHostIndex"),
)
if mibBuilder.loadTexts:
    f3UsbHostEntry.setStatus("current")
_F3UsbHostIndex_Type = PhysicalIndex
_F3UsbHostIndex_Object = MibTableColumn
f3UsbHostIndex = _F3UsbHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 1),
    _F3UsbHostIndex_Type()
)
f3UsbHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostIndex.setStatus("current")
_F3UsbHostEntityIndex_Type = PhysicalIndex
_F3UsbHostEntityIndex_Object = MibTableColumn
f3UsbHostEntityIndex = _F3UsbHostEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 2),
    _F3UsbHostEntityIndex_Type()
)
f3UsbHostEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostEntityIndex.setStatus("current")
_F3UsbHostUnitName_Type = DisplayString
_F3UsbHostUnitName_Object = MibTableColumn
f3UsbHostUnitName = _F3UsbHostUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 3),
    _F3UsbHostUnitName_Type()
)
f3UsbHostUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostUnitName.setStatus("current")
_F3UsbHostFormatVersion_Type = DisplayString
_F3UsbHostFormatVersion_Object = MibTableColumn
f3UsbHostFormatVersion = _F3UsbHostFormatVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 4),
    _F3UsbHostFormatVersion_Type()
)
f3UsbHostFormatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostFormatVersion.setStatus("current")
_F3UsbHostCLEICode_Type = DisplayString
_F3UsbHostCLEICode_Object = MibTableColumn
f3UsbHostCLEICode = _F3UsbHostCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 5),
    _F3UsbHostCLEICode_Type()
)
f3UsbHostCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostCLEICode.setStatus("current")
_F3UsbHostPartNumber_Type = DisplayString
_F3UsbHostPartNumber_Object = MibTableColumn
f3UsbHostPartNumber = _F3UsbHostPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 6),
    _F3UsbHostPartNumber_Type()
)
f3UsbHostPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostPartNumber.setStatus("current")
_F3UsbHostHwRev_Type = DisplayString
_F3UsbHostHwRev_Object = MibTableColumn
f3UsbHostHwRev = _F3UsbHostHwRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 7),
    _F3UsbHostHwRev_Type()
)
f3UsbHostHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostHwRev.setStatus("current")
_F3UsbHostSwRev_Type = DisplayString
_F3UsbHostSwRev_Object = MibTableColumn
f3UsbHostSwRev = _F3UsbHostSwRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 8),
    _F3UsbHostSwRev_Type()
)
f3UsbHostSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostSwRev.setStatus("current")
_F3UsbHostSerialNum_Type = DisplayString
_F3UsbHostSerialNum_Object = MibTableColumn
f3UsbHostSerialNum = _F3UsbHostSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 9),
    _F3UsbHostSerialNum_Type()
)
f3UsbHostSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostSerialNum.setStatus("current")
_F3UsbHostMfgName_Type = DisplayString
_F3UsbHostMfgName_Object = MibTableColumn
f3UsbHostMfgName = _F3UsbHostMfgName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 10),
    _F3UsbHostMfgName_Type()
)
f3UsbHostMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostMfgName.setStatus("current")
_F3UsbHostMfgDate_Type = DateAndTime
_F3UsbHostMfgDate_Object = MibTableColumn
f3UsbHostMfgDate = _F3UsbHostMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 11),
    _F3UsbHostMfgDate_Type()
)
f3UsbHostMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostMfgDate.setStatus("current")
_F3UsbHostMfgSite_Type = DisplayString
_F3UsbHostMfgSite_Object = MibTableColumn
f3UsbHostMfgSite = _F3UsbHostMfgSite_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 12),
    _F3UsbHostMfgSite_Type()
)
f3UsbHostMfgSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostMfgSite.setStatus("current")
_F3UsbHostSecondaryState_Type = SecondaryState
_F3UsbHostSecondaryState_Object = MibTableColumn
f3UsbHostSecondaryState = _F3UsbHostSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 13),
    _F3UsbHostSecondaryState_Type()
)
f3UsbHostSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostSecondaryState.setStatus("current")
_F3UsbHostPhysicalAddress_Type = DisplayString
_F3UsbHostPhysicalAddress_Object = MibTableColumn
f3UsbHostPhysicalAddress = _F3UsbHostPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 14),
    _F3UsbHostPhysicalAddress_Type()
)
f3UsbHostPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsbHostPhysicalAddress.setStatus("current")
_F3UsbHostMuxOperationalMode_Type = UsbOperationalMode
_F3UsbHostMuxOperationalMode_Object = MibTableColumn
f3UsbHostMuxOperationalMode = _F3UsbHostMuxOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 24, 1, 15),
    _F3UsbHostMuxOperationalMode_Type()
)
f3UsbHostMuxOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3UsbHostMuxOperationalMode.setStatus("current")
_EthernetNTEGE112CardTable_Object = MibTable
ethernetNTEGE112CardTable = _EthernetNTEGE112CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25)
)
if mibBuilder.loadTexts:
    ethernetNTEGE112CardTable.setStatus("current")
_EthernetNTEGE112CardEntry_Object = MibTableRow
ethernetNTEGE112CardEntry = _EthernetNTEGE112CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1)
)
ethernetNTEGE112CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE112CardEntry.setStatus("current")
_EthernetNTEGE112CardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE112CardEntityIndex_Object = MibTableColumn
ethernetNTEGE112CardEntityIndex = _EthernetNTEGE112CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 1),
    _EthernetNTEGE112CardEntityIndex_Type()
)
ethernetNTEGE112CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardEntityIndex.setStatus("current")
_EthernetNTEGE112CardAdminState_Type = AdminState
_EthernetNTEGE112CardAdminState_Object = MibTableColumn
ethernetNTEGE112CardAdminState = _EthernetNTEGE112CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 2),
    _EthernetNTEGE112CardAdminState_Type()
)
ethernetNTEGE112CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardAdminState.setStatus("current")
_EthernetNTEGE112CardOperationalState_Type = OperationalState
_EthernetNTEGE112CardOperationalState_Object = MibTableColumn
ethernetNTEGE112CardOperationalState = _EthernetNTEGE112CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 3),
    _EthernetNTEGE112CardOperationalState_Type()
)
ethernetNTEGE112CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardOperationalState.setStatus("current")
_EthernetNTEGE112CardSecondaryState_Type = SecondaryState
_EthernetNTEGE112CardSecondaryState_Object = MibTableColumn
ethernetNTEGE112CardSecondaryState = _EthernetNTEGE112CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 4),
    _EthernetNTEGE112CardSecondaryState_Type()
)
ethernetNTEGE112CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardSecondaryState.setStatus("current")
_EthernetNTEGE112CardVoltage_Type = Integer32
_EthernetNTEGE112CardVoltage_Object = MibTableColumn
ethernetNTEGE112CardVoltage = _EthernetNTEGE112CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 5),
    _EthernetNTEGE112CardVoltage_Type()
)
ethernetNTEGE112CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardVoltage.setStatus("current")
_EthernetNTEGE112CardTemperature_Type = Integer32
_EthernetNTEGE112CardTemperature_Object = MibTableColumn
ethernetNTEGE112CardTemperature = _EthernetNTEGE112CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 6),
    _EthernetNTEGE112CardTemperature_Type()
)
ethernetNTEGE112CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardTemperature.setStatus("current")
_EthernetNTEGE112CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE112CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE112CardSnmpDyingGaspEnabled = _EthernetNTEGE112CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 7),
    _EthernetNTEGE112CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE112CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE112CardRestartAction_Type = RestartType
_EthernetNTEGE112CardRestartAction_Object = MibTableColumn
ethernetNTEGE112CardRestartAction = _EthernetNTEGE112CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 8),
    _EthernetNTEGE112CardRestartAction_Type()
)
ethernetNTEGE112CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardRestartAction.setStatus("current")
_EthernetNTEGE112CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE112CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE112CardFineGrainedPmInterval = _EthernetNTEGE112CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 9),
    _EthernetNTEGE112CardFineGrainedPmInterval_Type()
)
ethernetNTEGE112CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112CardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE112CardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE112CardSwitchPortActionPort = _EthernetNTEGE112CardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 10),
    _EthernetNTEGE112CardSwitchPortActionPort_Type()
)
ethernetNTEGE112CardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE112CardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE112CardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE112CardSwitchPortAction = _EthernetNTEGE112CardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 25, 1, 11),
    _EthernetNTEGE112CardSwitchPortAction_Type()
)
ethernetNTEGE112CardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112CardSwitchPortAction.setStatus("current")
_EthernetNTEGE114CardTable_Object = MibTable
ethernetNTEGE114CardTable = _EthernetNTEGE114CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114CardTable.setStatus("current")
_EthernetNTEGE114CardEntry_Object = MibTableRow
ethernetNTEGE114CardEntry = _EthernetNTEGE114CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1)
)
ethernetNTEGE114CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114CardEntry.setStatus("current")
_EthernetNTEGE114CardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114CardEntityIndex_Object = MibTableColumn
ethernetNTEGE114CardEntityIndex = _EthernetNTEGE114CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 1),
    _EthernetNTEGE114CardEntityIndex_Type()
)
ethernetNTEGE114CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardEntityIndex.setStatus("current")
_EthernetNTEGE114CardAdminState_Type = AdminState
_EthernetNTEGE114CardAdminState_Object = MibTableColumn
ethernetNTEGE114CardAdminState = _EthernetNTEGE114CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 2),
    _EthernetNTEGE114CardAdminState_Type()
)
ethernetNTEGE114CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardAdminState.setStatus("current")
_EthernetNTEGE114CardOperationalState_Type = OperationalState
_EthernetNTEGE114CardOperationalState_Object = MibTableColumn
ethernetNTEGE114CardOperationalState = _EthernetNTEGE114CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 3),
    _EthernetNTEGE114CardOperationalState_Type()
)
ethernetNTEGE114CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardOperationalState.setStatus("current")
_EthernetNTEGE114CardSecondaryState_Type = SecondaryState
_EthernetNTEGE114CardSecondaryState_Object = MibTableColumn
ethernetNTEGE114CardSecondaryState = _EthernetNTEGE114CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 4),
    _EthernetNTEGE114CardSecondaryState_Type()
)
ethernetNTEGE114CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardSecondaryState.setStatus("current")
_EthernetNTEGE114CardVoltage_Type = Integer32
_EthernetNTEGE114CardVoltage_Object = MibTableColumn
ethernetNTEGE114CardVoltage = _EthernetNTEGE114CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 5),
    _EthernetNTEGE114CardVoltage_Type()
)
ethernetNTEGE114CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardVoltage.setStatus("current")
_EthernetNTEGE114CardTemperature_Type = Integer32
_EthernetNTEGE114CardTemperature_Object = MibTableColumn
ethernetNTEGE114CardTemperature = _EthernetNTEGE114CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 6),
    _EthernetNTEGE114CardTemperature_Type()
)
ethernetNTEGE114CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardTemperature.setStatus("current")
_EthernetNTEGE114CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114CardSnmpDyingGaspEnabled = _EthernetNTEGE114CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 7),
    _EthernetNTEGE114CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114CardRestartAction_Type = RestartType
_EthernetNTEGE114CardRestartAction_Object = MibTableColumn
ethernetNTEGE114CardRestartAction = _EthernetNTEGE114CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 8),
    _EthernetNTEGE114CardRestartAction_Type()
)
ethernetNTEGE114CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardRestartAction.setStatus("current")
_EthernetNTEGE114CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114CardFineGrainedPmInterval = _EthernetNTEGE114CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 9),
    _EthernetNTEGE114CardFineGrainedPmInterval_Type()
)
ethernetNTEGE114CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114CardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114CardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114CardSwitchPortActionPort = _EthernetNTEGE114CardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 10),
    _EthernetNTEGE114CardSwitchPortActionPort_Type()
)
ethernetNTEGE114CardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114CardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114CardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114CardSwitchPortAction = _EthernetNTEGE114CardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 26, 1, 11),
    _EthernetNTEGE114CardSwitchPortAction_Type()
)
ethernetNTEGE114CardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114CardSwitchPortAction.setStatus("current")
_EthernetNTEGE206VCardTable_Object = MibTable
ethernetNTEGE206VCardTable = _EthernetNTEGE206VCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27)
)
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardTable.setStatus("current")
_EthernetNTEGE206VCardEntry_Object = MibTableRow
ethernetNTEGE206VCardEntry = _EthernetNTEGE206VCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1)
)
ethernetNTEGE206VCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardEntry.setStatus("current")
_EthernetNTEGE206VCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE206VCardEntityIndex_Object = MibTableColumn
ethernetNTEGE206VCardEntityIndex = _EthernetNTEGE206VCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 1),
    _EthernetNTEGE206VCardEntityIndex_Type()
)
ethernetNTEGE206VCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardEntityIndex.setStatus("current")
_EthernetNTEGE206VCardAdminState_Type = AdminState
_EthernetNTEGE206VCardAdminState_Object = MibTableColumn
ethernetNTEGE206VCardAdminState = _EthernetNTEGE206VCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 2),
    _EthernetNTEGE206VCardAdminState_Type()
)
ethernetNTEGE206VCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardAdminState.setStatus("current")
_EthernetNTEGE206VCardOperationalState_Type = OperationalState
_EthernetNTEGE206VCardOperationalState_Object = MibTableColumn
ethernetNTEGE206VCardOperationalState = _EthernetNTEGE206VCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 3),
    _EthernetNTEGE206VCardOperationalState_Type()
)
ethernetNTEGE206VCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardOperationalState.setStatus("current")
_EthernetNTEGE206VCardSecondaryState_Type = SecondaryState
_EthernetNTEGE206VCardSecondaryState_Object = MibTableColumn
ethernetNTEGE206VCardSecondaryState = _EthernetNTEGE206VCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 4),
    _EthernetNTEGE206VCardSecondaryState_Type()
)
ethernetNTEGE206VCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardSecondaryState.setStatus("current")
_EthernetNTEGE206VCardVoltage_Type = Integer32
_EthernetNTEGE206VCardVoltage_Object = MibTableColumn
ethernetNTEGE206VCardVoltage = _EthernetNTEGE206VCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 5),
    _EthernetNTEGE206VCardVoltage_Type()
)
ethernetNTEGE206VCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardVoltage.setStatus("current")
_EthernetNTEGE206VCardTemperature_Type = Integer32
_EthernetNTEGE206VCardTemperature_Object = MibTableColumn
ethernetNTEGE206VCardTemperature = _EthernetNTEGE206VCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 6),
    _EthernetNTEGE206VCardTemperature_Type()
)
ethernetNTEGE206VCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardTemperature.setStatus("current")
_EthernetNTEGE206VCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE206VCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE206VCardSnmpDyingGaspEnabled = _EthernetNTEGE206VCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 7),
    _EthernetNTEGE206VCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE206VCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE206VCardRestartAction_Type = RestartType
_EthernetNTEGE206VCardRestartAction_Object = MibTableColumn
ethernetNTEGE206VCardRestartAction = _EthernetNTEGE206VCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 8),
    _EthernetNTEGE206VCardRestartAction_Type()
)
ethernetNTEGE206VCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardRestartAction.setStatus("current")
_EthernetNTEGE206VCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE206VCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE206VCardFineGrainedPmInterval = _EthernetNTEGE206VCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 27, 1, 9),
    _EthernetNTEGE206VCardFineGrainedPmInterval_Type()
)
ethernetNTEGE206VCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE206VCardFineGrainedPmInterval.setStatus("current")
_EthernetGE4SCCCardTable_Object = MibTable
ethernetGE4SCCCardTable = _EthernetGE4SCCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28)
)
if mibBuilder.loadTexts:
    ethernetGE4SCCCardTable.setStatus("current")
_EthernetGE4SCCCardEntry_Object = MibTableRow
ethernetGE4SCCCardEntry = _EthernetGE4SCCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1)
)
ethernetGE4SCCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetGE4SCCCardEntry.setStatus("current")
_EthernetGE4SCCCardEntityIndex_Type = PhysicalIndex
_EthernetGE4SCCCardEntityIndex_Object = MibTableColumn
ethernetGE4SCCCardEntityIndex = _EthernetGE4SCCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 1),
    _EthernetGE4SCCCardEntityIndex_Type()
)
ethernetGE4SCCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardEntityIndex.setStatus("current")
_EthernetGE4SCCCardAdminState_Type = AdminState
_EthernetGE4SCCCardAdminState_Object = MibTableColumn
ethernetGE4SCCCardAdminState = _EthernetGE4SCCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 2),
    _EthernetGE4SCCCardAdminState_Type()
)
ethernetGE4SCCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardAdminState.setStatus("current")
_EthernetGE4SCCCardOperationalState_Type = OperationalState
_EthernetGE4SCCCardOperationalState_Object = MibTableColumn
ethernetGE4SCCCardOperationalState = _EthernetGE4SCCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 3),
    _EthernetGE4SCCCardOperationalState_Type()
)
ethernetGE4SCCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardOperationalState.setStatus("current")
_EthernetGE4SCCCardSecondaryState_Type = SecondaryState
_EthernetGE4SCCCardSecondaryState_Object = MibTableColumn
ethernetGE4SCCCardSecondaryState = _EthernetGE4SCCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 4),
    _EthernetGE4SCCCardSecondaryState_Type()
)
ethernetGE4SCCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardSecondaryState.setStatus("current")
_EthernetGE4SCCCardVoltage_Type = Integer32
_EthernetGE4SCCCardVoltage_Object = MibTableColumn
ethernetGE4SCCCardVoltage = _EthernetGE4SCCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 5),
    _EthernetGE4SCCCardVoltage_Type()
)
ethernetGE4SCCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardVoltage.setStatus("current")
_EthernetGE4SCCCardTemperature_Type = Integer32
_EthernetGE4SCCCardTemperature_Object = MibTableColumn
ethernetGE4SCCCardTemperature = _EthernetGE4SCCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 6),
    _EthernetGE4SCCCardTemperature_Type()
)
ethernetGE4SCCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardTemperature.setStatus("current")
_EthernetGE4SCCCardRestartAction_Type = RestartType
_EthernetGE4SCCCardRestartAction_Object = MibTableColumn
ethernetGE4SCCCardRestartAction = _EthernetGE4SCCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 7),
    _EthernetGE4SCCCardRestartAction_Type()
)
ethernetGE4SCCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardRestartAction.setStatus("current")
_EthernetGE4SCCCardStorageType_Type = StorageType
_EthernetGE4SCCCardStorageType_Object = MibTableColumn
ethernetGE4SCCCardStorageType = _EthernetGE4SCCCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 8),
    _EthernetGE4SCCCardStorageType_Type()
)
ethernetGE4SCCCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardStorageType.setStatus("current")
_EthernetGE4SCCCardRowStatus_Type = RowStatus
_EthernetGE4SCCCardRowStatus_Object = MibTableColumn
ethernetGE4SCCCardRowStatus = _EthernetGE4SCCCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 28, 1, 9),
    _EthernetGE4SCCCardRowStatus_Type()
)
ethernetGE4SCCCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE4SCCCardRowStatus.setStatus("current")
_EthernetGE4ECCCardTable_Object = MibTable
ethernetGE4ECCCardTable = _EthernetGE4ECCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29)
)
if mibBuilder.loadTexts:
    ethernetGE4ECCCardTable.setStatus("current")
_EthernetGE4ECCCardEntry_Object = MibTableRow
ethernetGE4ECCCardEntry = _EthernetGE4ECCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1)
)
ethernetGE4ECCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetGE4ECCCardEntry.setStatus("current")
_EthernetGE4ECCCardEntityIndex_Type = PhysicalIndex
_EthernetGE4ECCCardEntityIndex_Object = MibTableColumn
ethernetGE4ECCCardEntityIndex = _EthernetGE4ECCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 1),
    _EthernetGE4ECCCardEntityIndex_Type()
)
ethernetGE4ECCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardEntityIndex.setStatus("current")
_EthernetGE4ECCCardAdminState_Type = AdminState
_EthernetGE4ECCCardAdminState_Object = MibTableColumn
ethernetGE4ECCCardAdminState = _EthernetGE4ECCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 2),
    _EthernetGE4ECCCardAdminState_Type()
)
ethernetGE4ECCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardAdminState.setStatus("current")
_EthernetGE4ECCCardOperationalState_Type = OperationalState
_EthernetGE4ECCCardOperationalState_Object = MibTableColumn
ethernetGE4ECCCardOperationalState = _EthernetGE4ECCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 3),
    _EthernetGE4ECCCardOperationalState_Type()
)
ethernetGE4ECCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardOperationalState.setStatus("current")
_EthernetGE4ECCCardSecondaryState_Type = SecondaryState
_EthernetGE4ECCCardSecondaryState_Object = MibTableColumn
ethernetGE4ECCCardSecondaryState = _EthernetGE4ECCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 4),
    _EthernetGE4ECCCardSecondaryState_Type()
)
ethernetGE4ECCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardSecondaryState.setStatus("current")
_EthernetGE4ECCCardVoltage_Type = Integer32
_EthernetGE4ECCCardVoltage_Object = MibTableColumn
ethernetGE4ECCCardVoltage = _EthernetGE4ECCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 5),
    _EthernetGE4ECCCardVoltage_Type()
)
ethernetGE4ECCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardVoltage.setStatus("current")
_EthernetGE4ECCCardTemperature_Type = Integer32
_EthernetGE4ECCCardTemperature_Object = MibTableColumn
ethernetGE4ECCCardTemperature = _EthernetGE4ECCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 6),
    _EthernetGE4ECCCardTemperature_Type()
)
ethernetGE4ECCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardTemperature.setStatus("current")
_EthernetGE4ECCCardRestartAction_Type = RestartType
_EthernetGE4ECCCardRestartAction_Object = MibTableColumn
ethernetGE4ECCCardRestartAction = _EthernetGE4ECCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 7),
    _EthernetGE4ECCCardRestartAction_Type()
)
ethernetGE4ECCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardRestartAction.setStatus("current")
_EthernetGE4ECCCardStorageType_Type = StorageType
_EthernetGE4ECCCardStorageType_Object = MibTableColumn
ethernetGE4ECCCardStorageType = _EthernetGE4ECCCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 8),
    _EthernetGE4ECCCardStorageType_Type()
)
ethernetGE4ECCCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardStorageType.setStatus("current")
_EthernetGE4ECCCardRowStatus_Type = RowStatus
_EthernetGE4ECCCardRowStatus_Object = MibTableColumn
ethernetGE4ECCCardRowStatus = _EthernetGE4ECCCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 29, 1, 9),
    _EthernetGE4ECCCardRowStatus_Type()
)
ethernetGE4ECCCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE4ECCCardRowStatus.setStatus("current")
_EthernetNTEXG210CardTable_Object = MibTable
ethernetNTEXG210CardTable = _EthernetNTEXG210CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30)
)
if mibBuilder.loadTexts:
    ethernetNTEXG210CardTable.setStatus("current")
_EthernetNTEXG210CardEntry_Object = MibTableRow
ethernetNTEXG210CardEntry = _EthernetNTEXG210CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1)
)
ethernetNTEXG210CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG210CardEntry.setStatus("current")
_EthernetNTEXG210CardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG210CardEntityIndex_Object = MibTableColumn
ethernetNTEXG210CardEntityIndex = _EthernetNTEXG210CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 1),
    _EthernetNTEXG210CardEntityIndex_Type()
)
ethernetNTEXG210CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardEntityIndex.setStatus("current")
_EthernetNTEXG210CardAdminState_Type = AdminState
_EthernetNTEXG210CardAdminState_Object = MibTableColumn
ethernetNTEXG210CardAdminState = _EthernetNTEXG210CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 2),
    _EthernetNTEXG210CardAdminState_Type()
)
ethernetNTEXG210CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardAdminState.setStatus("current")
_EthernetNTEXG210CardOperationalState_Type = OperationalState
_EthernetNTEXG210CardOperationalState_Object = MibTableColumn
ethernetNTEXG210CardOperationalState = _EthernetNTEXG210CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 3),
    _EthernetNTEXG210CardOperationalState_Type()
)
ethernetNTEXG210CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardOperationalState.setStatus("current")
_EthernetNTEXG210CardSecondaryState_Type = SecondaryState
_EthernetNTEXG210CardSecondaryState_Object = MibTableColumn
ethernetNTEXG210CardSecondaryState = _EthernetNTEXG210CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 4),
    _EthernetNTEXG210CardSecondaryState_Type()
)
ethernetNTEXG210CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardSecondaryState.setStatus("current")
_EthernetNTEXG210CardVoltage_Type = Integer32
_EthernetNTEXG210CardVoltage_Object = MibTableColumn
ethernetNTEXG210CardVoltage = _EthernetNTEXG210CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 5),
    _EthernetNTEXG210CardVoltage_Type()
)
ethernetNTEXG210CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardVoltage.setStatus("current")
_EthernetNTEXG210CardTemperature_Type = Integer32
_EthernetNTEXG210CardTemperature_Object = MibTableColumn
ethernetNTEXG210CardTemperature = _EthernetNTEXG210CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 6),
    _EthernetNTEXG210CardTemperature_Type()
)
ethernetNTEXG210CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardTemperature.setStatus("current")
_EthernetNTEXG210CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG210CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG210CardSnmpDyingGaspEnabled = _EthernetNTEXG210CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 7),
    _EthernetNTEXG210CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG210CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG210CardRestartAction_Type = RestartType
_EthernetNTEXG210CardRestartAction_Object = MibTableColumn
ethernetNTEXG210CardRestartAction = _EthernetNTEXG210CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 8),
    _EthernetNTEXG210CardRestartAction_Type()
)
ethernetNTEXG210CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardRestartAction.setStatus("current")
_EthernetNTEXG210CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG210CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG210CardFineGrainedPmInterval = _EthernetNTEXG210CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 30, 1, 9),
    _EthernetNTEXG210CardFineGrainedPmInterval_Type()
)
ethernetNTEXG210CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CardFineGrainedPmInterval.setStatus("current")
_EthernetXG1XCCCardTable_Object = MibTable
ethernetXG1XCCCardTable = _EthernetXG1XCCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31)
)
if mibBuilder.loadTexts:
    ethernetXG1XCCCardTable.setStatus("current")
_EthernetXG1XCCCardEntry_Object = MibTableRow
ethernetXG1XCCCardEntry = _EthernetXG1XCCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1)
)
ethernetXG1XCCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetXG1XCCCardEntry.setStatus("current")
_EthernetXG1XCCCardEntityIndex_Type = PhysicalIndex
_EthernetXG1XCCCardEntityIndex_Object = MibTableColumn
ethernetXG1XCCCardEntityIndex = _EthernetXG1XCCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 1),
    _EthernetXG1XCCCardEntityIndex_Type()
)
ethernetXG1XCCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardEntityIndex.setStatus("current")
_EthernetXG1XCCCardAdminState_Type = AdminState
_EthernetXG1XCCCardAdminState_Object = MibTableColumn
ethernetXG1XCCCardAdminState = _EthernetXG1XCCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 2),
    _EthernetXG1XCCCardAdminState_Type()
)
ethernetXG1XCCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardAdminState.setStatus("current")
_EthernetXG1XCCCardOperationalState_Type = OperationalState
_EthernetXG1XCCCardOperationalState_Object = MibTableColumn
ethernetXG1XCCCardOperationalState = _EthernetXG1XCCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 3),
    _EthernetXG1XCCCardOperationalState_Type()
)
ethernetXG1XCCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardOperationalState.setStatus("current")
_EthernetXG1XCCCardSecondaryState_Type = SecondaryState
_EthernetXG1XCCCardSecondaryState_Object = MibTableColumn
ethernetXG1XCCCardSecondaryState = _EthernetXG1XCCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 4),
    _EthernetXG1XCCCardSecondaryState_Type()
)
ethernetXG1XCCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardSecondaryState.setStatus("current")
_EthernetXG1XCCCardVoltage_Type = Integer32
_EthernetXG1XCCCardVoltage_Object = MibTableColumn
ethernetXG1XCCCardVoltage = _EthernetXG1XCCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 5),
    _EthernetXG1XCCCardVoltage_Type()
)
ethernetXG1XCCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardVoltage.setStatus("current")
_EthernetXG1XCCCardTemperature_Type = Integer32
_EthernetXG1XCCCardTemperature_Object = MibTableColumn
ethernetXG1XCCCardTemperature = _EthernetXG1XCCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 6),
    _EthernetXG1XCCCardTemperature_Type()
)
ethernetXG1XCCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardTemperature.setStatus("current")
_EthernetXG1XCCCardRestartAction_Type = RestartType
_EthernetXG1XCCCardRestartAction_Object = MibTableColumn
ethernetXG1XCCCardRestartAction = _EthernetXG1XCCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 7),
    _EthernetXG1XCCCardRestartAction_Type()
)
ethernetXG1XCCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardRestartAction.setStatus("current")
_EthernetXG1XCCCardStorageType_Type = StorageType
_EthernetXG1XCCCardStorageType_Object = MibTableColumn
ethernetXG1XCCCardStorageType = _EthernetXG1XCCCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 8),
    _EthernetXG1XCCCardStorageType_Type()
)
ethernetXG1XCCCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardStorageType.setStatus("current")
_EthernetXG1XCCCardRowStatus_Type = RowStatus
_EthernetXG1XCCCardRowStatus_Object = MibTableColumn
ethernetXG1XCCCardRowStatus = _EthernetXG1XCCCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 31, 1, 9),
    _EthernetXG1XCCCardRowStatus_Type()
)
ethernetXG1XCCCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetXG1XCCCardRowStatus.setStatus("current")
_EthernetXG1SCCCardTable_Object = MibTable
ethernetXG1SCCCardTable = _EthernetXG1SCCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32)
)
if mibBuilder.loadTexts:
    ethernetXG1SCCCardTable.setStatus("current")
_EthernetXG1SCCCardEntry_Object = MibTableRow
ethernetXG1SCCCardEntry = _EthernetXG1SCCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1)
)
ethernetXG1SCCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetXG1SCCCardEntry.setStatus("current")
_EthernetXG1SCCCardEntityIndex_Type = PhysicalIndex
_EthernetXG1SCCCardEntityIndex_Object = MibTableColumn
ethernetXG1SCCCardEntityIndex = _EthernetXG1SCCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 1),
    _EthernetXG1SCCCardEntityIndex_Type()
)
ethernetXG1SCCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardEntityIndex.setStatus("current")
_EthernetXG1SCCCardAdminState_Type = AdminState
_EthernetXG1SCCCardAdminState_Object = MibTableColumn
ethernetXG1SCCCardAdminState = _EthernetXG1SCCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 2),
    _EthernetXG1SCCCardAdminState_Type()
)
ethernetXG1SCCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardAdminState.setStatus("current")
_EthernetXG1SCCCardOperationalState_Type = OperationalState
_EthernetXG1SCCCardOperationalState_Object = MibTableColumn
ethernetXG1SCCCardOperationalState = _EthernetXG1SCCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 3),
    _EthernetXG1SCCCardOperationalState_Type()
)
ethernetXG1SCCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardOperationalState.setStatus("current")
_EthernetXG1SCCCardSecondaryState_Type = SecondaryState
_EthernetXG1SCCCardSecondaryState_Object = MibTableColumn
ethernetXG1SCCCardSecondaryState = _EthernetXG1SCCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 4),
    _EthernetXG1SCCCardSecondaryState_Type()
)
ethernetXG1SCCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardSecondaryState.setStatus("current")
_EthernetXG1SCCCardVoltage_Type = Integer32
_EthernetXG1SCCCardVoltage_Object = MibTableColumn
ethernetXG1SCCCardVoltage = _EthernetXG1SCCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 5),
    _EthernetXG1SCCCardVoltage_Type()
)
ethernetXG1SCCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardVoltage.setStatus("current")
_EthernetXG1SCCCardTemperature_Type = Integer32
_EthernetXG1SCCCardTemperature_Object = MibTableColumn
ethernetXG1SCCCardTemperature = _EthernetXG1SCCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 6),
    _EthernetXG1SCCCardTemperature_Type()
)
ethernetXG1SCCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardTemperature.setStatus("current")
_EthernetXG1SCCCardRestartAction_Type = RestartType
_EthernetXG1SCCCardRestartAction_Object = MibTableColumn
ethernetXG1SCCCardRestartAction = _EthernetXG1SCCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 7),
    _EthernetXG1SCCCardRestartAction_Type()
)
ethernetXG1SCCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardRestartAction.setStatus("current")
_EthernetXG1SCCCardStorageType_Type = StorageType
_EthernetXG1SCCCardStorageType_Object = MibTableColumn
ethernetXG1SCCCardStorageType = _EthernetXG1SCCCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 8),
    _EthernetXG1SCCCardStorageType_Type()
)
ethernetXG1SCCCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardStorageType.setStatus("current")
_EthernetXG1SCCCardRowStatus_Type = RowStatus
_EthernetXG1SCCCardRowStatus_Object = MibTableColumn
ethernetXG1SCCCardRowStatus = _EthernetXG1SCCCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 32, 1, 9),
    _EthernetXG1SCCCardRowStatus_Type()
)
ethernetXG1SCCCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetXG1SCCCardRowStatus.setStatus("current")
_EthernetOverOCSTMCardTable_Object = MibTable
ethernetOverOCSTMCardTable = _EthernetOverOCSTMCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33)
)
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardTable.setStatus("current")
_EthernetOverOCSTMCardEntry_Object = MibTableRow
ethernetOverOCSTMCardEntry = _EthernetOverOCSTMCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1)
)
ethernetOverOCSTMCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardEntry.setStatus("current")
_EthernetOverOCSTMCardEntityIndex_Type = PhysicalIndex
_EthernetOverOCSTMCardEntityIndex_Object = MibTableColumn
ethernetOverOCSTMCardEntityIndex = _EthernetOverOCSTMCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 1),
    _EthernetOverOCSTMCardEntityIndex_Type()
)
ethernetOverOCSTMCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardEntityIndex.setStatus("current")
_EthernetOverOCSTMCardAdminState_Type = AdminState
_EthernetOverOCSTMCardAdminState_Object = MibTableColumn
ethernetOverOCSTMCardAdminState = _EthernetOverOCSTMCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 2),
    _EthernetOverOCSTMCardAdminState_Type()
)
ethernetOverOCSTMCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardAdminState.setStatus("current")
_EthernetOverOCSTMCardOperationalState_Type = OperationalState
_EthernetOverOCSTMCardOperationalState_Object = MibTableColumn
ethernetOverOCSTMCardOperationalState = _EthernetOverOCSTMCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 3),
    _EthernetOverOCSTMCardOperationalState_Type()
)
ethernetOverOCSTMCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardOperationalState.setStatus("current")
_EthernetOverOCSTMCardSecondaryState_Type = SecondaryState
_EthernetOverOCSTMCardSecondaryState_Object = MibTableColumn
ethernetOverOCSTMCardSecondaryState = _EthernetOverOCSTMCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 4),
    _EthernetOverOCSTMCardSecondaryState_Type()
)
ethernetOverOCSTMCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardSecondaryState.setStatus("current")
_EthernetOverOCSTMCardTemperature_Type = Integer32
_EthernetOverOCSTMCardTemperature_Object = MibTableColumn
ethernetOverOCSTMCardTemperature = _EthernetOverOCSTMCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 5),
    _EthernetOverOCSTMCardTemperature_Type()
)
ethernetOverOCSTMCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardTemperature.setStatus("current")
_EthernetOverOCSTMCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetOverOCSTMCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetOverOCSTMCardSnmpDyingGaspEnabled = _EthernetOverOCSTMCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 6),
    _EthernetOverOCSTMCardSnmpDyingGaspEnabled_Type()
)
ethernetOverOCSTMCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetOverOCSTMCardRestartAction_Type = RestartType
_EthernetOverOCSTMCardRestartAction_Object = MibTableColumn
ethernetOverOCSTMCardRestartAction = _EthernetOverOCSTMCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 7),
    _EthernetOverOCSTMCardRestartAction_Type()
)
ethernetOverOCSTMCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardRestartAction.setStatus("current")
_EthernetOverOCSTMCardStorageType_Type = StorageType
_EthernetOverOCSTMCardStorageType_Object = MibTableColumn
ethernetOverOCSTMCardStorageType = _EthernetOverOCSTMCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 8),
    _EthernetOverOCSTMCardStorageType_Type()
)
ethernetOverOCSTMCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardStorageType.setStatus("current")
_EthernetOverOCSTMCardRowStatus_Type = RowStatus
_EthernetOverOCSTMCardRowStatus_Object = MibTableColumn
ethernetOverOCSTMCardRowStatus = _EthernetOverOCSTMCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 9),
    _EthernetOverOCSTMCardRowStatus_Type()
)
ethernetOverOCSTMCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardRowStatus.setStatus("current")
_EthernetOverOCSTMCardForceOffLineAction_Type = TruthValue
_EthernetOverOCSTMCardForceOffLineAction_Object = MibTableColumn
ethernetOverOCSTMCardForceOffLineAction = _EthernetOverOCSTMCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 10),
    _EthernetOverOCSTMCardForceOffLineAction_Type()
)
ethernetOverOCSTMCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardForceOffLineAction.setStatus("current")
_EthernetOverOCSTMCardMode_Type = PortCarrierType
_EthernetOverOCSTMCardMode_Object = MibTableColumn
ethernetOverOCSTMCardMode = _EthernetOverOCSTMCardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 33, 1, 11),
    _EthernetOverOCSTMCardMode_Type()
)
ethernetOverOCSTMCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardMode.setStatus("current")
_PseudoWireOcnStmCardTable_Object = MibTable
pseudoWireOcnStmCardTable = _PseudoWireOcnStmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34)
)
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardTable.setStatus("current")
_PseudoWireOcnStmCardEntry_Object = MibTableRow
pseudoWireOcnStmCardEntry = _PseudoWireOcnStmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1)
)
pseudoWireOcnStmCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardEntry.setStatus("current")
_PseudoWireOcnStmCardEntityIndex_Type = PhysicalIndex
_PseudoWireOcnStmCardEntityIndex_Object = MibTableColumn
pseudoWireOcnStmCardEntityIndex = _PseudoWireOcnStmCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 1),
    _PseudoWireOcnStmCardEntityIndex_Type()
)
pseudoWireOcnStmCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardEntityIndex.setStatus("current")
_PseudoWireOcnStmCardAdminState_Type = AdminState
_PseudoWireOcnStmCardAdminState_Object = MibTableColumn
pseudoWireOcnStmCardAdminState = _PseudoWireOcnStmCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 2),
    _PseudoWireOcnStmCardAdminState_Type()
)
pseudoWireOcnStmCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardAdminState.setStatus("current")
_PseudoWireOcnStmCardOperationalState_Type = OperationalState
_PseudoWireOcnStmCardOperationalState_Object = MibTableColumn
pseudoWireOcnStmCardOperationalState = _PseudoWireOcnStmCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 3),
    _PseudoWireOcnStmCardOperationalState_Type()
)
pseudoWireOcnStmCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardOperationalState.setStatus("current")
_PseudoWireOcnStmCardSecondaryState_Type = SecondaryState
_PseudoWireOcnStmCardSecondaryState_Object = MibTableColumn
pseudoWireOcnStmCardSecondaryState = _PseudoWireOcnStmCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 4),
    _PseudoWireOcnStmCardSecondaryState_Type()
)
pseudoWireOcnStmCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardSecondaryState.setStatus("current")
_PseudoWireOcnStmCardIpAddress_Type = IpAddress
_PseudoWireOcnStmCardIpAddress_Object = MibTableColumn
pseudoWireOcnStmCardIpAddress = _PseudoWireOcnStmCardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 5),
    _PseudoWireOcnStmCardIpAddress_Type()
)
pseudoWireOcnStmCardIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardIpAddress.setStatus("current")
_PseudoWireOcnStmCardMode_Type = PWE3OCNSTMCardMode
_PseudoWireOcnStmCardMode_Object = MibTableColumn
pseudoWireOcnStmCardMode = _PseudoWireOcnStmCardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 6),
    _PseudoWireOcnStmCardMode_Type()
)
pseudoWireOcnStmCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardMode.setStatus("current")
_PseudoWireOcnStmCardVoltage_Type = Integer32
_PseudoWireOcnStmCardVoltage_Object = MibTableColumn
pseudoWireOcnStmCardVoltage = _PseudoWireOcnStmCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 7),
    _PseudoWireOcnStmCardVoltage_Type()
)
pseudoWireOcnStmCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardVoltage.setStatus("current")
_PseudoWireOcnStmCardTemperature_Type = Integer32
_PseudoWireOcnStmCardTemperature_Object = MibTableColumn
pseudoWireOcnStmCardTemperature = _PseudoWireOcnStmCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 8),
    _PseudoWireOcnStmCardTemperature_Type()
)
pseudoWireOcnStmCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardTemperature.setStatus("current")
_PseudoWireOcnStmCardRestartAction_Type = RestartType
_PseudoWireOcnStmCardRestartAction_Object = MibTableColumn
pseudoWireOcnStmCardRestartAction = _PseudoWireOcnStmCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 9),
    _PseudoWireOcnStmCardRestartAction_Type()
)
pseudoWireOcnStmCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardRestartAction.setStatus("current")
_PseudoWireOcnStmCardStorageType_Type = StorageType
_PseudoWireOcnStmCardStorageType_Object = MibTableColumn
pseudoWireOcnStmCardStorageType = _PseudoWireOcnStmCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 10),
    _PseudoWireOcnStmCardStorageType_Type()
)
pseudoWireOcnStmCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardStorageType.setStatus("current")
_PseudoWireOcnStmCardRowStatus_Type = RowStatus
_PseudoWireOcnStmCardRowStatus_Object = MibTableColumn
pseudoWireOcnStmCardRowStatus = _PseudoWireOcnStmCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 11),
    _PseudoWireOcnStmCardRowStatus_Type()
)
pseudoWireOcnStmCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardRowStatus.setStatus("current")
_PseudoWireOcnStmCardPSNEncapsulation_Type = PSNEncapsulationMode
_PseudoWireOcnStmCardPSNEncapsulation_Object = MibTableColumn
pseudoWireOcnStmCardPSNEncapsulation = _PseudoWireOcnStmCardPSNEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 12),
    _PseudoWireOcnStmCardPSNEncapsulation_Type()
)
pseudoWireOcnStmCardPSNEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardPSNEncapsulation.setStatus("current")
_PseudoWireOcnStmCardFreqSourceType_Type = TDMFrequencySourceType
_PseudoWireOcnStmCardFreqSourceType_Object = MibTableColumn
pseudoWireOcnStmCardFreqSourceType = _PseudoWireOcnStmCardFreqSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 13),
    _PseudoWireOcnStmCardFreqSourceType_Type()
)
pseudoWireOcnStmCardFreqSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardFreqSourceType.setStatus("current")
_PseudoWireOcnStmCardFreqSource_Type = VariablePointer
_PseudoWireOcnStmCardFreqSource_Object = MibTableColumn
pseudoWireOcnStmCardFreqSource = _PseudoWireOcnStmCardFreqSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 14),
    _PseudoWireOcnStmCardFreqSource_Type()
)
pseudoWireOcnStmCardFreqSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardFreqSource.setStatus("current")
_PseudoWireOcnStmCardForceOffLineAction_Type = TruthValue
_PseudoWireOcnStmCardForceOffLineAction_Object = MibTableColumn
pseudoWireOcnStmCardForceOffLineAction = _PseudoWireOcnStmCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 34, 1, 15),
    _PseudoWireOcnStmCardForceOffLineAction_Type()
)
pseudoWireOcnStmCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireOcnStmCardForceOffLineAction.setStatus("current")
_PseudoWireE1T1CardTable_Object = MibTable
pseudoWireE1T1CardTable = _PseudoWireE1T1CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35)
)
if mibBuilder.loadTexts:
    pseudoWireE1T1CardTable.setStatus("current")
_PseudoWireE1T1CardEntry_Object = MibTableRow
pseudoWireE1T1CardEntry = _PseudoWireE1T1CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1)
)
pseudoWireE1T1CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    pseudoWireE1T1CardEntry.setStatus("current")
_PseudoWireE1T1CardEntityIndex_Type = PhysicalIndex
_PseudoWireE1T1CardEntityIndex_Object = MibTableColumn
pseudoWireE1T1CardEntityIndex = _PseudoWireE1T1CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 1),
    _PseudoWireE1T1CardEntityIndex_Type()
)
pseudoWireE1T1CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardEntityIndex.setStatus("current")
_PseudoWireE1T1CardAdminState_Type = AdminState
_PseudoWireE1T1CardAdminState_Object = MibTableColumn
pseudoWireE1T1CardAdminState = _PseudoWireE1T1CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 2),
    _PseudoWireE1T1CardAdminState_Type()
)
pseudoWireE1T1CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardAdminState.setStatus("current")
_PseudoWireE1T1CardOperationalState_Type = OperationalState
_PseudoWireE1T1CardOperationalState_Object = MibTableColumn
pseudoWireE1T1CardOperationalState = _PseudoWireE1T1CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 3),
    _PseudoWireE1T1CardOperationalState_Type()
)
pseudoWireE1T1CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardOperationalState.setStatus("current")
_PseudoWireE1T1CardSecondaryState_Type = SecondaryState
_PseudoWireE1T1CardSecondaryState_Object = MibTableColumn
pseudoWireE1T1CardSecondaryState = _PseudoWireE1T1CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 4),
    _PseudoWireE1T1CardSecondaryState_Type()
)
pseudoWireE1T1CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardSecondaryState.setStatus("current")
_PseudoWireE1T1CardIpAddress_Type = IpAddress
_PseudoWireE1T1CardIpAddress_Object = MibTableColumn
pseudoWireE1T1CardIpAddress = _PseudoWireE1T1CardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 5),
    _PseudoWireE1T1CardIpAddress_Type()
)
pseudoWireE1T1CardIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardIpAddress.setStatus("current")
_PseudoWireE1T1CardMode_Type = PWE3E1T1CardMode
_PseudoWireE1T1CardMode_Object = MibTableColumn
pseudoWireE1T1CardMode = _PseudoWireE1T1CardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 6),
    _PseudoWireE1T1CardMode_Type()
)
pseudoWireE1T1CardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardMode.setStatus("current")
_PseudoWireE1T1CardVoltage_Type = Integer32
_PseudoWireE1T1CardVoltage_Object = MibTableColumn
pseudoWireE1T1CardVoltage = _PseudoWireE1T1CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 7),
    _PseudoWireE1T1CardVoltage_Type()
)
pseudoWireE1T1CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardVoltage.setStatus("current")
_PseudoWireE1T1CardTemperature_Type = Integer32
_PseudoWireE1T1CardTemperature_Object = MibTableColumn
pseudoWireE1T1CardTemperature = _PseudoWireE1T1CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 8),
    _PseudoWireE1T1CardTemperature_Type()
)
pseudoWireE1T1CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardTemperature.setStatus("current")
_PseudoWireE1T1CardRestartAction_Type = RestartType
_PseudoWireE1T1CardRestartAction_Object = MibTableColumn
pseudoWireE1T1CardRestartAction = _PseudoWireE1T1CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 9),
    _PseudoWireE1T1CardRestartAction_Type()
)
pseudoWireE1T1CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardRestartAction.setStatus("current")
_PseudoWireE1T1CardStorageType_Type = StorageType
_PseudoWireE1T1CardStorageType_Object = MibTableColumn
pseudoWireE1T1CardStorageType = _PseudoWireE1T1CardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 10),
    _PseudoWireE1T1CardStorageType_Type()
)
pseudoWireE1T1CardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardStorageType.setStatus("current")
_PseudoWireE1T1CardRowStatus_Type = RowStatus
_PseudoWireE1T1CardRowStatus_Object = MibTableColumn
pseudoWireE1T1CardRowStatus = _PseudoWireE1T1CardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 11),
    _PseudoWireE1T1CardRowStatus_Type()
)
pseudoWireE1T1CardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardRowStatus.setStatus("current")
_PseudoWireE1T1CardPSNEncapsulation_Type = PSNEncapsulationMode
_PseudoWireE1T1CardPSNEncapsulation_Object = MibTableColumn
pseudoWireE1T1CardPSNEncapsulation = _PseudoWireE1T1CardPSNEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 35, 1, 12),
    _PseudoWireE1T1CardPSNEncapsulation_Type()
)
pseudoWireE1T1CardPSNEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pseudoWireE1T1CardPSNEncapsulation.setStatus("current")
_Ethernet1x10GHighPerCardTable_Object = MibTable
ethernet1x10GHighPerCardTable = _Ethernet1x10GHighPerCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36)
)
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardTable.setStatus("current")
_Ethernet1x10GHighPerCardEntry_Object = MibTableRow
ethernet1x10GHighPerCardEntry = _Ethernet1x10GHighPerCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1)
)
ethernet1x10GHighPerCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardEntry.setStatus("current")
_Ethernet1x10GHighPerCardEntityIndex_Type = PhysicalIndex
_Ethernet1x10GHighPerCardEntityIndex_Object = MibTableColumn
ethernet1x10GHighPerCardEntityIndex = _Ethernet1x10GHighPerCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 1),
    _Ethernet1x10GHighPerCardEntityIndex_Type()
)
ethernet1x10GHighPerCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardEntityIndex.setStatus("current")
_Ethernet1x10GHighPerCardAdminState_Type = AdminState
_Ethernet1x10GHighPerCardAdminState_Object = MibTableColumn
ethernet1x10GHighPerCardAdminState = _Ethernet1x10GHighPerCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 2),
    _Ethernet1x10GHighPerCardAdminState_Type()
)
ethernet1x10GHighPerCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardAdminState.setStatus("current")
_Ethernet1x10GHighPerCardOperationalState_Type = OperationalState
_Ethernet1x10GHighPerCardOperationalState_Object = MibTableColumn
ethernet1x10GHighPerCardOperationalState = _Ethernet1x10GHighPerCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 3),
    _Ethernet1x10GHighPerCardOperationalState_Type()
)
ethernet1x10GHighPerCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardOperationalState.setStatus("current")
_Ethernet1x10GHighPerCardSecondaryState_Type = SecondaryState
_Ethernet1x10GHighPerCardSecondaryState_Object = MibTableColumn
ethernet1x10GHighPerCardSecondaryState = _Ethernet1x10GHighPerCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 4),
    _Ethernet1x10GHighPerCardSecondaryState_Type()
)
ethernet1x10GHighPerCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardSecondaryState.setStatus("current")
_Ethernet1x10GHighPerCardTemperature_Type = Integer32
_Ethernet1x10GHighPerCardTemperature_Object = MibTableColumn
ethernet1x10GHighPerCardTemperature = _Ethernet1x10GHighPerCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 5),
    _Ethernet1x10GHighPerCardTemperature_Type()
)
ethernet1x10GHighPerCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardTemperature.setStatus("current")
_Ethernet1x10GHighPerCardSnmpDyingGaspEnabled_Type = TruthValue
_Ethernet1x10GHighPerCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernet1x10GHighPerCardSnmpDyingGaspEnabled = _Ethernet1x10GHighPerCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 6),
    _Ethernet1x10GHighPerCardSnmpDyingGaspEnabled_Type()
)
ethernet1x10GHighPerCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardSnmpDyingGaspEnabled.setStatus("current")
_Ethernet1x10GHighPerCardRestartAction_Type = RestartType
_Ethernet1x10GHighPerCardRestartAction_Object = MibTableColumn
ethernet1x10GHighPerCardRestartAction = _Ethernet1x10GHighPerCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 7),
    _Ethernet1x10GHighPerCardRestartAction_Type()
)
ethernet1x10GHighPerCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardRestartAction.setStatus("current")
_Ethernet1x10GHighPerCardStorageType_Type = StorageType
_Ethernet1x10GHighPerCardStorageType_Object = MibTableColumn
ethernet1x10GHighPerCardStorageType = _Ethernet1x10GHighPerCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 8),
    _Ethernet1x10GHighPerCardStorageType_Type()
)
ethernet1x10GHighPerCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardStorageType.setStatus("current")
_Ethernet1x10GHighPerCardRowStatus_Type = RowStatus
_Ethernet1x10GHighPerCardRowStatus_Object = MibTableColumn
ethernet1x10GHighPerCardRowStatus = _Ethernet1x10GHighPerCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 9),
    _Ethernet1x10GHighPerCardRowStatus_Type()
)
ethernet1x10GHighPerCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardRowStatus.setStatus("current")
_Ethernet1x10GHighPerCardForceOffLineAction_Type = TruthValue
_Ethernet1x10GHighPerCardForceOffLineAction_Object = MibTableColumn
ethernet1x10GHighPerCardForceOffLineAction = _Ethernet1x10GHighPerCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 36, 1, 10),
    _Ethernet1x10GHighPerCardForceOffLineAction_Type()
)
ethernet1x10GHighPerCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardForceOffLineAction.setStatus("current")
_Ethernet10x1GHighPerCardTable_Object = MibTable
ethernet10x1GHighPerCardTable = _Ethernet10x1GHighPerCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37)
)
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardTable.setStatus("current")
_Ethernet10x1GHighPerCardEntry_Object = MibTableRow
ethernet10x1GHighPerCardEntry = _Ethernet10x1GHighPerCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1)
)
ethernet10x1GHighPerCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardEntry.setStatus("current")
_Ethernet10x1GHighPerCardEntityIndex_Type = PhysicalIndex
_Ethernet10x1GHighPerCardEntityIndex_Object = MibTableColumn
ethernet10x1GHighPerCardEntityIndex = _Ethernet10x1GHighPerCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 1),
    _Ethernet10x1GHighPerCardEntityIndex_Type()
)
ethernet10x1GHighPerCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardEntityIndex.setStatus("current")
_Ethernet10x1GHighPerCardAdminState_Type = AdminState
_Ethernet10x1GHighPerCardAdminState_Object = MibTableColumn
ethernet10x1GHighPerCardAdminState = _Ethernet10x1GHighPerCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 2),
    _Ethernet10x1GHighPerCardAdminState_Type()
)
ethernet10x1GHighPerCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardAdminState.setStatus("current")
_Ethernet10x1GHighPerCardOperationalState_Type = OperationalState
_Ethernet10x1GHighPerCardOperationalState_Object = MibTableColumn
ethernet10x1GHighPerCardOperationalState = _Ethernet10x1GHighPerCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 3),
    _Ethernet10x1GHighPerCardOperationalState_Type()
)
ethernet10x1GHighPerCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardOperationalState.setStatus("current")
_Ethernet10x1GHighPerCardSecondaryState_Type = SecondaryState
_Ethernet10x1GHighPerCardSecondaryState_Object = MibTableColumn
ethernet10x1GHighPerCardSecondaryState = _Ethernet10x1GHighPerCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 4),
    _Ethernet10x1GHighPerCardSecondaryState_Type()
)
ethernet10x1GHighPerCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardSecondaryState.setStatus("current")
_Ethernet10x1GHighPerCardTemperature_Type = Integer32
_Ethernet10x1GHighPerCardTemperature_Object = MibTableColumn
ethernet10x1GHighPerCardTemperature = _Ethernet10x1GHighPerCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 5),
    _Ethernet10x1GHighPerCardTemperature_Type()
)
ethernet10x1GHighPerCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardTemperature.setStatus("current")
_Ethernet10x1GHighPerCardSnmpDyingGaspEnabled_Type = TruthValue
_Ethernet10x1GHighPerCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernet10x1GHighPerCardSnmpDyingGaspEnabled = _Ethernet10x1GHighPerCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 6),
    _Ethernet10x1GHighPerCardSnmpDyingGaspEnabled_Type()
)
ethernet10x1GHighPerCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardSnmpDyingGaspEnabled.setStatus("current")
_Ethernet10x1GHighPerCardRestartAction_Type = RestartType
_Ethernet10x1GHighPerCardRestartAction_Object = MibTableColumn
ethernet10x1GHighPerCardRestartAction = _Ethernet10x1GHighPerCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 7),
    _Ethernet10x1GHighPerCardRestartAction_Type()
)
ethernet10x1GHighPerCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardRestartAction.setStatus("current")
_Ethernet10x1GHighPerCardStorageType_Type = StorageType
_Ethernet10x1GHighPerCardStorageType_Object = MibTableColumn
ethernet10x1GHighPerCardStorageType = _Ethernet10x1GHighPerCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 8),
    _Ethernet10x1GHighPerCardStorageType_Type()
)
ethernet10x1GHighPerCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardStorageType.setStatus("current")
_Ethernet10x1GHighPerCardRowStatus_Type = RowStatus
_Ethernet10x1GHighPerCardRowStatus_Object = MibTableColumn
ethernet10x1GHighPerCardRowStatus = _Ethernet10x1GHighPerCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 9),
    _Ethernet10x1GHighPerCardRowStatus_Type()
)
ethernet10x1GHighPerCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardRowStatus.setStatus("current")
_Ethernet10x1GHighPerCardForceOffLineAction_Type = TruthValue
_Ethernet10x1GHighPerCardForceOffLineAction_Object = MibTableColumn
ethernet10x1GHighPerCardForceOffLineAction = _Ethernet10x1GHighPerCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 37, 1, 10),
    _Ethernet10x1GHighPerCardForceOffLineAction_Type()
)
ethernet10x1GHighPerCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet10x1GHighPerCardForceOffLineAction.setStatus("current")
_EthernetNTET1804CardTable_Object = MibTable
ethernetNTET1804CardTable = _EthernetNTET1804CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38)
)
if mibBuilder.loadTexts:
    ethernetNTET1804CardTable.setStatus("current")
_EthernetNTET1804CardEntry_Object = MibTableRow
ethernetNTET1804CardEntry = _EthernetNTET1804CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1)
)
ethernetNTET1804CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTET1804CardEntry.setStatus("current")
_EthernetNTET1804CardEntityIndex_Type = PhysicalIndex
_EthernetNTET1804CardEntityIndex_Object = MibTableColumn
ethernetNTET1804CardEntityIndex = _EthernetNTET1804CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 1),
    _EthernetNTET1804CardEntityIndex_Type()
)
ethernetNTET1804CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET1804CardEntityIndex.setStatus("current")
_EthernetNTET1804CardAdminState_Type = AdminState
_EthernetNTET1804CardAdminState_Object = MibTableColumn
ethernetNTET1804CardAdminState = _EthernetNTET1804CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 2),
    _EthernetNTET1804CardAdminState_Type()
)
ethernetNTET1804CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET1804CardAdminState.setStatus("current")
_EthernetNTET1804CardOperationalState_Type = OperationalState
_EthernetNTET1804CardOperationalState_Object = MibTableColumn
ethernetNTET1804CardOperationalState = _EthernetNTET1804CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 3),
    _EthernetNTET1804CardOperationalState_Type()
)
ethernetNTET1804CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET1804CardOperationalState.setStatus("current")
_EthernetNTET1804CardSecondaryState_Type = SecondaryState
_EthernetNTET1804CardSecondaryState_Object = MibTableColumn
ethernetNTET1804CardSecondaryState = _EthernetNTET1804CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 4),
    _EthernetNTET1804CardSecondaryState_Type()
)
ethernetNTET1804CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET1804CardSecondaryState.setStatus("current")
_EthernetNTET1804CardVoltage_Type = Integer32
_EthernetNTET1804CardVoltage_Object = MibTableColumn
ethernetNTET1804CardVoltage = _EthernetNTET1804CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 5),
    _EthernetNTET1804CardVoltage_Type()
)
ethernetNTET1804CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET1804CardVoltage.setStatus("current")
_EthernetNTET1804CardTemperature_Type = Integer32
_EthernetNTET1804CardTemperature_Object = MibTableColumn
ethernetNTET1804CardTemperature = _EthernetNTET1804CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 6),
    _EthernetNTET1804CardTemperature_Type()
)
ethernetNTET1804CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET1804CardTemperature.setStatus("current")
_EthernetNTET1804CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTET1804CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTET1804CardSnmpDyingGaspEnabled = _EthernetNTET1804CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 7),
    _EthernetNTET1804CardSnmpDyingGaspEnabled_Type()
)
ethernetNTET1804CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET1804CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTET1804CardRestartAction_Type = RestartType
_EthernetNTET1804CardRestartAction_Object = MibTableColumn
ethernetNTET1804CardRestartAction = _EthernetNTET1804CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 8),
    _EthernetNTET1804CardRestartAction_Type()
)
ethernetNTET1804CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET1804CardRestartAction.setStatus("current")
_EthernetNTET1804CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTET1804CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTET1804CardFineGrainedPmInterval = _EthernetNTET1804CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 9),
    _EthernetNTET1804CardFineGrainedPmInterval_Type()
)
ethernetNTET1804CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET1804CardFineGrainedPmInterval.setStatus("current")
_EthernetNTET1804CardMode_Type = PortCarrierType
_EthernetNTET1804CardMode_Object = MibTableColumn
ethernetNTET1804CardMode = _EthernetNTET1804CardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 38, 1, 10),
    _EthernetNTET1804CardMode_Type()
)
ethernetNTET1804CardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET1804CardMode.setStatus("current")
_EthernetNTET3204CardTable_Object = MibTable
ethernetNTET3204CardTable = _EthernetNTET3204CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39)
)
if mibBuilder.loadTexts:
    ethernetNTET3204CardTable.setStatus("current")
_EthernetNTET3204CardEntry_Object = MibTableRow
ethernetNTET3204CardEntry = _EthernetNTET3204CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1)
)
ethernetNTET3204CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTET3204CardEntry.setStatus("current")
_EthernetNTET3204CardEntityIndex_Type = PhysicalIndex
_EthernetNTET3204CardEntityIndex_Object = MibTableColumn
ethernetNTET3204CardEntityIndex = _EthernetNTET3204CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 1),
    _EthernetNTET3204CardEntityIndex_Type()
)
ethernetNTET3204CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET3204CardEntityIndex.setStatus("current")
_EthernetNTET3204CardAdminState_Type = AdminState
_EthernetNTET3204CardAdminState_Object = MibTableColumn
ethernetNTET3204CardAdminState = _EthernetNTET3204CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 2),
    _EthernetNTET3204CardAdminState_Type()
)
ethernetNTET3204CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET3204CardAdminState.setStatus("current")
_EthernetNTET3204CardOperationalState_Type = OperationalState
_EthernetNTET3204CardOperationalState_Object = MibTableColumn
ethernetNTET3204CardOperationalState = _EthernetNTET3204CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 3),
    _EthernetNTET3204CardOperationalState_Type()
)
ethernetNTET3204CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET3204CardOperationalState.setStatus("current")
_EthernetNTET3204CardSecondaryState_Type = SecondaryState
_EthernetNTET3204CardSecondaryState_Object = MibTableColumn
ethernetNTET3204CardSecondaryState = _EthernetNTET3204CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 4),
    _EthernetNTET3204CardSecondaryState_Type()
)
ethernetNTET3204CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET3204CardSecondaryState.setStatus("current")
_EthernetNTET3204CardVoltage_Type = Integer32
_EthernetNTET3204CardVoltage_Object = MibTableColumn
ethernetNTET3204CardVoltage = _EthernetNTET3204CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 5),
    _EthernetNTET3204CardVoltage_Type()
)
ethernetNTET3204CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET3204CardVoltage.setStatus("current")
_EthernetNTET3204CardTemperature_Type = Integer32
_EthernetNTET3204CardTemperature_Object = MibTableColumn
ethernetNTET3204CardTemperature = _EthernetNTET3204CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 6),
    _EthernetNTET3204CardTemperature_Type()
)
ethernetNTET3204CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTET3204CardTemperature.setStatus("current")
_EthernetNTET3204CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTET3204CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTET3204CardSnmpDyingGaspEnabled = _EthernetNTET3204CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 7),
    _EthernetNTET3204CardSnmpDyingGaspEnabled_Type()
)
ethernetNTET3204CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET3204CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTET3204CardRestartAction_Type = RestartType
_EthernetNTET3204CardRestartAction_Object = MibTableColumn
ethernetNTET3204CardRestartAction = _EthernetNTET3204CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 8),
    _EthernetNTET3204CardRestartAction_Type()
)
ethernetNTET3204CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET3204CardRestartAction.setStatus("current")
_EthernetNTET3204CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTET3204CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTET3204CardFineGrainedPmInterval = _EthernetNTET3204CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 9),
    _EthernetNTET3204CardFineGrainedPmInterval_Type()
)
ethernetNTET3204CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET3204CardFineGrainedPmInterval.setStatus("current")
_EthernetNTET3204CardMode_Type = PortCarrierType
_EthernetNTET3204CardMode_Object = MibTableColumn
ethernetNTET3204CardMode = _EthernetNTET3204CardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 39, 1, 10),
    _EthernetNTET3204CardMode_Type()
)
ethernetNTET3204CardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTET3204CardMode.setStatus("current")
_EthernetNTEGESyncProbeCardTable_Object = MibTable
ethernetNTEGESyncProbeCardTable = _EthernetNTEGESyncProbeCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40)
)
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardTable.setStatus("current")
_EthernetNTEGESyncProbeCardEntry_Object = MibTableRow
ethernetNTEGESyncProbeCardEntry = _EthernetNTEGESyncProbeCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1)
)
ethernetNTEGESyncProbeCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardEntry.setStatus("current")
_EthernetNTEGESyncProbeCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGESyncProbeCardEntityIndex_Object = MibTableColumn
ethernetNTEGESyncProbeCardEntityIndex = _EthernetNTEGESyncProbeCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 1),
    _EthernetNTEGESyncProbeCardEntityIndex_Type()
)
ethernetNTEGESyncProbeCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardEntityIndex.setStatus("current")
_EthernetNTEGESyncProbeCardAdminState_Type = AdminState
_EthernetNTEGESyncProbeCardAdminState_Object = MibTableColumn
ethernetNTEGESyncProbeCardAdminState = _EthernetNTEGESyncProbeCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 2),
    _EthernetNTEGESyncProbeCardAdminState_Type()
)
ethernetNTEGESyncProbeCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardAdminState.setStatus("current")
_EthernetNTEGESyncProbeCardOperationalState_Type = OperationalState
_EthernetNTEGESyncProbeCardOperationalState_Object = MibTableColumn
ethernetNTEGESyncProbeCardOperationalState = _EthernetNTEGESyncProbeCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 3),
    _EthernetNTEGESyncProbeCardOperationalState_Type()
)
ethernetNTEGESyncProbeCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardOperationalState.setStatus("current")
_EthernetNTEGESyncProbeCardSecondaryState_Type = SecondaryState
_EthernetNTEGESyncProbeCardSecondaryState_Object = MibTableColumn
ethernetNTEGESyncProbeCardSecondaryState = _EthernetNTEGESyncProbeCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 4),
    _EthernetNTEGESyncProbeCardSecondaryState_Type()
)
ethernetNTEGESyncProbeCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardSecondaryState.setStatus("current")
_EthernetNTEGESyncProbeCardVoltage_Type = Integer32
_EthernetNTEGESyncProbeCardVoltage_Object = MibTableColumn
ethernetNTEGESyncProbeCardVoltage = _EthernetNTEGESyncProbeCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 5),
    _EthernetNTEGESyncProbeCardVoltage_Type()
)
ethernetNTEGESyncProbeCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardVoltage.setStatus("current")
_EthernetNTEGESyncProbeCardTemperature_Type = Integer32
_EthernetNTEGESyncProbeCardTemperature_Object = MibTableColumn
ethernetNTEGESyncProbeCardTemperature = _EthernetNTEGESyncProbeCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 6),
    _EthernetNTEGESyncProbeCardTemperature_Type()
)
ethernetNTEGESyncProbeCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardTemperature.setStatus("current")
_EthernetNTEGESyncProbeCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGESyncProbeCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGESyncProbeCardSnmpDyingGaspEnabled = _EthernetNTEGESyncProbeCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 7),
    _EthernetNTEGESyncProbeCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGESyncProbeCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGESyncProbeCardRestartAction_Type = RestartType
_EthernetNTEGESyncProbeCardRestartAction_Object = MibTableColumn
ethernetNTEGESyncProbeCardRestartAction = _EthernetNTEGESyncProbeCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 8),
    _EthernetNTEGESyncProbeCardRestartAction_Type()
)
ethernetNTEGESyncProbeCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardRestartAction.setStatus("current")
_EthernetNTEGESyncProbeCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGESyncProbeCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGESyncProbeCardFineGrainedPmInterval = _EthernetNTEGESyncProbeCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 40, 1, 9),
    _EthernetNTEGESyncProbeCardFineGrainedPmInterval_Type()
)
ethernetNTEGESyncProbeCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGESyncProbeCardFineGrainedPmInterval.setStatus("current")
_EthernetGE8SCCCardTable_Object = MibTable
ethernetGE8SCCCardTable = _EthernetGE8SCCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41)
)
if mibBuilder.loadTexts:
    ethernetGE8SCCCardTable.setStatus("current")
_EthernetGE8SCCCardEntry_Object = MibTableRow
ethernetGE8SCCCardEntry = _EthernetGE8SCCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1)
)
ethernetGE8SCCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetGE8SCCCardEntry.setStatus("current")
_EthernetGE8SCCCardEntityIndex_Type = PhysicalIndex
_EthernetGE8SCCCardEntityIndex_Object = MibTableColumn
ethernetGE8SCCCardEntityIndex = _EthernetGE8SCCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 1),
    _EthernetGE8SCCCardEntityIndex_Type()
)
ethernetGE8SCCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardEntityIndex.setStatus("current")
_EthernetGE8SCCCardAdminState_Type = AdminState
_EthernetGE8SCCCardAdminState_Object = MibTableColumn
ethernetGE8SCCCardAdminState = _EthernetGE8SCCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 2),
    _EthernetGE8SCCCardAdminState_Type()
)
ethernetGE8SCCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardAdminState.setStatus("current")
_EthernetGE8SCCCardOperationalState_Type = OperationalState
_EthernetGE8SCCCardOperationalState_Object = MibTableColumn
ethernetGE8SCCCardOperationalState = _EthernetGE8SCCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 3),
    _EthernetGE8SCCCardOperationalState_Type()
)
ethernetGE8SCCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardOperationalState.setStatus("current")
_EthernetGE8SCCCardSecondaryState_Type = SecondaryState
_EthernetGE8SCCCardSecondaryState_Object = MibTableColumn
ethernetGE8SCCCardSecondaryState = _EthernetGE8SCCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 4),
    _EthernetGE8SCCCardSecondaryState_Type()
)
ethernetGE8SCCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardSecondaryState.setStatus("current")
_EthernetGE8SCCCardVoltage_Type = Integer32
_EthernetGE8SCCCardVoltage_Object = MibTableColumn
ethernetGE8SCCCardVoltage = _EthernetGE8SCCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 5),
    _EthernetGE8SCCCardVoltage_Type()
)
ethernetGE8SCCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardVoltage.setStatus("current")
_EthernetGE8SCCCardTemperature_Type = Integer32
_EthernetGE8SCCCardTemperature_Object = MibTableColumn
ethernetGE8SCCCardTemperature = _EthernetGE8SCCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 6),
    _EthernetGE8SCCCardTemperature_Type()
)
ethernetGE8SCCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardTemperature.setStatus("current")
_EthernetGE8SCCCardRestartAction_Type = RestartType
_EthernetGE8SCCCardRestartAction_Object = MibTableColumn
ethernetGE8SCCCardRestartAction = _EthernetGE8SCCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 7),
    _EthernetGE8SCCCardRestartAction_Type()
)
ethernetGE8SCCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardRestartAction.setStatus("current")
_EthernetGE8SCCCardStorageType_Type = StorageType
_EthernetGE8SCCCardStorageType_Object = MibTableColumn
ethernetGE8SCCCardStorageType = _EthernetGE8SCCCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 8),
    _EthernetGE8SCCCardStorageType_Type()
)
ethernetGE8SCCCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardStorageType.setStatus("current")
_EthernetGE8SCCCardRowStatus_Type = RowStatus
_EthernetGE8SCCCardRowStatus_Object = MibTableColumn
ethernetGE8SCCCardRowStatus = _EthernetGE8SCCCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 41, 1, 9),
    _EthernetGE8SCCCardRowStatus_Type()
)
ethernetGE8SCCCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE8SCCCardRowStatus.setStatus("current")
_EthernetNTEGE114HCardTable_Object = MibTable
ethernetNTEGE114HCardTable = _EthernetNTEGE114HCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardTable.setStatus("current")
_EthernetNTEGE114HCardEntry_Object = MibTableRow
ethernetNTEGE114HCardEntry = _EthernetNTEGE114HCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1)
)
ethernetNTEGE114HCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardEntry.setStatus("current")
_EthernetNTEGE114HCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114HCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114HCardEntityIndex = _EthernetNTEGE114HCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 1),
    _EthernetNTEGE114HCardEntityIndex_Type()
)
ethernetNTEGE114HCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardEntityIndex.setStatus("current")
_EthernetNTEGE114HCardAdminState_Type = AdminState
_EthernetNTEGE114HCardAdminState_Object = MibTableColumn
ethernetNTEGE114HCardAdminState = _EthernetNTEGE114HCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 2),
    _EthernetNTEGE114HCardAdminState_Type()
)
ethernetNTEGE114HCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardAdminState.setStatus("current")
_EthernetNTEGE114HCardOperationalState_Type = OperationalState
_EthernetNTEGE114HCardOperationalState_Object = MibTableColumn
ethernetNTEGE114HCardOperationalState = _EthernetNTEGE114HCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 3),
    _EthernetNTEGE114HCardOperationalState_Type()
)
ethernetNTEGE114HCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardOperationalState.setStatus("current")
_EthernetNTEGE114HCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114HCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114HCardSecondaryState = _EthernetNTEGE114HCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 4),
    _EthernetNTEGE114HCardSecondaryState_Type()
)
ethernetNTEGE114HCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardSecondaryState.setStatus("current")
_EthernetNTEGE114HCardVoltage_Type = Integer32
_EthernetNTEGE114HCardVoltage_Object = MibTableColumn
ethernetNTEGE114HCardVoltage = _EthernetNTEGE114HCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 5),
    _EthernetNTEGE114HCardVoltage_Type()
)
ethernetNTEGE114HCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardVoltage.setStatus("current")
_EthernetNTEGE114HCardTemperature_Type = Integer32
_EthernetNTEGE114HCardTemperature_Object = MibTableColumn
ethernetNTEGE114HCardTemperature = _EthernetNTEGE114HCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 6),
    _EthernetNTEGE114HCardTemperature_Type()
)
ethernetNTEGE114HCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardTemperature.setStatus("current")
_EthernetNTEGE114HCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114HCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114HCardSnmpDyingGaspEnabled = _EthernetNTEGE114HCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 7),
    _EthernetNTEGE114HCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114HCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114HCardRestartAction_Type = RestartType
_EthernetNTEGE114HCardRestartAction_Object = MibTableColumn
ethernetNTEGE114HCardRestartAction = _EthernetNTEGE114HCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 8),
    _EthernetNTEGE114HCardRestartAction_Type()
)
ethernetNTEGE114HCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardRestartAction.setStatus("current")
_EthernetNTEGE114HCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114HCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114HCardFineGrainedPmInterval = _EthernetNTEGE114HCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 9),
    _EthernetNTEGE114HCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114HCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114HCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114HCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114HCardSwitchPortActionPort = _EthernetNTEGE114HCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 10),
    _EthernetNTEGE114HCardSwitchPortActionPort_Type()
)
ethernetNTEGE114HCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114HCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114HCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114HCardSwitchPortAction = _EthernetNTEGE114HCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 42, 1, 11),
    _EthernetNTEGE114HCardSwitchPortAction_Type()
)
ethernetNTEGE114HCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114HCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114PHCardTable_Object = MibTable
ethernetNTEGE114PHCardTable = _EthernetNTEGE114PHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardTable.setStatus("current")
_EthernetNTEGE114PHCardEntry_Object = MibTableRow
ethernetNTEGE114PHCardEntry = _EthernetNTEGE114PHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1)
)
ethernetNTEGE114PHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardEntry.setStatus("current")
_EthernetNTEGE114PHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114PHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114PHCardEntityIndex = _EthernetNTEGE114PHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 1),
    _EthernetNTEGE114PHCardEntityIndex_Type()
)
ethernetNTEGE114PHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardEntityIndex.setStatus("current")
_EthernetNTEGE114PHCardAdminState_Type = AdminState
_EthernetNTEGE114PHCardAdminState_Object = MibTableColumn
ethernetNTEGE114PHCardAdminState = _EthernetNTEGE114PHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 2),
    _EthernetNTEGE114PHCardAdminState_Type()
)
ethernetNTEGE114PHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardAdminState.setStatus("current")
_EthernetNTEGE114PHCardOperationalState_Type = OperationalState
_EthernetNTEGE114PHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114PHCardOperationalState = _EthernetNTEGE114PHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 3),
    _EthernetNTEGE114PHCardOperationalState_Type()
)
ethernetNTEGE114PHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardOperationalState.setStatus("current")
_EthernetNTEGE114PHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114PHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114PHCardSecondaryState = _EthernetNTEGE114PHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 4),
    _EthernetNTEGE114PHCardSecondaryState_Type()
)
ethernetNTEGE114PHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardSecondaryState.setStatus("current")
_EthernetNTEGE114PHCardVoltage_Type = Integer32
_EthernetNTEGE114PHCardVoltage_Object = MibTableColumn
ethernetNTEGE114PHCardVoltage = _EthernetNTEGE114PHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 5),
    _EthernetNTEGE114PHCardVoltage_Type()
)
ethernetNTEGE114PHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardVoltage.setStatus("current")
_EthernetNTEGE114PHCardTemperature_Type = Integer32
_EthernetNTEGE114PHCardTemperature_Object = MibTableColumn
ethernetNTEGE114PHCardTemperature = _EthernetNTEGE114PHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 6),
    _EthernetNTEGE114PHCardTemperature_Type()
)
ethernetNTEGE114PHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardTemperature.setStatus("current")
_EthernetNTEGE114PHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114PHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114PHCardSnmpDyingGaspEnabled = _EthernetNTEGE114PHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 7),
    _EthernetNTEGE114PHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114PHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114PHCardRestartAction_Type = RestartType
_EthernetNTEGE114PHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114PHCardRestartAction = _EthernetNTEGE114PHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 8),
    _EthernetNTEGE114PHCardRestartAction_Type()
)
ethernetNTEGE114PHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardRestartAction.setStatus("current")
_EthernetNTEGE114PHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114PHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114PHCardFineGrainedPmInterval = _EthernetNTEGE114PHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 9),
    _EthernetNTEGE114PHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114PHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114PHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114PHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114PHCardSwitchPortActionPort = _EthernetNTEGE114PHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 10),
    _EthernetNTEGE114PHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114PHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114PHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114PHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114PHCardSwitchPortAction = _EthernetNTEGE114PHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 43, 1, 11),
    _EthernetNTEGE114PHCardSwitchPortAction_Type()
)
ethernetNTEGE114PHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114PHCardSwitchPortAction.setStatus("current")
_EthernetFE36ECardTable_Object = MibTable
ethernetFE36ECardTable = _EthernetFE36ECardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44)
)
if mibBuilder.loadTexts:
    ethernetFE36ECardTable.setStatus("current")
_EthernetFE36ECardEntry_Object = MibTableRow
ethernetFE36ECardEntry = _EthernetFE36ECardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1)
)
ethernetFE36ECardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetFE36ECardEntry.setStatus("current")
_EthernetFE36ECardEntityIndex_Type = PhysicalIndex
_EthernetFE36ECardEntityIndex_Object = MibTableColumn
ethernetFE36ECardEntityIndex = _EthernetFE36ECardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 1),
    _EthernetFE36ECardEntityIndex_Type()
)
ethernetFE36ECardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFE36ECardEntityIndex.setStatus("current")
_EthernetFE36ECardAdminState_Type = AdminState
_EthernetFE36ECardAdminState_Object = MibTableColumn
ethernetFE36ECardAdminState = _EthernetFE36ECardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 2),
    _EthernetFE36ECardAdminState_Type()
)
ethernetFE36ECardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetFE36ECardAdminState.setStatus("current")
_EthernetFE36ECardOperationalState_Type = OperationalState
_EthernetFE36ECardOperationalState_Object = MibTableColumn
ethernetFE36ECardOperationalState = _EthernetFE36ECardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 3),
    _EthernetFE36ECardOperationalState_Type()
)
ethernetFE36ECardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFE36ECardOperationalState.setStatus("current")
_EthernetFE36ECardSecondaryState_Type = SecondaryState
_EthernetFE36ECardSecondaryState_Object = MibTableColumn
ethernetFE36ECardSecondaryState = _EthernetFE36ECardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 4),
    _EthernetFE36ECardSecondaryState_Type()
)
ethernetFE36ECardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFE36ECardSecondaryState.setStatus("current")
_EthernetFE36ECardTemperature_Type = Integer32
_EthernetFE36ECardTemperature_Object = MibTableColumn
ethernetFE36ECardTemperature = _EthernetFE36ECardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 5),
    _EthernetFE36ECardTemperature_Type()
)
ethernetFE36ECardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFE36ECardTemperature.setStatus("current")
_EthernetFE36ECardRestartAction_Type = RestartType
_EthernetFE36ECardRestartAction_Object = MibTableColumn
ethernetFE36ECardRestartAction = _EthernetFE36ECardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 6),
    _EthernetFE36ECardRestartAction_Type()
)
ethernetFE36ECardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetFE36ECardRestartAction.setStatus("current")
_EthernetFE36ECardStorageType_Type = StorageType
_EthernetFE36ECardStorageType_Object = MibTableColumn
ethernetFE36ECardStorageType = _EthernetFE36ECardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 7),
    _EthernetFE36ECardStorageType_Type()
)
ethernetFE36ECardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetFE36ECardStorageType.setStatus("current")
_EthernetFE36ECardRowStatus_Type = RowStatus
_EthernetFE36ECardRowStatus_Object = MibTableColumn
ethernetFE36ECardRowStatus = _EthernetFE36ECardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 8),
    _EthernetFE36ECardRowStatus_Type()
)
ethernetFE36ECardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetFE36ECardRowStatus.setStatus("current")
_EthernetFE36ECardForceOffLineAction_Type = TruthValue
_EthernetFE36ECardForceOffLineAction_Object = MibTableColumn
ethernetFE36ECardForceOffLineAction = _EthernetFE36ECardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 9),
    _EthernetFE36ECardForceOffLineAction_Type()
)
ethernetFE36ECardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetFE36ECardForceOffLineAction.setStatus("current")
_EthernetFE36ECard8023azEnabled_Type = TruthValue
_EthernetFE36ECard8023azEnabled_Object = MibTableColumn
ethernetFE36ECard8023azEnabled = _EthernetFE36ECard8023azEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 44, 1, 10),
    _EthernetFE36ECard8023azEnabled_Type()
)
ethernetFE36ECard8023azEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetFE36ECard8023azEnabled.setStatus("current")
_EthernetNTEGE114SHCardTable_Object = MibTable
ethernetNTEGE114SHCardTable = _EthernetNTEGE114SHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardTable.setStatus("current")
_EthernetNTEGE114SHCardEntry_Object = MibTableRow
ethernetNTEGE114SHCardEntry = _EthernetNTEGE114SHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1)
)
ethernetNTEGE114SHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardEntry.setStatus("current")
_EthernetNTEGE114SHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114SHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114SHCardEntityIndex = _EthernetNTEGE114SHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 1),
    _EthernetNTEGE114SHCardEntityIndex_Type()
)
ethernetNTEGE114SHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardEntityIndex.setStatus("current")
_EthernetNTEGE114SHCardAdminState_Type = AdminState
_EthernetNTEGE114SHCardAdminState_Object = MibTableColumn
ethernetNTEGE114SHCardAdminState = _EthernetNTEGE114SHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 2),
    _EthernetNTEGE114SHCardAdminState_Type()
)
ethernetNTEGE114SHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardAdminState.setStatus("current")
_EthernetNTEGE114SHCardOperationalState_Type = OperationalState
_EthernetNTEGE114SHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114SHCardOperationalState = _EthernetNTEGE114SHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 3),
    _EthernetNTEGE114SHCardOperationalState_Type()
)
ethernetNTEGE114SHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardOperationalState.setStatus("current")
_EthernetNTEGE114SHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114SHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114SHCardSecondaryState = _EthernetNTEGE114SHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 4),
    _EthernetNTEGE114SHCardSecondaryState_Type()
)
ethernetNTEGE114SHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardSecondaryState.setStatus("current")
_EthernetNTEGE114SHCardVoltage_Type = Integer32
_EthernetNTEGE114SHCardVoltage_Object = MibTableColumn
ethernetNTEGE114SHCardVoltage = _EthernetNTEGE114SHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 5),
    _EthernetNTEGE114SHCardVoltage_Type()
)
ethernetNTEGE114SHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardVoltage.setStatus("current")
_EthernetNTEGE114SHCardTemperature_Type = Integer32
_EthernetNTEGE114SHCardTemperature_Object = MibTableColumn
ethernetNTEGE114SHCardTemperature = _EthernetNTEGE114SHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 6),
    _EthernetNTEGE114SHCardTemperature_Type()
)
ethernetNTEGE114SHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardTemperature.setStatus("current")
_EthernetNTEGE114SHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114SHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114SHCardSnmpDyingGaspEnabled = _EthernetNTEGE114SHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 7),
    _EthernetNTEGE114SHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114SHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114SHCardRestartAction_Type = RestartType
_EthernetNTEGE114SHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114SHCardRestartAction = _EthernetNTEGE114SHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 8),
    _EthernetNTEGE114SHCardRestartAction_Type()
)
ethernetNTEGE114SHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardRestartAction.setStatus("current")
_EthernetNTEGE114SHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114SHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114SHCardFineGrainedPmInterval = _EthernetNTEGE114SHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 9),
    _EthernetNTEGE114SHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114SHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114SHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114SHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114SHCardSwitchPortActionPort = _EthernetNTEGE114SHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 10),
    _EthernetNTEGE114SHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114SHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114SHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114SHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114SHCardSwitchPortAction = _EthernetNTEGE114SHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 45, 1, 11),
    _EthernetNTEGE114SHCardSwitchPortAction_Type()
)
ethernetNTEGE114SHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114SCardTable_Object = MibTable
ethernetNTEGE114SCardTable = _EthernetNTEGE114SCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardTable.setStatus("current")
_EthernetNTEGE114SCardEntry_Object = MibTableRow
ethernetNTEGE114SCardEntry = _EthernetNTEGE114SCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1)
)
ethernetNTEGE114SCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardEntry.setStatus("current")
_EthernetNTEGE114SCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114SCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114SCardEntityIndex = _EthernetNTEGE114SCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 1),
    _EthernetNTEGE114SCardEntityIndex_Type()
)
ethernetNTEGE114SCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardEntityIndex.setStatus("current")
_EthernetNTEGE114SCardAdminState_Type = AdminState
_EthernetNTEGE114SCardAdminState_Object = MibTableColumn
ethernetNTEGE114SCardAdminState = _EthernetNTEGE114SCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 2),
    _EthernetNTEGE114SCardAdminState_Type()
)
ethernetNTEGE114SCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardAdminState.setStatus("current")
_EthernetNTEGE114SCardOperationalState_Type = OperationalState
_EthernetNTEGE114SCardOperationalState_Object = MibTableColumn
ethernetNTEGE114SCardOperationalState = _EthernetNTEGE114SCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 3),
    _EthernetNTEGE114SCardOperationalState_Type()
)
ethernetNTEGE114SCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardOperationalState.setStatus("current")
_EthernetNTEGE114SCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114SCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114SCardSecondaryState = _EthernetNTEGE114SCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 4),
    _EthernetNTEGE114SCardSecondaryState_Type()
)
ethernetNTEGE114SCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardSecondaryState.setStatus("current")
_EthernetNTEGE114SCardVoltage_Type = Integer32
_EthernetNTEGE114SCardVoltage_Object = MibTableColumn
ethernetNTEGE114SCardVoltage = _EthernetNTEGE114SCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 5),
    _EthernetNTEGE114SCardVoltage_Type()
)
ethernetNTEGE114SCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardVoltage.setStatus("current")
_EthernetNTEGE114SCardTemperature_Type = Integer32
_EthernetNTEGE114SCardTemperature_Object = MibTableColumn
ethernetNTEGE114SCardTemperature = _EthernetNTEGE114SCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 6),
    _EthernetNTEGE114SCardTemperature_Type()
)
ethernetNTEGE114SCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardTemperature.setStatus("current")
_EthernetNTEGE114SCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114SCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114SCardSnmpDyingGaspEnabled = _EthernetNTEGE114SCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 7),
    _EthernetNTEGE114SCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114SCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114SCardRestartAction_Type = RestartType
_EthernetNTEGE114SCardRestartAction_Object = MibTableColumn
ethernetNTEGE114SCardRestartAction = _EthernetNTEGE114SCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 8),
    _EthernetNTEGE114SCardRestartAction_Type()
)
ethernetNTEGE114SCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardRestartAction.setStatus("current")
_EthernetNTEGE114SCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114SCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114SCardFineGrainedPmInterval = _EthernetNTEGE114SCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 9),
    _EthernetNTEGE114SCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114SCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114SCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114SCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114SCardSwitchPortActionPort = _EthernetNTEGE114SCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 10),
    _EthernetNTEGE114SCardSwitchPortActionPort_Type()
)
ethernetNTEGE114SCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114SCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114SCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114SCardSwitchPortAction = _EthernetNTEGE114SCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 46, 1, 11),
    _EthernetNTEGE114SCardSwitchPortAction_Type()
)
ethernetNTEGE114SCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114SCardSwitchPortAction.setStatus("current")
_StuHighPerCardTable_Object = MibTable
stuHighPerCardTable = _StuHighPerCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47)
)
if mibBuilder.loadTexts:
    stuHighPerCardTable.setStatus("current")
_StuHighPerCardEntry_Object = MibTableRow
stuHighPerCardEntry = _StuHighPerCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1)
)
stuHighPerCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    stuHighPerCardEntry.setStatus("current")
_StuHighPerCardEntityIndex_Type = PhysicalIndex
_StuHighPerCardEntityIndex_Object = MibTableColumn
stuHighPerCardEntityIndex = _StuHighPerCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 1),
    _StuHighPerCardEntityIndex_Type()
)
stuHighPerCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuHighPerCardEntityIndex.setStatus("current")
_StuHighPerCardAdminState_Type = AdminState
_StuHighPerCardAdminState_Object = MibTableColumn
stuHighPerCardAdminState = _StuHighPerCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 2),
    _StuHighPerCardAdminState_Type()
)
stuHighPerCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuHighPerCardAdminState.setStatus("current")
_StuHighPerCardOperationalState_Type = OperationalState
_StuHighPerCardOperationalState_Object = MibTableColumn
stuHighPerCardOperationalState = _StuHighPerCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 3),
    _StuHighPerCardOperationalState_Type()
)
stuHighPerCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuHighPerCardOperationalState.setStatus("current")
_StuHighPerCardSecondaryState_Type = SecondaryState
_StuHighPerCardSecondaryState_Object = MibTableColumn
stuHighPerCardSecondaryState = _StuHighPerCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 4),
    _StuHighPerCardSecondaryState_Type()
)
stuHighPerCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuHighPerCardSecondaryState.setStatus("current")
_StuHighPerCardTemperature_Type = Integer32
_StuHighPerCardTemperature_Object = MibTableColumn
stuHighPerCardTemperature = _StuHighPerCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 5),
    _StuHighPerCardTemperature_Type()
)
stuHighPerCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuHighPerCardTemperature.setStatus("current")
_StuHighPerCardRestartAction_Type = RestartType
_StuHighPerCardRestartAction_Object = MibTableColumn
stuHighPerCardRestartAction = _StuHighPerCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 6),
    _StuHighPerCardRestartAction_Type()
)
stuHighPerCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuHighPerCardRestartAction.setStatus("current")
_StuHighPerCardStorageType_Type = StorageType
_StuHighPerCardStorageType_Object = MibTableColumn
stuHighPerCardStorageType = _StuHighPerCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 7),
    _StuHighPerCardStorageType_Type()
)
stuHighPerCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuHighPerCardStorageType.setStatus("current")
_StuHighPerCardRowStatus_Type = RowStatus
_StuHighPerCardRowStatus_Object = MibTableColumn
stuHighPerCardRowStatus = _StuHighPerCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 8),
    _StuHighPerCardRowStatus_Type()
)
stuHighPerCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuHighPerCardRowStatus.setStatus("current")
_StuHighPerCardForceOffLineAction_Type = TruthValue
_StuHighPerCardForceOffLineAction_Object = MibTableColumn
stuHighPerCardForceOffLineAction = _StuHighPerCardForceOffLineAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 47, 1, 9),
    _StuHighPerCardForceOffLineAction_Type()
)
stuHighPerCardForceOffLineAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuHighPerCardForceOffLineAction.setStatus("current")
_StiHighPerTable_Object = MibTable
stiHighPerTable = _StiHighPerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48)
)
if mibBuilder.loadTexts:
    stiHighPerTable.setStatus("current")
_StiHighPerEntry_Object = MibTableRow
stiHighPerEntry = _StiHighPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1)
)
stiHighPerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    stiHighPerEntry.setStatus("current")
_StiHighPerEntityIndex_Type = PhysicalIndex
_StiHighPerEntityIndex_Object = MibTableColumn
stiHighPerEntityIndex = _StiHighPerEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 1),
    _StiHighPerEntityIndex_Type()
)
stiHighPerEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiHighPerEntityIndex.setStatus("current")
_StiHighPerAdminState_Type = AdminState
_StiHighPerAdminState_Object = MibTableColumn
stiHighPerAdminState = _StiHighPerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 2),
    _StiHighPerAdminState_Type()
)
stiHighPerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiHighPerAdminState.setStatus("current")
_StiHighPerOperationalState_Type = OperationalState
_StiHighPerOperationalState_Object = MibTableColumn
stiHighPerOperationalState = _StiHighPerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 3),
    _StiHighPerOperationalState_Type()
)
stiHighPerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiHighPerOperationalState.setStatus("current")
_StiHighPerSecondaryState_Type = SecondaryState
_StiHighPerSecondaryState_Object = MibTableColumn
stiHighPerSecondaryState = _StiHighPerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 4),
    _StiHighPerSecondaryState_Type()
)
stiHighPerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiHighPerSecondaryState.setStatus("current")
_StiHighPerTemperature_Type = Integer32
_StiHighPerTemperature_Object = MibTableColumn
stiHighPerTemperature = _StiHighPerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 5),
    _StiHighPerTemperature_Type()
)
stiHighPerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiHighPerTemperature.setStatus("current")
_StiHighPerStorageType_Type = StorageType
_StiHighPerStorageType_Object = MibTableColumn
stiHighPerStorageType = _StiHighPerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 6),
    _StiHighPerStorageType_Type()
)
stiHighPerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiHighPerStorageType.setStatus("current")
_StiHighPerRowStatus_Type = RowStatus
_StiHighPerRowStatus_Object = MibTableColumn
stiHighPerRowStatus = _StiHighPerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 48, 1, 7),
    _StiHighPerRowStatus_Type()
)
stiHighPerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiHighPerRowStatus.setStatus("current")
_EthernetGE8ECCCardTable_Object = MibTable
ethernetGE8ECCCardTable = _EthernetGE8ECCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49)
)
if mibBuilder.loadTexts:
    ethernetGE8ECCCardTable.setStatus("current")
_EthernetGE8ECCCardEntry_Object = MibTableRow
ethernetGE8ECCCardEntry = _EthernetGE8ECCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1)
)
ethernetGE8ECCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetGE8ECCCardEntry.setStatus("current")
_EthernetGE8ECCCardEntityIndex_Type = PhysicalIndex
_EthernetGE8ECCCardEntityIndex_Object = MibTableColumn
ethernetGE8ECCCardEntityIndex = _EthernetGE8ECCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 1),
    _EthernetGE8ECCCardEntityIndex_Type()
)
ethernetGE8ECCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardEntityIndex.setStatus("current")
_EthernetGE8ECCCardAdminState_Type = AdminState
_EthernetGE8ECCCardAdminState_Object = MibTableColumn
ethernetGE8ECCCardAdminState = _EthernetGE8ECCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 2),
    _EthernetGE8ECCCardAdminState_Type()
)
ethernetGE8ECCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardAdminState.setStatus("current")
_EthernetGE8ECCCardOperationalState_Type = OperationalState
_EthernetGE8ECCCardOperationalState_Object = MibTableColumn
ethernetGE8ECCCardOperationalState = _EthernetGE8ECCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 3),
    _EthernetGE8ECCCardOperationalState_Type()
)
ethernetGE8ECCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardOperationalState.setStatus("current")
_EthernetGE8ECCCardSecondaryState_Type = SecondaryState
_EthernetGE8ECCCardSecondaryState_Object = MibTableColumn
ethernetGE8ECCCardSecondaryState = _EthernetGE8ECCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 4),
    _EthernetGE8ECCCardSecondaryState_Type()
)
ethernetGE8ECCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardSecondaryState.setStatus("current")
_EthernetGE8ECCCardVoltage_Type = Integer32
_EthernetGE8ECCCardVoltage_Object = MibTableColumn
ethernetGE8ECCCardVoltage = _EthernetGE8ECCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 5),
    _EthernetGE8ECCCardVoltage_Type()
)
ethernetGE8ECCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardVoltage.setStatus("current")
_EthernetGE8ECCCardTemperature_Type = Integer32
_EthernetGE8ECCCardTemperature_Object = MibTableColumn
ethernetGE8ECCCardTemperature = _EthernetGE8ECCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 6),
    _EthernetGE8ECCCardTemperature_Type()
)
ethernetGE8ECCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardTemperature.setStatus("current")
_EthernetGE8ECCCardRestartAction_Type = RestartType
_EthernetGE8ECCCardRestartAction_Object = MibTableColumn
ethernetGE8ECCCardRestartAction = _EthernetGE8ECCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 7),
    _EthernetGE8ECCCardRestartAction_Type()
)
ethernetGE8ECCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardRestartAction.setStatus("current")
_EthernetGE8ECCCardStorageType_Type = StorageType
_EthernetGE8ECCCardStorageType_Object = MibTableColumn
ethernetGE8ECCCardStorageType = _EthernetGE8ECCCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 8),
    _EthernetGE8ECCCardStorageType_Type()
)
ethernetGE8ECCCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardStorageType.setStatus("current")
_EthernetGE8ECCCardRowStatus_Type = RowStatus
_EthernetGE8ECCCardRowStatus_Object = MibTableColumn
ethernetGE8ECCCardRowStatus = _EthernetGE8ECCCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 49, 1, 9),
    _EthernetGE8ECCCardRowStatus_Type()
)
ethernetGE8ECCCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE8ECCCardRowStatus.setStatus("current")
_NetworkElementLLDPParamsTable_Object = MibTable
networkElementLLDPParamsTable = _NetworkElementLLDPParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 50)
)
if mibBuilder.loadTexts:
    networkElementLLDPParamsTable.setStatus("current")
_NetworkElementLLDPParamsEntry_Object = MibTableRow
networkElementLLDPParamsEntry = _NetworkElementLLDPParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 50, 1)
)
if mibBuilder.loadTexts:
    networkElementLLDPParamsEntry.setStatus("current")
_NeLLDPParamsLLDPEnableAction_Type = LLDPEnableAction
_NeLLDPParamsLLDPEnableAction_Object = MibTableColumn
neLLDPParamsLLDPEnableAction = _NeLLDPParamsLLDPEnableAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 50, 1, 1),
    _NeLLDPParamsLLDPEnableAction_Type()
)
neLLDPParamsLLDPEnableAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neLLDPParamsLLDPEnableAction.setStatus("current")
_EthernetNTESH1PCSCardTable_Object = MibTable
ethernetNTESH1PCSCardTable = _EthernetNTESH1PCSCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51)
)
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardTable.setStatus("current")
_EthernetNTESH1PCSCardEntry_Object = MibTableRow
ethernetNTESH1PCSCardEntry = _EthernetNTESH1PCSCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1)
)
ethernetNTESH1PCSCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardEntry.setStatus("current")
_EthernetNTESH1PCSCardEntityIndex_Type = PhysicalIndex
_EthernetNTESH1PCSCardEntityIndex_Object = MibTableColumn
ethernetNTESH1PCSCardEntityIndex = _EthernetNTESH1PCSCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 1),
    _EthernetNTESH1PCSCardEntityIndex_Type()
)
ethernetNTESH1PCSCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardEntityIndex.setStatus("current")
_EthernetNTESH1PCSCardAdminState_Type = AdminState
_EthernetNTESH1PCSCardAdminState_Object = MibTableColumn
ethernetNTESH1PCSCardAdminState = _EthernetNTESH1PCSCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 2),
    _EthernetNTESH1PCSCardAdminState_Type()
)
ethernetNTESH1PCSCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardAdminState.setStatus("current")
_EthernetNTESH1PCSCardOperationalState_Type = OperationalState
_EthernetNTESH1PCSCardOperationalState_Object = MibTableColumn
ethernetNTESH1PCSCardOperationalState = _EthernetNTESH1PCSCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 3),
    _EthernetNTESH1PCSCardOperationalState_Type()
)
ethernetNTESH1PCSCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardOperationalState.setStatus("current")
_EthernetNTESH1PCSCardSecondaryState_Type = SecondaryState
_EthernetNTESH1PCSCardSecondaryState_Object = MibTableColumn
ethernetNTESH1PCSCardSecondaryState = _EthernetNTESH1PCSCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 4),
    _EthernetNTESH1PCSCardSecondaryState_Type()
)
ethernetNTESH1PCSCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardSecondaryState.setStatus("current")
_EthernetNTESH1PCSCardVoltage_Type = Integer32
_EthernetNTESH1PCSCardVoltage_Object = MibTableColumn
ethernetNTESH1PCSCardVoltage = _EthernetNTESH1PCSCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 5),
    _EthernetNTESH1PCSCardVoltage_Type()
)
ethernetNTESH1PCSCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardVoltage.setStatus("current")
_EthernetNTESH1PCSCardTemperature_Type = Integer32
_EthernetNTESH1PCSCardTemperature_Object = MibTableColumn
ethernetNTESH1PCSCardTemperature = _EthernetNTESH1PCSCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 6),
    _EthernetNTESH1PCSCardTemperature_Type()
)
ethernetNTESH1PCSCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardTemperature.setStatus("current")
_EthernetNTESH1PCSCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTESH1PCSCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTESH1PCSCardSnmpDyingGaspEnabled = _EthernetNTESH1PCSCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 7),
    _EthernetNTESH1PCSCardSnmpDyingGaspEnabled_Type()
)
ethernetNTESH1PCSCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTESH1PCSCardRestartAction_Type = RestartType
_EthernetNTESH1PCSCardRestartAction_Object = MibTableColumn
ethernetNTESH1PCSCardRestartAction = _EthernetNTESH1PCSCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 8),
    _EthernetNTESH1PCSCardRestartAction_Type()
)
ethernetNTESH1PCSCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardRestartAction.setStatus("current")
_EthernetNTESH1PCSCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTESH1PCSCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTESH1PCSCardFineGrainedPmInterval = _EthernetNTESH1PCSCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 51, 1, 9),
    _EthernetNTESH1PCSCardFineGrainedPmInterval_Type()
)
ethernetNTESH1PCSCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTESH1PCSCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEOSA5411CardTable_Object = MibTable
ethernetNTEOSA5411CardTable = _EthernetNTEOSA5411CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52)
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardTable.setStatus("current")
_EthernetNTEOSA5411CardEntry_Object = MibTableRow
ethernetNTEOSA5411CardEntry = _EthernetNTEOSA5411CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1)
)
ethernetNTEOSA5411CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardEntry.setStatus("current")
_EthernetNTEOSA5411CardEntityIndex_Type = PhysicalIndex
_EthernetNTEOSA5411CardEntityIndex_Object = MibTableColumn
ethernetNTEOSA5411CardEntityIndex = _EthernetNTEOSA5411CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 1),
    _EthernetNTEOSA5411CardEntityIndex_Type()
)
ethernetNTEOSA5411CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardEntityIndex.setStatus("current")
_EthernetNTEOSA5411CardAdminState_Type = AdminState
_EthernetNTEOSA5411CardAdminState_Object = MibTableColumn
ethernetNTEOSA5411CardAdminState = _EthernetNTEOSA5411CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 2),
    _EthernetNTEOSA5411CardAdminState_Type()
)
ethernetNTEOSA5411CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardAdminState.setStatus("current")
_EthernetNTEOSA5411CardOperationalState_Type = OperationalState
_EthernetNTEOSA5411CardOperationalState_Object = MibTableColumn
ethernetNTEOSA5411CardOperationalState = _EthernetNTEOSA5411CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 3),
    _EthernetNTEOSA5411CardOperationalState_Type()
)
ethernetNTEOSA5411CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardOperationalState.setStatus("current")
_EthernetNTEOSA5411CardSecondaryState_Type = SecondaryState
_EthernetNTEOSA5411CardSecondaryState_Object = MibTableColumn
ethernetNTEOSA5411CardSecondaryState = _EthernetNTEOSA5411CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 4),
    _EthernetNTEOSA5411CardSecondaryState_Type()
)
ethernetNTEOSA5411CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardSecondaryState.setStatus("current")
_EthernetNTEOSA5411CardVoltage_Type = Integer32
_EthernetNTEOSA5411CardVoltage_Object = MibTableColumn
ethernetNTEOSA5411CardVoltage = _EthernetNTEOSA5411CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 5),
    _EthernetNTEOSA5411CardVoltage_Type()
)
ethernetNTEOSA5411CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardVoltage.setStatus("current")
_EthernetNTEOSA5411CardTemperature_Type = Integer32
_EthernetNTEOSA5411CardTemperature_Object = MibTableColumn
ethernetNTEOSA5411CardTemperature = _EthernetNTEOSA5411CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 6),
    _EthernetNTEOSA5411CardTemperature_Type()
)
ethernetNTEOSA5411CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardTemperature.setStatus("current")
_EthernetNTEOSA5411CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEOSA5411CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEOSA5411CardSnmpDyingGaspEnabled = _EthernetNTEOSA5411CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 7),
    _EthernetNTEOSA5411CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEOSA5411CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEOSA5411CardRestartAction_Type = RestartType
_EthernetNTEOSA5411CardRestartAction_Object = MibTableColumn
ethernetNTEOSA5411CardRestartAction = _EthernetNTEOSA5411CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 8),
    _EthernetNTEOSA5411CardRestartAction_Type()
)
ethernetNTEOSA5411CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardRestartAction.setStatus("current")
_EthernetNTEOSA5411CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEOSA5411CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEOSA5411CardFineGrainedPmInterval = _EthernetNTEOSA5411CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 52, 1, 9),
    _EthernetNTEOSA5411CardFineGrainedPmInterval_Type()
)
ethernetNTEOSA5411CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5411CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112ProCardTable_Object = MibTable
ethernetNTEGE112ProCardTable = _EthernetNTEGE112ProCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53)
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardTable.setStatus("current")
_EthernetNTEGE112ProCardEntry_Object = MibTableRow
ethernetNTEGE112ProCardEntry = _EthernetNTEGE112ProCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1)
)
ethernetNTEGE112ProCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardEntry.setStatus("current")
_EthernetNTEGE112ProCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE112ProCardEntityIndex_Object = MibTableColumn
ethernetNTEGE112ProCardEntityIndex = _EthernetNTEGE112ProCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 1),
    _EthernetNTEGE112ProCardEntityIndex_Type()
)
ethernetNTEGE112ProCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardEntityIndex.setStatus("current")
_EthernetNTEGE112ProCardAdminState_Type = AdminState
_EthernetNTEGE112ProCardAdminState_Object = MibTableColumn
ethernetNTEGE112ProCardAdminState = _EthernetNTEGE112ProCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 2),
    _EthernetNTEGE112ProCardAdminState_Type()
)
ethernetNTEGE112ProCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardAdminState.setStatus("current")
_EthernetNTEGE112ProCardOperationalState_Type = OperationalState
_EthernetNTEGE112ProCardOperationalState_Object = MibTableColumn
ethernetNTEGE112ProCardOperationalState = _EthernetNTEGE112ProCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 3),
    _EthernetNTEGE112ProCardOperationalState_Type()
)
ethernetNTEGE112ProCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardOperationalState.setStatus("current")
_EthernetNTEGE112ProCardSecondaryState_Type = SecondaryState
_EthernetNTEGE112ProCardSecondaryState_Object = MibTableColumn
ethernetNTEGE112ProCardSecondaryState = _EthernetNTEGE112ProCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 4),
    _EthernetNTEGE112ProCardSecondaryState_Type()
)
ethernetNTEGE112ProCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardSecondaryState.setStatus("current")
_EthernetNTEGE112ProCardVoltage_Type = Integer32
_EthernetNTEGE112ProCardVoltage_Object = MibTableColumn
ethernetNTEGE112ProCardVoltage = _EthernetNTEGE112ProCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 5),
    _EthernetNTEGE112ProCardVoltage_Type()
)
ethernetNTEGE112ProCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardVoltage.setStatus("current")
_EthernetNTEGE112ProCardTemperature_Type = Integer32
_EthernetNTEGE112ProCardTemperature_Object = MibTableColumn
ethernetNTEGE112ProCardTemperature = _EthernetNTEGE112ProCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 6),
    _EthernetNTEGE112ProCardTemperature_Type()
)
ethernetNTEGE112ProCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardTemperature.setStatus("current")
_EthernetNTEGE112ProCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE112ProCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE112ProCardSnmpDyingGaspEnabled = _EthernetNTEGE112ProCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 7),
    _EthernetNTEGE112ProCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE112ProCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE112ProCardRestartAction_Type = RestartType
_EthernetNTEGE112ProCardRestartAction_Object = MibTableColumn
ethernetNTEGE112ProCardRestartAction = _EthernetNTEGE112ProCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 8),
    _EthernetNTEGE112ProCardRestartAction_Type()
)
ethernetNTEGE112ProCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardRestartAction.setStatus("current")
_EthernetNTEGE112ProCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE112ProCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE112ProCardFineGrainedPmInterval = _EthernetNTEGE112ProCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 9),
    _EthernetNTEGE112ProCardFineGrainedPmInterval_Type()
)
ethernetNTEGE112ProCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112ProCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE112ProCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE112ProCardSwitchPortActionPort = _EthernetNTEGE112ProCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 10),
    _EthernetNTEGE112ProCardSwitchPortActionPort_Type()
)
ethernetNTEGE112ProCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE112ProCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE112ProCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE112ProCardSwitchPortAction = _EthernetNTEGE112ProCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 53, 1, 11),
    _EthernetNTEGE112ProCardSwitchPortAction_Type()
)
ethernetNTEGE112ProCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProCardSwitchPortAction.setStatus("current")
_EthernetNTEGE112ProMCardTable_Object = MibTable
ethernetNTEGE112ProMCardTable = _EthernetNTEGE112ProMCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54)
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardTable.setStatus("current")
_EthernetNTEGE112ProMCardEntry_Object = MibTableRow
ethernetNTEGE112ProMCardEntry = _EthernetNTEGE112ProMCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1)
)
ethernetNTEGE112ProMCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardEntry.setStatus("current")
_EthernetNTEGE112ProMCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE112ProMCardEntityIndex_Object = MibTableColumn
ethernetNTEGE112ProMCardEntityIndex = _EthernetNTEGE112ProMCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 1),
    _EthernetNTEGE112ProMCardEntityIndex_Type()
)
ethernetNTEGE112ProMCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardEntityIndex.setStatus("current")
_EthernetNTEGE112ProMCardAdminState_Type = AdminState
_EthernetNTEGE112ProMCardAdminState_Object = MibTableColumn
ethernetNTEGE112ProMCardAdminState = _EthernetNTEGE112ProMCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 2),
    _EthernetNTEGE112ProMCardAdminState_Type()
)
ethernetNTEGE112ProMCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardAdminState.setStatus("current")
_EthernetNTEGE112ProMCardOperationalState_Type = OperationalState
_EthernetNTEGE112ProMCardOperationalState_Object = MibTableColumn
ethernetNTEGE112ProMCardOperationalState = _EthernetNTEGE112ProMCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 3),
    _EthernetNTEGE112ProMCardOperationalState_Type()
)
ethernetNTEGE112ProMCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardOperationalState.setStatus("current")
_EthernetNTEGE112ProMCardSecondaryState_Type = SecondaryState
_EthernetNTEGE112ProMCardSecondaryState_Object = MibTableColumn
ethernetNTEGE112ProMCardSecondaryState = _EthernetNTEGE112ProMCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 4),
    _EthernetNTEGE112ProMCardSecondaryState_Type()
)
ethernetNTEGE112ProMCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardSecondaryState.setStatus("current")
_EthernetNTEGE112ProMCardVoltage_Type = Integer32
_EthernetNTEGE112ProMCardVoltage_Object = MibTableColumn
ethernetNTEGE112ProMCardVoltage = _EthernetNTEGE112ProMCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 5),
    _EthernetNTEGE112ProMCardVoltage_Type()
)
ethernetNTEGE112ProMCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardVoltage.setStatus("current")
_EthernetNTEGE112ProMCardTemperature_Type = Integer32
_EthernetNTEGE112ProMCardTemperature_Object = MibTableColumn
ethernetNTEGE112ProMCardTemperature = _EthernetNTEGE112ProMCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 6),
    _EthernetNTEGE112ProMCardTemperature_Type()
)
ethernetNTEGE112ProMCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardTemperature.setStatus("current")
_EthernetNTEGE112ProMCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE112ProMCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE112ProMCardSnmpDyingGaspEnabled = _EthernetNTEGE112ProMCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 7),
    _EthernetNTEGE112ProMCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE112ProMCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE112ProMCardRestartAction_Type = RestartType
_EthernetNTEGE112ProMCardRestartAction_Object = MibTableColumn
ethernetNTEGE112ProMCardRestartAction = _EthernetNTEGE112ProMCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 8),
    _EthernetNTEGE112ProMCardRestartAction_Type()
)
ethernetNTEGE112ProMCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardRestartAction.setStatus("current")
_EthernetNTEGE112ProMCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE112ProMCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE112ProMCardFineGrainedPmInterval = _EthernetNTEGE112ProMCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 9),
    _EthernetNTEGE112ProMCardFineGrainedPmInterval_Type()
)
ethernetNTEGE112ProMCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112ProMCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE112ProMCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE112ProMCardSwitchPortActionPort = _EthernetNTEGE112ProMCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 10),
    _EthernetNTEGE112ProMCardSwitchPortActionPort_Type()
)
ethernetNTEGE112ProMCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE112ProMCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE112ProMCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE112ProMCardSwitchPortAction = _EthernetNTEGE112ProMCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 54, 1, 11),
    _EthernetNTEGE112ProMCardSwitchPortAction_Type()
)
ethernetNTEGE112ProMCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProMCardSwitchPortAction.setStatus("current")
_EthernetNTEXG210CCardTable_Object = MibTable
ethernetNTEXG210CCardTable = _EthernetNTEXG210CCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55)
)
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardTable.setStatus("current")
_EthernetNTEXG210CCardEntry_Object = MibTableRow
ethernetNTEXG210CCardEntry = _EthernetNTEXG210CCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1)
)
ethernetNTEXG210CCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardEntry.setStatus("current")
_EthernetNTEXG210CCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG210CCardEntityIndex_Object = MibTableColumn
ethernetNTEXG210CCardEntityIndex = _EthernetNTEXG210CCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 1),
    _EthernetNTEXG210CCardEntityIndex_Type()
)
ethernetNTEXG210CCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardEntityIndex.setStatus("current")
_EthernetNTEXG210CCardAdminState_Type = AdminState
_EthernetNTEXG210CCardAdminState_Object = MibTableColumn
ethernetNTEXG210CCardAdminState = _EthernetNTEXG210CCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 2),
    _EthernetNTEXG210CCardAdminState_Type()
)
ethernetNTEXG210CCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardAdminState.setStatus("current")
_EthernetNTEXG210CCardOperationalState_Type = OperationalState
_EthernetNTEXG210CCardOperationalState_Object = MibTableColumn
ethernetNTEXG210CCardOperationalState = _EthernetNTEXG210CCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 3),
    _EthernetNTEXG210CCardOperationalState_Type()
)
ethernetNTEXG210CCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardOperationalState.setStatus("current")
_EthernetNTEXG210CCardSecondaryState_Type = SecondaryState
_EthernetNTEXG210CCardSecondaryState_Object = MibTableColumn
ethernetNTEXG210CCardSecondaryState = _EthernetNTEXG210CCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 4),
    _EthernetNTEXG210CCardSecondaryState_Type()
)
ethernetNTEXG210CCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardSecondaryState.setStatus("current")
_EthernetNTEXG210CCardVoltage_Type = Integer32
_EthernetNTEXG210CCardVoltage_Object = MibTableColumn
ethernetNTEXG210CCardVoltage = _EthernetNTEXG210CCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 5),
    _EthernetNTEXG210CCardVoltage_Type()
)
ethernetNTEXG210CCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardVoltage.setStatus("current")
_EthernetNTEXG210CCardTemperature_Type = Integer32
_EthernetNTEXG210CCardTemperature_Object = MibTableColumn
ethernetNTEXG210CCardTemperature = _EthernetNTEXG210CCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 6),
    _EthernetNTEXG210CCardTemperature_Type()
)
ethernetNTEXG210CCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardTemperature.setStatus("current")
_EthernetNTEXG210CCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG210CCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG210CCardSnmpDyingGaspEnabled = _EthernetNTEXG210CCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 7),
    _EthernetNTEXG210CCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG210CCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG210CCardRestartAction_Type = RestartType
_EthernetNTEXG210CCardRestartAction_Object = MibTableColumn
ethernetNTEXG210CCardRestartAction = _EthernetNTEXG210CCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 8),
    _EthernetNTEXG210CCardRestartAction_Type()
)
ethernetNTEXG210CCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardRestartAction.setStatus("current")
_EthernetNTEXG210CCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG210CCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG210CCardFineGrainedPmInterval = _EthernetNTEXG210CCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 55, 1, 9),
    _EthernetNTEXG210CCardFineGrainedPmInterval_Type()
)
ethernetNTEXG210CCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG210CCardFineGrainedPmInterval.setStatus("current")
_EthernetGE8SCryptoConnectorCardTable_Object = MibTable
ethernetGE8SCryptoConnectorCardTable = _EthernetGE8SCryptoConnectorCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56)
)
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardTable.setStatus("current")
_EthernetGE8SCryptoConnectorCardEntry_Object = MibTableRow
ethernetGE8SCryptoConnectorCardEntry = _EthernetGE8SCryptoConnectorCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1)
)
ethernetGE8SCryptoConnectorCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardEntry.setStatus("current")
_EthernetGE8SCryptoConnectorCardEntityIndex_Type = PhysicalIndex
_EthernetGE8SCryptoConnectorCardEntityIndex_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardEntityIndex = _EthernetGE8SCryptoConnectorCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 1),
    _EthernetGE8SCryptoConnectorCardEntityIndex_Type()
)
ethernetGE8SCryptoConnectorCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardEntityIndex.setStatus("current")
_EthernetGE8SCryptoConnectorCardAdminState_Type = AdminState
_EthernetGE8SCryptoConnectorCardAdminState_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardAdminState = _EthernetGE8SCryptoConnectorCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 2),
    _EthernetGE8SCryptoConnectorCardAdminState_Type()
)
ethernetGE8SCryptoConnectorCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardAdminState.setStatus("current")
_EthernetGE8SCryptoConnectorCardOperationalState_Type = OperationalState
_EthernetGE8SCryptoConnectorCardOperationalState_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardOperationalState = _EthernetGE8SCryptoConnectorCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 3),
    _EthernetGE8SCryptoConnectorCardOperationalState_Type()
)
ethernetGE8SCryptoConnectorCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardOperationalState.setStatus("current")
_EthernetGE8SCryptoConnectorCardSecondaryState_Type = SecondaryState
_EthernetGE8SCryptoConnectorCardSecondaryState_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardSecondaryState = _EthernetGE8SCryptoConnectorCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 4),
    _EthernetGE8SCryptoConnectorCardSecondaryState_Type()
)
ethernetGE8SCryptoConnectorCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardSecondaryState.setStatus("current")
_EthernetGE8SCryptoConnectorCardVoltage_Type = Integer32
_EthernetGE8SCryptoConnectorCardVoltage_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardVoltage = _EthernetGE8SCryptoConnectorCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 5),
    _EthernetGE8SCryptoConnectorCardVoltage_Type()
)
ethernetGE8SCryptoConnectorCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardVoltage.setStatus("current")
_EthernetGE8SCryptoConnectorCardTemperature_Type = Integer32
_EthernetGE8SCryptoConnectorCardTemperature_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardTemperature = _EthernetGE8SCryptoConnectorCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 6),
    _EthernetGE8SCryptoConnectorCardTemperature_Type()
)
ethernetGE8SCryptoConnectorCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardTemperature.setStatus("current")
_EthernetGE8SCryptoConnectorCardRestartAction_Type = RestartType
_EthernetGE8SCryptoConnectorCardRestartAction_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardRestartAction = _EthernetGE8SCryptoConnectorCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 7),
    _EthernetGE8SCryptoConnectorCardRestartAction_Type()
)
ethernetGE8SCryptoConnectorCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardRestartAction.setStatus("current")
_EthernetGE8SCryptoConnectorCardStorageType_Type = StorageType
_EthernetGE8SCryptoConnectorCardStorageType_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardStorageType = _EthernetGE8SCryptoConnectorCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 8),
    _EthernetGE8SCryptoConnectorCardStorageType_Type()
)
ethernetGE8SCryptoConnectorCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardStorageType.setStatus("current")
_EthernetGE8SCryptoConnectorCardRowStatus_Type = RowStatus
_EthernetGE8SCryptoConnectorCardRowStatus_Object = MibTableColumn
ethernetGE8SCryptoConnectorCardRowStatus = _EthernetGE8SCryptoConnectorCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 56, 1, 9),
    _EthernetGE8SCryptoConnectorCardRowStatus_Type()
)
ethernetGE8SCryptoConnectorCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetGE8SCryptoConnectorCardRowStatus.setStatus("current")
_EthernetNTEGE114ProCardTable_Object = MibTable
ethernetNTEGE114ProCardTable = _EthernetNTEGE114ProCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardTable.setStatus("current")
_EthernetNTEGE114ProCardEntry_Object = MibTableRow
ethernetNTEGE114ProCardEntry = _EthernetNTEGE114ProCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1)
)
ethernetNTEGE114ProCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardEntry.setStatus("current")
_EthernetNTEGE114ProCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProCardEntityIndex = _EthernetNTEGE114ProCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 1),
    _EthernetNTEGE114ProCardEntityIndex_Type()
)
ethernetNTEGE114ProCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProCardAdminState_Type = AdminState
_EthernetNTEGE114ProCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProCardAdminState = _EthernetNTEGE114ProCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 2),
    _EthernetNTEGE114ProCardAdminState_Type()
)
ethernetNTEGE114ProCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardAdminState.setStatus("current")
_EthernetNTEGE114ProCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProCardOperationalState = _EthernetNTEGE114ProCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 3),
    _EthernetNTEGE114ProCardOperationalState_Type()
)
ethernetNTEGE114ProCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardOperationalState.setStatus("current")
_EthernetNTEGE114ProCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProCardSecondaryState = _EthernetNTEGE114ProCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 4),
    _EthernetNTEGE114ProCardSecondaryState_Type()
)
ethernetNTEGE114ProCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProCardVoltage_Type = Integer32
_EthernetNTEGE114ProCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProCardVoltage = _EthernetNTEGE114ProCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 5),
    _EthernetNTEGE114ProCardVoltage_Type()
)
ethernetNTEGE114ProCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardVoltage.setStatus("current")
_EthernetNTEGE114ProCardTemperature_Type = Integer32
_EthernetNTEGE114ProCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProCardTemperature = _EthernetNTEGE114ProCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 6),
    _EthernetNTEGE114ProCardTemperature_Type()
)
ethernetNTEGE114ProCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardTemperature.setStatus("current")
_EthernetNTEGE114ProCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 7),
    _EthernetNTEGE114ProCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProCardRestartAction_Type = RestartType
_EthernetNTEGE114ProCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProCardRestartAction = _EthernetNTEGE114ProCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 8),
    _EthernetNTEGE114ProCardRestartAction_Type()
)
ethernetNTEGE114ProCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardRestartAction.setStatus("current")
_EthernetNTEGE114ProCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProCardFineGrainedPmInterval = _EthernetNTEGE114ProCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 9),
    _EthernetNTEGE114ProCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProCardSwitchPortActionPort = _EthernetNTEGE114ProCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 10),
    _EthernetNTEGE114ProCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProCardSwitchPortAction = _EthernetNTEGE114ProCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 57, 1, 11),
    _EthernetNTEGE114ProCardSwitchPortAction_Type()
)
ethernetNTEGE114ProCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114ProCCardTable_Object = MibTable
ethernetNTEGE114ProCCardTable = _EthernetNTEGE114ProCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardTable.setStatus("current")
_EthernetNTEGE114ProCCardEntry_Object = MibTableRow
ethernetNTEGE114ProCCardEntry = _EthernetNTEGE114ProCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1)
)
ethernetNTEGE114ProCCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardEntry.setStatus("current")
_EthernetNTEGE114ProCCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProCCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProCCardEntityIndex = _EthernetNTEGE114ProCCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 1),
    _EthernetNTEGE114ProCCardEntityIndex_Type()
)
ethernetNTEGE114ProCCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProCCardAdminState_Type = AdminState
_EthernetNTEGE114ProCCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProCCardAdminState = _EthernetNTEGE114ProCCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 2),
    _EthernetNTEGE114ProCCardAdminState_Type()
)
ethernetNTEGE114ProCCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardAdminState.setStatus("current")
_EthernetNTEGE114ProCCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProCCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProCCardOperationalState = _EthernetNTEGE114ProCCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 3),
    _EthernetNTEGE114ProCCardOperationalState_Type()
)
ethernetNTEGE114ProCCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardOperationalState.setStatus("current")
_EthernetNTEGE114ProCCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProCCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProCCardSecondaryState = _EthernetNTEGE114ProCCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 4),
    _EthernetNTEGE114ProCCardSecondaryState_Type()
)
ethernetNTEGE114ProCCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProCCardVoltage_Type = Integer32
_EthernetNTEGE114ProCCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProCCardVoltage = _EthernetNTEGE114ProCCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 5),
    _EthernetNTEGE114ProCCardVoltage_Type()
)
ethernetNTEGE114ProCCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardVoltage.setStatus("current")
_EthernetNTEGE114ProCCardTemperature_Type = Integer32
_EthernetNTEGE114ProCCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProCCardTemperature = _EthernetNTEGE114ProCCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 6),
    _EthernetNTEGE114ProCCardTemperature_Type()
)
ethernetNTEGE114ProCCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardTemperature.setStatus("current")
_EthernetNTEGE114ProCCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProCCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProCCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProCCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 7),
    _EthernetNTEGE114ProCCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProCCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProCCardRestartAction_Type = RestartType
_EthernetNTEGE114ProCCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProCCardRestartAction = _EthernetNTEGE114ProCCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 8),
    _EthernetNTEGE114ProCCardRestartAction_Type()
)
ethernetNTEGE114ProCCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardRestartAction.setStatus("current")
_EthernetNTEGE114ProCCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProCCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProCCardFineGrainedPmInterval = _EthernetNTEGE114ProCCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 9),
    _EthernetNTEGE114ProCCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProCCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProCCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProCCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProCCardSwitchPortActionPort = _EthernetNTEGE114ProCCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 10),
    _EthernetNTEGE114ProCCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProCCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProCCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProCCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProCCardSwitchPortAction = _EthernetNTEGE114ProCCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 58, 1, 11),
    _EthernetNTEGE114ProCCardSwitchPortAction_Type()
)
ethernetNTEGE114ProCCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114ProSHCardTable_Object = MibTable
ethernetNTEGE114ProSHCardTable = _EthernetNTEGE114ProSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardTable.setStatus("current")
_EthernetNTEGE114ProSHCardEntry_Object = MibTableRow
ethernetNTEGE114ProSHCardEntry = _EthernetNTEGE114ProSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1)
)
ethernetNTEGE114ProSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardEntry.setStatus("current")
_EthernetNTEGE114ProSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProSHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProSHCardEntityIndex = _EthernetNTEGE114ProSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 1),
    _EthernetNTEGE114ProSHCardEntityIndex_Type()
)
ethernetNTEGE114ProSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProSHCardAdminState_Type = AdminState
_EthernetNTEGE114ProSHCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProSHCardAdminState = _EthernetNTEGE114ProSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 2),
    _EthernetNTEGE114ProSHCardAdminState_Type()
)
ethernetNTEGE114ProSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardAdminState.setStatus("current")
_EthernetNTEGE114ProSHCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProSHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProSHCardOperationalState = _EthernetNTEGE114ProSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 3),
    _EthernetNTEGE114ProSHCardOperationalState_Type()
)
ethernetNTEGE114ProSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardOperationalState.setStatus("current")
_EthernetNTEGE114ProSHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProSHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProSHCardSecondaryState = _EthernetNTEGE114ProSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 4),
    _EthernetNTEGE114ProSHCardSecondaryState_Type()
)
ethernetNTEGE114ProSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProSHCardVoltage_Type = Integer32
_EthernetNTEGE114ProSHCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProSHCardVoltage = _EthernetNTEGE114ProSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 5),
    _EthernetNTEGE114ProSHCardVoltage_Type()
)
ethernetNTEGE114ProSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardVoltage.setStatus("current")
_EthernetNTEGE114ProSHCardTemperature_Type = Integer32
_EthernetNTEGE114ProSHCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProSHCardTemperature = _EthernetNTEGE114ProSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 6),
    _EthernetNTEGE114ProSHCardTemperature_Type()
)
ethernetNTEGE114ProSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardTemperature.setStatus("current")
_EthernetNTEGE114ProSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProSHCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 7),
    _EthernetNTEGE114ProSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProSHCardRestartAction_Type = RestartType
_EthernetNTEGE114ProSHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProSHCardRestartAction = _EthernetNTEGE114ProSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 8),
    _EthernetNTEGE114ProSHCardRestartAction_Type()
)
ethernetNTEGE114ProSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardRestartAction.setStatus("current")
_EthernetNTEGE114ProSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProSHCardFineGrainedPmInterval = _EthernetNTEGE114ProSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 9),
    _EthernetNTEGE114ProSHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProSHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProSHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProSHCardSwitchPortActionPort = _EthernetNTEGE114ProSHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 10),
    _EthernetNTEGE114ProSHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProSHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProSHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProSHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProSHCardSwitchPortAction = _EthernetNTEGE114ProSHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 59, 1, 11),
    _EthernetNTEGE114ProSHCardSwitchPortAction_Type()
)
ethernetNTEGE114ProSHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProSHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114ProCSHCardTable_Object = MibTable
ethernetNTEGE114ProCSHCardTable = _EthernetNTEGE114ProCSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardTable.setStatus("current")
_EthernetNTEGE114ProCSHCardEntry_Object = MibTableRow
ethernetNTEGE114ProCSHCardEntry = _EthernetNTEGE114ProCSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1)
)
ethernetNTEGE114ProCSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardEntry.setStatus("current")
_EthernetNTEGE114ProCSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProCSHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProCSHCardEntityIndex = _EthernetNTEGE114ProCSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 1),
    _EthernetNTEGE114ProCSHCardEntityIndex_Type()
)
ethernetNTEGE114ProCSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProCSHCardAdminState_Type = AdminState
_EthernetNTEGE114ProCSHCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProCSHCardAdminState = _EthernetNTEGE114ProCSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 2),
    _EthernetNTEGE114ProCSHCardAdminState_Type()
)
ethernetNTEGE114ProCSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardAdminState.setStatus("current")
_EthernetNTEGE114ProCSHCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProCSHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProCSHCardOperationalState = _EthernetNTEGE114ProCSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 3),
    _EthernetNTEGE114ProCSHCardOperationalState_Type()
)
ethernetNTEGE114ProCSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardOperationalState.setStatus("current")
_EthernetNTEGE114ProCSHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProCSHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProCSHCardSecondaryState = _EthernetNTEGE114ProCSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 4),
    _EthernetNTEGE114ProCSHCardSecondaryState_Type()
)
ethernetNTEGE114ProCSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProCSHCardVoltage_Type = Integer32
_EthernetNTEGE114ProCSHCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProCSHCardVoltage = _EthernetNTEGE114ProCSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 5),
    _EthernetNTEGE114ProCSHCardVoltage_Type()
)
ethernetNTEGE114ProCSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardVoltage.setStatus("current")
_EthernetNTEGE114ProCSHCardTemperature_Type = Integer32
_EthernetNTEGE114ProCSHCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProCSHCardTemperature = _EthernetNTEGE114ProCSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 6),
    _EthernetNTEGE114ProCSHCardTemperature_Type()
)
ethernetNTEGE114ProCSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardTemperature.setStatus("current")
_EthernetNTEGE114ProCSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProCSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProCSHCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProCSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 7),
    _EthernetNTEGE114ProCSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProCSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProCSHCardRestartAction_Type = RestartType
_EthernetNTEGE114ProCSHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProCSHCardRestartAction = _EthernetNTEGE114ProCSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 8),
    _EthernetNTEGE114ProCSHCardRestartAction_Type()
)
ethernetNTEGE114ProCSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardRestartAction.setStatus("current")
_EthernetNTEGE114ProCSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProCSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProCSHCardFineGrainedPmInterval = _EthernetNTEGE114ProCSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 9),
    _EthernetNTEGE114ProCSHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProCSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProCSHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProCSHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProCSHCardSwitchPortActionPort = _EthernetNTEGE114ProCSHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 10),
    _EthernetNTEGE114ProCSHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProCSHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProCSHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProCSHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProCSHCardSwitchPortAction = _EthernetNTEGE114ProCSHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 60, 1, 11),
    _EthernetNTEGE114ProCSHCardSwitchPortAction_Type()
)
ethernetNTEGE114ProCSHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProCSHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114ProHECardTable_Object = MibTable
ethernetNTEGE114ProHECardTable = _EthernetNTEGE114ProHECardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardTable.setStatus("current")
_EthernetNTEGE114ProHECardEntry_Object = MibTableRow
ethernetNTEGE114ProHECardEntry = _EthernetNTEGE114ProHECardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1)
)
ethernetNTEGE114ProHECardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardEntry.setStatus("current")
_EthernetNTEGE114ProHECardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProHECardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProHECardEntityIndex = _EthernetNTEGE114ProHECardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 1),
    _EthernetNTEGE114ProHECardEntityIndex_Type()
)
ethernetNTEGE114ProHECardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardEntityIndex.setStatus("current")
_EthernetNTEGE114ProHECardAdminState_Type = AdminState
_EthernetNTEGE114ProHECardAdminState_Object = MibTableColumn
ethernetNTEGE114ProHECardAdminState = _EthernetNTEGE114ProHECardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 2),
    _EthernetNTEGE114ProHECardAdminState_Type()
)
ethernetNTEGE114ProHECardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardAdminState.setStatus("current")
_EthernetNTEGE114ProHECardOperationalState_Type = OperationalState
_EthernetNTEGE114ProHECardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProHECardOperationalState = _EthernetNTEGE114ProHECardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 3),
    _EthernetNTEGE114ProHECardOperationalState_Type()
)
ethernetNTEGE114ProHECardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardOperationalState.setStatus("current")
_EthernetNTEGE114ProHECardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProHECardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProHECardSecondaryState = _EthernetNTEGE114ProHECardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 4),
    _EthernetNTEGE114ProHECardSecondaryState_Type()
)
ethernetNTEGE114ProHECardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardSecondaryState.setStatus("current")
_EthernetNTEGE114ProHECardVoltage_Type = Integer32
_EthernetNTEGE114ProHECardVoltage_Object = MibTableColumn
ethernetNTEGE114ProHECardVoltage = _EthernetNTEGE114ProHECardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 5),
    _EthernetNTEGE114ProHECardVoltage_Type()
)
ethernetNTEGE114ProHECardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardVoltage.setStatus("current")
_EthernetNTEGE114ProHECardTemperature_Type = Integer32
_EthernetNTEGE114ProHECardTemperature_Object = MibTableColumn
ethernetNTEGE114ProHECardTemperature = _EthernetNTEGE114ProHECardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 6),
    _EthernetNTEGE114ProHECardTemperature_Type()
)
ethernetNTEGE114ProHECardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardTemperature.setStatus("current")
_EthernetNTEGE114ProHECardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProHECardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProHECardSnmpDyingGaspEnabled = _EthernetNTEGE114ProHECardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 7),
    _EthernetNTEGE114ProHECardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProHECardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProHECardRestartAction_Type = RestartType
_EthernetNTEGE114ProHECardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProHECardRestartAction = _EthernetNTEGE114ProHECardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 8),
    _EthernetNTEGE114ProHECardRestartAction_Type()
)
ethernetNTEGE114ProHECardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardRestartAction.setStatus("current")
_EthernetNTEGE114ProHECardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProHECardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProHECardFineGrainedPmInterval = _EthernetNTEGE114ProHECardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 9),
    _EthernetNTEGE114ProHECardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProHECardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProHECardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProHECardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProHECardSwitchPortActionPort = _EthernetNTEGE114ProHECardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 10),
    _EthernetNTEGE114ProHECardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProHECardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProHECardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProHECardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProHECardSwitchPortAction = _EthernetNTEGE114ProHECardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 61, 1, 11),
    _EthernetNTEGE114ProHECardSwitchPortAction_Type()
)
ethernetNTEGE114ProHECardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProHECardSwitchPortAction.setStatus("current")
_EthernetNTEGE112ProHCardTable_Object = MibTable
ethernetNTEGE112ProHCardTable = _EthernetNTEGE112ProHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62)
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardTable.setStatus("current")
_EthernetNTEGE112ProHCardEntry_Object = MibTableRow
ethernetNTEGE112ProHCardEntry = _EthernetNTEGE112ProHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1)
)
ethernetNTEGE112ProHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardEntry.setStatus("current")
_EthernetNTEGE112ProHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE112ProHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE112ProHCardEntityIndex = _EthernetNTEGE112ProHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 1),
    _EthernetNTEGE112ProHCardEntityIndex_Type()
)
ethernetNTEGE112ProHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardEntityIndex.setStatus("current")
_EthernetNTEGE112ProHCardAdminState_Type = AdminState
_EthernetNTEGE112ProHCardAdminState_Object = MibTableColumn
ethernetNTEGE112ProHCardAdminState = _EthernetNTEGE112ProHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 2),
    _EthernetNTEGE112ProHCardAdminState_Type()
)
ethernetNTEGE112ProHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardAdminState.setStatus("current")
_EthernetNTEGE112ProHCardOperationalState_Type = OperationalState
_EthernetNTEGE112ProHCardOperationalState_Object = MibTableColumn
ethernetNTEGE112ProHCardOperationalState = _EthernetNTEGE112ProHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 3),
    _EthernetNTEGE112ProHCardOperationalState_Type()
)
ethernetNTEGE112ProHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardOperationalState.setStatus("current")
_EthernetNTEGE112ProHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE112ProHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE112ProHCardSecondaryState = _EthernetNTEGE112ProHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 4),
    _EthernetNTEGE112ProHCardSecondaryState_Type()
)
ethernetNTEGE112ProHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardSecondaryState.setStatus("current")
_EthernetNTEGE112ProHCardVoltage_Type = Integer32
_EthernetNTEGE112ProHCardVoltage_Object = MibTableColumn
ethernetNTEGE112ProHCardVoltage = _EthernetNTEGE112ProHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 5),
    _EthernetNTEGE112ProHCardVoltage_Type()
)
ethernetNTEGE112ProHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardVoltage.setStatus("current")
_EthernetNTEGE112ProHCardTemperature_Type = Integer32
_EthernetNTEGE112ProHCardTemperature_Object = MibTableColumn
ethernetNTEGE112ProHCardTemperature = _EthernetNTEGE112ProHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 6),
    _EthernetNTEGE112ProHCardTemperature_Type()
)
ethernetNTEGE112ProHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardTemperature.setStatus("current")
_EthernetNTEGE112ProHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE112ProHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE112ProHCardSnmpDyingGaspEnabled = _EthernetNTEGE112ProHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 7),
    _EthernetNTEGE112ProHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE112ProHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE112ProHCardRestartAction_Type = RestartType
_EthernetNTEGE112ProHCardRestartAction_Object = MibTableColumn
ethernetNTEGE112ProHCardRestartAction = _EthernetNTEGE112ProHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 8),
    _EthernetNTEGE112ProHCardRestartAction_Type()
)
ethernetNTEGE112ProHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardRestartAction.setStatus("current")
_EthernetNTEGE112ProHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE112ProHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE112ProHCardFineGrainedPmInterval = _EthernetNTEGE112ProHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 9),
    _EthernetNTEGE112ProHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE112ProHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112ProHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE112ProHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE112ProHCardSwitchPortActionPort = _EthernetNTEGE112ProHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 10),
    _EthernetNTEGE112ProHCardSwitchPortActionPort_Type()
)
ethernetNTEGE112ProHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE112ProHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE112ProHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE112ProHCardSwitchPortAction = _EthernetNTEGE112ProHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 62, 1, 11),
    _EthernetNTEGE112ProHCardSwitchPortAction_Type()
)
ethernetNTEGE112ProHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProHCardSwitchPortAction.setStatus("current")
_EthernetNTEOSA5420CardTable_Object = MibTable
ethernetNTEOSA5420CardTable = _EthernetNTEOSA5420CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63)
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardTable.setStatus("current")
_EthernetNTEOSA5420CardEntry_Object = MibTableRow
ethernetNTEOSA5420CardEntry = _EthernetNTEOSA5420CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1)
)
ethernetNTEOSA5420CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardEntry.setStatus("current")
_EthernetNTEOSA5420CardEntityIndex_Type = PhysicalIndex
_EthernetNTEOSA5420CardEntityIndex_Object = MibTableColumn
ethernetNTEOSA5420CardEntityIndex = _EthernetNTEOSA5420CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 1),
    _EthernetNTEOSA5420CardEntityIndex_Type()
)
ethernetNTEOSA5420CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardEntityIndex.setStatus("current")
_EthernetNTEOSA5420CardAdminState_Type = AdminState
_EthernetNTEOSA5420CardAdminState_Object = MibTableColumn
ethernetNTEOSA5420CardAdminState = _EthernetNTEOSA5420CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 2),
    _EthernetNTEOSA5420CardAdminState_Type()
)
ethernetNTEOSA5420CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardAdminState.setStatus("current")
_EthernetNTEOSA5420CardOperationalState_Type = OperationalState
_EthernetNTEOSA5420CardOperationalState_Object = MibTableColumn
ethernetNTEOSA5420CardOperationalState = _EthernetNTEOSA5420CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 3),
    _EthernetNTEOSA5420CardOperationalState_Type()
)
ethernetNTEOSA5420CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardOperationalState.setStatus("current")
_EthernetNTEOSA5420CardSecondaryState_Type = SecondaryState
_EthernetNTEOSA5420CardSecondaryState_Object = MibTableColumn
ethernetNTEOSA5420CardSecondaryState = _EthernetNTEOSA5420CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 4),
    _EthernetNTEOSA5420CardSecondaryState_Type()
)
ethernetNTEOSA5420CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardSecondaryState.setStatus("current")
_EthernetNTEOSA5420CardVoltage_Type = Integer32
_EthernetNTEOSA5420CardVoltage_Object = MibTableColumn
ethernetNTEOSA5420CardVoltage = _EthernetNTEOSA5420CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 5),
    _EthernetNTEOSA5420CardVoltage_Type()
)
ethernetNTEOSA5420CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardVoltage.setStatus("current")
_EthernetNTEOSA5420CardTemperature_Type = Integer32
_EthernetNTEOSA5420CardTemperature_Object = MibTableColumn
ethernetNTEOSA5420CardTemperature = _EthernetNTEOSA5420CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 6),
    _EthernetNTEOSA5420CardTemperature_Type()
)
ethernetNTEOSA5420CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardTemperature.setStatus("current")
_EthernetNTEOSA5420CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEOSA5420CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEOSA5420CardSnmpDyingGaspEnabled = _EthernetNTEOSA5420CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 7),
    _EthernetNTEOSA5420CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEOSA5420CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEOSA5420CardRestartAction_Type = RestartType
_EthernetNTEOSA5420CardRestartAction_Object = MibTableColumn
ethernetNTEOSA5420CardRestartAction = _EthernetNTEOSA5420CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 8),
    _EthernetNTEOSA5420CardRestartAction_Type()
)
ethernetNTEOSA5420CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardRestartAction.setStatus("current")
_EthernetNTEOSA5420CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEOSA5420CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEOSA5420CardFineGrainedPmInterval = _EthernetNTEOSA5420CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 63, 1, 9),
    _EthernetNTEOSA5420CardFineGrainedPmInterval_Type()
)
ethernetNTEOSA5420CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5420CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEOSA5421CardTable_Object = MibTable
ethernetNTEOSA5421CardTable = _EthernetNTEOSA5421CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64)
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardTable.setStatus("current")
_EthernetNTEOSA5421CardEntry_Object = MibTableRow
ethernetNTEOSA5421CardEntry = _EthernetNTEOSA5421CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1)
)
ethernetNTEOSA5421CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardEntry.setStatus("current")
_EthernetNTEOSA5421CardEntityIndex_Type = PhysicalIndex
_EthernetNTEOSA5421CardEntityIndex_Object = MibTableColumn
ethernetNTEOSA5421CardEntityIndex = _EthernetNTEOSA5421CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 1),
    _EthernetNTEOSA5421CardEntityIndex_Type()
)
ethernetNTEOSA5421CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardEntityIndex.setStatus("current")
_EthernetNTEOSA5421CardAdminState_Type = AdminState
_EthernetNTEOSA5421CardAdminState_Object = MibTableColumn
ethernetNTEOSA5421CardAdminState = _EthernetNTEOSA5421CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 2),
    _EthernetNTEOSA5421CardAdminState_Type()
)
ethernetNTEOSA5421CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardAdminState.setStatus("current")
_EthernetNTEOSA5421CardOperationalState_Type = OperationalState
_EthernetNTEOSA5421CardOperationalState_Object = MibTableColumn
ethernetNTEOSA5421CardOperationalState = _EthernetNTEOSA5421CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 3),
    _EthernetNTEOSA5421CardOperationalState_Type()
)
ethernetNTEOSA5421CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardOperationalState.setStatus("current")
_EthernetNTEOSA5421CardSecondaryState_Type = SecondaryState
_EthernetNTEOSA5421CardSecondaryState_Object = MibTableColumn
ethernetNTEOSA5421CardSecondaryState = _EthernetNTEOSA5421CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 4),
    _EthernetNTEOSA5421CardSecondaryState_Type()
)
ethernetNTEOSA5421CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardSecondaryState.setStatus("current")
_EthernetNTEOSA5421CardVoltage_Type = Integer32
_EthernetNTEOSA5421CardVoltage_Object = MibTableColumn
ethernetNTEOSA5421CardVoltage = _EthernetNTEOSA5421CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 5),
    _EthernetNTEOSA5421CardVoltage_Type()
)
ethernetNTEOSA5421CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardVoltage.setStatus("current")
_EthernetNTEOSA5421CardTemperature_Type = Integer32
_EthernetNTEOSA5421CardTemperature_Object = MibTableColumn
ethernetNTEOSA5421CardTemperature = _EthernetNTEOSA5421CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 6),
    _EthernetNTEOSA5421CardTemperature_Type()
)
ethernetNTEOSA5421CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardTemperature.setStatus("current")
_EthernetNTEOSA5421CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEOSA5421CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEOSA5421CardSnmpDyingGaspEnabled = _EthernetNTEOSA5421CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 7),
    _EthernetNTEOSA5421CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEOSA5421CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEOSA5421CardRestartAction_Type = RestartType
_EthernetNTEOSA5421CardRestartAction_Object = MibTableColumn
ethernetNTEOSA5421CardRestartAction = _EthernetNTEOSA5421CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 8),
    _EthernetNTEOSA5421CardRestartAction_Type()
)
ethernetNTEOSA5421CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardRestartAction.setStatus("current")
_EthernetNTEOSA5421CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEOSA5421CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEOSA5421CardFineGrainedPmInterval = _EthernetNTEOSA5421CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 64, 1, 9),
    _EthernetNTEOSA5421CardFineGrainedPmInterval_Type()
)
ethernetNTEOSA5421CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5421CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114GCardTable_Object = MibTable
ethernetNTEGE114GCardTable = _EthernetNTEGE114GCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardTable.setStatus("current")
_EthernetNTEGE114GCardEntry_Object = MibTableRow
ethernetNTEGE114GCardEntry = _EthernetNTEGE114GCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1)
)
ethernetNTEGE114GCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardEntry.setStatus("current")
_EthernetNTEGE114GCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114GCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114GCardEntityIndex = _EthernetNTEGE114GCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 1),
    _EthernetNTEGE114GCardEntityIndex_Type()
)
ethernetNTEGE114GCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardEntityIndex.setStatus("current")
_EthernetNTEGE114GCardAdminState_Type = AdminState
_EthernetNTEGE114GCardAdminState_Object = MibTableColumn
ethernetNTEGE114GCardAdminState = _EthernetNTEGE114GCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 2),
    _EthernetNTEGE114GCardAdminState_Type()
)
ethernetNTEGE114GCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardAdminState.setStatus("current")
_EthernetNTEGE114GCardOperationalState_Type = OperationalState
_EthernetNTEGE114GCardOperationalState_Object = MibTableColumn
ethernetNTEGE114GCardOperationalState = _EthernetNTEGE114GCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 3),
    _EthernetNTEGE114GCardOperationalState_Type()
)
ethernetNTEGE114GCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardOperationalState.setStatus("current")
_EthernetNTEGE114GCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114GCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114GCardSecondaryState = _EthernetNTEGE114GCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 4),
    _EthernetNTEGE114GCardSecondaryState_Type()
)
ethernetNTEGE114GCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardSecondaryState.setStatus("current")
_EthernetNTEGE114GCardVoltage_Type = Integer32
_EthernetNTEGE114GCardVoltage_Object = MibTableColumn
ethernetNTEGE114GCardVoltage = _EthernetNTEGE114GCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 5),
    _EthernetNTEGE114GCardVoltage_Type()
)
ethernetNTEGE114GCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardVoltage.setStatus("current")
_EthernetNTEGE114GCardTemperature_Type = Integer32
_EthernetNTEGE114GCardTemperature_Object = MibTableColumn
ethernetNTEGE114GCardTemperature = _EthernetNTEGE114GCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 6),
    _EthernetNTEGE114GCardTemperature_Type()
)
ethernetNTEGE114GCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardTemperature.setStatus("current")
_EthernetNTEGE114GCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114GCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114GCardSnmpDyingGaspEnabled = _EthernetNTEGE114GCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 7),
    _EthernetNTEGE114GCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114GCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114GCardRestartAction_Type = RestartType
_EthernetNTEGE114GCardRestartAction_Object = MibTableColumn
ethernetNTEGE114GCardRestartAction = _EthernetNTEGE114GCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 8),
    _EthernetNTEGE114GCardRestartAction_Type()
)
ethernetNTEGE114GCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardRestartAction.setStatus("current")
_EthernetNTEGE114GCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114GCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114GCardFineGrainedPmInterval = _EthernetNTEGE114GCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 9),
    _EthernetNTEGE114GCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114GCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114GCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114GCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114GCardSwitchPortActionPort = _EthernetNTEGE114GCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 10),
    _EthernetNTEGE114GCardSwitchPortActionPort_Type()
)
ethernetNTEGE114GCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114GCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114GCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114GCardSwitchPortAction = _EthernetNTEGE114GCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 65, 1, 11),
    _EthernetNTEGE114GCardSwitchPortAction_Type()
)
ethernetNTEGE114GCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114GCardSwitchPortAction.setStatus("current")
_Bits16PortCardTable_Object = MibTable
bits16PortCardTable = _Bits16PortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66)
)
if mibBuilder.loadTexts:
    bits16PortCardTable.setStatus("current")
_Bits16PortCardEntry_Object = MibTableRow
bits16PortCardEntry = _Bits16PortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1)
)
bits16PortCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    bits16PortCardEntry.setStatus("current")
_Bits16PortCardEntityIndex_Type = PhysicalIndex
_Bits16PortCardEntityIndex_Object = MibTableColumn
bits16PortCardEntityIndex = _Bits16PortCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 1),
    _Bits16PortCardEntityIndex_Type()
)
bits16PortCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bits16PortCardEntityIndex.setStatus("current")
_Bits16PortCardAdminState_Type = AdminState
_Bits16PortCardAdminState_Object = MibTableColumn
bits16PortCardAdminState = _Bits16PortCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 2),
    _Bits16PortCardAdminState_Type()
)
bits16PortCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bits16PortCardAdminState.setStatus("current")
_Bits16PortCardOperationalState_Type = OperationalState
_Bits16PortCardOperationalState_Object = MibTableColumn
bits16PortCardOperationalState = _Bits16PortCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 3),
    _Bits16PortCardOperationalState_Type()
)
bits16PortCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bits16PortCardOperationalState.setStatus("current")
_Bits16PortCardSecondaryState_Type = SecondaryState
_Bits16PortCardSecondaryState_Object = MibTableColumn
bits16PortCardSecondaryState = _Bits16PortCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 4),
    _Bits16PortCardSecondaryState_Type()
)
bits16PortCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bits16PortCardSecondaryState.setStatus("current")
_Bits16PortCardRowStatus_Type = RowStatus
_Bits16PortCardRowStatus_Object = MibTableColumn
bits16PortCardRowStatus = _Bits16PortCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 5),
    _Bits16PortCardRowStatus_Type()
)
bits16PortCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bits16PortCardRowStatus.setStatus("current")


class _Bits16PortCardAlias_Type(DisplayString):
    """Custom type bits16PortCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Bits16PortCardAlias_Type.__name__ = "DisplayString"
_Bits16PortCardAlias_Object = MibTableColumn
bits16PortCardAlias = _Bits16PortCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 6),
    _Bits16PortCardAlias_Type()
)
bits16PortCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bits16PortCardAlias.setStatus("current")
_Bits16PortCardTemperature_Type = Integer32
_Bits16PortCardTemperature_Object = MibTableColumn
bits16PortCardTemperature = _Bits16PortCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 66, 1, 7),
    _Bits16PortCardTemperature_Type()
)
bits16PortCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bits16PortCardTemperature.setStatus("current")
_EthernetNTEGE114ProVmHCardTable_Object = MibTable
ethernetNTEGE114ProVmHCardTable = _EthernetNTEGE114ProVmHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardTable.setStatus("current")
_EthernetNTEGE114ProVmHCardEntry_Object = MibTableRow
ethernetNTEGE114ProVmHCardEntry = _EthernetNTEGE114ProVmHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1)
)
ethernetNTEGE114ProVmHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardEntry.setStatus("current")
_EthernetNTEGE114ProVmHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProVmHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProVmHCardEntityIndex = _EthernetNTEGE114ProVmHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 1),
    _EthernetNTEGE114ProVmHCardEntityIndex_Type()
)
ethernetNTEGE114ProVmHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProVmHCardAdminState_Type = AdminState
_EthernetNTEGE114ProVmHCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProVmHCardAdminState = _EthernetNTEGE114ProVmHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 2),
    _EthernetNTEGE114ProVmHCardAdminState_Type()
)
ethernetNTEGE114ProVmHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardAdminState.setStatus("current")
_EthernetNTEGE114ProVmHCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProVmHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProVmHCardOperationalState = _EthernetNTEGE114ProVmHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 3),
    _EthernetNTEGE114ProVmHCardOperationalState_Type()
)
ethernetNTEGE114ProVmHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardOperationalState.setStatus("current")
_EthernetNTEGE114ProVmHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProVmHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProVmHCardSecondaryState = _EthernetNTEGE114ProVmHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 4),
    _EthernetNTEGE114ProVmHCardSecondaryState_Type()
)
ethernetNTEGE114ProVmHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProVmHCardVoltage_Type = Integer32
_EthernetNTEGE114ProVmHCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProVmHCardVoltage = _EthernetNTEGE114ProVmHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 5),
    _EthernetNTEGE114ProVmHCardVoltage_Type()
)
ethernetNTEGE114ProVmHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardVoltage.setStatus("current")
_EthernetNTEGE114ProVmHCardTemperature_Type = Integer32
_EthernetNTEGE114ProVmHCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProVmHCardTemperature = _EthernetNTEGE114ProVmHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 6),
    _EthernetNTEGE114ProVmHCardTemperature_Type()
)
ethernetNTEGE114ProVmHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardTemperature.setStatus("current")
_EthernetNTEGE114ProVmHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProVmHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProVmHCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProVmHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 7),
    _EthernetNTEGE114ProVmHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProVmHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProVmHCardRestartAction_Type = RestartType
_EthernetNTEGE114ProVmHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProVmHCardRestartAction = _EthernetNTEGE114ProVmHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 8),
    _EthernetNTEGE114ProVmHCardRestartAction_Type()
)
ethernetNTEGE114ProVmHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardRestartAction.setStatus("current")
_EthernetNTEGE114ProVmHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProVmHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProVmHCardFineGrainedPmInterval = _EthernetNTEGE114ProVmHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 9),
    _EthernetNTEGE114ProVmHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProVmHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProVmHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProVmHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProVmHCardSwitchPortActionPort = _EthernetNTEGE114ProVmHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 10),
    _EthernetNTEGE114ProVmHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProVmHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProVmHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProVmHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProVmHCardSwitchPortAction = _EthernetNTEGE114ProVmHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 67, 1, 11),
    _EthernetNTEGE114ProVmHCardSwitchPortAction_Type()
)
ethernetNTEGE114ProVmHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114ProVmCHCardTable_Object = MibTable
ethernetNTEGE114ProVmCHCardTable = _EthernetNTEGE114ProVmCHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardTable.setStatus("current")
_EthernetNTEGE114ProVmCHCardEntry_Object = MibTableRow
ethernetNTEGE114ProVmCHCardEntry = _EthernetNTEGE114ProVmCHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1)
)
ethernetNTEGE114ProVmCHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardEntry.setStatus("current")
_EthernetNTEGE114ProVmCHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProVmCHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardEntityIndex = _EthernetNTEGE114ProVmCHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 1),
    _EthernetNTEGE114ProVmCHCardEntityIndex_Type()
)
ethernetNTEGE114ProVmCHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProVmCHCardAdminState_Type = AdminState
_EthernetNTEGE114ProVmCHCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardAdminState = _EthernetNTEGE114ProVmCHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 2),
    _EthernetNTEGE114ProVmCHCardAdminState_Type()
)
ethernetNTEGE114ProVmCHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardAdminState.setStatus("current")
_EthernetNTEGE114ProVmCHCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProVmCHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardOperationalState = _EthernetNTEGE114ProVmCHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 3),
    _EthernetNTEGE114ProVmCHCardOperationalState_Type()
)
ethernetNTEGE114ProVmCHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardOperationalState.setStatus("current")
_EthernetNTEGE114ProVmCHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProVmCHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardSecondaryState = _EthernetNTEGE114ProVmCHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 4),
    _EthernetNTEGE114ProVmCHCardSecondaryState_Type()
)
ethernetNTEGE114ProVmCHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProVmCHCardVoltage_Type = Integer32
_EthernetNTEGE114ProVmCHCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardVoltage = _EthernetNTEGE114ProVmCHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 5),
    _EthernetNTEGE114ProVmCHCardVoltage_Type()
)
ethernetNTEGE114ProVmCHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardVoltage.setStatus("current")
_EthernetNTEGE114ProVmCHCardTemperature_Type = Integer32
_EthernetNTEGE114ProVmCHCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardTemperature = _EthernetNTEGE114ProVmCHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 6),
    _EthernetNTEGE114ProVmCHCardTemperature_Type()
)
ethernetNTEGE114ProVmCHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardTemperature.setStatus("current")
_EthernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 7),
    _EthernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProVmCHCardRestartAction_Type = RestartType
_EthernetNTEGE114ProVmCHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardRestartAction = _EthernetNTEGE114ProVmCHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 8),
    _EthernetNTEGE114ProVmCHCardRestartAction_Type()
)
ethernetNTEGE114ProVmCHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardRestartAction.setStatus("current")
_EthernetNTEGE114ProVmCHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProVmCHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardFineGrainedPmInterval = _EthernetNTEGE114ProVmCHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 9),
    _EthernetNTEGE114ProVmCHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProVmCHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProVmCHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProVmCHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardSwitchPortActionPort = _EthernetNTEGE114ProVmCHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 10),
    _EthernetNTEGE114ProVmCHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProVmCHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProVmCHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProVmCHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProVmCHCardSwitchPortAction = _EthernetNTEGE114ProVmCHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 68, 1, 11),
    _EthernetNTEGE114ProVmCHCardSwitchPortAction_Type()
)
ethernetNTEGE114ProVmCHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE114ProVmCSHCardTable_Object = MibTable
ethernetNTEGE114ProVmCSHCardTable = _EthernetNTEGE114ProVmCSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardTable.setStatus("current")
_EthernetNTEGE114ProVmCSHCardEntry_Object = MibTableRow
ethernetNTEGE114ProVmCSHCardEntry = _EthernetNTEGE114ProVmCSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1)
)
ethernetNTEGE114ProVmCSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardEntry.setStatus("current")
_EthernetNTEGE114ProVmCSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProVmCSHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardEntityIndex = _EthernetNTEGE114ProVmCSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 1),
    _EthernetNTEGE114ProVmCSHCardEntityIndex_Type()
)
ethernetNTEGE114ProVmCSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProVmCSHCardAdminState_Type = AdminState
_EthernetNTEGE114ProVmCSHCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardAdminState = _EthernetNTEGE114ProVmCSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 2),
    _EthernetNTEGE114ProVmCSHCardAdminState_Type()
)
ethernetNTEGE114ProVmCSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardAdminState.setStatus("current")
_EthernetNTEGE114ProVmCSHCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProVmCSHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardOperationalState = _EthernetNTEGE114ProVmCSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 3),
    _EthernetNTEGE114ProVmCSHCardOperationalState_Type()
)
ethernetNTEGE114ProVmCSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardOperationalState.setStatus("current")
_EthernetNTEGE114ProVmCSHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProVmCSHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardSecondaryState = _EthernetNTEGE114ProVmCSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 4),
    _EthernetNTEGE114ProVmCSHCardSecondaryState_Type()
)
ethernetNTEGE114ProVmCSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProVmCSHCardVoltage_Type = Integer32
_EthernetNTEGE114ProVmCSHCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardVoltage = _EthernetNTEGE114ProVmCSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 5),
    _EthernetNTEGE114ProVmCSHCardVoltage_Type()
)
ethernetNTEGE114ProVmCSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardVoltage.setStatus("current")
_EthernetNTEGE114ProVmCSHCardTemperature_Type = Integer32
_EthernetNTEGE114ProVmCSHCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardTemperature = _EthernetNTEGE114ProVmCSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 6),
    _EthernetNTEGE114ProVmCSHCardTemperature_Type()
)
ethernetNTEGE114ProVmCSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardTemperature.setStatus("current")
_EthernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 7),
    _EthernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProVmCSHCardRestartAction_Type = RestartType
_EthernetNTEGE114ProVmCSHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardRestartAction = _EthernetNTEGE114ProVmCSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 8),
    _EthernetNTEGE114ProVmCSHCardRestartAction_Type()
)
ethernetNTEGE114ProVmCSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardRestartAction.setStatus("current")
_EthernetNTEGE114ProVmCSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProVmCSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardFineGrainedPmInterval = _EthernetNTEGE114ProVmCSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 9),
    _EthernetNTEGE114ProVmCSHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProVmCSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProVmCSHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProVmCSHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardSwitchPortActionPort = _EthernetNTEGE114ProVmCSHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 10),
    _EthernetNTEGE114ProVmCSHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProVmCSHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProVmCSHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProVmCSHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProVmCSHCardSwitchPortAction = _EthernetNTEGE114ProVmCSHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 69, 1, 11),
    _EthernetNTEGE114ProVmCSHCardSwitchPortAction_Type()
)
ethernetNTEGE114ProVmCSHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmCSHCardSwitchPortAction.setStatus("current")
_ServerCardTable_Object = MibTable
serverCardTable = _ServerCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70)
)
if mibBuilder.loadTexts:
    serverCardTable.setStatus("current")
_ServerCardEntry_Object = MibTableRow
serverCardEntry = _ServerCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1)
)
serverCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    serverCardEntry.setStatus("current")
_ServerCardEntityIndex_Type = PhysicalIndex
_ServerCardEntityIndex_Object = MibTableColumn
serverCardEntityIndex = _ServerCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 1),
    _ServerCardEntityIndex_Type()
)
serverCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardEntityIndex.setStatus("current")
_ServerCardAdminState_Type = AdminState
_ServerCardAdminState_Object = MibTableColumn
serverCardAdminState = _ServerCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 2),
    _ServerCardAdminState_Type()
)
serverCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverCardAdminState.setStatus("current")
_ServerCardOperationalState_Type = OperationalState
_ServerCardOperationalState_Object = MibTableColumn
serverCardOperationalState = _ServerCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 3),
    _ServerCardOperationalState_Type()
)
serverCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardOperationalState.setStatus("current")
_ServerCardSecondaryState_Type = SecondaryState
_ServerCardSecondaryState_Object = MibTableColumn
serverCardSecondaryState = _ServerCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 4),
    _ServerCardSecondaryState_Type()
)
serverCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardSecondaryState.setStatus("current")
_ServerCardStorageType_Type = StorageType
_ServerCardStorageType_Object = MibTableColumn
serverCardStorageType = _ServerCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 5),
    _ServerCardStorageType_Type()
)
serverCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serverCardStorageType.setStatus("current")
_ServerCardVoltage_Type = Integer32
_ServerCardVoltage_Object = MibTableColumn
serverCardVoltage = _ServerCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 6),
    _ServerCardVoltage_Type()
)
serverCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardVoltage.setStatus("current")
_ServerCardTemperature_Type = Integer32
_ServerCardTemperature_Object = MibTableColumn
serverCardTemperature = _ServerCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 7),
    _ServerCardTemperature_Type()
)
serverCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardTemperature.setStatus("current")
_ServerCardUpTime_Type = Integer32
_ServerCardUpTime_Object = MibTableColumn
serverCardUpTime = _ServerCardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 8),
    _ServerCardUpTime_Type()
)
serverCardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardUpTime.setStatus("current")
_ServerCardVmNumber_Type = Integer32
_ServerCardVmNumber_Object = MibTableColumn
serverCardVmNumber = _ServerCardVmNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 9),
    _ServerCardVmNumber_Type()
)
serverCardVmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardVmNumber.setStatus("current")
_ServerCardVirtualCpuTotal_Type = Integer32
_ServerCardVirtualCpuTotal_Object = MibTableColumn
serverCardVirtualCpuTotal = _ServerCardVirtualCpuTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 10),
    _ServerCardVirtualCpuTotal_Type()
)
serverCardVirtualCpuTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardVirtualCpuTotal.setStatus("current")
_ServerCardVirtualCpuAvailiable_Type = Integer32
_ServerCardVirtualCpuAvailiable_Object = MibTableColumn
serverCardVirtualCpuAvailiable = _ServerCardVirtualCpuAvailiable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 11),
    _ServerCardVirtualCpuAvailiable_Type()
)
serverCardVirtualCpuAvailiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardVirtualCpuAvailiable.setStatus("current")
_ServerCardMemoryTotal_Type = Integer32
_ServerCardMemoryTotal_Object = MibTableColumn
serverCardMemoryTotal = _ServerCardMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 12),
    _ServerCardMemoryTotal_Type()
)
serverCardMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardMemoryTotal.setStatus("current")
_ServerCardMemoryAvailiable_Type = Integer32
_ServerCardMemoryAvailiable_Object = MibTableColumn
serverCardMemoryAvailiable = _ServerCardMemoryAvailiable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 13),
    _ServerCardMemoryAvailiable_Type()
)
serverCardMemoryAvailiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardMemoryAvailiable.setStatus("current")
_ServerCardStorageTotal_Type = Integer32
_ServerCardStorageTotal_Object = MibTableColumn
serverCardStorageTotal = _ServerCardStorageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 14),
    _ServerCardStorageTotal_Type()
)
serverCardStorageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardStorageTotal.setStatus("current")
_ServerCardStorageAvailiable_Type = Integer32
_ServerCardStorageAvailiable_Object = MibTableColumn
serverCardStorageAvailiable = _ServerCardStorageAvailiable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 15),
    _ServerCardStorageAvailiable_Type()
)
serverCardStorageAvailiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardStorageAvailiable.setStatus("current")


class _ServerCardHvVersion_Type(DisplayString):
    """Custom type serverCardHvVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ServerCardHvVersion_Type.__name__ = "DisplayString"
_ServerCardHvVersion_Object = MibTableColumn
serverCardHvVersion = _ServerCardHvVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 16),
    _ServerCardHvVersion_Type()
)
serverCardHvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCardHvVersion.setStatus("current")


class _ServerCardHostName_Type(DisplayString):
    """Custom type serverCardHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ServerCardHostName_Type.__name__ = "DisplayString"
_ServerCardHostName_Object = MibTableColumn
serverCardHostName = _ServerCardHostName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 17),
    _ServerCardHostName_Type()
)
serverCardHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serverCardHostName.setStatus("current")
_ServerCardRestartAction_Type = RestartType
_ServerCardRestartAction_Object = MibTableColumn
serverCardRestartAction = _ServerCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 18),
    _ServerCardRestartAction_Type()
)
serverCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverCardRestartAction.setStatus("current")
_ServerCardRowStatus_Type = RowStatus
_ServerCardRowStatus_Object = MibTableColumn
serverCardRowStatus = _ServerCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 19),
    _ServerCardRowStatus_Type()
)
serverCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serverCardRowStatus.setStatus("current")
_ServerCardIgnoreWatchdog_Type = TruthValue
_ServerCardIgnoreWatchdog_Object = MibTableColumn
serverCardIgnoreWatchdog = _ServerCardIgnoreWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 70, 1, 20),
    _ServerCardIgnoreWatchdog_Type()
)
serverCardIgnoreWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverCardIgnoreWatchdog.setStatus("current")
_Pps16PortCardTable_Object = MibTable
pps16PortCardTable = _Pps16PortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71)
)
if mibBuilder.loadTexts:
    pps16PortCardTable.setStatus("current")
_Pps16PortCardEntry_Object = MibTableRow
pps16PortCardEntry = _Pps16PortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1)
)
pps16PortCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    pps16PortCardEntry.setStatus("current")
_Pps16PortCardEntityIndex_Type = PhysicalIndex
_Pps16PortCardEntityIndex_Object = MibTableColumn
pps16PortCardEntityIndex = _Pps16PortCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1, 1),
    _Pps16PortCardEntityIndex_Type()
)
pps16PortCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pps16PortCardEntityIndex.setStatus("current")
_Pps16PortCardAdminState_Type = AdminState
_Pps16PortCardAdminState_Object = MibTableColumn
pps16PortCardAdminState = _Pps16PortCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1, 2),
    _Pps16PortCardAdminState_Type()
)
pps16PortCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps16PortCardAdminState.setStatus("current")
_Pps16PortCardOperationalState_Type = OperationalState
_Pps16PortCardOperationalState_Object = MibTableColumn
pps16PortCardOperationalState = _Pps16PortCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1, 3),
    _Pps16PortCardOperationalState_Type()
)
pps16PortCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pps16PortCardOperationalState.setStatus("current")
_Pps16PortCardSecondaryState_Type = SecondaryState
_Pps16PortCardSecondaryState_Object = MibTableColumn
pps16PortCardSecondaryState = _Pps16PortCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1, 4),
    _Pps16PortCardSecondaryState_Type()
)
pps16PortCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pps16PortCardSecondaryState.setStatus("current")
_Pps16PortCardRowStatus_Type = RowStatus
_Pps16PortCardRowStatus_Object = MibTableColumn
pps16PortCardRowStatus = _Pps16PortCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1, 5),
    _Pps16PortCardRowStatus_Type()
)
pps16PortCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pps16PortCardRowStatus.setStatus("current")


class _Pps16PortCardAlias_Type(DisplayString):
    """Custom type pps16PortCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Pps16PortCardAlias_Type.__name__ = "DisplayString"
_Pps16PortCardAlias_Object = MibTableColumn
pps16PortCardAlias = _Pps16PortCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 71, 1, 6),
    _Pps16PortCardAlias_Type()
)
pps16PortCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps16PortCardAlias.setStatus("current")
_Clk16PortCardTable_Object = MibTable
clk16PortCardTable = _Clk16PortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72)
)
if mibBuilder.loadTexts:
    clk16PortCardTable.setStatus("current")
_Clk16PortCardEntry_Object = MibTableRow
clk16PortCardEntry = _Clk16PortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1)
)
clk16PortCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    clk16PortCardEntry.setStatus("current")
_Clk16PortCardEntityIndex_Type = PhysicalIndex
_Clk16PortCardEntityIndex_Object = MibTableColumn
clk16PortCardEntityIndex = _Clk16PortCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1, 1),
    _Clk16PortCardEntityIndex_Type()
)
clk16PortCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clk16PortCardEntityIndex.setStatus("current")
_Clk16PortCardAdminState_Type = AdminState
_Clk16PortCardAdminState_Object = MibTableColumn
clk16PortCardAdminState = _Clk16PortCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1, 2),
    _Clk16PortCardAdminState_Type()
)
clk16PortCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clk16PortCardAdminState.setStatus("current")
_Clk16PortCardOperationalState_Type = OperationalState
_Clk16PortCardOperationalState_Object = MibTableColumn
clk16PortCardOperationalState = _Clk16PortCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1, 3),
    _Clk16PortCardOperationalState_Type()
)
clk16PortCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clk16PortCardOperationalState.setStatus("current")
_Clk16PortCardSecondaryState_Type = SecondaryState
_Clk16PortCardSecondaryState_Object = MibTableColumn
clk16PortCardSecondaryState = _Clk16PortCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1, 4),
    _Clk16PortCardSecondaryState_Type()
)
clk16PortCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clk16PortCardSecondaryState.setStatus("current")
_Clk16PortCardRowStatus_Type = RowStatus
_Clk16PortCardRowStatus_Object = MibTableColumn
clk16PortCardRowStatus = _Clk16PortCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1, 5),
    _Clk16PortCardRowStatus_Type()
)
clk16PortCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clk16PortCardRowStatus.setStatus("current")


class _Clk16PortCardAlias_Type(DisplayString):
    """Custom type clk16PortCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Clk16PortCardAlias_Type.__name__ = "DisplayString"
_Clk16PortCardAlias_Object = MibTableColumn
clk16PortCardAlias = _Clk16PortCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 72, 1, 6),
    _Clk16PortCardAlias_Type()
)
clk16PortCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clk16PortCardAlias.setStatus("current")
_TodPps16PortCardTable_Object = MibTable
todPps16PortCardTable = _TodPps16PortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73)
)
if mibBuilder.loadTexts:
    todPps16PortCardTable.setStatus("current")
_TodPps16PortCardEntry_Object = MibTableRow
todPps16PortCardEntry = _TodPps16PortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1)
)
todPps16PortCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    todPps16PortCardEntry.setStatus("current")
_TodPps16PortCardEntityIndex_Type = PhysicalIndex
_TodPps16PortCardEntityIndex_Object = MibTableColumn
todPps16PortCardEntityIndex = _TodPps16PortCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1, 1),
    _TodPps16PortCardEntityIndex_Type()
)
todPps16PortCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todPps16PortCardEntityIndex.setStatus("current")
_TodPps16PortCardAdminState_Type = AdminState
_TodPps16PortCardAdminState_Object = MibTableColumn
todPps16PortCardAdminState = _TodPps16PortCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1, 2),
    _TodPps16PortCardAdminState_Type()
)
todPps16PortCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    todPps16PortCardAdminState.setStatus("current")
_TodPps16PortCardOperationalState_Type = OperationalState
_TodPps16PortCardOperationalState_Object = MibTableColumn
todPps16PortCardOperationalState = _TodPps16PortCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1, 3),
    _TodPps16PortCardOperationalState_Type()
)
todPps16PortCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todPps16PortCardOperationalState.setStatus("current")
_TodPps16PortCardSecondaryState_Type = SecondaryState
_TodPps16PortCardSecondaryState_Object = MibTableColumn
todPps16PortCardSecondaryState = _TodPps16PortCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1, 4),
    _TodPps16PortCardSecondaryState_Type()
)
todPps16PortCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todPps16PortCardSecondaryState.setStatus("current")
_TodPps16PortCardRowStatus_Type = RowStatus
_TodPps16PortCardRowStatus_Object = MibTableColumn
todPps16PortCardRowStatus = _TodPps16PortCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1, 5),
    _TodPps16PortCardRowStatus_Type()
)
todPps16PortCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    todPps16PortCardRowStatus.setStatus("current")


class _TodPps16PortCardAlias_Type(DisplayString):
    """Custom type todPps16PortCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TodPps16PortCardAlias_Type.__name__ = "DisplayString"
_TodPps16PortCardAlias_Object = MibTableColumn
todPps16PortCardAlias = _TodPps16PortCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 73, 1, 6),
    _TodPps16PortCardAlias_Type()
)
todPps16PortCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    todPps16PortCardAlias.setStatus("current")
_EthernetNTEGE101ProCardTable_Object = MibTable
ethernetNTEGE101ProCardTable = _EthernetNTEGE101ProCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74)
)
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardTable.setStatus("current")
_EthernetNTEGE101ProCardEntry_Object = MibTableRow
ethernetNTEGE101ProCardEntry = _EthernetNTEGE101ProCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1)
)
ethernetNTEGE101ProCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardEntry.setStatus("current")
_EthernetNTEGE101ProCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE101ProCardEntityIndex_Object = MibTableColumn
ethernetNTEGE101ProCardEntityIndex = _EthernetNTEGE101ProCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 1),
    _EthernetNTEGE101ProCardEntityIndex_Type()
)
ethernetNTEGE101ProCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardEntityIndex.setStatus("current")
_EthernetNTEGE101ProCardAdminState_Type = AdminState
_EthernetNTEGE101ProCardAdminState_Object = MibTableColumn
ethernetNTEGE101ProCardAdminState = _EthernetNTEGE101ProCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 2),
    _EthernetNTEGE101ProCardAdminState_Type()
)
ethernetNTEGE101ProCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardAdminState.setStatus("current")
_EthernetNTEGE101ProCardOperationalState_Type = OperationalState
_EthernetNTEGE101ProCardOperationalState_Object = MibTableColumn
ethernetNTEGE101ProCardOperationalState = _EthernetNTEGE101ProCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 3),
    _EthernetNTEGE101ProCardOperationalState_Type()
)
ethernetNTEGE101ProCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardOperationalState.setStatus("current")
_EthernetNTEGE101ProCardSecondaryState_Type = SecondaryState
_EthernetNTEGE101ProCardSecondaryState_Object = MibTableColumn
ethernetNTEGE101ProCardSecondaryState = _EthernetNTEGE101ProCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 4),
    _EthernetNTEGE101ProCardSecondaryState_Type()
)
ethernetNTEGE101ProCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardSecondaryState.setStatus("current")
_EthernetNTEGE101ProCardVoltage_Type = Integer32
_EthernetNTEGE101ProCardVoltage_Object = MibTableColumn
ethernetNTEGE101ProCardVoltage = _EthernetNTEGE101ProCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 5),
    _EthernetNTEGE101ProCardVoltage_Type()
)
ethernetNTEGE101ProCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardVoltage.setStatus("current")
_EthernetNTEGE101ProCardTemperature_Type = Integer32
_EthernetNTEGE101ProCardTemperature_Object = MibTableColumn
ethernetNTEGE101ProCardTemperature = _EthernetNTEGE101ProCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 6),
    _EthernetNTEGE101ProCardTemperature_Type()
)
ethernetNTEGE101ProCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardTemperature.setStatus("current")
_EthernetNTEGE101ProCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE101ProCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE101ProCardSnmpDyingGaspEnabled = _EthernetNTEGE101ProCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 7),
    _EthernetNTEGE101ProCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE101ProCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE101ProCardRestartAction_Type = RestartType
_EthernetNTEGE101ProCardRestartAction_Object = MibTableColumn
ethernetNTEGE101ProCardRestartAction = _EthernetNTEGE101ProCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 8),
    _EthernetNTEGE101ProCardRestartAction_Type()
)
ethernetNTEGE101ProCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardRestartAction.setStatus("current")
_EthernetNTEGE101ProCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE101ProCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE101ProCardFineGrainedPmInterval = _EthernetNTEGE101ProCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 9),
    _EthernetNTEGE101ProCardFineGrainedPmInterval_Type()
)
ethernetNTEGE101ProCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE101ProCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE101ProCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE101ProCardSwitchPortActionPort = _EthernetNTEGE101ProCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 10),
    _EthernetNTEGE101ProCardSwitchPortActionPort_Type()
)
ethernetNTEGE101ProCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE101ProCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE101ProCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE101ProCardSwitchPortAction = _EthernetNTEGE101ProCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 74, 1, 11),
    _EthernetNTEGE101ProCardSwitchPortAction_Type()
)
ethernetNTEGE101ProCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE101ProCardSwitchPortAction.setStatus("current")
_EthernetNTEGO102ProSCardTable_Object = MibTable
ethernetNTEGO102ProSCardTable = _EthernetNTEGO102ProSCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75)
)
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardTable.setStatus("current")
_EthernetNTEGO102ProSCardEntry_Object = MibTableRow
ethernetNTEGO102ProSCardEntry = _EthernetNTEGO102ProSCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1)
)
ethernetNTEGO102ProSCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardEntry.setStatus("current")
_EthernetNTEGO102ProSCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGO102ProSCardEntityIndex_Object = MibTableColumn
ethernetNTEGO102ProSCardEntityIndex = _EthernetNTEGO102ProSCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 1),
    _EthernetNTEGO102ProSCardEntityIndex_Type()
)
ethernetNTEGO102ProSCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardEntityIndex.setStatus("current")
_EthernetNTEGO102ProSCardAdminState_Type = AdminState
_EthernetNTEGO102ProSCardAdminState_Object = MibTableColumn
ethernetNTEGO102ProSCardAdminState = _EthernetNTEGO102ProSCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 2),
    _EthernetNTEGO102ProSCardAdminState_Type()
)
ethernetNTEGO102ProSCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardAdminState.setStatus("current")
_EthernetNTEGO102ProSCardOperationalState_Type = OperationalState
_EthernetNTEGO102ProSCardOperationalState_Object = MibTableColumn
ethernetNTEGO102ProSCardOperationalState = _EthernetNTEGO102ProSCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 3),
    _EthernetNTEGO102ProSCardOperationalState_Type()
)
ethernetNTEGO102ProSCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardOperationalState.setStatus("current")
_EthernetNTEGO102ProSCardSecondaryState_Type = SecondaryState
_EthernetNTEGO102ProSCardSecondaryState_Object = MibTableColumn
ethernetNTEGO102ProSCardSecondaryState = _EthernetNTEGO102ProSCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 4),
    _EthernetNTEGO102ProSCardSecondaryState_Type()
)
ethernetNTEGO102ProSCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardSecondaryState.setStatus("current")
_EthernetNTEGO102ProSCardVoltage_Type = Integer32
_EthernetNTEGO102ProSCardVoltage_Object = MibTableColumn
ethernetNTEGO102ProSCardVoltage = _EthernetNTEGO102ProSCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 5),
    _EthernetNTEGO102ProSCardVoltage_Type()
)
ethernetNTEGO102ProSCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardVoltage.setStatus("current")
_EthernetNTEGO102ProSCardTemperature_Type = Integer32
_EthernetNTEGO102ProSCardTemperature_Object = MibTableColumn
ethernetNTEGO102ProSCardTemperature = _EthernetNTEGO102ProSCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 6),
    _EthernetNTEGO102ProSCardTemperature_Type()
)
ethernetNTEGO102ProSCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardTemperature.setStatus("current")
_EthernetNTEGO102ProSCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGO102ProSCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGO102ProSCardSnmpDyingGaspEnabled = _EthernetNTEGO102ProSCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 7),
    _EthernetNTEGO102ProSCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGO102ProSCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGO102ProSCardRestartAction_Type = RestartType
_EthernetNTEGO102ProSCardRestartAction_Object = MibTableColumn
ethernetNTEGO102ProSCardRestartAction = _EthernetNTEGO102ProSCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 8),
    _EthernetNTEGO102ProSCardRestartAction_Type()
)
ethernetNTEGO102ProSCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardRestartAction.setStatus("current")
_EthernetNTEGO102ProSCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGO102ProSCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGO102ProSCardFineGrainedPmInterval = _EthernetNTEGO102ProSCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 9),
    _EthernetNTEGO102ProSCardFineGrainedPmInterval_Type()
)
ethernetNTEGO102ProSCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGO102ProSCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGO102ProSCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGO102ProSCardSwitchPortActionPort = _EthernetNTEGO102ProSCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 10),
    _EthernetNTEGO102ProSCardSwitchPortActionPort_Type()
)
ethernetNTEGO102ProSCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGO102ProSCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGO102ProSCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGO102ProSCardSwitchPortAction = _EthernetNTEGO102ProSCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 75, 1, 11),
    _EthernetNTEGO102ProSCardSwitchPortAction_Type()
)
ethernetNTEGO102ProSCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSCardSwitchPortAction.setStatus("current")
_EthernetNTEGO102ProSPCardTable_Object = MibTable
ethernetNTEGO102ProSPCardTable = _EthernetNTEGO102ProSPCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76)
)
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardTable.setStatus("current")
_EthernetNTEGO102ProSPCardEntry_Object = MibTableRow
ethernetNTEGO102ProSPCardEntry = _EthernetNTEGO102ProSPCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1)
)
ethernetNTEGO102ProSPCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardEntry.setStatus("current")
_EthernetNTEGO102ProSPCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGO102ProSPCardEntityIndex_Object = MibTableColumn
ethernetNTEGO102ProSPCardEntityIndex = _EthernetNTEGO102ProSPCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 1),
    _EthernetNTEGO102ProSPCardEntityIndex_Type()
)
ethernetNTEGO102ProSPCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardEntityIndex.setStatus("current")
_EthernetNTEGO102ProSPCardAdminState_Type = AdminState
_EthernetNTEGO102ProSPCardAdminState_Object = MibTableColumn
ethernetNTEGO102ProSPCardAdminState = _EthernetNTEGO102ProSPCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 2),
    _EthernetNTEGO102ProSPCardAdminState_Type()
)
ethernetNTEGO102ProSPCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardAdminState.setStatus("current")
_EthernetNTEGO102ProSPCardOperationalState_Type = OperationalState
_EthernetNTEGO102ProSPCardOperationalState_Object = MibTableColumn
ethernetNTEGO102ProSPCardOperationalState = _EthernetNTEGO102ProSPCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 3),
    _EthernetNTEGO102ProSPCardOperationalState_Type()
)
ethernetNTEGO102ProSPCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardOperationalState.setStatus("current")
_EthernetNTEGO102ProSPCardSecondaryState_Type = SecondaryState
_EthernetNTEGO102ProSPCardSecondaryState_Object = MibTableColumn
ethernetNTEGO102ProSPCardSecondaryState = _EthernetNTEGO102ProSPCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 4),
    _EthernetNTEGO102ProSPCardSecondaryState_Type()
)
ethernetNTEGO102ProSPCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardSecondaryState.setStatus("current")
_EthernetNTEGO102ProSPCardVoltage_Type = Integer32
_EthernetNTEGO102ProSPCardVoltage_Object = MibTableColumn
ethernetNTEGO102ProSPCardVoltage = _EthernetNTEGO102ProSPCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 5),
    _EthernetNTEGO102ProSPCardVoltage_Type()
)
ethernetNTEGO102ProSPCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardVoltage.setStatus("current")
_EthernetNTEGO102ProSPCardTemperature_Type = Integer32
_EthernetNTEGO102ProSPCardTemperature_Object = MibTableColumn
ethernetNTEGO102ProSPCardTemperature = _EthernetNTEGO102ProSPCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 6),
    _EthernetNTEGO102ProSPCardTemperature_Type()
)
ethernetNTEGO102ProSPCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardTemperature.setStatus("current")
_EthernetNTEGO102ProSPCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGO102ProSPCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGO102ProSPCardSnmpDyingGaspEnabled = _EthernetNTEGO102ProSPCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 7),
    _EthernetNTEGO102ProSPCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGO102ProSPCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGO102ProSPCardRestartAction_Type = RestartType
_EthernetNTEGO102ProSPCardRestartAction_Object = MibTableColumn
ethernetNTEGO102ProSPCardRestartAction = _EthernetNTEGO102ProSPCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 8),
    _EthernetNTEGO102ProSPCardRestartAction_Type()
)
ethernetNTEGO102ProSPCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardRestartAction.setStatus("current")
_EthernetNTEGO102ProSPCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGO102ProSPCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGO102ProSPCardFineGrainedPmInterval = _EthernetNTEGO102ProSPCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 9),
    _EthernetNTEGO102ProSPCardFineGrainedPmInterval_Type()
)
ethernetNTEGO102ProSPCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGO102ProSPCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGO102ProSPCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGO102ProSPCardSwitchPortActionPort = _EthernetNTEGO102ProSPCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 10),
    _EthernetNTEGO102ProSPCardSwitchPortActionPort_Type()
)
ethernetNTEGO102ProSPCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGO102ProSPCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGO102ProSPCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGO102ProSPCardSwitchPortAction = _EthernetNTEGO102ProSPCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 76, 1, 11),
    _EthernetNTEGO102ProSPCardSwitchPortAction_Type()
)
ethernetNTEGO102ProSPCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSPCardSwitchPortAction.setStatus("current")
_EthernetNTECX101Pro30ACardTable_Object = MibTable
ethernetNTECX101Pro30ACardTable = _EthernetNTECX101Pro30ACardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77)
)
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardTable.setStatus("current")
_EthernetNTECX101Pro30ACardEntry_Object = MibTableRow
ethernetNTECX101Pro30ACardEntry = _EthernetNTECX101Pro30ACardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1)
)
ethernetNTECX101Pro30ACardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardEntry.setStatus("current")
_EthernetNTECX101Pro30ACardEntityIndex_Type = PhysicalIndex
_EthernetNTECX101Pro30ACardEntityIndex_Object = MibTableColumn
ethernetNTECX101Pro30ACardEntityIndex = _EthernetNTECX101Pro30ACardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 1),
    _EthernetNTECX101Pro30ACardEntityIndex_Type()
)
ethernetNTECX101Pro30ACardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardEntityIndex.setStatus("current")
_EthernetNTECX101Pro30ACardAdminState_Type = AdminState
_EthernetNTECX101Pro30ACardAdminState_Object = MibTableColumn
ethernetNTECX101Pro30ACardAdminState = _EthernetNTECX101Pro30ACardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 2),
    _EthernetNTECX101Pro30ACardAdminState_Type()
)
ethernetNTECX101Pro30ACardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardAdminState.setStatus("current")
_EthernetNTECX101Pro30ACardOperationalState_Type = OperationalState
_EthernetNTECX101Pro30ACardOperationalState_Object = MibTableColumn
ethernetNTECX101Pro30ACardOperationalState = _EthernetNTECX101Pro30ACardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 3),
    _EthernetNTECX101Pro30ACardOperationalState_Type()
)
ethernetNTECX101Pro30ACardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardOperationalState.setStatus("current")
_EthernetNTECX101Pro30ACardSecondaryState_Type = SecondaryState
_EthernetNTECX101Pro30ACardSecondaryState_Object = MibTableColumn
ethernetNTECX101Pro30ACardSecondaryState = _EthernetNTECX101Pro30ACardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 4),
    _EthernetNTECX101Pro30ACardSecondaryState_Type()
)
ethernetNTECX101Pro30ACardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardSecondaryState.setStatus("current")
_EthernetNTECX101Pro30ACardVoltage_Type = Integer32
_EthernetNTECX101Pro30ACardVoltage_Object = MibTableColumn
ethernetNTECX101Pro30ACardVoltage = _EthernetNTECX101Pro30ACardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 5),
    _EthernetNTECX101Pro30ACardVoltage_Type()
)
ethernetNTECX101Pro30ACardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardVoltage.setStatus("current")
_EthernetNTECX101Pro30ACardTemperature_Type = Integer32
_EthernetNTECX101Pro30ACardTemperature_Object = MibTableColumn
ethernetNTECX101Pro30ACardTemperature = _EthernetNTECX101Pro30ACardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 6),
    _EthernetNTECX101Pro30ACardTemperature_Type()
)
ethernetNTECX101Pro30ACardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardTemperature.setStatus("current")
_EthernetNTECX101Pro30ACardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTECX101Pro30ACardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTECX101Pro30ACardSnmpDyingGaspEnabled = _EthernetNTECX101Pro30ACardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 7),
    _EthernetNTECX101Pro30ACardSnmpDyingGaspEnabled_Type()
)
ethernetNTECX101Pro30ACardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTECX101Pro30ACardRestartAction_Type = RestartType
_EthernetNTECX101Pro30ACardRestartAction_Object = MibTableColumn
ethernetNTECX101Pro30ACardRestartAction = _EthernetNTECX101Pro30ACardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 8),
    _EthernetNTECX101Pro30ACardRestartAction_Type()
)
ethernetNTECX101Pro30ACardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardRestartAction.setStatus("current")
_EthernetNTECX101Pro30ACardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTECX101Pro30ACardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTECX101Pro30ACardFineGrainedPmInterval = _EthernetNTECX101Pro30ACardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 9),
    _EthernetNTECX101Pro30ACardFineGrainedPmInterval_Type()
)
ethernetNTECX101Pro30ACardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardFineGrainedPmInterval.setStatus("current")
_EthernetNTECX101Pro30ACardSwitchPortActionPort_Type = VariablePointer
_EthernetNTECX101Pro30ACardSwitchPortActionPort_Object = MibTableColumn
ethernetNTECX101Pro30ACardSwitchPortActionPort = _EthernetNTECX101Pro30ACardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 10),
    _EthernetNTECX101Pro30ACardSwitchPortActionPort_Type()
)
ethernetNTECX101Pro30ACardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardSwitchPortActionPort.setStatus("current")
_EthernetNTECX101Pro30ACardSwitchPortAction_Type = SwitchPortAction
_EthernetNTECX101Pro30ACardSwitchPortAction_Object = MibTableColumn
ethernetNTECX101Pro30ACardSwitchPortAction = _EthernetNTECX101Pro30ACardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 77, 1, 11),
    _EthernetNTECX101Pro30ACardSwitchPortAction_Type()
)
ethernetNTECX101Pro30ACardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX101Pro30ACardSwitchPortAction.setStatus("current")
_EthernetNTECX102Pro30ACardTable_Object = MibTable
ethernetNTECX102Pro30ACardTable = _EthernetNTECX102Pro30ACardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78)
)
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardTable.setStatus("current")
_EthernetNTECX102Pro30ACardEntry_Object = MibTableRow
ethernetNTECX102Pro30ACardEntry = _EthernetNTECX102Pro30ACardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1)
)
ethernetNTECX102Pro30ACardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardEntry.setStatus("current")
_EthernetNTECX102Pro30ACardEntityIndex_Type = PhysicalIndex
_EthernetNTECX102Pro30ACardEntityIndex_Object = MibTableColumn
ethernetNTECX102Pro30ACardEntityIndex = _EthernetNTECX102Pro30ACardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 1),
    _EthernetNTECX102Pro30ACardEntityIndex_Type()
)
ethernetNTECX102Pro30ACardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardEntityIndex.setStatus("current")
_EthernetNTECX102Pro30ACardAdminState_Type = AdminState
_EthernetNTECX102Pro30ACardAdminState_Object = MibTableColumn
ethernetNTECX102Pro30ACardAdminState = _EthernetNTECX102Pro30ACardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 2),
    _EthernetNTECX102Pro30ACardAdminState_Type()
)
ethernetNTECX102Pro30ACardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardAdminState.setStatus("current")
_EthernetNTECX102Pro30ACardOperationalState_Type = OperationalState
_EthernetNTECX102Pro30ACardOperationalState_Object = MibTableColumn
ethernetNTECX102Pro30ACardOperationalState = _EthernetNTECX102Pro30ACardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 3),
    _EthernetNTECX102Pro30ACardOperationalState_Type()
)
ethernetNTECX102Pro30ACardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardOperationalState.setStatus("current")
_EthernetNTECX102Pro30ACardSecondaryState_Type = SecondaryState
_EthernetNTECX102Pro30ACardSecondaryState_Object = MibTableColumn
ethernetNTECX102Pro30ACardSecondaryState = _EthernetNTECX102Pro30ACardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 4),
    _EthernetNTECX102Pro30ACardSecondaryState_Type()
)
ethernetNTECX102Pro30ACardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardSecondaryState.setStatus("current")
_EthernetNTECX102Pro30ACardVoltage_Type = Integer32
_EthernetNTECX102Pro30ACardVoltage_Object = MibTableColumn
ethernetNTECX102Pro30ACardVoltage = _EthernetNTECX102Pro30ACardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 5),
    _EthernetNTECX102Pro30ACardVoltage_Type()
)
ethernetNTECX102Pro30ACardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardVoltage.setStatus("current")
_EthernetNTECX102Pro30ACardTemperature_Type = Integer32
_EthernetNTECX102Pro30ACardTemperature_Object = MibTableColumn
ethernetNTECX102Pro30ACardTemperature = _EthernetNTECX102Pro30ACardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 6),
    _EthernetNTECX102Pro30ACardTemperature_Type()
)
ethernetNTECX102Pro30ACardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardTemperature.setStatus("current")
_EthernetNTECX102Pro30ACardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTECX102Pro30ACardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTECX102Pro30ACardSnmpDyingGaspEnabled = _EthernetNTECX102Pro30ACardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 7),
    _EthernetNTECX102Pro30ACardSnmpDyingGaspEnabled_Type()
)
ethernetNTECX102Pro30ACardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTECX102Pro30ACardRestartAction_Type = RestartType
_EthernetNTECX102Pro30ACardRestartAction_Object = MibTableColumn
ethernetNTECX102Pro30ACardRestartAction = _EthernetNTECX102Pro30ACardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 8),
    _EthernetNTECX102Pro30ACardRestartAction_Type()
)
ethernetNTECX102Pro30ACardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardRestartAction.setStatus("current")
_EthernetNTECX102Pro30ACardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTECX102Pro30ACardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTECX102Pro30ACardFineGrainedPmInterval = _EthernetNTECX102Pro30ACardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 9),
    _EthernetNTECX102Pro30ACardFineGrainedPmInterval_Type()
)
ethernetNTECX102Pro30ACardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardFineGrainedPmInterval.setStatus("current")
_EthernetNTECX102Pro30ACardSwitchPortActionPort_Type = VariablePointer
_EthernetNTECX102Pro30ACardSwitchPortActionPort_Object = MibTableColumn
ethernetNTECX102Pro30ACardSwitchPortActionPort = _EthernetNTECX102Pro30ACardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 10),
    _EthernetNTECX102Pro30ACardSwitchPortActionPort_Type()
)
ethernetNTECX102Pro30ACardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardSwitchPortActionPort.setStatus("current")
_EthernetNTECX102Pro30ACardSwitchPortAction_Type = SwitchPortAction
_EthernetNTECX102Pro30ACardSwitchPortAction_Object = MibTableColumn
ethernetNTECX102Pro30ACardSwitchPortAction = _EthernetNTECX102Pro30ACardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 78, 1, 11),
    _EthernetNTECX102Pro30ACardSwitchPortAction_Type()
)
ethernetNTECX102Pro30ACardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTECX102Pro30ACardSwitchPortAction.setStatus("current")
_Ge4PortCardTable_Object = MibTable
ge4PortCardTable = _Ge4PortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79)
)
if mibBuilder.loadTexts:
    ge4PortCardTable.setStatus("current")
_Ge4PortCardEntry_Object = MibTableRow
ge4PortCardEntry = _Ge4PortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1)
)
ge4PortCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ge4PortCardEntry.setStatus("current")
_Ge4PortCardEntityIndex_Type = PhysicalIndex
_Ge4PortCardEntityIndex_Object = MibTableColumn
ge4PortCardEntityIndex = _Ge4PortCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 1),
    _Ge4PortCardEntityIndex_Type()
)
ge4PortCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ge4PortCardEntityIndex.setStatus("current")
_Ge4PortCardAdminState_Type = AdminState
_Ge4PortCardAdminState_Object = MibTableColumn
ge4PortCardAdminState = _Ge4PortCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 2),
    _Ge4PortCardAdminState_Type()
)
ge4PortCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ge4PortCardAdminState.setStatus("current")
_Ge4PortCardOperationalState_Type = OperationalState
_Ge4PortCardOperationalState_Object = MibTableColumn
ge4PortCardOperationalState = _Ge4PortCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 3),
    _Ge4PortCardOperationalState_Type()
)
ge4PortCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ge4PortCardOperationalState.setStatus("current")
_Ge4PortCardSecondaryState_Type = SecondaryState
_Ge4PortCardSecondaryState_Object = MibTableColumn
ge4PortCardSecondaryState = _Ge4PortCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 4),
    _Ge4PortCardSecondaryState_Type()
)
ge4PortCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ge4PortCardSecondaryState.setStatus("current")
_Ge4PortCardRowStatus_Type = RowStatus
_Ge4PortCardRowStatus_Object = MibTableColumn
ge4PortCardRowStatus = _Ge4PortCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 5),
    _Ge4PortCardRowStatus_Type()
)
ge4PortCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ge4PortCardRowStatus.setStatus("current")


class _Ge4PortCardAlias_Type(DisplayString):
    """Custom type ge4PortCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Ge4PortCardAlias_Type.__name__ = "DisplayString"
_Ge4PortCardAlias_Object = MibTableColumn
ge4PortCardAlias = _Ge4PortCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 6),
    _Ge4PortCardAlias_Type()
)
ge4PortCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ge4PortCardAlias.setStatus("current")
_Ge4PortCardTemperature_Type = Integer32
_Ge4PortCardTemperature_Object = MibTableColumn
ge4PortCardTemperature = _Ge4PortCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 79, 1, 7),
    _Ge4PortCardTemperature_Type()
)
ge4PortCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ge4PortCardTemperature.setStatus("current")
_EthernetNTEXG116PROCardTable_Object = MibTable
ethernetNTEXG116PROCardTable = _EthernetNTEXG116PROCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80)
)
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardTable.setStatus("current")
_EthernetNTEXG116PROCardEntry_Object = MibTableRow
ethernetNTEXG116PROCardEntry = _EthernetNTEXG116PROCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1)
)
ethernetNTEXG116PROCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardEntry.setStatus("current")
_EthernetNTEXG116PROCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG116PROCardEntityIndex_Object = MibTableColumn
ethernetNTEXG116PROCardEntityIndex = _EthernetNTEXG116PROCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 1),
    _EthernetNTEXG116PROCardEntityIndex_Type()
)
ethernetNTEXG116PROCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardEntityIndex.setStatus("current")
_EthernetNTEXG116PROCardAdminState_Type = AdminState
_EthernetNTEXG116PROCardAdminState_Object = MibTableColumn
ethernetNTEXG116PROCardAdminState = _EthernetNTEXG116PROCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 2),
    _EthernetNTEXG116PROCardAdminState_Type()
)
ethernetNTEXG116PROCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardAdminState.setStatus("current")
_EthernetNTEXG116PROCardOperationalState_Type = OperationalState
_EthernetNTEXG116PROCardOperationalState_Object = MibTableColumn
ethernetNTEXG116PROCardOperationalState = _EthernetNTEXG116PROCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 3),
    _EthernetNTEXG116PROCardOperationalState_Type()
)
ethernetNTEXG116PROCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardOperationalState.setStatus("current")
_EthernetNTEXG116PROCardSecondaryState_Type = SecondaryState
_EthernetNTEXG116PROCardSecondaryState_Object = MibTableColumn
ethernetNTEXG116PROCardSecondaryState = _EthernetNTEXG116PROCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 4),
    _EthernetNTEXG116PROCardSecondaryState_Type()
)
ethernetNTEXG116PROCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardSecondaryState.setStatus("current")
_EthernetNTEXG116PROCardVoltage_Type = Integer32
_EthernetNTEXG116PROCardVoltage_Object = MibTableColumn
ethernetNTEXG116PROCardVoltage = _EthernetNTEXG116PROCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 5),
    _EthernetNTEXG116PROCardVoltage_Type()
)
ethernetNTEXG116PROCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardVoltage.setStatus("current")
_EthernetNTEXG116PROCardTemperature_Type = Integer32
_EthernetNTEXG116PROCardTemperature_Object = MibTableColumn
ethernetNTEXG116PROCardTemperature = _EthernetNTEXG116PROCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 6),
    _EthernetNTEXG116PROCardTemperature_Type()
)
ethernetNTEXG116PROCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardTemperature.setStatus("current")
_EthernetNTEXG116PROCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG116PROCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG116PROCardSnmpDyingGaspEnabled = _EthernetNTEXG116PROCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 7),
    _EthernetNTEXG116PROCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG116PROCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG116PROCardRestartAction_Type = RestartType
_EthernetNTEXG116PROCardRestartAction_Object = MibTableColumn
ethernetNTEXG116PROCardRestartAction = _EthernetNTEXG116PROCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 8),
    _EthernetNTEXG116PROCardRestartAction_Type()
)
ethernetNTEXG116PROCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardRestartAction.setStatus("current")
_EthernetNTEXG116PROCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG116PROCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG116PROCardFineGrainedPmInterval = _EthernetNTEXG116PROCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 80, 1, 9),
    _EthernetNTEXG116PROCardFineGrainedPmInterval_Type()
)
ethernetNTEXG116PROCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEXG120PROCardTable_Object = MibTable
ethernetNTEXG120PROCardTable = _EthernetNTEXG120PROCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81)
)
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardTable.setStatus("current")
_EthernetNTEXG120PROCardEntry_Object = MibTableRow
ethernetNTEXG120PROCardEntry = _EthernetNTEXG120PROCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1)
)
ethernetNTEXG120PROCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardEntry.setStatus("current")
_EthernetNTEXG120PROCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG120PROCardEntityIndex_Object = MibTableColumn
ethernetNTEXG120PROCardEntityIndex = _EthernetNTEXG120PROCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 1),
    _EthernetNTEXG120PROCardEntityIndex_Type()
)
ethernetNTEXG120PROCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardEntityIndex.setStatus("current")
_EthernetNTEXG120PROCardAdminState_Type = AdminState
_EthernetNTEXG120PROCardAdminState_Object = MibTableColumn
ethernetNTEXG120PROCardAdminState = _EthernetNTEXG120PROCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 2),
    _EthernetNTEXG120PROCardAdminState_Type()
)
ethernetNTEXG120PROCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardAdminState.setStatus("current")
_EthernetNTEXG120PROCardOperationalState_Type = OperationalState
_EthernetNTEXG120PROCardOperationalState_Object = MibTableColumn
ethernetNTEXG120PROCardOperationalState = _EthernetNTEXG120PROCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 3),
    _EthernetNTEXG120PROCardOperationalState_Type()
)
ethernetNTEXG120PROCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardOperationalState.setStatus("current")
_EthernetNTEXG120PROCardSecondaryState_Type = SecondaryState
_EthernetNTEXG120PROCardSecondaryState_Object = MibTableColumn
ethernetNTEXG120PROCardSecondaryState = _EthernetNTEXG120PROCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 4),
    _EthernetNTEXG120PROCardSecondaryState_Type()
)
ethernetNTEXG120PROCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardSecondaryState.setStatus("current")
_EthernetNTEXG120PROCardVoltage_Type = Integer32
_EthernetNTEXG120PROCardVoltage_Object = MibTableColumn
ethernetNTEXG120PROCardVoltage = _EthernetNTEXG120PROCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 5),
    _EthernetNTEXG120PROCardVoltage_Type()
)
ethernetNTEXG120PROCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardVoltage.setStatus("current")
_EthernetNTEXG120PROCardTemperature_Type = Integer32
_EthernetNTEXG120PROCardTemperature_Object = MibTableColumn
ethernetNTEXG120PROCardTemperature = _EthernetNTEXG120PROCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 6),
    _EthernetNTEXG120PROCardTemperature_Type()
)
ethernetNTEXG120PROCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardTemperature.setStatus("current")
_EthernetNTEXG120PROCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG120PROCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG120PROCardSnmpDyingGaspEnabled = _EthernetNTEXG120PROCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 7),
    _EthernetNTEXG120PROCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG120PROCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG120PROCardRestartAction_Type = RestartType
_EthernetNTEXG120PROCardRestartAction_Object = MibTableColumn
ethernetNTEXG120PROCardRestartAction = _EthernetNTEXG120PROCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 8),
    _EthernetNTEXG120PROCardRestartAction_Type()
)
ethernetNTEXG120PROCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardRestartAction.setStatus("current")
_EthernetNTEXG120PROCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG120PROCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG120PROCardFineGrainedPmInterval = _EthernetNTEXG120PROCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 81, 1, 9),
    _EthernetNTEXG120PROCardFineGrainedPmInterval_Type()
)
ethernetNTEXG120PROCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112ProVmCardTable_Object = MibTable
ethernetNTEGE112ProVmCardTable = _EthernetNTEGE112ProVmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82)
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardTable.setStatus("current")
_EthernetNTEGE112ProVmCardEntry_Object = MibTableRow
ethernetNTEGE112ProVmCardEntry = _EthernetNTEGE112ProVmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1)
)
ethernetNTEGE112ProVmCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardEntry.setStatus("current")
_EthernetNTEGE112ProVmCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE112ProVmCardEntityIndex_Object = MibTableColumn
ethernetNTEGE112ProVmCardEntityIndex = _EthernetNTEGE112ProVmCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 1),
    _EthernetNTEGE112ProVmCardEntityIndex_Type()
)
ethernetNTEGE112ProVmCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardEntityIndex.setStatus("current")
_EthernetNTEGE112ProVmCardAdminState_Type = AdminState
_EthernetNTEGE112ProVmCardAdminState_Object = MibTableColumn
ethernetNTEGE112ProVmCardAdminState = _EthernetNTEGE112ProVmCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 2),
    _EthernetNTEGE112ProVmCardAdminState_Type()
)
ethernetNTEGE112ProVmCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardAdminState.setStatus("current")
_EthernetNTEGE112ProVmCardOperationalState_Type = OperationalState
_EthernetNTEGE112ProVmCardOperationalState_Object = MibTableColumn
ethernetNTEGE112ProVmCardOperationalState = _EthernetNTEGE112ProVmCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 3),
    _EthernetNTEGE112ProVmCardOperationalState_Type()
)
ethernetNTEGE112ProVmCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardOperationalState.setStatus("current")
_EthernetNTEGE112ProVmCardSecondaryState_Type = SecondaryState
_EthernetNTEGE112ProVmCardSecondaryState_Object = MibTableColumn
ethernetNTEGE112ProVmCardSecondaryState = _EthernetNTEGE112ProVmCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 4),
    _EthernetNTEGE112ProVmCardSecondaryState_Type()
)
ethernetNTEGE112ProVmCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardSecondaryState.setStatus("current")
_EthernetNTEGE112ProVmCardVoltage_Type = Integer32
_EthernetNTEGE112ProVmCardVoltage_Object = MibTableColumn
ethernetNTEGE112ProVmCardVoltage = _EthernetNTEGE112ProVmCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 5),
    _EthernetNTEGE112ProVmCardVoltage_Type()
)
ethernetNTEGE112ProVmCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardVoltage.setStatus("current")
_EthernetNTEGE112ProVmCardTemperature_Type = Integer32
_EthernetNTEGE112ProVmCardTemperature_Object = MibTableColumn
ethernetNTEGE112ProVmCardTemperature = _EthernetNTEGE112ProVmCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 6),
    _EthernetNTEGE112ProVmCardTemperature_Type()
)
ethernetNTEGE112ProVmCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardTemperature.setStatus("current")
_EthernetNTEGE112ProVmCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE112ProVmCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE112ProVmCardSnmpDyingGaspEnabled = _EthernetNTEGE112ProVmCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 7),
    _EthernetNTEGE112ProVmCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE112ProVmCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE112ProVmCardRestartAction_Type = RestartType
_EthernetNTEGE112ProVmCardRestartAction_Object = MibTableColumn
ethernetNTEGE112ProVmCardRestartAction = _EthernetNTEGE112ProVmCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 8),
    _EthernetNTEGE112ProVmCardRestartAction_Type()
)
ethernetNTEGE112ProVmCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardRestartAction.setStatus("current")
_EthernetNTEGE112ProVmCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE112ProVmCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE112ProVmCardFineGrainedPmInterval = _EthernetNTEGE112ProVmCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 9),
    _EthernetNTEGE112ProVmCardFineGrainedPmInterval_Type()
)
ethernetNTEGE112ProVmCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE112ProVmCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE112ProVmCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE112ProVmCardSwitchPortActionPort = _EthernetNTEGE112ProVmCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 10),
    _EthernetNTEGE112ProVmCardSwitchPortActionPort_Type()
)
ethernetNTEGE112ProVmCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE112ProVmCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE112ProVmCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE112ProVmCardSwitchPortAction = _EthernetNTEGE112ProVmCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 82, 1, 11),
    _EthernetNTEGE112ProVmCardSwitchPortAction_Type()
)
ethernetNTEGE112ProVmCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE112ProVmCardSwitchPortAction.setStatus("current")
_EthernetNTEOSA5401CardTable_Object = MibTable
ethernetNTEOSA5401CardTable = _EthernetNTEOSA5401CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 83)
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5401CardTable.setStatus("current")
_EthernetNTEOSA5401CardEntry_Object = MibTableRow
ethernetNTEOSA5401CardEntry = _EthernetNTEOSA5401CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 83, 1)
)
ethernetNTEOSA5401CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5401CardEntry.setStatus("current")
_EthernetNTEOSA5401CardEntityIndex_Type = PhysicalIndex
_EthernetNTEOSA5401CardEntityIndex_Object = MibTableColumn
ethernetNTEOSA5401CardEntityIndex = _EthernetNTEOSA5401CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 83, 1, 1),
    _EthernetNTEOSA5401CardEntityIndex_Type()
)
ethernetNTEOSA5401CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5401CardEntityIndex.setStatus("current")
_EthernetNTEOSA5401CardAdminState_Type = AdminState
_EthernetNTEOSA5401CardAdminState_Object = MibTableColumn
ethernetNTEOSA5401CardAdminState = _EthernetNTEOSA5401CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 83, 1, 2),
    _EthernetNTEOSA5401CardAdminState_Type()
)
ethernetNTEOSA5401CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5401CardAdminState.setStatus("current")
_EthernetNTEOSA5401CardOperationalState_Type = OperationalState
_EthernetNTEOSA5401CardOperationalState_Object = MibTableColumn
ethernetNTEOSA5401CardOperationalState = _EthernetNTEOSA5401CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 83, 1, 3),
    _EthernetNTEOSA5401CardOperationalState_Type()
)
ethernetNTEOSA5401CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5401CardOperationalState.setStatus("current")
_EthernetNTEOSA5401CardTableRestartAction_Type = RestartType
_EthernetNTEOSA5401CardTableRestartAction_Object = MibTableColumn
ethernetNTEOSA5401CardTableRestartAction = _EthernetNTEOSA5401CardTableRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 83, 1, 4),
    _EthernetNTEOSA5401CardTableRestartAction_Type()
)
ethernetNTEOSA5401CardTableRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5401CardTableRestartAction.setStatus("current")
_EthernetNTEOSA5405CardTable_Object = MibTable
ethernetNTEOSA5405CardTable = _EthernetNTEOSA5405CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84)
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardTable.setStatus("current")
_EthernetNTEOSA5405CardEntry_Object = MibTableRow
ethernetNTEOSA5405CardEntry = _EthernetNTEOSA5405CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1)
)
ethernetNTEOSA5405CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardEntry.setStatus("current")
_EthernetNTEOSA5405CardEntityIndex_Type = PhysicalIndex
_EthernetNTEOSA5405CardEntityIndex_Object = MibTableColumn
ethernetNTEOSA5405CardEntityIndex = _EthernetNTEOSA5405CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1, 1),
    _EthernetNTEOSA5405CardEntityIndex_Type()
)
ethernetNTEOSA5405CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardEntityIndex.setStatus("current")
_EthernetNTEOSA5405CardAdminState_Type = AdminState
_EthernetNTEOSA5405CardAdminState_Object = MibTableColumn
ethernetNTEOSA5405CardAdminState = _EthernetNTEOSA5405CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1, 2),
    _EthernetNTEOSA5405CardAdminState_Type()
)
ethernetNTEOSA5405CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardAdminState.setStatus("current")
_EthernetNTEOSA5405CardOperationalState_Type = OperationalState
_EthernetNTEOSA5405CardOperationalState_Object = MibTableColumn
ethernetNTEOSA5405CardOperationalState = _EthernetNTEOSA5405CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1, 3),
    _EthernetNTEOSA5405CardOperationalState_Type()
)
ethernetNTEOSA5405CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardOperationalState.setStatus("current")
_EthernetNTEOSA5405CardVoltage_Type = Integer32
_EthernetNTEOSA5405CardVoltage_Object = MibTableColumn
ethernetNTEOSA5405CardVoltage = _EthernetNTEOSA5405CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1, 4),
    _EthernetNTEOSA5405CardVoltage_Type()
)
ethernetNTEOSA5405CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardVoltage.setStatus("current")
_EthernetNTEOSA5405CardTemperature_Type = Integer32
_EthernetNTEOSA5405CardTemperature_Object = MibTableColumn
ethernetNTEOSA5405CardTemperature = _EthernetNTEOSA5405CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1, 5),
    _EthernetNTEOSA5405CardTemperature_Type()
)
ethernetNTEOSA5405CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardTemperature.setStatus("current")
_EthernetNTEOSA5405CardTableRestartAction_Type = RestartType
_EthernetNTEOSA5405CardTableRestartAction_Object = MibTableColumn
ethernetNTEOSA5405CardTableRestartAction = _EthernetNTEOSA5405CardTableRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 84, 1, 6),
    _EthernetNTEOSA5405CardTableRestartAction_Type()
)
ethernetNTEOSA5405CardTableRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEOSA5405CardTableRestartAction.setStatus("current")
_EthernetCSMCardTable_Object = MibTable
ethernetCSMCardTable = _EthernetCSMCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85)
)
if mibBuilder.loadTexts:
    ethernetCSMCardTable.setStatus("current")
_EthernetCSMCardEntry_Object = MibTableRow
ethernetCSMCardEntry = _EthernetCSMCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1)
)
ethernetCSMCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetCSMCardEntry.setStatus("current")
_EthernetCSMCardEntityIndex_Type = PhysicalIndex
_EthernetCSMCardEntityIndex_Object = MibTableColumn
ethernetCSMCardEntityIndex = _EthernetCSMCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 1),
    _EthernetCSMCardEntityIndex_Type()
)
ethernetCSMCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCSMCardEntityIndex.setStatus("current")
_EthernetCSMCardAdminState_Type = AdminState
_EthernetCSMCardAdminState_Object = MibTableColumn
ethernetCSMCardAdminState = _EthernetCSMCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 2),
    _EthernetCSMCardAdminState_Type()
)
ethernetCSMCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCSMCardAdminState.setStatus("current")
_EthernetCSMCardOperationalState_Type = OperationalState
_EthernetCSMCardOperationalState_Object = MibTableColumn
ethernetCSMCardOperationalState = _EthernetCSMCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 3),
    _EthernetCSMCardOperationalState_Type()
)
ethernetCSMCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCSMCardOperationalState.setStatus("current")
_EthernetCSMCardSecondaryState_Type = SecondaryState
_EthernetCSMCardSecondaryState_Object = MibTableColumn
ethernetCSMCardSecondaryState = _EthernetCSMCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 4),
    _EthernetCSMCardSecondaryState_Type()
)
ethernetCSMCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCSMCardSecondaryState.setStatus("current")
_EthernetCSMCardVoltage_Type = Integer32
_EthernetCSMCardVoltage_Object = MibTableColumn
ethernetCSMCardVoltage = _EthernetCSMCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 5),
    _EthernetCSMCardVoltage_Type()
)
ethernetCSMCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCSMCardVoltage.setStatus("current")
_EthernetCSMCardTemperature_Type = Integer32
_EthernetCSMCardTemperature_Object = MibTableColumn
ethernetCSMCardTemperature = _EthernetCSMCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 6),
    _EthernetCSMCardTemperature_Type()
)
ethernetCSMCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCSMCardTemperature.setStatus("current")
_EthernetCSMCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetCSMCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetCSMCardSnmpDyingGaspEnabled = _EthernetCSMCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 7),
    _EthernetCSMCardSnmpDyingGaspEnabled_Type()
)
ethernetCSMCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCSMCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetCSMCardRestartAction_Type = RestartType
_EthernetCSMCardRestartAction_Object = MibTableColumn
ethernetCSMCardRestartAction = _EthernetCSMCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 8),
    _EthernetCSMCardRestartAction_Type()
)
ethernetCSMCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCSMCardRestartAction.setStatus("current")
_EthernetCSMCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetCSMCardFineGrainedPmInterval_Object = MibTableColumn
ethernetCSMCardFineGrainedPmInterval = _EthernetCSMCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 9),
    _EthernetCSMCardFineGrainedPmInterval_Type()
)
ethernetCSMCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCSMCardFineGrainedPmInterval.setStatus("current")


class _EthernetCSMCardOscillatorType_Type(DisplayString):
    """Custom type ethernetCSMCardOscillatorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EthernetCSMCardOscillatorType_Type.__name__ = "DisplayString"
_EthernetCSMCardOscillatorType_Object = MibTableColumn
ethernetCSMCardOscillatorType = _EthernetCSMCardOscillatorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 85, 1, 10),
    _EthernetCSMCardOscillatorType_Type()
)
ethernetCSMCardOscillatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCSMCardOscillatorType.setStatus("current")
_AuxPortCardTable_Object = MibTable
auxPortCardTable = _AuxPortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87)
)
if mibBuilder.loadTexts:
    auxPortCardTable.setStatus("current")
_AuxPortCardEntry_Object = MibTableRow
auxPortCardEntry = _AuxPortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1)
)
auxPortCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    auxPortCardEntry.setStatus("current")
_AuxPortCardEntityIndex_Type = PhysicalIndex
_AuxPortCardEntityIndex_Object = MibTableColumn
auxPortCardEntityIndex = _AuxPortCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 1),
    _AuxPortCardEntityIndex_Type()
)
auxPortCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortCardEntityIndex.setStatus("current")
_AuxPortCardAdminState_Type = AdminState
_AuxPortCardAdminState_Object = MibTableColumn
auxPortCardAdminState = _AuxPortCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 2),
    _AuxPortCardAdminState_Type()
)
auxPortCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPortCardAdminState.setStatus("current")
_AuxPortCardOperationalState_Type = OperationalState
_AuxPortCardOperationalState_Object = MibTableColumn
auxPortCardOperationalState = _AuxPortCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 3),
    _AuxPortCardOperationalState_Type()
)
auxPortCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortCardOperationalState.setStatus("current")
_AuxPortCardSecondaryState_Type = SecondaryState
_AuxPortCardSecondaryState_Object = MibTableColumn
auxPortCardSecondaryState = _AuxPortCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 4),
    _AuxPortCardSecondaryState_Type()
)
auxPortCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortCardSecondaryState.setStatus("current")
_AuxPortCardRowStatus_Type = RowStatus
_AuxPortCardRowStatus_Object = MibTableColumn
auxPortCardRowStatus = _AuxPortCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 5),
    _AuxPortCardRowStatus_Type()
)
auxPortCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxPortCardRowStatus.setStatus("current")


class _AuxPortCardAlias_Type(DisplayString):
    """Custom type auxPortCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AuxPortCardAlias_Type.__name__ = "DisplayString"
_AuxPortCardAlias_Object = MibTableColumn
auxPortCardAlias = _AuxPortCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 6),
    _AuxPortCardAlias_Type()
)
auxPortCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPortCardAlias.setStatus("current")
_AuxPortCardTemperature_Type = Integer32
_AuxPortCardTemperature_Object = MibTableColumn
auxPortCardTemperature = _AuxPortCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 87, 1, 7),
    _AuxPortCardTemperature_Type()
)
auxPortCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortCardTemperature.setStatus("current")
_EthernetNTEGE102ProHCardTable_Object = MibTable
ethernetNTEGE102ProHCardTable = _EthernetNTEGE102ProHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88)
)
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardTable.setStatus("current")
_EthernetNTEGE102ProHCardEntry_Object = MibTableRow
ethernetNTEGE102ProHCardEntry = _EthernetNTEGE102ProHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1)
)
ethernetNTEGE102ProHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardEntry.setStatus("current")
_EthernetNTEGE102ProHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE102ProHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE102ProHCardEntityIndex = _EthernetNTEGE102ProHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 1),
    _EthernetNTEGE102ProHCardEntityIndex_Type()
)
ethernetNTEGE102ProHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardEntityIndex.setStatus("current")
_EthernetNTEGE102ProHCardAdminState_Type = AdminState
_EthernetNTEGE102ProHCardAdminState_Object = MibTableColumn
ethernetNTEGE102ProHCardAdminState = _EthernetNTEGE102ProHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 2),
    _EthernetNTEGE102ProHCardAdminState_Type()
)
ethernetNTEGE102ProHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardAdminState.setStatus("current")
_EthernetNTEGE102ProHCardOperationalState_Type = OperationalState
_EthernetNTEGE102ProHCardOperationalState_Object = MibTableColumn
ethernetNTEGE102ProHCardOperationalState = _EthernetNTEGE102ProHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 3),
    _EthernetNTEGE102ProHCardOperationalState_Type()
)
ethernetNTEGE102ProHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardOperationalState.setStatus("current")
_EthernetNTEGE102ProHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE102ProHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE102ProHCardSecondaryState = _EthernetNTEGE102ProHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 4),
    _EthernetNTEGE102ProHCardSecondaryState_Type()
)
ethernetNTEGE102ProHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardSecondaryState.setStatus("current")
_EthernetNTEGE102ProHCardVoltage_Type = Integer32
_EthernetNTEGE102ProHCardVoltage_Object = MibTableColumn
ethernetNTEGE102ProHCardVoltage = _EthernetNTEGE102ProHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 5),
    _EthernetNTEGE102ProHCardVoltage_Type()
)
ethernetNTEGE102ProHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardVoltage.setStatus("current")
_EthernetNTEGE102ProHCardTemperature_Type = Integer32
_EthernetNTEGE102ProHCardTemperature_Object = MibTableColumn
ethernetNTEGE102ProHCardTemperature = _EthernetNTEGE102ProHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 6),
    _EthernetNTEGE102ProHCardTemperature_Type()
)
ethernetNTEGE102ProHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardTemperature.setStatus("current")
_EthernetNTEGE102ProHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE102ProHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE102ProHCardSnmpDyingGaspEnabled = _EthernetNTEGE102ProHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 7),
    _EthernetNTEGE102ProHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE102ProHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE102ProHCardRestartAction_Type = RestartType
_EthernetNTEGE102ProHCardRestartAction_Object = MibTableColumn
ethernetNTEGE102ProHCardRestartAction = _EthernetNTEGE102ProHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 8),
    _EthernetNTEGE102ProHCardRestartAction_Type()
)
ethernetNTEGE102ProHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardRestartAction.setStatus("current")
_EthernetNTEGE102ProHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE102ProHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE102ProHCardFineGrainedPmInterval = _EthernetNTEGE102ProHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 9),
    _EthernetNTEGE102ProHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE102ProHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE102ProHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE102ProHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE102ProHCardSwitchPortActionPort = _EthernetNTEGE102ProHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 10),
    _EthernetNTEGE102ProHCardSwitchPortActionPort_Type()
)
ethernetNTEGE102ProHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE102ProHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE102ProHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE102ProHCardSwitchPortAction = _EthernetNTEGE102ProHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 11),
    _EthernetNTEGE102ProHCardSwitchPortAction_Type()
)
ethernetNTEGE102ProHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE102ProHCardPSU1State_Type = OperationalState
_EthernetNTEGE102ProHCardPSU1State_Object = MibTableColumn
ethernetNTEGE102ProHCardPSU1State = _EthernetNTEGE102ProHCardPSU1State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 12),
    _EthernetNTEGE102ProHCardPSU1State_Type()
)
ethernetNTEGE102ProHCardPSU1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardPSU1State.setStatus("current")
_EthernetNTEGE102ProHCardPSU2State_Type = OperationalState
_EthernetNTEGE102ProHCardPSU2State_Object = MibTableColumn
ethernetNTEGE102ProHCardPSU2State = _EthernetNTEGE102ProHCardPSU2State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 13),
    _EthernetNTEGE102ProHCardPSU2State_Type()
)
ethernetNTEGE102ProHCardPSU2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardPSU2State.setStatus("current")
_EthernetNTEGE102ProHCardFAN1State_Type = OperationalState
_EthernetNTEGE102ProHCardFAN1State_Object = MibTableColumn
ethernetNTEGE102ProHCardFAN1State = _EthernetNTEGE102ProHCardFAN1State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 14),
    _EthernetNTEGE102ProHCardFAN1State_Type()
)
ethernetNTEGE102ProHCardFAN1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardFAN1State.setStatus("current")
_EthernetNTEGE102ProHCardFAN2State_Type = OperationalState
_EthernetNTEGE102ProHCardFAN2State_Object = MibTableColumn
ethernetNTEGE102ProHCardFAN2State = _EthernetNTEGE102ProHCardFAN2State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 15),
    _EthernetNTEGE102ProHCardFAN2State_Type()
)
ethernetNTEGE102ProHCardFAN2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardFAN2State.setStatus("current")
_EthernetNTEGE102ProHCardPsuType_Type = PsuType
_EthernetNTEGE102ProHCardPsuType_Object = MibTableColumn
ethernetNTEGE102ProHCardPsuType = _EthernetNTEGE102ProHCardPsuType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 88, 1, 16),
    _EthernetNTEGE102ProHCardPsuType_Type()
)
ethernetNTEGE102ProHCardPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProHCardPsuType.setStatus("current")
_EthernetNTEGE102ProEFMHCardTable_Object = MibTable
ethernetNTEGE102ProEFMHCardTable = _EthernetNTEGE102ProEFMHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89)
)
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardTable.setStatus("current")
_EthernetNTEGE102ProEFMHCardEntry_Object = MibTableRow
ethernetNTEGE102ProEFMHCardEntry = _EthernetNTEGE102ProEFMHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1)
)
ethernetNTEGE102ProEFMHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardEntry.setStatus("current")
_EthernetNTEGE102ProEFMHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE102ProEFMHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardEntityIndex = _EthernetNTEGE102ProEFMHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 1),
    _EthernetNTEGE102ProEFMHCardEntityIndex_Type()
)
ethernetNTEGE102ProEFMHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardEntityIndex.setStatus("current")
_EthernetNTEGE102ProEFMHCardAdminState_Type = AdminState
_EthernetNTEGE102ProEFMHCardAdminState_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardAdminState = _EthernetNTEGE102ProEFMHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 2),
    _EthernetNTEGE102ProEFMHCardAdminState_Type()
)
ethernetNTEGE102ProEFMHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardAdminState.setStatus("current")
_EthernetNTEGE102ProEFMHCardOperationalState_Type = OperationalState
_EthernetNTEGE102ProEFMHCardOperationalState_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardOperationalState = _EthernetNTEGE102ProEFMHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 3),
    _EthernetNTEGE102ProEFMHCardOperationalState_Type()
)
ethernetNTEGE102ProEFMHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardOperationalState.setStatus("current")
_EthernetNTEGE102ProEFMHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE102ProEFMHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardSecondaryState = _EthernetNTEGE102ProEFMHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 4),
    _EthernetNTEGE102ProEFMHCardSecondaryState_Type()
)
ethernetNTEGE102ProEFMHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardSecondaryState.setStatus("current")
_EthernetNTEGE102ProEFMHCardVoltage_Type = Integer32
_EthernetNTEGE102ProEFMHCardVoltage_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardVoltage = _EthernetNTEGE102ProEFMHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 5),
    _EthernetNTEGE102ProEFMHCardVoltage_Type()
)
ethernetNTEGE102ProEFMHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardVoltage.setStatus("current")
_EthernetNTEGE102ProEFMHCardTemperature_Type = Integer32
_EthernetNTEGE102ProEFMHCardTemperature_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardTemperature = _EthernetNTEGE102ProEFMHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 6),
    _EthernetNTEGE102ProEFMHCardTemperature_Type()
)
ethernetNTEGE102ProEFMHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardTemperature.setStatus("current")
_EthernetNTEGE102ProEFMHCardRestartAction_Type = RestartType
_EthernetNTEGE102ProEFMHCardRestartAction_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardRestartAction = _EthernetNTEGE102ProEFMHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 7),
    _EthernetNTEGE102ProEFMHCardRestartAction_Type()
)
ethernetNTEGE102ProEFMHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardRestartAction.setStatus("current")
_EthernetNTEGE102ProEFMHCardPSU1State_Type = OperationalState
_EthernetNTEGE102ProEFMHCardPSU1State_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardPSU1State = _EthernetNTEGE102ProEFMHCardPSU1State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 8),
    _EthernetNTEGE102ProEFMHCardPSU1State_Type()
)
ethernetNTEGE102ProEFMHCardPSU1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardPSU1State.setStatus("current")
_EthernetNTEGE102ProEFMHCardPSU2State_Type = OperationalState
_EthernetNTEGE102ProEFMHCardPSU2State_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardPSU2State = _EthernetNTEGE102ProEFMHCardPSU2State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 9),
    _EthernetNTEGE102ProEFMHCardPSU2State_Type()
)
ethernetNTEGE102ProEFMHCardPSU2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardPSU2State.setStatus("current")
_EthernetNTEGE102ProEFMHCardFAN1State_Type = OperationalState
_EthernetNTEGE102ProEFMHCardFAN1State_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardFAN1State = _EthernetNTEGE102ProEFMHCardFAN1State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 10),
    _EthernetNTEGE102ProEFMHCardFAN1State_Type()
)
ethernetNTEGE102ProEFMHCardFAN1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardFAN1State.setStatus("current")
_EthernetNTEGE102ProEFMHCardFAN2State_Type = OperationalState
_EthernetNTEGE102ProEFMHCardFAN2State_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardFAN2State = _EthernetNTEGE102ProEFMHCardFAN2State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 11),
    _EthernetNTEGE102ProEFMHCardFAN2State_Type()
)
ethernetNTEGE102ProEFMHCardFAN2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardFAN2State.setStatus("current")
_EthernetNTEGE102ProEFMHCardPsuType_Type = PsuType
_EthernetNTEGE102ProEFMHCardPsuType_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardPsuType = _EthernetNTEGE102ProEFMHCardPsuType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 12),
    _EthernetNTEGE102ProEFMHCardPsuType_Type()
)
ethernetNTEGE102ProEFMHCardPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardPsuType.setStatus("current")
_EthernetNTEGE102ProEFMHCardLLFMode_Type = CmCPMRLinkLossFwdMode
_EthernetNTEGE102ProEFMHCardLLFMode_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardLLFMode = _EthernetNTEGE102ProEFMHCardLLFMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 13),
    _EthernetNTEGE102ProEFMHCardLLFMode_Type()
)
ethernetNTEGE102ProEFMHCardLLFMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardLLFMode.setStatus("current")
_EthernetNTEGE102ProEFMHCardLLFModeAction_Type = CmCPMRLinkLossFwdMode
_EthernetNTEGE102ProEFMHCardLLFModeAction_Object = MibTableColumn
ethernetNTEGE102ProEFMHCardLLFModeAction = _EthernetNTEGE102ProEFMHCardLLFModeAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 89, 1, 14),
    _EthernetNTEGE102ProEFMHCardLLFModeAction_Type()
)
ethernetNTEGE102ProEFMHCardLLFModeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE102ProEFMHCardLLFModeAction.setStatus("current")
_EthernetOsa3350MgntCardTable_Object = MibTable
ethernetOsa3350MgntCardTable = _EthernetOsa3350MgntCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90)
)
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardTable.setStatus("current")
_EthernetOsa3350MgntCardEntry_Object = MibTableRow
ethernetOsa3350MgntCardEntry = _EthernetOsa3350MgntCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1)
)
ethernetOsa3350MgntCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardEntry.setStatus("current")
_EthernetOsa3350MgntCardEntityIndex_Type = PhysicalIndex
_EthernetOsa3350MgntCardEntityIndex_Object = MibTableColumn
ethernetOsa3350MgntCardEntityIndex = _EthernetOsa3350MgntCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1, 1),
    _EthernetOsa3350MgntCardEntityIndex_Type()
)
ethernetOsa3350MgntCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardEntityIndex.setStatus("current")
_EthernetOsa3350MgntCardAdminState_Type = AdminState
_EthernetOsa3350MgntCardAdminState_Object = MibTableColumn
ethernetOsa3350MgntCardAdminState = _EthernetOsa3350MgntCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1, 2),
    _EthernetOsa3350MgntCardAdminState_Type()
)
ethernetOsa3350MgntCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardAdminState.setStatus("current")
_EthernetOsa3350MgntCardOperationalState_Type = OperationalState
_EthernetOsa3350MgntCardOperationalState_Object = MibTableColumn
ethernetOsa3350MgntCardOperationalState = _EthernetOsa3350MgntCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1, 3),
    _EthernetOsa3350MgntCardOperationalState_Type()
)
ethernetOsa3350MgntCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardOperationalState.setStatus("current")
_EthernetOsa3350MgntCardSecondaryState_Type = SecondaryState
_EthernetOsa3350MgntCardSecondaryState_Object = MibTableColumn
ethernetOsa3350MgntCardSecondaryState = _EthernetOsa3350MgntCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1, 4),
    _EthernetOsa3350MgntCardSecondaryState_Type()
)
ethernetOsa3350MgntCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardSecondaryState.setStatus("current")
_EthernetOsa3350MgntCardRestartAction_Type = RestartType
_EthernetOsa3350MgntCardRestartAction_Object = MibTableColumn
ethernetOsa3350MgntCardRestartAction = _EthernetOsa3350MgntCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1, 5),
    _EthernetOsa3350MgntCardRestartAction_Type()
)
ethernetOsa3350MgntCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardRestartAction.setStatus("current")
_EthernetOsa3350MgntCardResyncAction_Type = ResyncType
_EthernetOsa3350MgntCardResyncAction_Object = MibTableColumn
ethernetOsa3350MgntCardResyncAction = _EthernetOsa3350MgntCardResyncAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 90, 1, 6),
    _EthernetOsa3350MgntCardResyncAction_Type()
)
ethernetOsa3350MgntCardResyncAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardResyncAction.setStatus("current")
_EthernetNTEXG116PROHCardTable_Object = MibTable
ethernetNTEXG116PROHCardTable = _EthernetNTEXG116PROHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91)
)
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardTable.setStatus("current")
_EthernetNTEXG116PROHCardEntry_Object = MibTableRow
ethernetNTEXG116PROHCardEntry = _EthernetNTEXG116PROHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1)
)
ethernetNTEXG116PROHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardEntry.setStatus("current")
_EthernetNTEXG116PROHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG116PROHCardEntityIndex_Object = MibTableColumn
ethernetNTEXG116PROHCardEntityIndex = _EthernetNTEXG116PROHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 1),
    _EthernetNTEXG116PROHCardEntityIndex_Type()
)
ethernetNTEXG116PROHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardEntityIndex.setStatus("current")
_EthernetNTEXG116PROHCardAdminState_Type = AdminState
_EthernetNTEXG116PROHCardAdminState_Object = MibTableColumn
ethernetNTEXG116PROHCardAdminState = _EthernetNTEXG116PROHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 2),
    _EthernetNTEXG116PROHCardAdminState_Type()
)
ethernetNTEXG116PROHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardAdminState.setStatus("current")
_EthernetNTEXG116PROHCardOperationalState_Type = OperationalState
_EthernetNTEXG116PROHCardOperationalState_Object = MibTableColumn
ethernetNTEXG116PROHCardOperationalState = _EthernetNTEXG116PROHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 3),
    _EthernetNTEXG116PROHCardOperationalState_Type()
)
ethernetNTEXG116PROHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardOperationalState.setStatus("current")
_EthernetNTEXG116PROHCardSecondaryState_Type = SecondaryState
_EthernetNTEXG116PROHCardSecondaryState_Object = MibTableColumn
ethernetNTEXG116PROHCardSecondaryState = _EthernetNTEXG116PROHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 4),
    _EthernetNTEXG116PROHCardSecondaryState_Type()
)
ethernetNTEXG116PROHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardSecondaryState.setStatus("current")
_EthernetNTEXG116PROHCardVoltage_Type = Integer32
_EthernetNTEXG116PROHCardVoltage_Object = MibTableColumn
ethernetNTEXG116PROHCardVoltage = _EthernetNTEXG116PROHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 5),
    _EthernetNTEXG116PROHCardVoltage_Type()
)
ethernetNTEXG116PROHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardVoltage.setStatus("current")
_EthernetNTEXG116PROHCardTemperature_Type = Integer32
_EthernetNTEXG116PROHCardTemperature_Object = MibTableColumn
ethernetNTEXG116PROHCardTemperature = _EthernetNTEXG116PROHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 6),
    _EthernetNTEXG116PROHCardTemperature_Type()
)
ethernetNTEXG116PROHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardTemperature.setStatus("current")
_EthernetNTEXG116PROHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG116PROHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG116PROHCardSnmpDyingGaspEnabled = _EthernetNTEXG116PROHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 7),
    _EthernetNTEXG116PROHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG116PROHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG116PROHCardRestartAction_Type = RestartType
_EthernetNTEXG116PROHCardRestartAction_Object = MibTableColumn
ethernetNTEXG116PROHCardRestartAction = _EthernetNTEXG116PROHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 8),
    _EthernetNTEXG116PROHCardRestartAction_Type()
)
ethernetNTEXG116PROHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardRestartAction.setStatus("current")
_EthernetNTEXG116PROHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG116PROHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG116PROHCardFineGrainedPmInterval = _EthernetNTEXG116PROHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 91, 1, 9),
    _EthernetNTEXG116PROHCardFineGrainedPmInterval_Type()
)
ethernetNTEXG116PROHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG116PROHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGO102ProSMCardTable_Object = MibTable
ethernetNTEGO102ProSMCardTable = _EthernetNTEGO102ProSMCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92)
)
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardTable.setStatus("current")
_EthernetNTEGO102ProSMCardEntry_Object = MibTableRow
ethernetNTEGO102ProSMCardEntry = _EthernetNTEGO102ProSMCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1)
)
ethernetNTEGO102ProSMCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardEntry.setStatus("current")
_EthernetNTEGO102ProSMCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGO102ProSMCardEntityIndex_Object = MibTableColumn
ethernetNTEGO102ProSMCardEntityIndex = _EthernetNTEGO102ProSMCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 1),
    _EthernetNTEGO102ProSMCardEntityIndex_Type()
)
ethernetNTEGO102ProSMCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardEntityIndex.setStatus("current")
_EthernetNTEGO102ProSMCardAdminState_Type = AdminState
_EthernetNTEGO102ProSMCardAdminState_Object = MibTableColumn
ethernetNTEGO102ProSMCardAdminState = _EthernetNTEGO102ProSMCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 2),
    _EthernetNTEGO102ProSMCardAdminState_Type()
)
ethernetNTEGO102ProSMCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardAdminState.setStatus("current")
_EthernetNTEGO102ProSMCardOperationalState_Type = OperationalState
_EthernetNTEGO102ProSMCardOperationalState_Object = MibTableColumn
ethernetNTEGO102ProSMCardOperationalState = _EthernetNTEGO102ProSMCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 3),
    _EthernetNTEGO102ProSMCardOperationalState_Type()
)
ethernetNTEGO102ProSMCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardOperationalState.setStatus("current")
_EthernetNTEGO102ProSMCardSecondaryState_Type = SecondaryState
_EthernetNTEGO102ProSMCardSecondaryState_Object = MibTableColumn
ethernetNTEGO102ProSMCardSecondaryState = _EthernetNTEGO102ProSMCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 4),
    _EthernetNTEGO102ProSMCardSecondaryState_Type()
)
ethernetNTEGO102ProSMCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardSecondaryState.setStatus("current")
_EthernetNTEGO102ProSMCardVoltage_Type = Integer32
_EthernetNTEGO102ProSMCardVoltage_Object = MibTableColumn
ethernetNTEGO102ProSMCardVoltage = _EthernetNTEGO102ProSMCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 5),
    _EthernetNTEGO102ProSMCardVoltage_Type()
)
ethernetNTEGO102ProSMCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardVoltage.setStatus("current")
_EthernetNTEGO102ProSMCardTemperature_Type = Integer32
_EthernetNTEGO102ProSMCardTemperature_Object = MibTableColumn
ethernetNTEGO102ProSMCardTemperature = _EthernetNTEGO102ProSMCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 6),
    _EthernetNTEGO102ProSMCardTemperature_Type()
)
ethernetNTEGO102ProSMCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardTemperature.setStatus("current")
_EthernetNTEGO102ProSMCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGO102ProSMCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGO102ProSMCardSnmpDyingGaspEnabled = _EthernetNTEGO102ProSMCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 7),
    _EthernetNTEGO102ProSMCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGO102ProSMCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGO102ProSMCardRestartAction_Type = RestartType
_EthernetNTEGO102ProSMCardRestartAction_Object = MibTableColumn
ethernetNTEGO102ProSMCardRestartAction = _EthernetNTEGO102ProSMCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 8),
    _EthernetNTEGO102ProSMCardRestartAction_Type()
)
ethernetNTEGO102ProSMCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardRestartAction.setStatus("current")
_EthernetNTEGO102ProSMCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGO102ProSMCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGO102ProSMCardFineGrainedPmInterval = _EthernetNTEGO102ProSMCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 9),
    _EthernetNTEGO102ProSMCardFineGrainedPmInterval_Type()
)
ethernetNTEGO102ProSMCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGO102ProSMCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGO102ProSMCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGO102ProSMCardSwitchPortActionPort = _EthernetNTEGO102ProSMCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 10),
    _EthernetNTEGO102ProSMCardSwitchPortActionPort_Type()
)
ethernetNTEGO102ProSMCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGO102ProSMCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGO102ProSMCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGO102ProSMCardSwitchPortAction = _EthernetNTEGO102ProSMCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 92, 1, 11),
    _EthernetNTEGO102ProSMCardSwitchPortAction_Type()
)
ethernetNTEGO102ProSMCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGO102ProSMCardSwitchPortAction.setStatus("current")
_EthernetNTEXG118PROSHCardTable_Object = MibTable
ethernetNTEXG118PROSHCardTable = _EthernetNTEXG118PROSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93)
)
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardTable.setStatus("current")
_EthernetNTEXG118PROSHCardEntry_Object = MibTableRow
ethernetNTEXG118PROSHCardEntry = _EthernetNTEXG118PROSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1)
)
ethernetNTEXG118PROSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardEntry.setStatus("current")
_EthernetNTEXG118PROSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG118PROSHCardEntityIndex_Object = MibTableColumn
ethernetNTEXG118PROSHCardEntityIndex = _EthernetNTEXG118PROSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 1),
    _EthernetNTEXG118PROSHCardEntityIndex_Type()
)
ethernetNTEXG118PROSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardEntityIndex.setStatus("current")
_EthernetNTEXG118PROSHCardAdminState_Type = AdminState
_EthernetNTEXG118PROSHCardAdminState_Object = MibTableColumn
ethernetNTEXG118PROSHCardAdminState = _EthernetNTEXG118PROSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 2),
    _EthernetNTEXG118PROSHCardAdminState_Type()
)
ethernetNTEXG118PROSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardAdminState.setStatus("current")
_EthernetNTEXG118PROSHCardOperationalState_Type = OperationalState
_EthernetNTEXG118PROSHCardOperationalState_Object = MibTableColumn
ethernetNTEXG118PROSHCardOperationalState = _EthernetNTEXG118PROSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 3),
    _EthernetNTEXG118PROSHCardOperationalState_Type()
)
ethernetNTEXG118PROSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardOperationalState.setStatus("current")
_EthernetNTEXG118PROSHCardSecondaryState_Type = SecondaryState
_EthernetNTEXG118PROSHCardSecondaryState_Object = MibTableColumn
ethernetNTEXG118PROSHCardSecondaryState = _EthernetNTEXG118PROSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 4),
    _EthernetNTEXG118PROSHCardSecondaryState_Type()
)
ethernetNTEXG118PROSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardSecondaryState.setStatus("current")
_EthernetNTEXG118PROSHCardVoltage_Type = Integer32
_EthernetNTEXG118PROSHCardVoltage_Object = MibTableColumn
ethernetNTEXG118PROSHCardVoltage = _EthernetNTEXG118PROSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 5),
    _EthernetNTEXG118PROSHCardVoltage_Type()
)
ethernetNTEXG118PROSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardVoltage.setStatus("current")
_EthernetNTEXG118PROSHCardTemperature_Type = Integer32
_EthernetNTEXG118PROSHCardTemperature_Object = MibTableColumn
ethernetNTEXG118PROSHCardTemperature = _EthernetNTEXG118PROSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 6),
    _EthernetNTEXG118PROSHCardTemperature_Type()
)
ethernetNTEXG118PROSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardTemperature.setStatus("current")
_EthernetNTEXG118PROSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG118PROSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG118PROSHCardSnmpDyingGaspEnabled = _EthernetNTEXG118PROSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 7),
    _EthernetNTEXG118PROSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG118PROSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG118PROSHCardRestartAction_Type = RestartType
_EthernetNTEXG118PROSHCardRestartAction_Object = MibTableColumn
ethernetNTEXG118PROSHCardRestartAction = _EthernetNTEXG118PROSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 8),
    _EthernetNTEXG118PROSHCardRestartAction_Type()
)
ethernetNTEXG118PROSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardRestartAction.setStatus("current")
_EthernetNTEXG118PROSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG118PROSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG118PROSHCardFineGrainedPmInterval = _EthernetNTEXG118PROSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 93, 1, 9),
    _EthernetNTEXG118PROSHCardFineGrainedPmInterval_Type()
)
ethernetNTEXG118PROSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROSHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEXG118PROACSHCardTable_Object = MibTable
ethernetNTEXG118PROACSHCardTable = _EthernetNTEXG118PROACSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94)
)
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardTable.setStatus("current")
_EthernetNTEXG118PROACSHCardEntry_Object = MibTableRow
ethernetNTEXG118PROACSHCardEntry = _EthernetNTEXG118PROACSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1)
)
ethernetNTEXG118PROACSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardEntry.setStatus("current")
_EthernetNTEXG118PROACSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG118PROACSHCardEntityIndex_Object = MibTableColumn
ethernetNTEXG118PROACSHCardEntityIndex = _EthernetNTEXG118PROACSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 1),
    _EthernetNTEXG118PROACSHCardEntityIndex_Type()
)
ethernetNTEXG118PROACSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardEntityIndex.setStatus("current")
_EthernetNTEXG118PROACSHCardAdminState_Type = AdminState
_EthernetNTEXG118PROACSHCardAdminState_Object = MibTableColumn
ethernetNTEXG118PROACSHCardAdminState = _EthernetNTEXG118PROACSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 2),
    _EthernetNTEXG118PROACSHCardAdminState_Type()
)
ethernetNTEXG118PROACSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardAdminState.setStatus("current")
_EthernetNTEXG118PROACSHCardOperationalState_Type = OperationalState
_EthernetNTEXG118PROACSHCardOperationalState_Object = MibTableColumn
ethernetNTEXG118PROACSHCardOperationalState = _EthernetNTEXG118PROACSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 3),
    _EthernetNTEXG118PROACSHCardOperationalState_Type()
)
ethernetNTEXG118PROACSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardOperationalState.setStatus("current")
_EthernetNTEXG118PROACSHCardSecondaryState_Type = SecondaryState
_EthernetNTEXG118PROACSHCardSecondaryState_Object = MibTableColumn
ethernetNTEXG118PROACSHCardSecondaryState = _EthernetNTEXG118PROACSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 4),
    _EthernetNTEXG118PROACSHCardSecondaryState_Type()
)
ethernetNTEXG118PROACSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardSecondaryState.setStatus("current")
_EthernetNTEXG118PROACSHCardVoltage_Type = Integer32
_EthernetNTEXG118PROACSHCardVoltage_Object = MibTableColumn
ethernetNTEXG118PROACSHCardVoltage = _EthernetNTEXG118PROACSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 5),
    _EthernetNTEXG118PROACSHCardVoltage_Type()
)
ethernetNTEXG118PROACSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardVoltage.setStatus("current")
_EthernetNTEXG118PROACSHCardTemperature_Type = Integer32
_EthernetNTEXG118PROACSHCardTemperature_Object = MibTableColumn
ethernetNTEXG118PROACSHCardTemperature = _EthernetNTEXG118PROACSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 6),
    _EthernetNTEXG118PROACSHCardTemperature_Type()
)
ethernetNTEXG118PROACSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardTemperature.setStatus("current")
_EthernetNTEXG118PROACSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG118PROACSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG118PROACSHCardSnmpDyingGaspEnabled = _EthernetNTEXG118PROACSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 7),
    _EthernetNTEXG118PROACSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG118PROACSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG118PROACSHCardRestartAction_Type = RestartType
_EthernetNTEXG118PROACSHCardRestartAction_Object = MibTableColumn
ethernetNTEXG118PROACSHCardRestartAction = _EthernetNTEXG118PROACSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 8),
    _EthernetNTEXG118PROACSHCardRestartAction_Type()
)
ethernetNTEXG118PROACSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardRestartAction.setStatus("current")
_EthernetNTEXG118PROACSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG118PROACSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG118PROACSHCardFineGrainedPmInterval = _EthernetNTEXG118PROACSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 94, 1, 9),
    _EthernetNTEXG118PROACSHCardFineGrainedPmInterval_Type()
)
ethernetNTEXG118PROACSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG118PROACSHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProVmSHCardTable_Object = MibTable
ethernetNTEGE114ProVmSHCardTable = _EthernetNTEGE114ProVmSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95)
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardTable.setStatus("current")
_EthernetNTEGE114ProVmSHCardEntry_Object = MibTableRow
ethernetNTEGE114ProVmSHCardEntry = _EthernetNTEGE114ProVmSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1)
)
ethernetNTEGE114ProVmSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardEntry.setStatus("current")
_EthernetNTEGE114ProVmSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE114ProVmSHCardEntityIndex_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardEntityIndex = _EthernetNTEGE114ProVmSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 1),
    _EthernetNTEGE114ProVmSHCardEntityIndex_Type()
)
ethernetNTEGE114ProVmSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardEntityIndex.setStatus("current")
_EthernetNTEGE114ProVmSHCardAdminState_Type = AdminState
_EthernetNTEGE114ProVmSHCardAdminState_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardAdminState = _EthernetNTEGE114ProVmSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 2),
    _EthernetNTEGE114ProVmSHCardAdminState_Type()
)
ethernetNTEGE114ProVmSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardAdminState.setStatus("current")
_EthernetNTEGE114ProVmSHCardOperationalState_Type = OperationalState
_EthernetNTEGE114ProVmSHCardOperationalState_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardOperationalState = _EthernetNTEGE114ProVmSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 3),
    _EthernetNTEGE114ProVmSHCardOperationalState_Type()
)
ethernetNTEGE114ProVmSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardOperationalState.setStatus("current")
_EthernetNTEGE114ProVmSHCardSecondaryState_Type = SecondaryState
_EthernetNTEGE114ProVmSHCardSecondaryState_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardSecondaryState = _EthernetNTEGE114ProVmSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 4),
    _EthernetNTEGE114ProVmSHCardSecondaryState_Type()
)
ethernetNTEGE114ProVmSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardSecondaryState.setStatus("current")
_EthernetNTEGE114ProVmSHCardVoltage_Type = Integer32
_EthernetNTEGE114ProVmSHCardVoltage_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardVoltage = _EthernetNTEGE114ProVmSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 5),
    _EthernetNTEGE114ProVmSHCardVoltage_Type()
)
ethernetNTEGE114ProVmSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardVoltage.setStatus("current")
_EthernetNTEGE114ProVmSHCardTemperature_Type = Integer32
_EthernetNTEGE114ProVmSHCardTemperature_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardTemperature = _EthernetNTEGE114ProVmSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 6),
    _EthernetNTEGE114ProVmSHCardTemperature_Type()
)
ethernetNTEGE114ProVmSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardTemperature.setStatus("current")
_EthernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled = _EthernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 7),
    _EthernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE114ProVmSHCardRestartAction_Type = RestartType
_EthernetNTEGE114ProVmSHCardRestartAction_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardRestartAction = _EthernetNTEGE114ProVmSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 8),
    _EthernetNTEGE114ProVmSHCardRestartAction_Type()
)
ethernetNTEGE114ProVmSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardRestartAction.setStatus("current")
_EthernetNTEGE114ProVmSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE114ProVmSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardFineGrainedPmInterval = _EthernetNTEGE114ProVmSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 9),
    _EthernetNTEGE114ProVmSHCardFineGrainedPmInterval_Type()
)
ethernetNTEGE114ProVmSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE114ProVmSHCardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE114ProVmSHCardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardSwitchPortActionPort = _EthernetNTEGE114ProVmSHCardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 10),
    _EthernetNTEGE114ProVmSHCardSwitchPortActionPort_Type()
)
ethernetNTEGE114ProVmSHCardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE114ProVmSHCardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE114ProVmSHCardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE114ProVmSHCardSwitchPortAction = _EthernetNTEGE114ProVmSHCardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 95, 1, 11),
    _EthernetNTEGE114ProVmSHCardSwitchPortAction_Type()
)
ethernetNTEGE114ProVmSHCardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE114ProVmSHCardSwitchPortAction.setStatus("current")
_EthernetNTEGE104CardTable_Object = MibTable
ethernetNTEGE104CardTable = _EthernetNTEGE104CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96)
)
if mibBuilder.loadTexts:
    ethernetNTEGE104CardTable.setStatus("current")
_EthernetNTEGE104CardEntry_Object = MibTableRow
ethernetNTEGE104CardEntry = _EthernetNTEGE104CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1)
)
ethernetNTEGE104CardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEGE104CardEntry.setStatus("current")
_EthernetNTEGE104CardEntityIndex_Type = PhysicalIndex
_EthernetNTEGE104CardEntityIndex_Object = MibTableColumn
ethernetNTEGE104CardEntityIndex = _EthernetNTEGE104CardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 1),
    _EthernetNTEGE104CardEntityIndex_Type()
)
ethernetNTEGE104CardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardEntityIndex.setStatus("current")
_EthernetNTEGE104CardAdminState_Type = AdminState
_EthernetNTEGE104CardAdminState_Object = MibTableColumn
ethernetNTEGE104CardAdminState = _EthernetNTEGE104CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 2),
    _EthernetNTEGE104CardAdminState_Type()
)
ethernetNTEGE104CardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardAdminState.setStatus("current")
_EthernetNTEGE104CardOperationalState_Type = OperationalState
_EthernetNTEGE104CardOperationalState_Object = MibTableColumn
ethernetNTEGE104CardOperationalState = _EthernetNTEGE104CardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 3),
    _EthernetNTEGE104CardOperationalState_Type()
)
ethernetNTEGE104CardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardOperationalState.setStatus("current")
_EthernetNTEGE104CardSecondaryState_Type = SecondaryState
_EthernetNTEGE104CardSecondaryState_Object = MibTableColumn
ethernetNTEGE104CardSecondaryState = _EthernetNTEGE104CardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 4),
    _EthernetNTEGE104CardSecondaryState_Type()
)
ethernetNTEGE104CardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardSecondaryState.setStatus("current")
_EthernetNTEGE104CardVoltage_Type = Integer32
_EthernetNTEGE104CardVoltage_Object = MibTableColumn
ethernetNTEGE104CardVoltage = _EthernetNTEGE104CardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 5),
    _EthernetNTEGE104CardVoltage_Type()
)
ethernetNTEGE104CardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardVoltage.setStatus("current")
_EthernetNTEGE104CardTemperature_Type = Integer32
_EthernetNTEGE104CardTemperature_Object = MibTableColumn
ethernetNTEGE104CardTemperature = _EthernetNTEGE104CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 6),
    _EthernetNTEGE104CardTemperature_Type()
)
ethernetNTEGE104CardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardTemperature.setStatus("current")
_EthernetNTEGE104CardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEGE104CardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEGE104CardSnmpDyingGaspEnabled = _EthernetNTEGE104CardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 7),
    _EthernetNTEGE104CardSnmpDyingGaspEnabled_Type()
)
ethernetNTEGE104CardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEGE104CardRestartAction_Type = RestartType
_EthernetNTEGE104CardRestartAction_Object = MibTableColumn
ethernetNTEGE104CardRestartAction = _EthernetNTEGE104CardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 8),
    _EthernetNTEGE104CardRestartAction_Type()
)
ethernetNTEGE104CardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardRestartAction.setStatus("current")
_EthernetNTEGE104CardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEGE104CardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEGE104CardFineGrainedPmInterval = _EthernetNTEGE104CardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 9),
    _EthernetNTEGE104CardFineGrainedPmInterval_Type()
)
ethernetNTEGE104CardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardFineGrainedPmInterval.setStatus("current")
_EthernetNTEGE104CardSwitchPortActionPort_Type = VariablePointer
_EthernetNTEGE104CardSwitchPortActionPort_Object = MibTableColumn
ethernetNTEGE104CardSwitchPortActionPort = _EthernetNTEGE104CardSwitchPortActionPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 10),
    _EthernetNTEGE104CardSwitchPortActionPort_Type()
)
ethernetNTEGE104CardSwitchPortActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardSwitchPortActionPort.setStatus("current")
_EthernetNTEGE104CardSwitchPortAction_Type = SwitchPortAction
_EthernetNTEGE104CardSwitchPortAction_Object = MibTableColumn
ethernetNTEGE104CardSwitchPortAction = _EthernetNTEGE104CardSwitchPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 96, 1, 11),
    _EthernetNTEGE104CardSwitchPortAction_Type()
)
ethernetNTEGE104CardSwitchPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEGE104CardSwitchPortAction.setStatus("current")
_EthernetNTEXG120PROSHCardTable_Object = MibTable
ethernetNTEXG120PROSHCardTable = _EthernetNTEXG120PROSHCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97)
)
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardTable.setStatus("current")
_EthernetNTEXG120PROSHCardEntry_Object = MibTableRow
ethernetNTEXG120PROSHCardEntry = _EthernetNTEXG120PROSHCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1)
)
ethernetNTEXG120PROSHCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardEntry.setStatus("current")
_EthernetNTEXG120PROSHCardEntityIndex_Type = PhysicalIndex
_EthernetNTEXG120PROSHCardEntityIndex_Object = MibTableColumn
ethernetNTEXG120PROSHCardEntityIndex = _EthernetNTEXG120PROSHCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 1),
    _EthernetNTEXG120PROSHCardEntityIndex_Type()
)
ethernetNTEXG120PROSHCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardEntityIndex.setStatus("current")
_EthernetNTEXG120PROSHCardAdminState_Type = AdminState
_EthernetNTEXG120PROSHCardAdminState_Object = MibTableColumn
ethernetNTEXG120PROSHCardAdminState = _EthernetNTEXG120PROSHCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 2),
    _EthernetNTEXG120PROSHCardAdminState_Type()
)
ethernetNTEXG120PROSHCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardAdminState.setStatus("current")
_EthernetNTEXG120PROSHCardOperationalState_Type = OperationalState
_EthernetNTEXG120PROSHCardOperationalState_Object = MibTableColumn
ethernetNTEXG120PROSHCardOperationalState = _EthernetNTEXG120PROSHCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 3),
    _EthernetNTEXG120PROSHCardOperationalState_Type()
)
ethernetNTEXG120PROSHCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardOperationalState.setStatus("current")
_EthernetNTEXG120PROSHCardSecondaryState_Type = SecondaryState
_EthernetNTEXG120PROSHCardSecondaryState_Object = MibTableColumn
ethernetNTEXG120PROSHCardSecondaryState = _EthernetNTEXG120PROSHCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 4),
    _EthernetNTEXG120PROSHCardSecondaryState_Type()
)
ethernetNTEXG120PROSHCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardSecondaryState.setStatus("current")
_EthernetNTEXG120PROSHCardVoltage_Type = Integer32
_EthernetNTEXG120PROSHCardVoltage_Object = MibTableColumn
ethernetNTEXG120PROSHCardVoltage = _EthernetNTEXG120PROSHCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 5),
    _EthernetNTEXG120PROSHCardVoltage_Type()
)
ethernetNTEXG120PROSHCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardVoltage.setStatus("current")
_EthernetNTEXG120PROSHCardTemperature_Type = Integer32
_EthernetNTEXG120PROSHCardTemperature_Object = MibTableColumn
ethernetNTEXG120PROSHCardTemperature = _EthernetNTEXG120PROSHCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 6),
    _EthernetNTEXG120PROSHCardTemperature_Type()
)
ethernetNTEXG120PROSHCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardTemperature.setStatus("current")
_EthernetNTEXG120PROSHCardSnmpDyingGaspEnabled_Type = TruthValue
_EthernetNTEXG120PROSHCardSnmpDyingGaspEnabled_Object = MibTableColumn
ethernetNTEXG120PROSHCardSnmpDyingGaspEnabled = _EthernetNTEXG120PROSHCardSnmpDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 7),
    _EthernetNTEXG120PROSHCardSnmpDyingGaspEnabled_Type()
)
ethernetNTEXG120PROSHCardSnmpDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardSnmpDyingGaspEnabled.setStatus("current")
_EthernetNTEXG120PROSHCardRestartAction_Type = RestartType
_EthernetNTEXG120PROSHCardRestartAction_Object = MibTableColumn
ethernetNTEXG120PROSHCardRestartAction = _EthernetNTEXG120PROSHCardRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 8),
    _EthernetNTEXG120PROSHCardRestartAction_Type()
)
ethernetNTEXG120PROSHCardRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardRestartAction.setStatus("current")
_EthernetNTEXG120PROSHCardFineGrainedPmInterval_Type = CmPmIntervalType
_EthernetNTEXG120PROSHCardFineGrainedPmInterval_Object = MibTableColumn
ethernetNTEXG120PROSHCardFineGrainedPmInterval = _EthernetNTEXG120PROSHCardFineGrainedPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 97, 1, 9),
    _EthernetNTEXG120PROSHCardFineGrainedPmInterval_Type()
)
ethernetNTEXG120PROSHCardFineGrainedPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNTEXG120PROSHCardFineGrainedPmInterval.setStatus("current")
_MbGnssCardTable_Object = MibTable
mbGnssCardTable = _MbGnssCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98)
)
if mibBuilder.loadTexts:
    mbGnssCardTable.setStatus("current")
_MbGnssCardEntry_Object = MibTableRow
mbGnssCardEntry = _MbGnssCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1)
)
mbGnssCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    mbGnssCardEntry.setStatus("current")
_MbGnssCardEntityIndex_Type = PhysicalIndex
_MbGnssCardEntityIndex_Object = MibTableColumn
mbGnssCardEntityIndex = _MbGnssCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1, 1),
    _MbGnssCardEntityIndex_Type()
)
mbGnssCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbGnssCardEntityIndex.setStatus("current")
_MbGnssCardAdminState_Type = AdminState
_MbGnssCardAdminState_Object = MibTableColumn
mbGnssCardAdminState = _MbGnssCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1, 2),
    _MbGnssCardAdminState_Type()
)
mbGnssCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbGnssCardAdminState.setStatus("current")
_MbGnssCardOperationalState_Type = OperationalState
_MbGnssCardOperationalState_Object = MibTableColumn
mbGnssCardOperationalState = _MbGnssCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1, 3),
    _MbGnssCardOperationalState_Type()
)
mbGnssCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbGnssCardOperationalState.setStatus("current")
_MbGnssCardSecondaryState_Type = SecondaryState
_MbGnssCardSecondaryState_Object = MibTableColumn
mbGnssCardSecondaryState = _MbGnssCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1, 4),
    _MbGnssCardSecondaryState_Type()
)
mbGnssCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbGnssCardSecondaryState.setStatus("current")
_MbGnssCardRowStatus_Type = RowStatus
_MbGnssCardRowStatus_Object = MibTableColumn
mbGnssCardRowStatus = _MbGnssCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1, 5),
    _MbGnssCardRowStatus_Type()
)
mbGnssCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbGnssCardRowStatus.setStatus("current")


class _MbGnssCardAlias_Type(DisplayString):
    """Custom type mbGnssCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MbGnssCardAlias_Type.__name__ = "DisplayString"
_MbGnssCardAlias_Object = MibTableColumn
mbGnssCardAlias = _MbGnssCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 98, 1, 6),
    _MbGnssCardAlias_Type()
)
mbGnssCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbGnssCardAlias.setStatus("current")
_F3IrigCardTable_Object = MibTable
f3IrigCardTable = _F3IrigCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99)
)
if mibBuilder.loadTexts:
    f3IrigCardTable.setStatus("current")
_F3IrigCardEntry_Object = MibTableRow
f3IrigCardEntry = _F3IrigCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1)
)
f3IrigCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    f3IrigCardEntry.setStatus("current")
_F3IrigCardEntityIndex_Type = PhysicalIndex
_F3IrigCardEntityIndex_Object = MibTableColumn
f3IrigCardEntityIndex = _F3IrigCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 1),
    _F3IrigCardEntityIndex_Type()
)
f3IrigCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3IrigCardEntityIndex.setStatus("current")


class _F3IrigCardAlias_Type(DisplayString):
    """Custom type f3IrigCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3IrigCardAlias_Type.__name__ = "DisplayString"
_F3IrigCardAlias_Object = MibTableColumn
f3IrigCardAlias = _F3IrigCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 2),
    _F3IrigCardAlias_Type()
)
f3IrigCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IrigCardAlias.setStatus("current")
_F3IrigCardAdminState_Type = AdminState
_F3IrigCardAdminState_Object = MibTableColumn
f3IrigCardAdminState = _F3IrigCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 3),
    _F3IrigCardAdminState_Type()
)
f3IrigCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IrigCardAdminState.setStatus("current")
_F3IrigCardOperationalState_Type = OperationalState
_F3IrigCardOperationalState_Object = MibTableColumn
f3IrigCardOperationalState = _F3IrigCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 4),
    _F3IrigCardOperationalState_Type()
)
f3IrigCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3IrigCardOperationalState.setStatus("current")
_F3IrigCardSecondaryState_Type = SecondaryState
_F3IrigCardSecondaryState_Object = MibTableColumn
f3IrigCardSecondaryState = _F3IrigCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 5),
    _F3IrigCardSecondaryState_Type()
)
f3IrigCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3IrigCardSecondaryState.setStatus("current")
_F3IrigCardTemperature_Type = Integer32
_F3IrigCardTemperature_Object = MibTableColumn
f3IrigCardTemperature = _F3IrigCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 6),
    _F3IrigCardTemperature_Type()
)
f3IrigCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3IrigCardTemperature.setStatus("current")
_F3IrigCardStorageType_Type = StorageType
_F3IrigCardStorageType_Object = MibTableColumn
f3IrigCardStorageType = _F3IrigCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 7),
    _F3IrigCardStorageType_Type()
)
f3IrigCardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IrigCardStorageType.setStatus("current")
_F3IrigCardRowStatus_Type = RowStatus
_F3IrigCardRowStatus_Object = MibTableColumn
f3IrigCardRowStatus = _F3IrigCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 99, 1, 8),
    _F3IrigCardRowStatus_Type()
)
f3IrigCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IrigCardRowStatus.setStatus("current")
_CompositeClockCardTable_Object = MibTable
compositeClockCardTable = _CompositeClockCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100)
)
if mibBuilder.loadTexts:
    compositeClockCardTable.setStatus("current")
_CompositeClockCardEntry_Object = MibTableRow
compositeClockCardEntry = _CompositeClockCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1)
)
compositeClockCardEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    compositeClockCardEntry.setStatus("current")
_CompositeClockCardEntityIndex_Type = PhysicalIndex
_CompositeClockCardEntityIndex_Object = MibTableColumn
compositeClockCardEntityIndex = _CompositeClockCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1, 1),
    _CompositeClockCardEntityIndex_Type()
)
compositeClockCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compositeClockCardEntityIndex.setStatus("current")
_CompositeClockCardAdminState_Type = AdminState
_CompositeClockCardAdminState_Object = MibTableColumn
compositeClockCardAdminState = _CompositeClockCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1, 2),
    _CompositeClockCardAdminState_Type()
)
compositeClockCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compositeClockCardAdminState.setStatus("current")
_CompositeClockCardOperationalState_Type = OperationalState
_CompositeClockCardOperationalState_Object = MibTableColumn
compositeClockCardOperationalState = _CompositeClockCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1, 3),
    _CompositeClockCardOperationalState_Type()
)
compositeClockCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compositeClockCardOperationalState.setStatus("current")
_CompositeClockCardSecondaryState_Type = SecondaryState
_CompositeClockCardSecondaryState_Object = MibTableColumn
compositeClockCardSecondaryState = _CompositeClockCardSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1, 4),
    _CompositeClockCardSecondaryState_Type()
)
compositeClockCardSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compositeClockCardSecondaryState.setStatus("current")
_CompositeClockCardRowStatus_Type = RowStatus
_CompositeClockCardRowStatus_Object = MibTableColumn
compositeClockCardRowStatus = _CompositeClockCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1, 5),
    _CompositeClockCardRowStatus_Type()
)
compositeClockCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    compositeClockCardRowStatus.setStatus("current")


class _CompositeClockCardAlias_Type(DisplayString):
    """Custom type compositeClockCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CompositeClockCardAlias_Type.__name__ = "DisplayString"
_CompositeClockCardAlias_Object = MibTableColumn
compositeClockCardAlias = _CompositeClockCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 100, 1, 6),
    _CompositeClockCardAlias_Type()
)
compositeClockCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compositeClockCardAlias.setStatus("current")
_F3StorageDeviceTable_Object = MibTable
f3StorageDeviceTable = _F3StorageDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 101)
)
if mibBuilder.loadTexts:
    f3StorageDeviceTable.setStatus("current")
_F3StorageDeviceEntry_Object = MibTableRow
f3StorageDeviceEntry = _F3StorageDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 101, 1)
)
if mibBuilder.loadTexts:
    f3StorageDeviceEntry.setStatus("current")
_F3StorageDeviceInternalSsdHealth_Type = TruthValue
_F3StorageDeviceInternalSsdHealth_Object = MibTableColumn
f3StorageDeviceInternalSsdHealth = _F3StorageDeviceInternalSsdHealth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 101, 1, 1),
    _F3StorageDeviceInternalSsdHealth_Type()
)
f3StorageDeviceInternalSsdHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3StorageDeviceInternalSsdHealth.setStatus("current")
_F3StorageDeviceExternalSsdStatus_Type = StorageStatus
_F3StorageDeviceExternalSsdStatus_Object = MibTableColumn
f3StorageDeviceExternalSsdStatus = _F3StorageDeviceExternalSsdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 101, 1, 2),
    _F3StorageDeviceExternalSsdStatus_Type()
)
f3StorageDeviceExternalSsdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3StorageDeviceExternalSsdStatus.setStatus("current")
_F3StorageDeviceWearoutLevel_Type = Integer32
_F3StorageDeviceWearoutLevel_Object = MibTableColumn
f3StorageDeviceWearoutLevel = _F3StorageDeviceWearoutLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 1, 101, 1, 3),
    _F3StorageDeviceWearoutLevel_Type()
)
f3StorageDeviceWearoutLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3StorageDeviceWearoutLevel.setStatus("current")
_CmEntityConformance_ObjectIdentity = ObjectIdentity
cmEntityConformance = _CmEntityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2)
)
_CmEntityCompliances_ObjectIdentity = ObjectIdentity
cmEntityCompliances = _CmEntityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 1)
)
_CmEntityGroups_ObjectIdentity = ObjectIdentity
cmEntityGroups = _CmEntityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2)
)
networkElementEntry.registerAugmentions(
    ("CM-ENTITY-MIB",
     "networkElementLLDPParamsEntry")
)
networkElementLLDPParamsEntry.setIndexNames(*networkElementEntry.getIndexNames())
serverCardEntry.registerAugmentions(
    ("CM-ENTITY-MIB",
     "f3StorageDeviceEntry")
)
f3StorageDeviceEntry.setIndexNames(*serverCardEntry.getIndexNames())

# Managed Objects groups

cmEntityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 1)
)
cmEntityObjectGroup.setObjects(
      *(("CM-ENTITY-MIB", "neIndex"),
        ("CM-ENTITY-MIB", "neName"),
        ("CM-ENTITY-MIB", "neType"),
        ("CM-ENTITY-MIB", "neContact"),
        ("CM-ENTITY-MIB", "neLocation"),
        ("CM-ENTITY-MIB", "neDescription"),
        ("CM-ENTITY-MIB", "neCmdPromptPrefix"),
        ("CM-ENTITY-MIB", "neAccepted"),
        ("CM-ENTITY-MIB", "neFromPort"),
        ("CM-ENTITY-MIB", "neProvAction"),
        ("CM-ENTITY-MIB", "neStorageType"),
        ("CM-ENTITY-MIB", "neRowStatus"),
        ("CM-ENTITY-MIB", "shelfIndex"),
        ("CM-ENTITY-MIB", "shelfEntityIndex"),
        ("CM-ENTITY-MIB", "shelfType"),
        ("CM-ENTITY-MIB", "shelfbackplaneRev"),
        ("CM-ENTITY-MIB", "shelfbackplaneDOM"),
        ("CM-ENTITY-MIB", "shelfbackplaneSerialNo"),
        ("CM-ENTITY-MIB", "shelfAction"),
        ("CM-ENTITY-MIB", "shelfAdminState"),
        ("CM-ENTITY-MIB", "shelfOperationalState"),
        ("CM-ENTITY-MIB", "shelfSecondaryState"),
        ("CM-ENTITY-MIB", "shelfMfgSite"),
        ("CM-ENTITY-MIB", "shelfOscillatorType"),
        ("CM-ENTITY-MIB", "shelfLedControl"),
        ("CM-ENTITY-MIB", "slotIndex"),
        ("CM-ENTITY-MIB", "slotEntityIndex"),
        ("CM-ENTITY-MIB", "slotType"),
        ("CM-ENTITY-MIB", "slotCardType"),
        ("CM-ENTITY-MIB", "slotCardUnitName"),
        ("CM-ENTITY-MIB", "slotCardFormatVersion"),
        ("CM-ENTITY-MIB", "slotCardCLEICode"),
        ("CM-ENTITY-MIB", "slotCardPartNumber"),
        ("CM-ENTITY-MIB", "slotCardHwRev"),
        ("CM-ENTITY-MIB", "slotCardSwRev"),
        ("CM-ENTITY-MIB", "slotCardSerialNum"),
        ("CM-ENTITY-MIB", "slotCardMfgName"),
        ("CM-ENTITY-MIB", "slotCardMfgDate"),
        ("CM-ENTITY-MIB", "slotCardMfgSite"),
        ("CM-ENTITY-MIB", "slotSecondaryState"),
        ("CM-ENTITY-MIB", "slotCardPhysicalAddress"),
        ("CM-ENTITY-MIB", "psuEntityIndex"),
        ("CM-ENTITY-MIB", "psuType"),
        ("CM-ENTITY-MIB", "psuAdminState"),
        ("CM-ENTITY-MIB", "psuOperationalState"),
        ("CM-ENTITY-MIB", "psuSecondaryState"),
        ("CM-ENTITY-MIB", "psuOutputVoltage"),
        ("CM-ENTITY-MIB", "psuTemperature"),
        ("CM-ENTITY-MIB", "psuOutputCurrent"),
        ("CM-ENTITY-MIB", "psuStorageType"),
        ("CM-ENTITY-MIB", "psuRowStatus"),
        ("CM-ENTITY-MIB", "fanEntityIndex"),
        ("CM-ENTITY-MIB", "fanAdminState"),
        ("CM-ENTITY-MIB", "fanOperationalState"),
        ("CM-ENTITY-MIB", "fanSecondaryState"),
        ("CM-ENTITY-MIB", "scuEntityIndex"),
        ("CM-ENTITY-MIB", "scuAdminState"),
        ("CM-ENTITY-MIB", "scuOperationalState"),
        ("CM-ENTITY-MIB", "scuSecondaryState"),
        ("CM-ENTITY-MIB", "scuVoltage"),
        ("CM-ENTITY-MIB", "scuTemperature"),
        ("CM-ENTITY-MIB", "scuRestartAction"),
        ("CM-ENTITY-MIB", "scuStorageType"),
        ("CM-ENTITY-MIB", "scuRowStatus"),
        ("CM-ENTITY-MIB", "nemiEntityIndex"),
        ("CM-ENTITY-MIB", "nemiAdminState"),
        ("CM-ENTITY-MIB", "nemiOperationalState"),
        ("CM-ENTITY-MIB", "nemiSecondaryState"),
        ("CM-ENTITY-MIB", "nemiVoltage"),
        ("CM-ENTITY-MIB", "nemiTemperature"),
        ("CM-ENTITY-MIB", "nemiRestartAction"),
        ("CM-ENTITY-MIB", "nemiStorageType"),
        ("CM-ENTITY-MIB", "nemiRowStatus"),
        ("CM-ENTITY-MIB", "nemiForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernetNTUCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTUCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTUCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTUCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTUCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTUCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTUCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetNTUCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardPSU1State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardPSU2State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardFAN1State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardFAN2State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardPsuType"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardLLFMode"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardLLFModeAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardRestartAction"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardEntityIndex"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardAdminState"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardOperationalState"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardSecondaryState"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardIpAddress"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardIpNetmask"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardIpGateway"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardDhcpEnabled"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardMgmtVlanId"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardTimeOfDay"),
        ("CM-ENTITY-MIB", "pseudoWireE3CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardAdminState"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardTemperature"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardStorageType"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernet1x10GCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardAdminState"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardTemperature"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardStorageType"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernet10x1GCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernetSWFCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetSWFCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetSWFCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetSWFCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetSWFCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetSWFCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetSWFCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetSWFCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernetSWFCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "stuCardEntityIndex"),
        ("CM-ENTITY-MIB", "stuCardAdminState"),
        ("CM-ENTITY-MIB", "stuCardOperationalState"),
        ("CM-ENTITY-MIB", "stuCardSecondaryState"),
        ("CM-ENTITY-MIB", "stuCardTemperature"),
        ("CM-ENTITY-MIB", "stuCardRestartAction"),
        ("CM-ENTITY-MIB", "stuCardStorageType"),
        ("CM-ENTITY-MIB", "stuCardRowStatus"),
        ("CM-ENTITY-MIB", "stuCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "amiEntityIndex"),
        ("CM-ENTITY-MIB", "amiAdminState"),
        ("CM-ENTITY-MIB", "amiOperationalState"),
        ("CM-ENTITY-MIB", "amiSecondaryState"),
        ("CM-ENTITY-MIB", "amiTemperature"),
        ("CM-ENTITY-MIB", "amiRestartAction"),
        ("CM-ENTITY-MIB", "stiEntityIndex"),
        ("CM-ENTITY-MIB", "stiAdminState"),
        ("CM-ENTITY-MIB", "stiOperationalState"),
        ("CM-ENTITY-MIB", "stiSecondaryState"),
        ("CM-ENTITY-MIB", "stiTemperature"),
        ("CM-ENTITY-MIB", "stiStorageType"),
        ("CM-ENTITY-MIB", "stiRowStatus"),
        ("CM-ENTITY-MIB", "f3UsbHostIndex"),
        ("CM-ENTITY-MIB", "f3UsbHostEntityIndex"),
        ("CM-ENTITY-MIB", "f3UsbHostUnitName"),
        ("CM-ENTITY-MIB", "f3UsbHostFormatVersion"),
        ("CM-ENTITY-MIB", "f3UsbHostCLEICode"),
        ("CM-ENTITY-MIB", "f3UsbHostPartNumber"),
        ("CM-ENTITY-MIB", "f3UsbHostHwRev"),
        ("CM-ENTITY-MIB", "f3UsbHostSwRev"),
        ("CM-ENTITY-MIB", "f3UsbHostSerialNum"),
        ("CM-ENTITY-MIB", "f3UsbHostMfgName"),
        ("CM-ENTITY-MIB", "f3UsbHostMfgDate"),
        ("CM-ENTITY-MIB", "f3UsbHostMfgSite"),
        ("CM-ENTITY-MIB", "f3UsbHostSecondaryState"),
        ("CM-ENTITY-MIB", "f3UsbHostPhysicalAddress"),
        ("CM-ENTITY-MIB", "f3UsbHostMuxOperationalMode"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSwitchPortAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSwitchPortAction"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardMode"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardAdminState"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardTemperature"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardStorageType"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardAdminState"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardTemperature"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardStorageType"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernet10x1GHighPerCardForceOffLineAction"))
)
if mibBuilder.loadTexts:
    cmEntityObjectGroup.setStatus("deprecated")

commonEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 2)
)
commonEntityGroup.setObjects(
      *(("CM-ENTITY-MIB", "neIndex"),
        ("CM-ENTITY-MIB", "neName"),
        ("CM-ENTITY-MIB", "neType"),
        ("CM-ENTITY-MIB", "neContact"),
        ("CM-ENTITY-MIB", "neLocation"),
        ("CM-ENTITY-MIB", "neDescription"),
        ("CM-ENTITY-MIB", "neCmdPromptPrefix"),
        ("CM-ENTITY-MIB", "neAccepted"),
        ("CM-ENTITY-MIB", "neFromPort"),
        ("CM-ENTITY-MIB", "neProvAction"),
        ("CM-ENTITY-MIB", "neStorageType"),
        ("CM-ENTITY-MIB", "neRowStatus"),
        ("CM-ENTITY-MIB", "neAutoProvMode"),
        ("CM-ENTITY-MIB", "neFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "shelfIndex"),
        ("CM-ENTITY-MIB", "shelfEntityIndex"),
        ("CM-ENTITY-MIB", "shelfType"),
        ("CM-ENTITY-MIB", "shelfbackplaneRev"),
        ("CM-ENTITY-MIB", "shelfbackplaneDOM"),
        ("CM-ENTITY-MIB", "shelfbackplaneSerialNo"),
        ("CM-ENTITY-MIB", "shelfAction"),
        ("CM-ENTITY-MIB", "shelfAdminState"),
        ("CM-ENTITY-MIB", "shelfOperationalState"),
        ("CM-ENTITY-MIB", "shelfSecondaryState"),
        ("CM-ENTITY-MIB", "shelfMfgSite"),
        ("CM-ENTITY-MIB", "shelfOscillatorType"),
        ("CM-ENTITY-MIB", "shelfLedControl"),
        ("CM-ENTITY-MIB", "slotIndex"),
        ("CM-ENTITY-MIB", "slotEntityIndex"),
        ("CM-ENTITY-MIB", "slotType"),
        ("CM-ENTITY-MIB", "slotCardType"),
        ("CM-ENTITY-MIB", "slotCardUnitName"),
        ("CM-ENTITY-MIB", "slotCardFormatVersion"),
        ("CM-ENTITY-MIB", "slotCardCLEICode"),
        ("CM-ENTITY-MIB", "slotCardPartNumber"),
        ("CM-ENTITY-MIB", "slotCardHwRev"),
        ("CM-ENTITY-MIB", "slotCardSwRev"),
        ("CM-ENTITY-MIB", "slotCardSerialNum"),
        ("CM-ENTITY-MIB", "slotCardMfgName"),
        ("CM-ENTITY-MIB", "slotCardMfgDate"),
        ("CM-ENTITY-MIB", "slotCardMfgSite"),
        ("CM-ENTITY-MIB", "slotSecondaryState"),
        ("CM-ENTITY-MIB", "slotCardPhysicalAddress"))
)
if mibBuilder.loadTexts:
    commonEntityGroup.setStatus("current")

psuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 3)
)
psuGroup.setObjects(
      *(("CM-ENTITY-MIB", "psuEntityIndex"),
        ("CM-ENTITY-MIB", "psuType"),
        ("CM-ENTITY-MIB", "psuAdminState"),
        ("CM-ENTITY-MIB", "psuOperationalState"),
        ("CM-ENTITY-MIB", "psuSecondaryState"))
)
if mibBuilder.loadTexts:
    psuGroup.setStatus("current")

fanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 4)
)
fanGroup.setObjects(
      *(("CM-ENTITY-MIB", "fanEntityIndex"),
        ("CM-ENTITY-MIB", "fanAdminState"),
        ("CM-ENTITY-MIB", "fanOperationalState"),
        ("CM-ENTITY-MIB", "fanSecondaryState"),
        ("CM-ENTITY-MIB", "fanStorageType"),
        ("CM-ENTITY-MIB", "fanRowStatus"))
)
if mibBuilder.loadTexts:
    fanGroup.setStatus("current")

hubshelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 5)
)
hubshelfGroup.setObjects(
      *(("CM-ENTITY-MIB", "scuEntityIndex"),
        ("CM-ENTITY-MIB", "scuAdminState"),
        ("CM-ENTITY-MIB", "scuOperationalState"),
        ("CM-ENTITY-MIB", "scuSecondaryState"),
        ("CM-ENTITY-MIB", "scuVoltage"),
        ("CM-ENTITY-MIB", "scuTemperature"),
        ("CM-ENTITY-MIB", "scuRestartAction"),
        ("CM-ENTITY-MIB", "scuStorageType"),
        ("CM-ENTITY-MIB", "scuRowStatus"),
        ("CM-ENTITY-MIB", "scuFlashModelNum"),
        ("CM-ENTITY-MIB", "scuFlashFirmwareRev"),
        ("CM-ENTITY-MIB", "scuFlashSerialNum"),
        ("CM-ENTITY-MIB", "nemiEntityIndex"),
        ("CM-ENTITY-MIB", "nemiAdminState"),
        ("CM-ENTITY-MIB", "nemiOperationalState"),
        ("CM-ENTITY-MIB", "nemiSecondaryState"),
        ("CM-ENTITY-MIB", "nemiVoltage"),
        ("CM-ENTITY-MIB", "nemiTemperature"),
        ("CM-ENTITY-MIB", "nemiRestartAction"),
        ("CM-ENTITY-MIB", "nemiStorageType"),
        ("CM-ENTITY-MIB", "nemiRowStatus"),
        ("CM-ENTITY-MIB", "nemiFlashModelNum"),
        ("CM-ENTITY-MIB", "nemiFlashFirmwareRev"),
        ("CM-ENTITY-MIB", "nemiFlashSerialNum"),
        ("CM-ENTITY-MIB", "ethernetNTUCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTUCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTUCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTUCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTUCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTUCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTUCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTUCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTUCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetNTUCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardPSU1State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardPSU2State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardFAN1State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardFAN2State"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardPsuType"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardLLFMode"),
        ("CM-ENTITY-MIB", "ethernetCPMRCardLLFModeAction"),
        ("CM-ENTITY-MIB", "scuTEntityIndex"),
        ("CM-ENTITY-MIB", "scuTAdminState"),
        ("CM-ENTITY-MIB", "scuTOperationalState"),
        ("CM-ENTITY-MIB", "scuTSecondaryState"),
        ("CM-ENTITY-MIB", "scuTVoltage"),
        ("CM-ENTITY-MIB", "scuTTemperature"),
        ("CM-ENTITY-MIB", "scuTRestartAction"),
        ("CM-ENTITY-MIB", "scuTStorageType"),
        ("CM-ENTITY-MIB", "scuTRowStatus"),
        ("CM-ENTITY-MIB", "ethernetNTECardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTECardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTECardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTECardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTECardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTECardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTECardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTECardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTECardStorageType"),
        ("CM-ENTITY-MIB", "ethernetNTECardRowStatus"))
)
if mibBuilder.loadTexts:
    hubshelfGroup.setStatus("current")

nteGe206CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 6)
)
nteGe206CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE206CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206CardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteGe206CardGroup.setStatus("current")

nteGe201SyncECardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 7)
)
nteGe201SyncECardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201SyncECardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteGe201SyncECardGroup.setStatus("current")

nteGe201NonSyncECardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 8)
)
nteGe201NonSyncECardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE201CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE201CardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteGe201NonSyncECardGroup.setStatus("current")

nteGe206FCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 9)
)
nteGe206FCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE206FCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206FCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteGe206FCardGroup.setStatus("current")

nteGe112CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 10)
)
nteGe112CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE112CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112CardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe112CardGroup.setStatus("current")

nteGe114CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 11)
)
nteGe114CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114CardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114CardGroup.setStatus("current")

nteGe206VCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 12)
)
nteGe206VCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE206VCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE206VCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteGe206VCardGroup.setStatus("current")

nteXg210CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 13)
)
nteXg210CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG210CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg210CardGroup.setStatus("current")

pseudoWireCardOcnStmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 14)
)
pseudoWireCardOcnStmCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "pseudoWireOcnStmCardEntityIndex"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardAdminState"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardOperationalState"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardSecondaryState"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardIpAddress"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardMode"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardVoltage"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardTemperature"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardRestartAction"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardStorageType"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardRowStatus"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardPSNEncapsulation"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardFreqSourceType"),
        ("CM-ENTITY-MIB", "pseudoWireOcnStmCardFreqSource"))
)
if mibBuilder.loadTexts:
    pseudoWireCardOcnStmCardGroup.setStatus("current")

pseudoWireCardE1T1CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 15)
)
pseudoWireCardE1T1CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "pseudoWireE1T1CardEntityIndex"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardAdminState"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardOperationalState"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardSecondaryState"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardIpAddress"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardMode"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardVoltage"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardTemperature"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardRestartAction"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardStorageType"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardRowStatus"),
        ("CM-ENTITY-MIB", "pseudoWireE1T1CardPSNEncapsulation"))
)
if mibBuilder.loadTexts:
    pseudoWireCardE1T1CardGroup.setStatus("current")

nteT1804CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 16)
)
nteT1804CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTET1804CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTET1804CardMode"))
)
if mibBuilder.loadTexts:
    nteT1804CardGroup.setStatus("current")

nteT3204CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 17)
)
nteT3204CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTET3204CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTET3204CardMode"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardRowStatus"))
)
if mibBuilder.loadTexts:
    nteT3204CardGroup.setStatus("current")

nteGeSyncProbeCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 18)
)
nteGeSyncProbeCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGESyncProbeCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    nteGeSyncProbeCardGroup.setStatus("current")

xg1XCCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 19)
)
xg1XCCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetXG1XCCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetXG1XCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    xg1XCCCardGroup.setStatus("current")

xg1SCCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 20)
)
xg1SCCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetXG1SCCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetXG1SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    xg1SCCCardGroup.setStatus("current")

ge4ECCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 21)
)
ge4ECCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetGE4ECCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4ECCCardRowStatus"))
)
if mibBuilder.loadTexts:
    ge4ECCCardGroup.setStatus("current")

ge4SCCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 22)
)
ge4SCCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetGE4SCCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    ge4SCCCardGroup.setStatus("current")

ge8SCCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 23)
)
ge8SCCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetGE8SCCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE8SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    ge8SCCCardGroup.setStatus("current")

nteGe114HCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 24)
)
nteGe114HCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114HCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114HCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114HCardGroup.setStatus("current")

nteGe114PHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 25)
)
nteGe114PHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114PHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114PHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114PHCardGroup.setStatus("current")

ethernetOverOCSTMCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 26)
)
ethernetOverOCSTMCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetOverOCSTMCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernetOverOCSTMCardMode"))
)
if mibBuilder.loadTexts:
    ethernetOverOCSTMCardGroup.setStatus("current")

ethernet1x10GHighPerCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 27)
)
ethernet1x10GHighPerCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernet1x10GHighPerCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardAdminState"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardTemperature"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardStorageType"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardRowStatus"),
        ("CM-ENTITY-MIB", "ethernet1x10GHighPerCardForceOffLineAction"))
)
if mibBuilder.loadTexts:
    ethernet1x10GHighPerCardGroup.setStatus("current")

ethernetFE36ECardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 28)
)
ethernetFE36ECardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetFE36ECardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardAdminState"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardTemperature"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardStorageType"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardRowStatus"),
        ("CM-ENTITY-MIB", "ethernetFE36ECardForceOffLineAction"),
        ("CM-ENTITY-MIB", "ethernetFE36ECard8023azEnabled"))
)
if mibBuilder.loadTexts:
    ethernetFE36ECardGroup.setStatus("current")

nteGe114SHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 29)
)
nteGe114SHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114SHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114SHCardGroup.setStatus("current")

nteGe114SCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 30)
)
nteGe114SCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114SCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114SCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114SCardGroup.setStatus("current")

ge8ECCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 31)
)
ge8ECCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetGE8ECCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE8ECCCardRowStatus"))
)
if mibBuilder.loadTexts:
    ge8ECCCardGroup.setStatus("current")

neLLDPParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 32)
)
neLLDPParamsGroup.setObjects(
    ("CM-ENTITY-MIB", "neLLDPParamsLLDPEnableAction")
)
if mibBuilder.loadTexts:
    neLLDPParamsGroup.setStatus("current")

nteSh1PcsCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 33)
)
nteSh1PcsCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTESH1PCSCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTESH1PCSCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteSh1PcsCardGroup.setStatus("current")

nteOsa5411CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 34)
)
nteOsa5411CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEOSA5411CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5411CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    nteOsa5411CardGroup.setStatus("current")

nteGe112ProCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 35)
)
nteGe112ProCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE112ProCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe112ProCardGroup.setStatus("current")

nteGe112ProMCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 36)
)
nteGe112ProMCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProMCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe112ProMCardGroup.setStatus("current")

nteGe114ProCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 37)
)
nteGe114ProCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114ProCardGroup.setStatus("current")

nteGe114ProCCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 38)
)
nteGe114ProCCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114ProCCardGroup.setStatus("current")

nteGe114ProSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 39)
)
nteGe114ProSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProSHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114ProSHCardGroup.setStatus("current")

nteGe114ProCSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 40)
)
nteGe114ProCSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProCSHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114ProCSHCardGroup.setStatus("current")

nteGe114ProHECardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 41)
)
nteGe114ProHECardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProHECardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114ProHECardGroup.setStatus("current")

nteGe112ProHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 42)
)
nteGe112ProHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe112ProHCardGroup.setStatus("current")

nteXg210CCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 43)
)
nteXg210CCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG210CCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG210CCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg210CCardGroup.setStatus("current")

geGE8SCryptoConnectorCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 44)
)
geGE8SCryptoConnectorCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE8SCryptoConnectorCardRowStatus"))
)
if mibBuilder.loadTexts:
    geGE8SCryptoConnectorCardGroup.setStatus("current")

nteOsa5420CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 45)
)
nteOsa5420CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEOSA5420CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5420CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    nteOsa5420CardGroup.setStatus("current")

nteOsa5421CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 46)
)
nteOsa5421CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEOSA5421CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5421CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardStorageType"),
        ("CM-ENTITY-MIB", "ethernetGE4SCCCardRowStatus"))
)
if mibBuilder.loadTexts:
    nteOsa5421CardGroup.setStatus("current")

nteGe114GCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 47)
)
nteGe114GCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114GCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114GCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe114GCardGroup.setStatus("current")

bits16PortCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 48)
)
bits16PortCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "bits16PortCardEntityIndex"),
        ("CM-ENTITY-MIB", "bits16PortCardAdminState"),
        ("CM-ENTITY-MIB", "bits16PortCardOperationalState"),
        ("CM-ENTITY-MIB", "bits16PortCardSecondaryState"),
        ("CM-ENTITY-MIB", "bits16PortCardRowStatus"),
        ("CM-ENTITY-MIB", "bits16PortCardAlias"),
        ("CM-ENTITY-MIB", "bits16PortCardTemperature"))
)
if mibBuilder.loadTexts:
    bits16PortCardGroup.setStatus("current")

nteGE114ProVmHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 49)
)
nteGE114ProVmHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGE114ProVmHCardGroup.setStatus("current")

nteGE114ProVmCHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 50)
)
nteGE114ProVmCHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGE114ProVmCHCardGroup.setStatus("current")

nteGE114ProVmCSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 51)
)
nteGE114ProVmCSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmCSHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGE114ProVmCSHCardGroup.setStatus("current")

serverCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 52)
)
serverCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "serverCardEntityIndex"),
        ("CM-ENTITY-MIB", "serverCardAdminState"),
        ("CM-ENTITY-MIB", "serverCardOperationalState"),
        ("CM-ENTITY-MIB", "serverCardSecondaryState"),
        ("CM-ENTITY-MIB", "serverCardStorageType"),
        ("CM-ENTITY-MIB", "serverCardVoltage"),
        ("CM-ENTITY-MIB", "serverCardTemperature"),
        ("CM-ENTITY-MIB", "serverCardUpTime"),
        ("CM-ENTITY-MIB", "serverCardVmNumber"),
        ("CM-ENTITY-MIB", "serverCardVirtualCpuTotal"),
        ("CM-ENTITY-MIB", "serverCardVirtualCpuAvailiable"),
        ("CM-ENTITY-MIB", "serverCardMemoryTotal"),
        ("CM-ENTITY-MIB", "serverCardMemoryAvailiable"),
        ("CM-ENTITY-MIB", "serverCardStorageTotal"),
        ("CM-ENTITY-MIB", "serverCardStorageAvailiable"),
        ("CM-ENTITY-MIB", "serverCardHvVersion"),
        ("CM-ENTITY-MIB", "serverCardHostName"),
        ("CM-ENTITY-MIB", "serverCardRestartAction"),
        ("CM-ENTITY-MIB", "serverCardRowStatus"),
        ("CM-ENTITY-MIB", "serverCardIgnoreWatchdog"),
        ("CM-ENTITY-MIB", "f3StorageDeviceInternalSsdHealth"),
        ("CM-ENTITY-MIB", "f3StorageDeviceExternalSsdStatus"),
        ("CM-ENTITY-MIB", "f3StorageDeviceWearoutLevel"))
)
if mibBuilder.loadTexts:
    serverCardGroup.setStatus("current")

pps16PortCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 53)
)
pps16PortCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "pps16PortCardEntityIndex"),
        ("CM-ENTITY-MIB", "pps16PortCardAdminState"),
        ("CM-ENTITY-MIB", "pps16PortCardOperationalState"),
        ("CM-ENTITY-MIB", "pps16PortCardSecondaryState"),
        ("CM-ENTITY-MIB", "pps16PortCardRowStatus"),
        ("CM-ENTITY-MIB", "pps16PortCardAlias"))
)
if mibBuilder.loadTexts:
    pps16PortCardGroup.setStatus("current")

clk16PortCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 54)
)
clk16PortCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "clk16PortCardEntityIndex"),
        ("CM-ENTITY-MIB", "clk16PortCardAdminState"),
        ("CM-ENTITY-MIB", "clk16PortCardOperationalState"),
        ("CM-ENTITY-MIB", "clk16PortCardSecondaryState"),
        ("CM-ENTITY-MIB", "clk16PortCardRowStatus"),
        ("CM-ENTITY-MIB", "clk16PortCardAlias"))
)
if mibBuilder.loadTexts:
    clk16PortCardGroup.setStatus("current")

todPps16PortCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 55)
)
todPps16PortCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "todPps16PortCardEntityIndex"),
        ("CM-ENTITY-MIB", "todPps16PortCardAdminState"),
        ("CM-ENTITY-MIB", "todPps16PortCardOperationalState"),
        ("CM-ENTITY-MIB", "todPps16PortCardSecondaryState"),
        ("CM-ENTITY-MIB", "todPps16PortCardRowStatus"),
        ("CM-ENTITY-MIB", "todPps16PortCardAlias"))
)
if mibBuilder.loadTexts:
    todPps16PortCardGroup.setStatus("current")

nteGe101ProCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 56)
)
nteGe101ProCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE101ProCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE101ProCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGe101ProCardGroup.setStatus("current")

nteGo102ProSCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 57)
)
nteGo102ProSCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGo102ProSCardGroup.setStatus("current")

nteGo102ProSPCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 58)
)
nteGo102ProSPCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSPCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGo102ProSPCardGroup.setStatus("current")

nteCx101Pro30ACardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 59)
)
nteCx101Pro30ACardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTECX101Pro30ACardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteCx101Pro30ACardGroup.setStatus("current")

nteCx102Pro30ACardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 60)
)
nteCx102Pro30ACardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTECX102Pro30ACardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteCx102Pro30ACardGroup.setStatus("current")

ge4PortCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 61)
)
ge4PortCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ge4PortCardEntityIndex"),
        ("CM-ENTITY-MIB", "ge4PortCardAdminState"),
        ("CM-ENTITY-MIB", "ge4PortCardOperationalState"),
        ("CM-ENTITY-MIB", "ge4PortCardSecondaryState"),
        ("CM-ENTITY-MIB", "ge4PortCardRowStatus"),
        ("CM-ENTITY-MIB", "ge4PortCardAlias"),
        ("CM-ENTITY-MIB", "ge4PortCardTemperature"))
)
if mibBuilder.loadTexts:
    ge4PortCardGroup.setStatus("current")

nteXg116ProCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 62)
)
nteXg116ProCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG116PROCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg116ProCardGroup.setStatus("current")

nteXg120ProCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 63)
)
nteXg120ProCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG120PROCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg120ProCardGroup.setStatus("current")

nteGE112ProVmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 64)
)
nteGE112ProVmCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE112ProVmCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGE112ProVmCardGroup.setStatus("current")

nteOsa5401CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 65)
)
nteOsa5401CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEOSA5401CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5401CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5401CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5401CardTableRestartAction"))
)
if mibBuilder.loadTexts:
    nteOsa5401CardGroup.setStatus("current")

nteOsa5405CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 66)
)
nteOsa5405CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEOSA5405CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5405CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5405CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5405CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5405CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEOSA5405CardTableRestartAction"))
)
if mibBuilder.loadTexts:
    nteOsa5405CardGroup.setStatus("current")

csmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 67)
)
csmCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetCSMCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetCSMCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetCSMCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetCSMCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetCSMCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetCSMCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetCSMCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetCSMCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetCSMCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetCSMCardOscillatorType"))
)
if mibBuilder.loadTexts:
    csmCardGroup.setStatus("current")

auxPortCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 68)
)
auxPortCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "auxPortCardEntityIndex"),
        ("CM-ENTITY-MIB", "auxPortCardAdminState"),
        ("CM-ENTITY-MIB", "auxPortCardOperationalState"),
        ("CM-ENTITY-MIB", "auxPortCardSecondaryState"),
        ("CM-ENTITY-MIB", "auxPortCardRowStatus"),
        ("CM-ENTITY-MIB", "auxPortCardAlias"),
        ("CM-ENTITY-MIB", "auxPortCardTemperature"))
)
if mibBuilder.loadTexts:
    auxPortCardGroup.setStatus("current")

nteGe102ProHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 69)
)
nteGe102ProHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardSwitchPortAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardPSU1State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardPSU2State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardFAN1State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardFAN2State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProHCardPsuType"))
)
if mibBuilder.loadTexts:
    nteGe102ProHCardGroup.setStatus("current")

nteGe102ProEFMHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 70)
)
nteGe102ProEFMHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardPSU1State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardPSU2State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardFAN1State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardFAN2State"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardPsuType"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardLLFMode"),
        ("CM-ENTITY-MIB", "ethernetNTEGE102ProEFMHCardLLFModeAction"))
)
if mibBuilder.loadTexts:
    nteGe102ProEFMHCardGroup.setStatus("current")

ethernetOsa3350MgntCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 71)
)
ethernetOsa3350MgntCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetOsa3350MgntCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetOsa3350MgntCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetOsa3350MgntCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetOsa3350MgntCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetOsa3350MgntCardRestartAction"))
)
if mibBuilder.loadTexts:
    ethernetOsa3350MgntCardGroup.setStatus("current")

nteXg116ProHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 72)
)
nteXg116ProHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG116PROHCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg116ProHCardGroup.setStatus("current")

nteGo102ProSMCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 73)
)
nteGo102ProSMCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGO102ProSMCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGo102ProSMCardGroup.setStatus("current")

nteXg118ProSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 74)
)
nteXg118ProSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROSHCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg118ProSHCardGroup.setStatus("current")

nteXg118ProacSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 75)
)
nteXg118ProacSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG118PROACSHCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg118ProacSHCardGroup.setStatus("current")

nteGE114ProVmSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 76)
)
nteGE114ProVmSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE114ProVmSHCardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGE114ProVmSHCardGroup.setStatus("current")

nteGE104CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 77)
)
nteGE104CardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEGE104CardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardFineGrainedPmInterval"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardSwitchPortActionPort"),
        ("CM-ENTITY-MIB", "ethernetNTEGE104CardSwitchPortAction"))
)
if mibBuilder.loadTexts:
    nteGE104CardGroup.setStatus("current")

nteXg120ProSHCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 78)
)
nteXg120ProSHCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardEntityIndex"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardAdminState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardOperationalState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardSecondaryState"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardVoltage"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardTemperature"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardSnmpDyingGaspEnabled"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardRestartAction"),
        ("CM-ENTITY-MIB", "ethernetNTEXG120PROSHCardFineGrainedPmInterval"))
)
if mibBuilder.loadTexts:
    nteXg120ProSHCardGroup.setStatus("current")

mbGnssCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 79)
)
mbGnssCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "mbGnssCardEntityIndex"),
        ("CM-ENTITY-MIB", "mbGnssCardAdminState"),
        ("CM-ENTITY-MIB", "mbGnssCardOperationalState"),
        ("CM-ENTITY-MIB", "mbGnssCardSecondaryState"),
        ("CM-ENTITY-MIB", "mbGnssCardRowStatus"),
        ("CM-ENTITY-MIB", "mbGnssCardAlias"))
)
if mibBuilder.loadTexts:
    mbGnssCardGroup.setStatus("current")

f3IrigCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 80)
)
f3IrigCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "f3IrigCardEntityIndex"),
        ("CM-ENTITY-MIB", "f3IrigCardAlias"),
        ("CM-ENTITY-MIB", "f3IrigCardAdminState"),
        ("CM-ENTITY-MIB", "f3IrigCardOperationalState"),
        ("CM-ENTITY-MIB", "f3IrigCardSecondaryState"),
        ("CM-ENTITY-MIB", "f3IrigCardTemperature"),
        ("CM-ENTITY-MIB", "f3IrigCardStorageType"),
        ("CM-ENTITY-MIB", "f3IrigCardRowStatus"))
)
if mibBuilder.loadTexts:
    f3IrigCardGroup.setStatus("current")

compositeClockCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 2, 81)
)
compositeClockCardGroup.setObjects(
      *(("CM-ENTITY-MIB", "compositeClockCardEntityIndex"),
        ("CM-ENTITY-MIB", "compositeClockCardAdminState"),
        ("CM-ENTITY-MIB", "compositeClockCardOperationalState"),
        ("CM-ENTITY-MIB", "compositeClockCardSecondaryState"),
        ("CM-ENTITY-MIB", "compositeClockCardRowStatus"),
        ("CM-ENTITY-MIB", "compositeClockCardAlias"))
)
if mibBuilder.loadTexts:
    compositeClockCardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmEntityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 3, 2, 1, 1)
)
cmEntityCompliance.setObjects(
      *(("CM-ENTITY-MIB", "cmEntityObjectGroup"),
        ("CM-ENTITY-MIB", "commonEntityGroup"),
        ("CM-ENTITY-MIB", "psuGroup"),
        ("CM-ENTITY-MIB", "fanGroup"),
        ("CM-ENTITY-MIB", "hubshelfGroup"),
        ("CM-ENTITY-MIB", "nteGe206CardGroup"),
        ("CM-ENTITY-MIB", "nteGe201SyncECardGroup"),
        ("CM-ENTITY-MIB", "nteGe201NonSyncECardGroup"),
        ("CM-ENTITY-MIB", "nteGe206FCardGroup"),
        ("CM-ENTITY-MIB", "nteGe206VCardGroup"),
        ("CM-ENTITY-MIB", "nteXg210CardGroup"),
        ("CM-ENTITY-MIB", "neLLDPParamsGroup"),
        ("CM-ENTITY-MIB", "nteSh1PcsCardGroup"),
        ("CM-ENTITY-MIB", "nteXg210CCardGroup"),
        ("CM-ENTITY-MIB", "geGE8SCryptoConnectorCardGroup"),
        ("CM-ENTITY-MIB", "nteOsa5420CardGroup"),
        ("CM-ENTITY-MIB", "nteOsa5421CardGroup"),
        ("CM-ENTITY-MIB", "bits16PortCardGroup"),
        ("CM-ENTITY-MIB", "pps16PortCardGroup"),
        ("CM-ENTITY-MIB", "clk16PortCardGroup"),
        ("CM-ENTITY-MIB", "todPps16PortCardGroup"),
        ("CM-ENTITY-MIB", "ge4PortCardGroup"),
        ("CM-ENTITY-MIB", "nteXg116ProCardGroup"),
        ("CM-ENTITY-MIB", "nteXg120ProCardGroup"),
        ("CM-ENTITY-MIB", "nteOsa5401CardGroup"),
        ("CM-ENTITY-MIB", "nteOsa5405CardGroup"),
        ("CM-ENTITY-MIB", "csmCardGroup"),
        ("CM-ENTITY-MIB", "auxPortCardGroup"),
        ("CM-ENTITY-MIB", "nteGe102ProHCardGroup"),
        ("CM-ENTITY-MIB", "nteGe102ProEFMHCardGroup"),
        ("CM-ENTITY-MIB", "nteXg116ProHCardGroup"),
        ("CM-ENTITY-MIB", "nteXg118ProSHCardGroup"),
        ("CM-ENTITY-MIB", "nteXg118ProacSHCardGroup"),
        ("CM-ENTITY-MIB", "nteXg120ProSHCardGroup"))
)
if mibBuilder.loadTexts:
    cmEntityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-ENTITY-MIB",
    **{"NeProvAction": NeProvAction,
       "NetworkElementType": NetworkElementType,
       "SlotType": SlotType,
       "ShelfType": ShelfType,
       "ShelfAction": ShelfAction,
       "PsuType": PsuType,
       "CardType": CardType,
       "CmCPMRLinkLossFwdMode": CmCPMRLinkLossFwdMode,
       "PWE3OCNSTMCardMode": PWE3OCNSTMCardMode,
       "PWE3E1T1CardMode": PWE3E1T1CardMode,
       "PSNEncapsulationMode": PSNEncapsulationMode,
       "LLDPEnableAction": LLDPEnableAction,
       "LedControlType": LedControlType,
       "ResyncType": ResyncType,
       "StorageStatus": StorageStatus,
       "SwitchPortAction": SwitchPortAction,
       "PortCarrierType": PortCarrierType,
       "cmEntityMIB": cmEntityMIB,
       "cmEntityObjects": cmEntityObjects,
       "networkElementTable": networkElementTable,
       "networkElementEntry": networkElementEntry,
       "neIndex": neIndex,
       "neName": neName,
       "neType": neType,
       "neContact": neContact,
       "neLocation": neLocation,
       "neDescription": neDescription,
       "neCmdPromptPrefix": neCmdPromptPrefix,
       "neAccepted": neAccepted,
       "neFromPort": neFromPort,
       "neProvAction": neProvAction,
       "neStorageType": neStorageType,
       "neRowStatus": neRowStatus,
       "neAutoProvMode": neAutoProvMode,
       "neFineGrainedPmInterval": neFineGrainedPmInterval,
       "shelfTable": shelfTable,
       "shelfEntry": shelfEntry,
       "shelfIndex": shelfIndex,
       "shelfEntityIndex": shelfEntityIndex,
       "shelfType": shelfType,
       "shelfbackplaneRev": shelfbackplaneRev,
       "shelfbackplaneDOM": shelfbackplaneDOM,
       "shelfbackplaneSerialNo": shelfbackplaneSerialNo,
       "shelfAction": shelfAction,
       "shelfAdminState": shelfAdminState,
       "shelfOperationalState": shelfOperationalState,
       "shelfSecondaryState": shelfSecondaryState,
       "shelfMfgSite": shelfMfgSite,
       "shelfOscillatorType": shelfOscillatorType,
       "shelfLedControl": shelfLedControl,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotIndex": slotIndex,
       "slotEntityIndex": slotEntityIndex,
       "slotType": slotType,
       "slotCardType": slotCardType,
       "slotCardUnitName": slotCardUnitName,
       "slotCardFormatVersion": slotCardFormatVersion,
       "slotCardCLEICode": slotCardCLEICode,
       "slotCardPartNumber": slotCardPartNumber,
       "slotCardHwRev": slotCardHwRev,
       "slotCardSwRev": slotCardSwRev,
       "slotCardSerialNum": slotCardSerialNum,
       "slotCardMfgName": slotCardMfgName,
       "slotCardMfgDate": slotCardMfgDate,
       "slotCardMfgSite": slotCardMfgSite,
       "slotSecondaryState": slotSecondaryState,
       "slotCardPhysicalAddress": slotCardPhysicalAddress,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuEntityIndex": psuEntityIndex,
       "psuType": psuType,
       "psuAdminState": psuAdminState,
       "psuOperationalState": psuOperationalState,
       "psuSecondaryState": psuSecondaryState,
       "psuOutputVoltage": psuOutputVoltage,
       "psuTemperature": psuTemperature,
       "psuOutputCurrent": psuOutputCurrent,
       "psuStorageType": psuStorageType,
       "psuRowStatus": psuRowStatus,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanEntityIndex": fanEntityIndex,
       "fanAdminState": fanAdminState,
       "fanOperationalState": fanOperationalState,
       "fanSecondaryState": fanSecondaryState,
       "fanStorageType": fanStorageType,
       "fanRowStatus": fanRowStatus,
       "scuTable": scuTable,
       "scuEntry": scuEntry,
       "scuEntityIndex": scuEntityIndex,
       "scuAdminState": scuAdminState,
       "scuOperationalState": scuOperationalState,
       "scuSecondaryState": scuSecondaryState,
       "scuVoltage": scuVoltage,
       "scuTemperature": scuTemperature,
       "scuRestartAction": scuRestartAction,
       "scuStorageType": scuStorageType,
       "scuRowStatus": scuRowStatus,
       "scuFlashModelNum": scuFlashModelNum,
       "scuFlashFirmwareRev": scuFlashFirmwareRev,
       "scuFlashSerialNum": scuFlashSerialNum,
       "nemiTable": nemiTable,
       "nemiEntry": nemiEntry,
       "nemiEntityIndex": nemiEntityIndex,
       "nemiAdminState": nemiAdminState,
       "nemiOperationalState": nemiOperationalState,
       "nemiSecondaryState": nemiSecondaryState,
       "nemiVoltage": nemiVoltage,
       "nemiTemperature": nemiTemperature,
       "nemiRestartAction": nemiRestartAction,
       "nemiStorageType": nemiStorageType,
       "nemiRowStatus": nemiRowStatus,
       "nemiForceOffLineAction": nemiForceOffLineAction,
       "nemiFlashModelNum": nemiFlashModelNum,
       "nemiFlashFirmwareRev": nemiFlashFirmwareRev,
       "nemiFlashSerialNum": nemiFlashSerialNum,
       "ethernetNTUCardTable": ethernetNTUCardTable,
       "ethernetNTUCardEntry": ethernetNTUCardEntry,
       "ethernetNTUCardEntityIndex": ethernetNTUCardEntityIndex,
       "ethernetNTUCardAdminState": ethernetNTUCardAdminState,
       "ethernetNTUCardOperationalState": ethernetNTUCardOperationalState,
       "ethernetNTUCardSecondaryState": ethernetNTUCardSecondaryState,
       "ethernetNTUCardVoltage": ethernetNTUCardVoltage,
       "ethernetNTUCardTemperature": ethernetNTUCardTemperature,
       "ethernetNTUCardSnmpDyingGaspEnabled": ethernetNTUCardSnmpDyingGaspEnabled,
       "ethernetNTUCardRestartAction": ethernetNTUCardRestartAction,
       "ethernetNTUCardStorageType": ethernetNTUCardStorageType,
       "ethernetNTUCardRowStatus": ethernetNTUCardRowStatus,
       "ethernetCPMRCardTable": ethernetCPMRCardTable,
       "ethernetCPMRCardEntry": ethernetCPMRCardEntry,
       "ethernetCPMRCardEntityIndex": ethernetCPMRCardEntityIndex,
       "ethernetCPMRCardAdminState": ethernetCPMRCardAdminState,
       "ethernetCPMRCardOperationalState": ethernetCPMRCardOperationalState,
       "ethernetCPMRCardSecondaryState": ethernetCPMRCardSecondaryState,
       "ethernetCPMRCardVoltage": ethernetCPMRCardVoltage,
       "ethernetCPMRCardTemperature": ethernetCPMRCardTemperature,
       "ethernetCPMRCardRestartAction": ethernetCPMRCardRestartAction,
       "ethernetCPMRCardPSU1State": ethernetCPMRCardPSU1State,
       "ethernetCPMRCardPSU2State": ethernetCPMRCardPSU2State,
       "ethernetCPMRCardFAN1State": ethernetCPMRCardFAN1State,
       "ethernetCPMRCardFAN2State": ethernetCPMRCardFAN2State,
       "ethernetCPMRCardPsuType": ethernetCPMRCardPsuType,
       "ethernetCPMRCardLLFMode": ethernetCPMRCardLLFMode,
       "ethernetCPMRCardLLFModeAction": ethernetCPMRCardLLFModeAction,
       "ethernetNTEGE101CardTable": ethernetNTEGE101CardTable,
       "ethernetNTEGE101CardEntry": ethernetNTEGE101CardEntry,
       "ethernetNTEGE101CardEntityIndex": ethernetNTEGE101CardEntityIndex,
       "ethernetNTEGE101CardAdminState": ethernetNTEGE101CardAdminState,
       "ethernetNTEGE101CardOperationalState": ethernetNTEGE101CardOperationalState,
       "ethernetNTEGE101CardSecondaryState": ethernetNTEGE101CardSecondaryState,
       "ethernetNTEGE101CardVoltage": ethernetNTEGE101CardVoltage,
       "ethernetNTEGE101CardTemperature": ethernetNTEGE101CardTemperature,
       "ethernetNTEGE101CardSnmpDyingGaspEnabled": ethernetNTEGE101CardSnmpDyingGaspEnabled,
       "ethernetNTEGE101CardRestartAction": ethernetNTEGE101CardRestartAction,
       "ethernetNTEGE206CardTable": ethernetNTEGE206CardTable,
       "ethernetNTEGE206CardEntry": ethernetNTEGE206CardEntry,
       "ethernetNTEGE206CardEntityIndex": ethernetNTEGE206CardEntityIndex,
       "ethernetNTEGE206CardAdminState": ethernetNTEGE206CardAdminState,
       "ethernetNTEGE206CardOperationalState": ethernetNTEGE206CardOperationalState,
       "ethernetNTEGE206CardSecondaryState": ethernetNTEGE206CardSecondaryState,
       "ethernetNTEGE206CardVoltage": ethernetNTEGE206CardVoltage,
       "ethernetNTEGE206CardTemperature": ethernetNTEGE206CardTemperature,
       "ethernetNTEGE206CardSnmpDyingGaspEnabled": ethernetNTEGE206CardSnmpDyingGaspEnabled,
       "ethernetNTEGE206CardRestartAction": ethernetNTEGE206CardRestartAction,
       "ethernetNTEGE206CardFineGrainedPmInterval": ethernetNTEGE206CardFineGrainedPmInterval,
       "pseudoWireE3CardTable": pseudoWireE3CardTable,
       "pseudoWireE3CardEntry": pseudoWireE3CardEntry,
       "pseudoWireE3CardEntityIndex": pseudoWireE3CardEntityIndex,
       "pseudoWireE3CardAdminState": pseudoWireE3CardAdminState,
       "pseudoWireE3CardOperationalState": pseudoWireE3CardOperationalState,
       "pseudoWireE3CardSecondaryState": pseudoWireE3CardSecondaryState,
       "pseudoWireE3CardIpAddress": pseudoWireE3CardIpAddress,
       "pseudoWireE3CardIpNetmask": pseudoWireE3CardIpNetmask,
       "pseudoWireE3CardIpGateway": pseudoWireE3CardIpGateway,
       "pseudoWireE3CardDhcpEnabled": pseudoWireE3CardDhcpEnabled,
       "pseudoWireE3CardMgmtVlanId": pseudoWireE3CardMgmtVlanId,
       "pseudoWireE3CardTimeOfDay": pseudoWireE3CardTimeOfDay,
       "pseudoWireE3CardRestartAction": pseudoWireE3CardRestartAction,
       "scuTTable": scuTTable,
       "scuTEntry": scuTEntry,
       "scuTEntityIndex": scuTEntityIndex,
       "scuTAdminState": scuTAdminState,
       "scuTOperationalState": scuTOperationalState,
       "scuTSecondaryState": scuTSecondaryState,
       "scuTVoltage": scuTVoltage,
       "scuTTemperature": scuTTemperature,
       "scuTRestartAction": scuTRestartAction,
       "scuTStorageType": scuTStorageType,
       "scuTRowStatus": scuTRowStatus,
       "ethernetNTECardTable": ethernetNTECardTable,
       "ethernetNTECardEntry": ethernetNTECardEntry,
       "ethernetNTECardEntityIndex": ethernetNTECardEntityIndex,
       "ethernetNTECardAdminState": ethernetNTECardAdminState,
       "ethernetNTECardOperationalState": ethernetNTECardOperationalState,
       "ethernetNTECardSecondaryState": ethernetNTECardSecondaryState,
       "ethernetNTECardVoltage": ethernetNTECardVoltage,
       "ethernetNTECardTemperature": ethernetNTECardTemperature,
       "ethernetNTECardSnmpDyingGaspEnabled": ethernetNTECardSnmpDyingGaspEnabled,
       "ethernetNTECardRestartAction": ethernetNTECardRestartAction,
       "ethernetNTECardStorageType": ethernetNTECardStorageType,
       "ethernetNTECardRowStatus": ethernetNTECardRowStatus,
       "ethernetNTEGE201CardTable": ethernetNTEGE201CardTable,
       "ethernetNTEGE201CardEntry": ethernetNTEGE201CardEntry,
       "ethernetNTEGE201CardEntityIndex": ethernetNTEGE201CardEntityIndex,
       "ethernetNTEGE201CardAdminState": ethernetNTEGE201CardAdminState,
       "ethernetNTEGE201CardOperationalState": ethernetNTEGE201CardOperationalState,
       "ethernetNTEGE201CardSecondaryState": ethernetNTEGE201CardSecondaryState,
       "ethernetNTEGE201CardVoltage": ethernetNTEGE201CardVoltage,
       "ethernetNTEGE201CardTemperature": ethernetNTEGE201CardTemperature,
       "ethernetNTEGE201CardSnmpDyingGaspEnabled": ethernetNTEGE201CardSnmpDyingGaspEnabled,
       "ethernetNTEGE201CardRestartAction": ethernetNTEGE201CardRestartAction,
       "ethernetNTEGE201CardFineGrainedPmInterval": ethernetNTEGE201CardFineGrainedPmInterval,
       "ethernetNTEGE201SyncECardTable": ethernetNTEGE201SyncECardTable,
       "ethernetNTEGE201SyncECardEntry": ethernetNTEGE201SyncECardEntry,
       "ethernetNTEGE201SyncECardEntityIndex": ethernetNTEGE201SyncECardEntityIndex,
       "ethernetNTEGE201SyncECardAdminState": ethernetNTEGE201SyncECardAdminState,
       "ethernetNTEGE201SyncECardOperationalState": ethernetNTEGE201SyncECardOperationalState,
       "ethernetNTEGE201SyncECardSecondaryState": ethernetNTEGE201SyncECardSecondaryState,
       "ethernetNTEGE201SyncECardVoltage": ethernetNTEGE201SyncECardVoltage,
       "ethernetNTEGE201SyncECardTemperature": ethernetNTEGE201SyncECardTemperature,
       "ethernetNTEGE201SyncECardSnmpDyingGaspEnabled": ethernetNTEGE201SyncECardSnmpDyingGaspEnabled,
       "ethernetNTEGE201SyncECardRestartAction": ethernetNTEGE201SyncECardRestartAction,
       "ethernetNTEGE201SyncECardFineGrainedPmInterval": ethernetNTEGE201SyncECardFineGrainedPmInterval,
       "ethernetNTEGE206FCardTable": ethernetNTEGE206FCardTable,
       "ethernetNTEGE206FCardEntry": ethernetNTEGE206FCardEntry,
       "ethernetNTEGE206FCardEntityIndex": ethernetNTEGE206FCardEntityIndex,
       "ethernetNTEGE206FCardAdminState": ethernetNTEGE206FCardAdminState,
       "ethernetNTEGE206FCardOperationalState": ethernetNTEGE206FCardOperationalState,
       "ethernetNTEGE206FCardSecondaryState": ethernetNTEGE206FCardSecondaryState,
       "ethernetNTEGE206FCardVoltage": ethernetNTEGE206FCardVoltage,
       "ethernetNTEGE206FCardTemperature": ethernetNTEGE206FCardTemperature,
       "ethernetNTEGE206FCardSnmpDyingGaspEnabled": ethernetNTEGE206FCardSnmpDyingGaspEnabled,
       "ethernetNTEGE206FCardRestartAction": ethernetNTEGE206FCardRestartAction,
       "ethernetNTEGE206FCardFineGrainedPmInterval": ethernetNTEGE206FCardFineGrainedPmInterval,
       "ethernet1x10GCardTable": ethernet1x10GCardTable,
       "ethernet1x10GCardEntry": ethernet1x10GCardEntry,
       "ethernet1x10GCardEntityIndex": ethernet1x10GCardEntityIndex,
       "ethernet1x10GCardAdminState": ethernet1x10GCardAdminState,
       "ethernet1x10GCardOperationalState": ethernet1x10GCardOperationalState,
       "ethernet1x10GCardSecondaryState": ethernet1x10GCardSecondaryState,
       "ethernet1x10GCardTemperature": ethernet1x10GCardTemperature,
       "ethernet1x10GCardSnmpDyingGaspEnabled": ethernet1x10GCardSnmpDyingGaspEnabled,
       "ethernet1x10GCardRestartAction": ethernet1x10GCardRestartAction,
       "ethernet1x10GCardStorageType": ethernet1x10GCardStorageType,
       "ethernet1x10GCardRowStatus": ethernet1x10GCardRowStatus,
       "ethernet1x10GCardForceOffLineAction": ethernet1x10GCardForceOffLineAction,
       "ethernet10x1GCardTable": ethernet10x1GCardTable,
       "ethernet10x1GCardEntry": ethernet10x1GCardEntry,
       "ethernet10x1GCardEntityIndex": ethernet10x1GCardEntityIndex,
       "ethernet10x1GCardAdminState": ethernet10x1GCardAdminState,
       "ethernet10x1GCardOperationalState": ethernet10x1GCardOperationalState,
       "ethernet10x1GCardSecondaryState": ethernet10x1GCardSecondaryState,
       "ethernet10x1GCardTemperature": ethernet10x1GCardTemperature,
       "ethernet10x1GCardSnmpDyingGaspEnabled": ethernet10x1GCardSnmpDyingGaspEnabled,
       "ethernet10x1GCardRestartAction": ethernet10x1GCardRestartAction,
       "ethernet10x1GCardStorageType": ethernet10x1GCardStorageType,
       "ethernet10x1GCardRowStatus": ethernet10x1GCardRowStatus,
       "ethernet10x1GCardForceOffLineAction": ethernet10x1GCardForceOffLineAction,
       "ethernetSWFCardTable": ethernetSWFCardTable,
       "ethernetSWFCardEntry": ethernetSWFCardEntry,
       "ethernetSWFCardEntityIndex": ethernetSWFCardEntityIndex,
       "ethernetSWFCardAdminState": ethernetSWFCardAdminState,
       "ethernetSWFCardOperationalState": ethernetSWFCardOperationalState,
       "ethernetSWFCardSecondaryState": ethernetSWFCardSecondaryState,
       "ethernetSWFCardTemperature": ethernetSWFCardTemperature,
       "ethernetSWFCardRestartAction": ethernetSWFCardRestartAction,
       "ethernetSWFCardStorageType": ethernetSWFCardStorageType,
       "ethernetSWFCardRowStatus": ethernetSWFCardRowStatus,
       "ethernetSWFCardForceOffLineAction": ethernetSWFCardForceOffLineAction,
       "stuCardTable": stuCardTable,
       "stuCardEntry": stuCardEntry,
       "stuCardEntityIndex": stuCardEntityIndex,
       "stuCardAdminState": stuCardAdminState,
       "stuCardOperationalState": stuCardOperationalState,
       "stuCardSecondaryState": stuCardSecondaryState,
       "stuCardTemperature": stuCardTemperature,
       "stuCardRestartAction": stuCardRestartAction,
       "stuCardStorageType": stuCardStorageType,
       "stuCardRowStatus": stuCardRowStatus,
       "stuCardForceOffLineAction": stuCardForceOffLineAction,
       "amiTable": amiTable,
       "amiEntry": amiEntry,
       "amiEntityIndex": amiEntityIndex,
       "amiAdminState": amiAdminState,
       "amiOperationalState": amiOperationalState,
       "amiSecondaryState": amiSecondaryState,
       "amiTemperature": amiTemperature,
       "amiRestartAction": amiRestartAction,
       "stiTable": stiTable,
       "stiEntry": stiEntry,
       "stiEntityIndex": stiEntityIndex,
       "stiAdminState": stiAdminState,
       "stiOperationalState": stiOperationalState,
       "stiSecondaryState": stiSecondaryState,
       "stiTemperature": stiTemperature,
       "stiStorageType": stiStorageType,
       "stiRowStatus": stiRowStatus,
       "f3UsbHostTable": f3UsbHostTable,
       "f3UsbHostEntry": f3UsbHostEntry,
       "f3UsbHostIndex": f3UsbHostIndex,
       "f3UsbHostEntityIndex": f3UsbHostEntityIndex,
       "f3UsbHostUnitName": f3UsbHostUnitName,
       "f3UsbHostFormatVersion": f3UsbHostFormatVersion,
       "f3UsbHostCLEICode": f3UsbHostCLEICode,
       "f3UsbHostPartNumber": f3UsbHostPartNumber,
       "f3UsbHostHwRev": f3UsbHostHwRev,
       "f3UsbHostSwRev": f3UsbHostSwRev,
       "f3UsbHostSerialNum": f3UsbHostSerialNum,
       "f3UsbHostMfgName": f3UsbHostMfgName,
       "f3UsbHostMfgDate": f3UsbHostMfgDate,
       "f3UsbHostMfgSite": f3UsbHostMfgSite,
       "f3UsbHostSecondaryState": f3UsbHostSecondaryState,
       "f3UsbHostPhysicalAddress": f3UsbHostPhysicalAddress,
       "f3UsbHostMuxOperationalMode": f3UsbHostMuxOperationalMode,
       "ethernetNTEGE112CardTable": ethernetNTEGE112CardTable,
       "ethernetNTEGE112CardEntry": ethernetNTEGE112CardEntry,
       "ethernetNTEGE112CardEntityIndex": ethernetNTEGE112CardEntityIndex,
       "ethernetNTEGE112CardAdminState": ethernetNTEGE112CardAdminState,
       "ethernetNTEGE112CardOperationalState": ethernetNTEGE112CardOperationalState,
       "ethernetNTEGE112CardSecondaryState": ethernetNTEGE112CardSecondaryState,
       "ethernetNTEGE112CardVoltage": ethernetNTEGE112CardVoltage,
       "ethernetNTEGE112CardTemperature": ethernetNTEGE112CardTemperature,
       "ethernetNTEGE112CardSnmpDyingGaspEnabled": ethernetNTEGE112CardSnmpDyingGaspEnabled,
       "ethernetNTEGE112CardRestartAction": ethernetNTEGE112CardRestartAction,
       "ethernetNTEGE112CardFineGrainedPmInterval": ethernetNTEGE112CardFineGrainedPmInterval,
       "ethernetNTEGE112CardSwitchPortActionPort": ethernetNTEGE112CardSwitchPortActionPort,
       "ethernetNTEGE112CardSwitchPortAction": ethernetNTEGE112CardSwitchPortAction,
       "ethernetNTEGE114CardTable": ethernetNTEGE114CardTable,
       "ethernetNTEGE114CardEntry": ethernetNTEGE114CardEntry,
       "ethernetNTEGE114CardEntityIndex": ethernetNTEGE114CardEntityIndex,
       "ethernetNTEGE114CardAdminState": ethernetNTEGE114CardAdminState,
       "ethernetNTEGE114CardOperationalState": ethernetNTEGE114CardOperationalState,
       "ethernetNTEGE114CardSecondaryState": ethernetNTEGE114CardSecondaryState,
       "ethernetNTEGE114CardVoltage": ethernetNTEGE114CardVoltage,
       "ethernetNTEGE114CardTemperature": ethernetNTEGE114CardTemperature,
       "ethernetNTEGE114CardSnmpDyingGaspEnabled": ethernetNTEGE114CardSnmpDyingGaspEnabled,
       "ethernetNTEGE114CardRestartAction": ethernetNTEGE114CardRestartAction,
       "ethernetNTEGE114CardFineGrainedPmInterval": ethernetNTEGE114CardFineGrainedPmInterval,
       "ethernetNTEGE114CardSwitchPortActionPort": ethernetNTEGE114CardSwitchPortActionPort,
       "ethernetNTEGE114CardSwitchPortAction": ethernetNTEGE114CardSwitchPortAction,
       "ethernetNTEGE206VCardTable": ethernetNTEGE206VCardTable,
       "ethernetNTEGE206VCardEntry": ethernetNTEGE206VCardEntry,
       "ethernetNTEGE206VCardEntityIndex": ethernetNTEGE206VCardEntityIndex,
       "ethernetNTEGE206VCardAdminState": ethernetNTEGE206VCardAdminState,
       "ethernetNTEGE206VCardOperationalState": ethernetNTEGE206VCardOperationalState,
       "ethernetNTEGE206VCardSecondaryState": ethernetNTEGE206VCardSecondaryState,
       "ethernetNTEGE206VCardVoltage": ethernetNTEGE206VCardVoltage,
       "ethernetNTEGE206VCardTemperature": ethernetNTEGE206VCardTemperature,
       "ethernetNTEGE206VCardSnmpDyingGaspEnabled": ethernetNTEGE206VCardSnmpDyingGaspEnabled,
       "ethernetNTEGE206VCardRestartAction": ethernetNTEGE206VCardRestartAction,
       "ethernetNTEGE206VCardFineGrainedPmInterval": ethernetNTEGE206VCardFineGrainedPmInterval,
       "ethernetGE4SCCCardTable": ethernetGE4SCCCardTable,
       "ethernetGE4SCCCardEntry": ethernetGE4SCCCardEntry,
       "ethernetGE4SCCCardEntityIndex": ethernetGE4SCCCardEntityIndex,
       "ethernetGE4SCCCardAdminState": ethernetGE4SCCCardAdminState,
       "ethernetGE4SCCCardOperationalState": ethernetGE4SCCCardOperationalState,
       "ethernetGE4SCCCardSecondaryState": ethernetGE4SCCCardSecondaryState,
       "ethernetGE4SCCCardVoltage": ethernetGE4SCCCardVoltage,
       "ethernetGE4SCCCardTemperature": ethernetGE4SCCCardTemperature,
       "ethernetGE4SCCCardRestartAction": ethernetGE4SCCCardRestartAction,
       "ethernetGE4SCCCardStorageType": ethernetGE4SCCCardStorageType,
       "ethernetGE4SCCCardRowStatus": ethernetGE4SCCCardRowStatus,
       "ethernetGE4ECCCardTable": ethernetGE4ECCCardTable,
       "ethernetGE4ECCCardEntry": ethernetGE4ECCCardEntry,
       "ethernetGE4ECCCardEntityIndex": ethernetGE4ECCCardEntityIndex,
       "ethernetGE4ECCCardAdminState": ethernetGE4ECCCardAdminState,
       "ethernetGE4ECCCardOperationalState": ethernetGE4ECCCardOperationalState,
       "ethernetGE4ECCCardSecondaryState": ethernetGE4ECCCardSecondaryState,
       "ethernetGE4ECCCardVoltage": ethernetGE4ECCCardVoltage,
       "ethernetGE4ECCCardTemperature": ethernetGE4ECCCardTemperature,
       "ethernetGE4ECCCardRestartAction": ethernetGE4ECCCardRestartAction,
       "ethernetGE4ECCCardStorageType": ethernetGE4ECCCardStorageType,
       "ethernetGE4ECCCardRowStatus": ethernetGE4ECCCardRowStatus,
       "ethernetNTEXG210CardTable": ethernetNTEXG210CardTable,
       "ethernetNTEXG210CardEntry": ethernetNTEXG210CardEntry,
       "ethernetNTEXG210CardEntityIndex": ethernetNTEXG210CardEntityIndex,
       "ethernetNTEXG210CardAdminState": ethernetNTEXG210CardAdminState,
       "ethernetNTEXG210CardOperationalState": ethernetNTEXG210CardOperationalState,
       "ethernetNTEXG210CardSecondaryState": ethernetNTEXG210CardSecondaryState,
       "ethernetNTEXG210CardVoltage": ethernetNTEXG210CardVoltage,
       "ethernetNTEXG210CardTemperature": ethernetNTEXG210CardTemperature,
       "ethernetNTEXG210CardSnmpDyingGaspEnabled": ethernetNTEXG210CardSnmpDyingGaspEnabled,
       "ethernetNTEXG210CardRestartAction": ethernetNTEXG210CardRestartAction,
       "ethernetNTEXG210CardFineGrainedPmInterval": ethernetNTEXG210CardFineGrainedPmInterval,
       "ethernetXG1XCCCardTable": ethernetXG1XCCCardTable,
       "ethernetXG1XCCCardEntry": ethernetXG1XCCCardEntry,
       "ethernetXG1XCCCardEntityIndex": ethernetXG1XCCCardEntityIndex,
       "ethernetXG1XCCCardAdminState": ethernetXG1XCCCardAdminState,
       "ethernetXG1XCCCardOperationalState": ethernetXG1XCCCardOperationalState,
       "ethernetXG1XCCCardSecondaryState": ethernetXG1XCCCardSecondaryState,
       "ethernetXG1XCCCardVoltage": ethernetXG1XCCCardVoltage,
       "ethernetXG1XCCCardTemperature": ethernetXG1XCCCardTemperature,
       "ethernetXG1XCCCardRestartAction": ethernetXG1XCCCardRestartAction,
       "ethernetXG1XCCCardStorageType": ethernetXG1XCCCardStorageType,
       "ethernetXG1XCCCardRowStatus": ethernetXG1XCCCardRowStatus,
       "ethernetXG1SCCCardTable": ethernetXG1SCCCardTable,
       "ethernetXG1SCCCardEntry": ethernetXG1SCCCardEntry,
       "ethernetXG1SCCCardEntityIndex": ethernetXG1SCCCardEntityIndex,
       "ethernetXG1SCCCardAdminState": ethernetXG1SCCCardAdminState,
       "ethernetXG1SCCCardOperationalState": ethernetXG1SCCCardOperationalState,
       "ethernetXG1SCCCardSecondaryState": ethernetXG1SCCCardSecondaryState,
       "ethernetXG1SCCCardVoltage": ethernetXG1SCCCardVoltage,
       "ethernetXG1SCCCardTemperature": ethernetXG1SCCCardTemperature,
       "ethernetXG1SCCCardRestartAction": ethernetXG1SCCCardRestartAction,
       "ethernetXG1SCCCardStorageType": ethernetXG1SCCCardStorageType,
       "ethernetXG1SCCCardRowStatus": ethernetXG1SCCCardRowStatus,
       "ethernetOverOCSTMCardTable": ethernetOverOCSTMCardTable,
       "ethernetOverOCSTMCardEntry": ethernetOverOCSTMCardEntry,
       "ethernetOverOCSTMCardEntityIndex": ethernetOverOCSTMCardEntityIndex,
       "ethernetOverOCSTMCardAdminState": ethernetOverOCSTMCardAdminState,
       "ethernetOverOCSTMCardOperationalState": ethernetOverOCSTMCardOperationalState,
       "ethernetOverOCSTMCardSecondaryState": ethernetOverOCSTMCardSecondaryState,
       "ethernetOverOCSTMCardTemperature": ethernetOverOCSTMCardTemperature,
       "ethernetOverOCSTMCardSnmpDyingGaspEnabled": ethernetOverOCSTMCardSnmpDyingGaspEnabled,
       "ethernetOverOCSTMCardRestartAction": ethernetOverOCSTMCardRestartAction,
       "ethernetOverOCSTMCardStorageType": ethernetOverOCSTMCardStorageType,
       "ethernetOverOCSTMCardRowStatus": ethernetOverOCSTMCardRowStatus,
       "ethernetOverOCSTMCardForceOffLineAction": ethernetOverOCSTMCardForceOffLineAction,
       "ethernetOverOCSTMCardMode": ethernetOverOCSTMCardMode,
       "pseudoWireOcnStmCardTable": pseudoWireOcnStmCardTable,
       "pseudoWireOcnStmCardEntry": pseudoWireOcnStmCardEntry,
       "pseudoWireOcnStmCardEntityIndex": pseudoWireOcnStmCardEntityIndex,
       "pseudoWireOcnStmCardAdminState": pseudoWireOcnStmCardAdminState,
       "pseudoWireOcnStmCardOperationalState": pseudoWireOcnStmCardOperationalState,
       "pseudoWireOcnStmCardSecondaryState": pseudoWireOcnStmCardSecondaryState,
       "pseudoWireOcnStmCardIpAddress": pseudoWireOcnStmCardIpAddress,
       "pseudoWireOcnStmCardMode": pseudoWireOcnStmCardMode,
       "pseudoWireOcnStmCardVoltage": pseudoWireOcnStmCardVoltage,
       "pseudoWireOcnStmCardTemperature": pseudoWireOcnStmCardTemperature,
       "pseudoWireOcnStmCardRestartAction": pseudoWireOcnStmCardRestartAction,
       "pseudoWireOcnStmCardStorageType": pseudoWireOcnStmCardStorageType,
       "pseudoWireOcnStmCardRowStatus": pseudoWireOcnStmCardRowStatus,
       "pseudoWireOcnStmCardPSNEncapsulation": pseudoWireOcnStmCardPSNEncapsulation,
       "pseudoWireOcnStmCardFreqSourceType": pseudoWireOcnStmCardFreqSourceType,
       "pseudoWireOcnStmCardFreqSource": pseudoWireOcnStmCardFreqSource,
       "pseudoWireOcnStmCardForceOffLineAction": pseudoWireOcnStmCardForceOffLineAction,
       "pseudoWireE1T1CardTable": pseudoWireE1T1CardTable,
       "pseudoWireE1T1CardEntry": pseudoWireE1T1CardEntry,
       "pseudoWireE1T1CardEntityIndex": pseudoWireE1T1CardEntityIndex,
       "pseudoWireE1T1CardAdminState": pseudoWireE1T1CardAdminState,
       "pseudoWireE1T1CardOperationalState": pseudoWireE1T1CardOperationalState,
       "pseudoWireE1T1CardSecondaryState": pseudoWireE1T1CardSecondaryState,
       "pseudoWireE1T1CardIpAddress": pseudoWireE1T1CardIpAddress,
       "pseudoWireE1T1CardMode": pseudoWireE1T1CardMode,
       "pseudoWireE1T1CardVoltage": pseudoWireE1T1CardVoltage,
       "pseudoWireE1T1CardTemperature": pseudoWireE1T1CardTemperature,
       "pseudoWireE1T1CardRestartAction": pseudoWireE1T1CardRestartAction,
       "pseudoWireE1T1CardStorageType": pseudoWireE1T1CardStorageType,
       "pseudoWireE1T1CardRowStatus": pseudoWireE1T1CardRowStatus,
       "pseudoWireE1T1CardPSNEncapsulation": pseudoWireE1T1CardPSNEncapsulation,
       "ethernet1x10GHighPerCardTable": ethernet1x10GHighPerCardTable,
       "ethernet1x10GHighPerCardEntry": ethernet1x10GHighPerCardEntry,
       "ethernet1x10GHighPerCardEntityIndex": ethernet1x10GHighPerCardEntityIndex,
       "ethernet1x10GHighPerCardAdminState": ethernet1x10GHighPerCardAdminState,
       "ethernet1x10GHighPerCardOperationalState": ethernet1x10GHighPerCardOperationalState,
       "ethernet1x10GHighPerCardSecondaryState": ethernet1x10GHighPerCardSecondaryState,
       "ethernet1x10GHighPerCardTemperature": ethernet1x10GHighPerCardTemperature,
       "ethernet1x10GHighPerCardSnmpDyingGaspEnabled": ethernet1x10GHighPerCardSnmpDyingGaspEnabled,
       "ethernet1x10GHighPerCardRestartAction": ethernet1x10GHighPerCardRestartAction,
       "ethernet1x10GHighPerCardStorageType": ethernet1x10GHighPerCardStorageType,
       "ethernet1x10GHighPerCardRowStatus": ethernet1x10GHighPerCardRowStatus,
       "ethernet1x10GHighPerCardForceOffLineAction": ethernet1x10GHighPerCardForceOffLineAction,
       "ethernet10x1GHighPerCardTable": ethernet10x1GHighPerCardTable,
       "ethernet10x1GHighPerCardEntry": ethernet10x1GHighPerCardEntry,
       "ethernet10x1GHighPerCardEntityIndex": ethernet10x1GHighPerCardEntityIndex,
       "ethernet10x1GHighPerCardAdminState": ethernet10x1GHighPerCardAdminState,
       "ethernet10x1GHighPerCardOperationalState": ethernet10x1GHighPerCardOperationalState,
       "ethernet10x1GHighPerCardSecondaryState": ethernet10x1GHighPerCardSecondaryState,
       "ethernet10x1GHighPerCardTemperature": ethernet10x1GHighPerCardTemperature,
       "ethernet10x1GHighPerCardSnmpDyingGaspEnabled": ethernet10x1GHighPerCardSnmpDyingGaspEnabled,
       "ethernet10x1GHighPerCardRestartAction": ethernet10x1GHighPerCardRestartAction,
       "ethernet10x1GHighPerCardStorageType": ethernet10x1GHighPerCardStorageType,
       "ethernet10x1GHighPerCardRowStatus": ethernet10x1GHighPerCardRowStatus,
       "ethernet10x1GHighPerCardForceOffLineAction": ethernet10x1GHighPerCardForceOffLineAction,
       "ethernetNTET1804CardTable": ethernetNTET1804CardTable,
       "ethernetNTET1804CardEntry": ethernetNTET1804CardEntry,
       "ethernetNTET1804CardEntityIndex": ethernetNTET1804CardEntityIndex,
       "ethernetNTET1804CardAdminState": ethernetNTET1804CardAdminState,
       "ethernetNTET1804CardOperationalState": ethernetNTET1804CardOperationalState,
       "ethernetNTET1804CardSecondaryState": ethernetNTET1804CardSecondaryState,
       "ethernetNTET1804CardVoltage": ethernetNTET1804CardVoltage,
       "ethernetNTET1804CardTemperature": ethernetNTET1804CardTemperature,
       "ethernetNTET1804CardSnmpDyingGaspEnabled": ethernetNTET1804CardSnmpDyingGaspEnabled,
       "ethernetNTET1804CardRestartAction": ethernetNTET1804CardRestartAction,
       "ethernetNTET1804CardFineGrainedPmInterval": ethernetNTET1804CardFineGrainedPmInterval,
       "ethernetNTET1804CardMode": ethernetNTET1804CardMode,
       "ethernetNTET3204CardTable": ethernetNTET3204CardTable,
       "ethernetNTET3204CardEntry": ethernetNTET3204CardEntry,
       "ethernetNTET3204CardEntityIndex": ethernetNTET3204CardEntityIndex,
       "ethernetNTET3204CardAdminState": ethernetNTET3204CardAdminState,
       "ethernetNTET3204CardOperationalState": ethernetNTET3204CardOperationalState,
       "ethernetNTET3204CardSecondaryState": ethernetNTET3204CardSecondaryState,
       "ethernetNTET3204CardVoltage": ethernetNTET3204CardVoltage,
       "ethernetNTET3204CardTemperature": ethernetNTET3204CardTemperature,
       "ethernetNTET3204CardSnmpDyingGaspEnabled": ethernetNTET3204CardSnmpDyingGaspEnabled,
       "ethernetNTET3204CardRestartAction": ethernetNTET3204CardRestartAction,
       "ethernetNTET3204CardFineGrainedPmInterval": ethernetNTET3204CardFineGrainedPmInterval,
       "ethernetNTET3204CardMode": ethernetNTET3204CardMode,
       "ethernetNTEGESyncProbeCardTable": ethernetNTEGESyncProbeCardTable,
       "ethernetNTEGESyncProbeCardEntry": ethernetNTEGESyncProbeCardEntry,
       "ethernetNTEGESyncProbeCardEntityIndex": ethernetNTEGESyncProbeCardEntityIndex,
       "ethernetNTEGESyncProbeCardAdminState": ethernetNTEGESyncProbeCardAdminState,
       "ethernetNTEGESyncProbeCardOperationalState": ethernetNTEGESyncProbeCardOperationalState,
       "ethernetNTEGESyncProbeCardSecondaryState": ethernetNTEGESyncProbeCardSecondaryState,
       "ethernetNTEGESyncProbeCardVoltage": ethernetNTEGESyncProbeCardVoltage,
       "ethernetNTEGESyncProbeCardTemperature": ethernetNTEGESyncProbeCardTemperature,
       "ethernetNTEGESyncProbeCardSnmpDyingGaspEnabled": ethernetNTEGESyncProbeCardSnmpDyingGaspEnabled,
       "ethernetNTEGESyncProbeCardRestartAction": ethernetNTEGESyncProbeCardRestartAction,
       "ethernetNTEGESyncProbeCardFineGrainedPmInterval": ethernetNTEGESyncProbeCardFineGrainedPmInterval,
       "ethernetGE8SCCCardTable": ethernetGE8SCCCardTable,
       "ethernetGE8SCCCardEntry": ethernetGE8SCCCardEntry,
       "ethernetGE8SCCCardEntityIndex": ethernetGE8SCCCardEntityIndex,
       "ethernetGE8SCCCardAdminState": ethernetGE8SCCCardAdminState,
       "ethernetGE8SCCCardOperationalState": ethernetGE8SCCCardOperationalState,
       "ethernetGE8SCCCardSecondaryState": ethernetGE8SCCCardSecondaryState,
       "ethernetGE8SCCCardVoltage": ethernetGE8SCCCardVoltage,
       "ethernetGE8SCCCardTemperature": ethernetGE8SCCCardTemperature,
       "ethernetGE8SCCCardRestartAction": ethernetGE8SCCCardRestartAction,
       "ethernetGE8SCCCardStorageType": ethernetGE8SCCCardStorageType,
       "ethernetGE8SCCCardRowStatus": ethernetGE8SCCCardRowStatus,
       "ethernetNTEGE114HCardTable": ethernetNTEGE114HCardTable,
       "ethernetNTEGE114HCardEntry": ethernetNTEGE114HCardEntry,
       "ethernetNTEGE114HCardEntityIndex": ethernetNTEGE114HCardEntityIndex,
       "ethernetNTEGE114HCardAdminState": ethernetNTEGE114HCardAdminState,
       "ethernetNTEGE114HCardOperationalState": ethernetNTEGE114HCardOperationalState,
       "ethernetNTEGE114HCardSecondaryState": ethernetNTEGE114HCardSecondaryState,
       "ethernetNTEGE114HCardVoltage": ethernetNTEGE114HCardVoltage,
       "ethernetNTEGE114HCardTemperature": ethernetNTEGE114HCardTemperature,
       "ethernetNTEGE114HCardSnmpDyingGaspEnabled": ethernetNTEGE114HCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114HCardRestartAction": ethernetNTEGE114HCardRestartAction,
       "ethernetNTEGE114HCardFineGrainedPmInterval": ethernetNTEGE114HCardFineGrainedPmInterval,
       "ethernetNTEGE114HCardSwitchPortActionPort": ethernetNTEGE114HCardSwitchPortActionPort,
       "ethernetNTEGE114HCardSwitchPortAction": ethernetNTEGE114HCardSwitchPortAction,
       "ethernetNTEGE114PHCardTable": ethernetNTEGE114PHCardTable,
       "ethernetNTEGE114PHCardEntry": ethernetNTEGE114PHCardEntry,
       "ethernetNTEGE114PHCardEntityIndex": ethernetNTEGE114PHCardEntityIndex,
       "ethernetNTEGE114PHCardAdminState": ethernetNTEGE114PHCardAdminState,
       "ethernetNTEGE114PHCardOperationalState": ethernetNTEGE114PHCardOperationalState,
       "ethernetNTEGE114PHCardSecondaryState": ethernetNTEGE114PHCardSecondaryState,
       "ethernetNTEGE114PHCardVoltage": ethernetNTEGE114PHCardVoltage,
       "ethernetNTEGE114PHCardTemperature": ethernetNTEGE114PHCardTemperature,
       "ethernetNTEGE114PHCardSnmpDyingGaspEnabled": ethernetNTEGE114PHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114PHCardRestartAction": ethernetNTEGE114PHCardRestartAction,
       "ethernetNTEGE114PHCardFineGrainedPmInterval": ethernetNTEGE114PHCardFineGrainedPmInterval,
       "ethernetNTEGE114PHCardSwitchPortActionPort": ethernetNTEGE114PHCardSwitchPortActionPort,
       "ethernetNTEGE114PHCardSwitchPortAction": ethernetNTEGE114PHCardSwitchPortAction,
       "ethernetFE36ECardTable": ethernetFE36ECardTable,
       "ethernetFE36ECardEntry": ethernetFE36ECardEntry,
       "ethernetFE36ECardEntityIndex": ethernetFE36ECardEntityIndex,
       "ethernetFE36ECardAdminState": ethernetFE36ECardAdminState,
       "ethernetFE36ECardOperationalState": ethernetFE36ECardOperationalState,
       "ethernetFE36ECardSecondaryState": ethernetFE36ECardSecondaryState,
       "ethernetFE36ECardTemperature": ethernetFE36ECardTemperature,
       "ethernetFE36ECardRestartAction": ethernetFE36ECardRestartAction,
       "ethernetFE36ECardStorageType": ethernetFE36ECardStorageType,
       "ethernetFE36ECardRowStatus": ethernetFE36ECardRowStatus,
       "ethernetFE36ECardForceOffLineAction": ethernetFE36ECardForceOffLineAction,
       "ethernetFE36ECard8023azEnabled": ethernetFE36ECard8023azEnabled,
       "ethernetNTEGE114SHCardTable": ethernetNTEGE114SHCardTable,
       "ethernetNTEGE114SHCardEntry": ethernetNTEGE114SHCardEntry,
       "ethernetNTEGE114SHCardEntityIndex": ethernetNTEGE114SHCardEntityIndex,
       "ethernetNTEGE114SHCardAdminState": ethernetNTEGE114SHCardAdminState,
       "ethernetNTEGE114SHCardOperationalState": ethernetNTEGE114SHCardOperationalState,
       "ethernetNTEGE114SHCardSecondaryState": ethernetNTEGE114SHCardSecondaryState,
       "ethernetNTEGE114SHCardVoltage": ethernetNTEGE114SHCardVoltage,
       "ethernetNTEGE114SHCardTemperature": ethernetNTEGE114SHCardTemperature,
       "ethernetNTEGE114SHCardSnmpDyingGaspEnabled": ethernetNTEGE114SHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114SHCardRestartAction": ethernetNTEGE114SHCardRestartAction,
       "ethernetNTEGE114SHCardFineGrainedPmInterval": ethernetNTEGE114SHCardFineGrainedPmInterval,
       "ethernetNTEGE114SHCardSwitchPortActionPort": ethernetNTEGE114SHCardSwitchPortActionPort,
       "ethernetNTEGE114SHCardSwitchPortAction": ethernetNTEGE114SHCardSwitchPortAction,
       "ethernetNTEGE114SCardTable": ethernetNTEGE114SCardTable,
       "ethernetNTEGE114SCardEntry": ethernetNTEGE114SCardEntry,
       "ethernetNTEGE114SCardEntityIndex": ethernetNTEGE114SCardEntityIndex,
       "ethernetNTEGE114SCardAdminState": ethernetNTEGE114SCardAdminState,
       "ethernetNTEGE114SCardOperationalState": ethernetNTEGE114SCardOperationalState,
       "ethernetNTEGE114SCardSecondaryState": ethernetNTEGE114SCardSecondaryState,
       "ethernetNTEGE114SCardVoltage": ethernetNTEGE114SCardVoltage,
       "ethernetNTEGE114SCardTemperature": ethernetNTEGE114SCardTemperature,
       "ethernetNTEGE114SCardSnmpDyingGaspEnabled": ethernetNTEGE114SCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114SCardRestartAction": ethernetNTEGE114SCardRestartAction,
       "ethernetNTEGE114SCardFineGrainedPmInterval": ethernetNTEGE114SCardFineGrainedPmInterval,
       "ethernetNTEGE114SCardSwitchPortActionPort": ethernetNTEGE114SCardSwitchPortActionPort,
       "ethernetNTEGE114SCardSwitchPortAction": ethernetNTEGE114SCardSwitchPortAction,
       "stuHighPerCardTable": stuHighPerCardTable,
       "stuHighPerCardEntry": stuHighPerCardEntry,
       "stuHighPerCardEntityIndex": stuHighPerCardEntityIndex,
       "stuHighPerCardAdminState": stuHighPerCardAdminState,
       "stuHighPerCardOperationalState": stuHighPerCardOperationalState,
       "stuHighPerCardSecondaryState": stuHighPerCardSecondaryState,
       "stuHighPerCardTemperature": stuHighPerCardTemperature,
       "stuHighPerCardRestartAction": stuHighPerCardRestartAction,
       "stuHighPerCardStorageType": stuHighPerCardStorageType,
       "stuHighPerCardRowStatus": stuHighPerCardRowStatus,
       "stuHighPerCardForceOffLineAction": stuHighPerCardForceOffLineAction,
       "stiHighPerTable": stiHighPerTable,
       "stiHighPerEntry": stiHighPerEntry,
       "stiHighPerEntityIndex": stiHighPerEntityIndex,
       "stiHighPerAdminState": stiHighPerAdminState,
       "stiHighPerOperationalState": stiHighPerOperationalState,
       "stiHighPerSecondaryState": stiHighPerSecondaryState,
       "stiHighPerTemperature": stiHighPerTemperature,
       "stiHighPerStorageType": stiHighPerStorageType,
       "stiHighPerRowStatus": stiHighPerRowStatus,
       "ethernetGE8ECCCardTable": ethernetGE8ECCCardTable,
       "ethernetGE8ECCCardEntry": ethernetGE8ECCCardEntry,
       "ethernetGE8ECCCardEntityIndex": ethernetGE8ECCCardEntityIndex,
       "ethernetGE8ECCCardAdminState": ethernetGE8ECCCardAdminState,
       "ethernetGE8ECCCardOperationalState": ethernetGE8ECCCardOperationalState,
       "ethernetGE8ECCCardSecondaryState": ethernetGE8ECCCardSecondaryState,
       "ethernetGE8ECCCardVoltage": ethernetGE8ECCCardVoltage,
       "ethernetGE8ECCCardTemperature": ethernetGE8ECCCardTemperature,
       "ethernetGE8ECCCardRestartAction": ethernetGE8ECCCardRestartAction,
       "ethernetGE8ECCCardStorageType": ethernetGE8ECCCardStorageType,
       "ethernetGE8ECCCardRowStatus": ethernetGE8ECCCardRowStatus,
       "networkElementLLDPParamsTable": networkElementLLDPParamsTable,
       "networkElementLLDPParamsEntry": networkElementLLDPParamsEntry,
       "neLLDPParamsLLDPEnableAction": neLLDPParamsLLDPEnableAction,
       "ethernetNTESH1PCSCardTable": ethernetNTESH1PCSCardTable,
       "ethernetNTESH1PCSCardEntry": ethernetNTESH1PCSCardEntry,
       "ethernetNTESH1PCSCardEntityIndex": ethernetNTESH1PCSCardEntityIndex,
       "ethernetNTESH1PCSCardAdminState": ethernetNTESH1PCSCardAdminState,
       "ethernetNTESH1PCSCardOperationalState": ethernetNTESH1PCSCardOperationalState,
       "ethernetNTESH1PCSCardSecondaryState": ethernetNTESH1PCSCardSecondaryState,
       "ethernetNTESH1PCSCardVoltage": ethernetNTESH1PCSCardVoltage,
       "ethernetNTESH1PCSCardTemperature": ethernetNTESH1PCSCardTemperature,
       "ethernetNTESH1PCSCardSnmpDyingGaspEnabled": ethernetNTESH1PCSCardSnmpDyingGaspEnabled,
       "ethernetNTESH1PCSCardRestartAction": ethernetNTESH1PCSCardRestartAction,
       "ethernetNTESH1PCSCardFineGrainedPmInterval": ethernetNTESH1PCSCardFineGrainedPmInterval,
       "ethernetNTEOSA5411CardTable": ethernetNTEOSA5411CardTable,
       "ethernetNTEOSA5411CardEntry": ethernetNTEOSA5411CardEntry,
       "ethernetNTEOSA5411CardEntityIndex": ethernetNTEOSA5411CardEntityIndex,
       "ethernetNTEOSA5411CardAdminState": ethernetNTEOSA5411CardAdminState,
       "ethernetNTEOSA5411CardOperationalState": ethernetNTEOSA5411CardOperationalState,
       "ethernetNTEOSA5411CardSecondaryState": ethernetNTEOSA5411CardSecondaryState,
       "ethernetNTEOSA5411CardVoltage": ethernetNTEOSA5411CardVoltage,
       "ethernetNTEOSA5411CardTemperature": ethernetNTEOSA5411CardTemperature,
       "ethernetNTEOSA5411CardSnmpDyingGaspEnabled": ethernetNTEOSA5411CardSnmpDyingGaspEnabled,
       "ethernetNTEOSA5411CardRestartAction": ethernetNTEOSA5411CardRestartAction,
       "ethernetNTEOSA5411CardFineGrainedPmInterval": ethernetNTEOSA5411CardFineGrainedPmInterval,
       "ethernetNTEGE112ProCardTable": ethernetNTEGE112ProCardTable,
       "ethernetNTEGE112ProCardEntry": ethernetNTEGE112ProCardEntry,
       "ethernetNTEGE112ProCardEntityIndex": ethernetNTEGE112ProCardEntityIndex,
       "ethernetNTEGE112ProCardAdminState": ethernetNTEGE112ProCardAdminState,
       "ethernetNTEGE112ProCardOperationalState": ethernetNTEGE112ProCardOperationalState,
       "ethernetNTEGE112ProCardSecondaryState": ethernetNTEGE112ProCardSecondaryState,
       "ethernetNTEGE112ProCardVoltage": ethernetNTEGE112ProCardVoltage,
       "ethernetNTEGE112ProCardTemperature": ethernetNTEGE112ProCardTemperature,
       "ethernetNTEGE112ProCardSnmpDyingGaspEnabled": ethernetNTEGE112ProCardSnmpDyingGaspEnabled,
       "ethernetNTEGE112ProCardRestartAction": ethernetNTEGE112ProCardRestartAction,
       "ethernetNTEGE112ProCardFineGrainedPmInterval": ethernetNTEGE112ProCardFineGrainedPmInterval,
       "ethernetNTEGE112ProCardSwitchPortActionPort": ethernetNTEGE112ProCardSwitchPortActionPort,
       "ethernetNTEGE112ProCardSwitchPortAction": ethernetNTEGE112ProCardSwitchPortAction,
       "ethernetNTEGE112ProMCardTable": ethernetNTEGE112ProMCardTable,
       "ethernetNTEGE112ProMCardEntry": ethernetNTEGE112ProMCardEntry,
       "ethernetNTEGE112ProMCardEntityIndex": ethernetNTEGE112ProMCardEntityIndex,
       "ethernetNTEGE112ProMCardAdminState": ethernetNTEGE112ProMCardAdminState,
       "ethernetNTEGE112ProMCardOperationalState": ethernetNTEGE112ProMCardOperationalState,
       "ethernetNTEGE112ProMCardSecondaryState": ethernetNTEGE112ProMCardSecondaryState,
       "ethernetNTEGE112ProMCardVoltage": ethernetNTEGE112ProMCardVoltage,
       "ethernetNTEGE112ProMCardTemperature": ethernetNTEGE112ProMCardTemperature,
       "ethernetNTEGE112ProMCardSnmpDyingGaspEnabled": ethernetNTEGE112ProMCardSnmpDyingGaspEnabled,
       "ethernetNTEGE112ProMCardRestartAction": ethernetNTEGE112ProMCardRestartAction,
       "ethernetNTEGE112ProMCardFineGrainedPmInterval": ethernetNTEGE112ProMCardFineGrainedPmInterval,
       "ethernetNTEGE112ProMCardSwitchPortActionPort": ethernetNTEGE112ProMCardSwitchPortActionPort,
       "ethernetNTEGE112ProMCardSwitchPortAction": ethernetNTEGE112ProMCardSwitchPortAction,
       "ethernetNTEXG210CCardTable": ethernetNTEXG210CCardTable,
       "ethernetNTEXG210CCardEntry": ethernetNTEXG210CCardEntry,
       "ethernetNTEXG210CCardEntityIndex": ethernetNTEXG210CCardEntityIndex,
       "ethernetNTEXG210CCardAdminState": ethernetNTEXG210CCardAdminState,
       "ethernetNTEXG210CCardOperationalState": ethernetNTEXG210CCardOperationalState,
       "ethernetNTEXG210CCardSecondaryState": ethernetNTEXG210CCardSecondaryState,
       "ethernetNTEXG210CCardVoltage": ethernetNTEXG210CCardVoltage,
       "ethernetNTEXG210CCardTemperature": ethernetNTEXG210CCardTemperature,
       "ethernetNTEXG210CCardSnmpDyingGaspEnabled": ethernetNTEXG210CCardSnmpDyingGaspEnabled,
       "ethernetNTEXG210CCardRestartAction": ethernetNTEXG210CCardRestartAction,
       "ethernetNTEXG210CCardFineGrainedPmInterval": ethernetNTEXG210CCardFineGrainedPmInterval,
       "ethernetGE8SCryptoConnectorCardTable": ethernetGE8SCryptoConnectorCardTable,
       "ethernetGE8SCryptoConnectorCardEntry": ethernetGE8SCryptoConnectorCardEntry,
       "ethernetGE8SCryptoConnectorCardEntityIndex": ethernetGE8SCryptoConnectorCardEntityIndex,
       "ethernetGE8SCryptoConnectorCardAdminState": ethernetGE8SCryptoConnectorCardAdminState,
       "ethernetGE8SCryptoConnectorCardOperationalState": ethernetGE8SCryptoConnectorCardOperationalState,
       "ethernetGE8SCryptoConnectorCardSecondaryState": ethernetGE8SCryptoConnectorCardSecondaryState,
       "ethernetGE8SCryptoConnectorCardVoltage": ethernetGE8SCryptoConnectorCardVoltage,
       "ethernetGE8SCryptoConnectorCardTemperature": ethernetGE8SCryptoConnectorCardTemperature,
       "ethernetGE8SCryptoConnectorCardRestartAction": ethernetGE8SCryptoConnectorCardRestartAction,
       "ethernetGE8SCryptoConnectorCardStorageType": ethernetGE8SCryptoConnectorCardStorageType,
       "ethernetGE8SCryptoConnectorCardRowStatus": ethernetGE8SCryptoConnectorCardRowStatus,
       "ethernetNTEGE114ProCardTable": ethernetNTEGE114ProCardTable,
       "ethernetNTEGE114ProCardEntry": ethernetNTEGE114ProCardEntry,
       "ethernetNTEGE114ProCardEntityIndex": ethernetNTEGE114ProCardEntityIndex,
       "ethernetNTEGE114ProCardAdminState": ethernetNTEGE114ProCardAdminState,
       "ethernetNTEGE114ProCardOperationalState": ethernetNTEGE114ProCardOperationalState,
       "ethernetNTEGE114ProCardSecondaryState": ethernetNTEGE114ProCardSecondaryState,
       "ethernetNTEGE114ProCardVoltage": ethernetNTEGE114ProCardVoltage,
       "ethernetNTEGE114ProCardTemperature": ethernetNTEGE114ProCardTemperature,
       "ethernetNTEGE114ProCardSnmpDyingGaspEnabled": ethernetNTEGE114ProCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProCardRestartAction": ethernetNTEGE114ProCardRestartAction,
       "ethernetNTEGE114ProCardFineGrainedPmInterval": ethernetNTEGE114ProCardFineGrainedPmInterval,
       "ethernetNTEGE114ProCardSwitchPortActionPort": ethernetNTEGE114ProCardSwitchPortActionPort,
       "ethernetNTEGE114ProCardSwitchPortAction": ethernetNTEGE114ProCardSwitchPortAction,
       "ethernetNTEGE114ProCCardTable": ethernetNTEGE114ProCCardTable,
       "ethernetNTEGE114ProCCardEntry": ethernetNTEGE114ProCCardEntry,
       "ethernetNTEGE114ProCCardEntityIndex": ethernetNTEGE114ProCCardEntityIndex,
       "ethernetNTEGE114ProCCardAdminState": ethernetNTEGE114ProCCardAdminState,
       "ethernetNTEGE114ProCCardOperationalState": ethernetNTEGE114ProCCardOperationalState,
       "ethernetNTEGE114ProCCardSecondaryState": ethernetNTEGE114ProCCardSecondaryState,
       "ethernetNTEGE114ProCCardVoltage": ethernetNTEGE114ProCCardVoltage,
       "ethernetNTEGE114ProCCardTemperature": ethernetNTEGE114ProCCardTemperature,
       "ethernetNTEGE114ProCCardSnmpDyingGaspEnabled": ethernetNTEGE114ProCCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProCCardRestartAction": ethernetNTEGE114ProCCardRestartAction,
       "ethernetNTEGE114ProCCardFineGrainedPmInterval": ethernetNTEGE114ProCCardFineGrainedPmInterval,
       "ethernetNTEGE114ProCCardSwitchPortActionPort": ethernetNTEGE114ProCCardSwitchPortActionPort,
       "ethernetNTEGE114ProCCardSwitchPortAction": ethernetNTEGE114ProCCardSwitchPortAction,
       "ethernetNTEGE114ProSHCardTable": ethernetNTEGE114ProSHCardTable,
       "ethernetNTEGE114ProSHCardEntry": ethernetNTEGE114ProSHCardEntry,
       "ethernetNTEGE114ProSHCardEntityIndex": ethernetNTEGE114ProSHCardEntityIndex,
       "ethernetNTEGE114ProSHCardAdminState": ethernetNTEGE114ProSHCardAdminState,
       "ethernetNTEGE114ProSHCardOperationalState": ethernetNTEGE114ProSHCardOperationalState,
       "ethernetNTEGE114ProSHCardSecondaryState": ethernetNTEGE114ProSHCardSecondaryState,
       "ethernetNTEGE114ProSHCardVoltage": ethernetNTEGE114ProSHCardVoltage,
       "ethernetNTEGE114ProSHCardTemperature": ethernetNTEGE114ProSHCardTemperature,
       "ethernetNTEGE114ProSHCardSnmpDyingGaspEnabled": ethernetNTEGE114ProSHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProSHCardRestartAction": ethernetNTEGE114ProSHCardRestartAction,
       "ethernetNTEGE114ProSHCardFineGrainedPmInterval": ethernetNTEGE114ProSHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProSHCardSwitchPortActionPort": ethernetNTEGE114ProSHCardSwitchPortActionPort,
       "ethernetNTEGE114ProSHCardSwitchPortAction": ethernetNTEGE114ProSHCardSwitchPortAction,
       "ethernetNTEGE114ProCSHCardTable": ethernetNTEGE114ProCSHCardTable,
       "ethernetNTEGE114ProCSHCardEntry": ethernetNTEGE114ProCSHCardEntry,
       "ethernetNTEGE114ProCSHCardEntityIndex": ethernetNTEGE114ProCSHCardEntityIndex,
       "ethernetNTEGE114ProCSHCardAdminState": ethernetNTEGE114ProCSHCardAdminState,
       "ethernetNTEGE114ProCSHCardOperationalState": ethernetNTEGE114ProCSHCardOperationalState,
       "ethernetNTEGE114ProCSHCardSecondaryState": ethernetNTEGE114ProCSHCardSecondaryState,
       "ethernetNTEGE114ProCSHCardVoltage": ethernetNTEGE114ProCSHCardVoltage,
       "ethernetNTEGE114ProCSHCardTemperature": ethernetNTEGE114ProCSHCardTemperature,
       "ethernetNTEGE114ProCSHCardSnmpDyingGaspEnabled": ethernetNTEGE114ProCSHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProCSHCardRestartAction": ethernetNTEGE114ProCSHCardRestartAction,
       "ethernetNTEGE114ProCSHCardFineGrainedPmInterval": ethernetNTEGE114ProCSHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProCSHCardSwitchPortActionPort": ethernetNTEGE114ProCSHCardSwitchPortActionPort,
       "ethernetNTEGE114ProCSHCardSwitchPortAction": ethernetNTEGE114ProCSHCardSwitchPortAction,
       "ethernetNTEGE114ProHECardTable": ethernetNTEGE114ProHECardTable,
       "ethernetNTEGE114ProHECardEntry": ethernetNTEGE114ProHECardEntry,
       "ethernetNTEGE114ProHECardEntityIndex": ethernetNTEGE114ProHECardEntityIndex,
       "ethernetNTEGE114ProHECardAdminState": ethernetNTEGE114ProHECardAdminState,
       "ethernetNTEGE114ProHECardOperationalState": ethernetNTEGE114ProHECardOperationalState,
       "ethernetNTEGE114ProHECardSecondaryState": ethernetNTEGE114ProHECardSecondaryState,
       "ethernetNTEGE114ProHECardVoltage": ethernetNTEGE114ProHECardVoltage,
       "ethernetNTEGE114ProHECardTemperature": ethernetNTEGE114ProHECardTemperature,
       "ethernetNTEGE114ProHECardSnmpDyingGaspEnabled": ethernetNTEGE114ProHECardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProHECardRestartAction": ethernetNTEGE114ProHECardRestartAction,
       "ethernetNTEGE114ProHECardFineGrainedPmInterval": ethernetNTEGE114ProHECardFineGrainedPmInterval,
       "ethernetNTEGE114ProHECardSwitchPortActionPort": ethernetNTEGE114ProHECardSwitchPortActionPort,
       "ethernetNTEGE114ProHECardSwitchPortAction": ethernetNTEGE114ProHECardSwitchPortAction,
       "ethernetNTEGE112ProHCardTable": ethernetNTEGE112ProHCardTable,
       "ethernetNTEGE112ProHCardEntry": ethernetNTEGE112ProHCardEntry,
       "ethernetNTEGE112ProHCardEntityIndex": ethernetNTEGE112ProHCardEntityIndex,
       "ethernetNTEGE112ProHCardAdminState": ethernetNTEGE112ProHCardAdminState,
       "ethernetNTEGE112ProHCardOperationalState": ethernetNTEGE112ProHCardOperationalState,
       "ethernetNTEGE112ProHCardSecondaryState": ethernetNTEGE112ProHCardSecondaryState,
       "ethernetNTEGE112ProHCardVoltage": ethernetNTEGE112ProHCardVoltage,
       "ethernetNTEGE112ProHCardTemperature": ethernetNTEGE112ProHCardTemperature,
       "ethernetNTEGE112ProHCardSnmpDyingGaspEnabled": ethernetNTEGE112ProHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE112ProHCardRestartAction": ethernetNTEGE112ProHCardRestartAction,
       "ethernetNTEGE112ProHCardFineGrainedPmInterval": ethernetNTEGE112ProHCardFineGrainedPmInterval,
       "ethernetNTEGE112ProHCardSwitchPortActionPort": ethernetNTEGE112ProHCardSwitchPortActionPort,
       "ethernetNTEGE112ProHCardSwitchPortAction": ethernetNTEGE112ProHCardSwitchPortAction,
       "ethernetNTEOSA5420CardTable": ethernetNTEOSA5420CardTable,
       "ethernetNTEOSA5420CardEntry": ethernetNTEOSA5420CardEntry,
       "ethernetNTEOSA5420CardEntityIndex": ethernetNTEOSA5420CardEntityIndex,
       "ethernetNTEOSA5420CardAdminState": ethernetNTEOSA5420CardAdminState,
       "ethernetNTEOSA5420CardOperationalState": ethernetNTEOSA5420CardOperationalState,
       "ethernetNTEOSA5420CardSecondaryState": ethernetNTEOSA5420CardSecondaryState,
       "ethernetNTEOSA5420CardVoltage": ethernetNTEOSA5420CardVoltage,
       "ethernetNTEOSA5420CardTemperature": ethernetNTEOSA5420CardTemperature,
       "ethernetNTEOSA5420CardSnmpDyingGaspEnabled": ethernetNTEOSA5420CardSnmpDyingGaspEnabled,
       "ethernetNTEOSA5420CardRestartAction": ethernetNTEOSA5420CardRestartAction,
       "ethernetNTEOSA5420CardFineGrainedPmInterval": ethernetNTEOSA5420CardFineGrainedPmInterval,
       "ethernetNTEOSA5421CardTable": ethernetNTEOSA5421CardTable,
       "ethernetNTEOSA5421CardEntry": ethernetNTEOSA5421CardEntry,
       "ethernetNTEOSA5421CardEntityIndex": ethernetNTEOSA5421CardEntityIndex,
       "ethernetNTEOSA5421CardAdminState": ethernetNTEOSA5421CardAdminState,
       "ethernetNTEOSA5421CardOperationalState": ethernetNTEOSA5421CardOperationalState,
       "ethernetNTEOSA5421CardSecondaryState": ethernetNTEOSA5421CardSecondaryState,
       "ethernetNTEOSA5421CardVoltage": ethernetNTEOSA5421CardVoltage,
       "ethernetNTEOSA5421CardTemperature": ethernetNTEOSA5421CardTemperature,
       "ethernetNTEOSA5421CardSnmpDyingGaspEnabled": ethernetNTEOSA5421CardSnmpDyingGaspEnabled,
       "ethernetNTEOSA5421CardRestartAction": ethernetNTEOSA5421CardRestartAction,
       "ethernetNTEOSA5421CardFineGrainedPmInterval": ethernetNTEOSA5421CardFineGrainedPmInterval,
       "ethernetNTEGE114GCardTable": ethernetNTEGE114GCardTable,
       "ethernetNTEGE114GCardEntry": ethernetNTEGE114GCardEntry,
       "ethernetNTEGE114GCardEntityIndex": ethernetNTEGE114GCardEntityIndex,
       "ethernetNTEGE114GCardAdminState": ethernetNTEGE114GCardAdminState,
       "ethernetNTEGE114GCardOperationalState": ethernetNTEGE114GCardOperationalState,
       "ethernetNTEGE114GCardSecondaryState": ethernetNTEGE114GCardSecondaryState,
       "ethernetNTEGE114GCardVoltage": ethernetNTEGE114GCardVoltage,
       "ethernetNTEGE114GCardTemperature": ethernetNTEGE114GCardTemperature,
       "ethernetNTEGE114GCardSnmpDyingGaspEnabled": ethernetNTEGE114GCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114GCardRestartAction": ethernetNTEGE114GCardRestartAction,
       "ethernetNTEGE114GCardFineGrainedPmInterval": ethernetNTEGE114GCardFineGrainedPmInterval,
       "ethernetNTEGE114GCardSwitchPortActionPort": ethernetNTEGE114GCardSwitchPortActionPort,
       "ethernetNTEGE114GCardSwitchPortAction": ethernetNTEGE114GCardSwitchPortAction,
       "bits16PortCardTable": bits16PortCardTable,
       "bits16PortCardEntry": bits16PortCardEntry,
       "bits16PortCardEntityIndex": bits16PortCardEntityIndex,
       "bits16PortCardAdminState": bits16PortCardAdminState,
       "bits16PortCardOperationalState": bits16PortCardOperationalState,
       "bits16PortCardSecondaryState": bits16PortCardSecondaryState,
       "bits16PortCardRowStatus": bits16PortCardRowStatus,
       "bits16PortCardAlias": bits16PortCardAlias,
       "bits16PortCardTemperature": bits16PortCardTemperature,
       "ethernetNTEGE114ProVmHCardTable": ethernetNTEGE114ProVmHCardTable,
       "ethernetNTEGE114ProVmHCardEntry": ethernetNTEGE114ProVmHCardEntry,
       "ethernetNTEGE114ProVmHCardEntityIndex": ethernetNTEGE114ProVmHCardEntityIndex,
       "ethernetNTEGE114ProVmHCardAdminState": ethernetNTEGE114ProVmHCardAdminState,
       "ethernetNTEGE114ProVmHCardOperationalState": ethernetNTEGE114ProVmHCardOperationalState,
       "ethernetNTEGE114ProVmHCardSecondaryState": ethernetNTEGE114ProVmHCardSecondaryState,
       "ethernetNTEGE114ProVmHCardVoltage": ethernetNTEGE114ProVmHCardVoltage,
       "ethernetNTEGE114ProVmHCardTemperature": ethernetNTEGE114ProVmHCardTemperature,
       "ethernetNTEGE114ProVmHCardSnmpDyingGaspEnabled": ethernetNTEGE114ProVmHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProVmHCardRestartAction": ethernetNTEGE114ProVmHCardRestartAction,
       "ethernetNTEGE114ProVmHCardFineGrainedPmInterval": ethernetNTEGE114ProVmHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProVmHCardSwitchPortActionPort": ethernetNTEGE114ProVmHCardSwitchPortActionPort,
       "ethernetNTEGE114ProVmHCardSwitchPortAction": ethernetNTEGE114ProVmHCardSwitchPortAction,
       "ethernetNTEGE114ProVmCHCardTable": ethernetNTEGE114ProVmCHCardTable,
       "ethernetNTEGE114ProVmCHCardEntry": ethernetNTEGE114ProVmCHCardEntry,
       "ethernetNTEGE114ProVmCHCardEntityIndex": ethernetNTEGE114ProVmCHCardEntityIndex,
       "ethernetNTEGE114ProVmCHCardAdminState": ethernetNTEGE114ProVmCHCardAdminState,
       "ethernetNTEGE114ProVmCHCardOperationalState": ethernetNTEGE114ProVmCHCardOperationalState,
       "ethernetNTEGE114ProVmCHCardSecondaryState": ethernetNTEGE114ProVmCHCardSecondaryState,
       "ethernetNTEGE114ProVmCHCardVoltage": ethernetNTEGE114ProVmCHCardVoltage,
       "ethernetNTEGE114ProVmCHCardTemperature": ethernetNTEGE114ProVmCHCardTemperature,
       "ethernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled": ethernetNTEGE114ProVmCHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProVmCHCardRestartAction": ethernetNTEGE114ProVmCHCardRestartAction,
       "ethernetNTEGE114ProVmCHCardFineGrainedPmInterval": ethernetNTEGE114ProVmCHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProVmCHCardSwitchPortActionPort": ethernetNTEGE114ProVmCHCardSwitchPortActionPort,
       "ethernetNTEGE114ProVmCHCardSwitchPortAction": ethernetNTEGE114ProVmCHCardSwitchPortAction,
       "ethernetNTEGE114ProVmCSHCardTable": ethernetNTEGE114ProVmCSHCardTable,
       "ethernetNTEGE114ProVmCSHCardEntry": ethernetNTEGE114ProVmCSHCardEntry,
       "ethernetNTEGE114ProVmCSHCardEntityIndex": ethernetNTEGE114ProVmCSHCardEntityIndex,
       "ethernetNTEGE114ProVmCSHCardAdminState": ethernetNTEGE114ProVmCSHCardAdminState,
       "ethernetNTEGE114ProVmCSHCardOperationalState": ethernetNTEGE114ProVmCSHCardOperationalState,
       "ethernetNTEGE114ProVmCSHCardSecondaryState": ethernetNTEGE114ProVmCSHCardSecondaryState,
       "ethernetNTEGE114ProVmCSHCardVoltage": ethernetNTEGE114ProVmCSHCardVoltage,
       "ethernetNTEGE114ProVmCSHCardTemperature": ethernetNTEGE114ProVmCSHCardTemperature,
       "ethernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled": ethernetNTEGE114ProVmCSHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProVmCSHCardRestartAction": ethernetNTEGE114ProVmCSHCardRestartAction,
       "ethernetNTEGE114ProVmCSHCardFineGrainedPmInterval": ethernetNTEGE114ProVmCSHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProVmCSHCardSwitchPortActionPort": ethernetNTEGE114ProVmCSHCardSwitchPortActionPort,
       "ethernetNTEGE114ProVmCSHCardSwitchPortAction": ethernetNTEGE114ProVmCSHCardSwitchPortAction,
       "serverCardTable": serverCardTable,
       "serverCardEntry": serverCardEntry,
       "serverCardEntityIndex": serverCardEntityIndex,
       "serverCardAdminState": serverCardAdminState,
       "serverCardOperationalState": serverCardOperationalState,
       "serverCardSecondaryState": serverCardSecondaryState,
       "serverCardStorageType": serverCardStorageType,
       "serverCardVoltage": serverCardVoltage,
       "serverCardTemperature": serverCardTemperature,
       "serverCardUpTime": serverCardUpTime,
       "serverCardVmNumber": serverCardVmNumber,
       "serverCardVirtualCpuTotal": serverCardVirtualCpuTotal,
       "serverCardVirtualCpuAvailiable": serverCardVirtualCpuAvailiable,
       "serverCardMemoryTotal": serverCardMemoryTotal,
       "serverCardMemoryAvailiable": serverCardMemoryAvailiable,
       "serverCardStorageTotal": serverCardStorageTotal,
       "serverCardStorageAvailiable": serverCardStorageAvailiable,
       "serverCardHvVersion": serverCardHvVersion,
       "serverCardHostName": serverCardHostName,
       "serverCardRestartAction": serverCardRestartAction,
       "serverCardRowStatus": serverCardRowStatus,
       "serverCardIgnoreWatchdog": serverCardIgnoreWatchdog,
       "pps16PortCardTable": pps16PortCardTable,
       "pps16PortCardEntry": pps16PortCardEntry,
       "pps16PortCardEntityIndex": pps16PortCardEntityIndex,
       "pps16PortCardAdminState": pps16PortCardAdminState,
       "pps16PortCardOperationalState": pps16PortCardOperationalState,
       "pps16PortCardSecondaryState": pps16PortCardSecondaryState,
       "pps16PortCardRowStatus": pps16PortCardRowStatus,
       "pps16PortCardAlias": pps16PortCardAlias,
       "clk16PortCardTable": clk16PortCardTable,
       "clk16PortCardEntry": clk16PortCardEntry,
       "clk16PortCardEntityIndex": clk16PortCardEntityIndex,
       "clk16PortCardAdminState": clk16PortCardAdminState,
       "clk16PortCardOperationalState": clk16PortCardOperationalState,
       "clk16PortCardSecondaryState": clk16PortCardSecondaryState,
       "clk16PortCardRowStatus": clk16PortCardRowStatus,
       "clk16PortCardAlias": clk16PortCardAlias,
       "todPps16PortCardTable": todPps16PortCardTable,
       "todPps16PortCardEntry": todPps16PortCardEntry,
       "todPps16PortCardEntityIndex": todPps16PortCardEntityIndex,
       "todPps16PortCardAdminState": todPps16PortCardAdminState,
       "todPps16PortCardOperationalState": todPps16PortCardOperationalState,
       "todPps16PortCardSecondaryState": todPps16PortCardSecondaryState,
       "todPps16PortCardRowStatus": todPps16PortCardRowStatus,
       "todPps16PortCardAlias": todPps16PortCardAlias,
       "ethernetNTEGE101ProCardTable": ethernetNTEGE101ProCardTable,
       "ethernetNTEGE101ProCardEntry": ethernetNTEGE101ProCardEntry,
       "ethernetNTEGE101ProCardEntityIndex": ethernetNTEGE101ProCardEntityIndex,
       "ethernetNTEGE101ProCardAdminState": ethernetNTEGE101ProCardAdminState,
       "ethernetNTEGE101ProCardOperationalState": ethernetNTEGE101ProCardOperationalState,
       "ethernetNTEGE101ProCardSecondaryState": ethernetNTEGE101ProCardSecondaryState,
       "ethernetNTEGE101ProCardVoltage": ethernetNTEGE101ProCardVoltage,
       "ethernetNTEGE101ProCardTemperature": ethernetNTEGE101ProCardTemperature,
       "ethernetNTEGE101ProCardSnmpDyingGaspEnabled": ethernetNTEGE101ProCardSnmpDyingGaspEnabled,
       "ethernetNTEGE101ProCardRestartAction": ethernetNTEGE101ProCardRestartAction,
       "ethernetNTEGE101ProCardFineGrainedPmInterval": ethernetNTEGE101ProCardFineGrainedPmInterval,
       "ethernetNTEGE101ProCardSwitchPortActionPort": ethernetNTEGE101ProCardSwitchPortActionPort,
       "ethernetNTEGE101ProCardSwitchPortAction": ethernetNTEGE101ProCardSwitchPortAction,
       "ethernetNTEGO102ProSCardTable": ethernetNTEGO102ProSCardTable,
       "ethernetNTEGO102ProSCardEntry": ethernetNTEGO102ProSCardEntry,
       "ethernetNTEGO102ProSCardEntityIndex": ethernetNTEGO102ProSCardEntityIndex,
       "ethernetNTEGO102ProSCardAdminState": ethernetNTEGO102ProSCardAdminState,
       "ethernetNTEGO102ProSCardOperationalState": ethernetNTEGO102ProSCardOperationalState,
       "ethernetNTEGO102ProSCardSecondaryState": ethernetNTEGO102ProSCardSecondaryState,
       "ethernetNTEGO102ProSCardVoltage": ethernetNTEGO102ProSCardVoltage,
       "ethernetNTEGO102ProSCardTemperature": ethernetNTEGO102ProSCardTemperature,
       "ethernetNTEGO102ProSCardSnmpDyingGaspEnabled": ethernetNTEGO102ProSCardSnmpDyingGaspEnabled,
       "ethernetNTEGO102ProSCardRestartAction": ethernetNTEGO102ProSCardRestartAction,
       "ethernetNTEGO102ProSCardFineGrainedPmInterval": ethernetNTEGO102ProSCardFineGrainedPmInterval,
       "ethernetNTEGO102ProSCardSwitchPortActionPort": ethernetNTEGO102ProSCardSwitchPortActionPort,
       "ethernetNTEGO102ProSCardSwitchPortAction": ethernetNTEGO102ProSCardSwitchPortAction,
       "ethernetNTEGO102ProSPCardTable": ethernetNTEGO102ProSPCardTable,
       "ethernetNTEGO102ProSPCardEntry": ethernetNTEGO102ProSPCardEntry,
       "ethernetNTEGO102ProSPCardEntityIndex": ethernetNTEGO102ProSPCardEntityIndex,
       "ethernetNTEGO102ProSPCardAdminState": ethernetNTEGO102ProSPCardAdminState,
       "ethernetNTEGO102ProSPCardOperationalState": ethernetNTEGO102ProSPCardOperationalState,
       "ethernetNTEGO102ProSPCardSecondaryState": ethernetNTEGO102ProSPCardSecondaryState,
       "ethernetNTEGO102ProSPCardVoltage": ethernetNTEGO102ProSPCardVoltage,
       "ethernetNTEGO102ProSPCardTemperature": ethernetNTEGO102ProSPCardTemperature,
       "ethernetNTEGO102ProSPCardSnmpDyingGaspEnabled": ethernetNTEGO102ProSPCardSnmpDyingGaspEnabled,
       "ethernetNTEGO102ProSPCardRestartAction": ethernetNTEGO102ProSPCardRestartAction,
       "ethernetNTEGO102ProSPCardFineGrainedPmInterval": ethernetNTEGO102ProSPCardFineGrainedPmInterval,
       "ethernetNTEGO102ProSPCardSwitchPortActionPort": ethernetNTEGO102ProSPCardSwitchPortActionPort,
       "ethernetNTEGO102ProSPCardSwitchPortAction": ethernetNTEGO102ProSPCardSwitchPortAction,
       "ethernetNTECX101Pro30ACardTable": ethernetNTECX101Pro30ACardTable,
       "ethernetNTECX101Pro30ACardEntry": ethernetNTECX101Pro30ACardEntry,
       "ethernetNTECX101Pro30ACardEntityIndex": ethernetNTECX101Pro30ACardEntityIndex,
       "ethernetNTECX101Pro30ACardAdminState": ethernetNTECX101Pro30ACardAdminState,
       "ethernetNTECX101Pro30ACardOperationalState": ethernetNTECX101Pro30ACardOperationalState,
       "ethernetNTECX101Pro30ACardSecondaryState": ethernetNTECX101Pro30ACardSecondaryState,
       "ethernetNTECX101Pro30ACardVoltage": ethernetNTECX101Pro30ACardVoltage,
       "ethernetNTECX101Pro30ACardTemperature": ethernetNTECX101Pro30ACardTemperature,
       "ethernetNTECX101Pro30ACardSnmpDyingGaspEnabled": ethernetNTECX101Pro30ACardSnmpDyingGaspEnabled,
       "ethernetNTECX101Pro30ACardRestartAction": ethernetNTECX101Pro30ACardRestartAction,
       "ethernetNTECX101Pro30ACardFineGrainedPmInterval": ethernetNTECX101Pro30ACardFineGrainedPmInterval,
       "ethernetNTECX101Pro30ACardSwitchPortActionPort": ethernetNTECX101Pro30ACardSwitchPortActionPort,
       "ethernetNTECX101Pro30ACardSwitchPortAction": ethernetNTECX101Pro30ACardSwitchPortAction,
       "ethernetNTECX102Pro30ACardTable": ethernetNTECX102Pro30ACardTable,
       "ethernetNTECX102Pro30ACardEntry": ethernetNTECX102Pro30ACardEntry,
       "ethernetNTECX102Pro30ACardEntityIndex": ethernetNTECX102Pro30ACardEntityIndex,
       "ethernetNTECX102Pro30ACardAdminState": ethernetNTECX102Pro30ACardAdminState,
       "ethernetNTECX102Pro30ACardOperationalState": ethernetNTECX102Pro30ACardOperationalState,
       "ethernetNTECX102Pro30ACardSecondaryState": ethernetNTECX102Pro30ACardSecondaryState,
       "ethernetNTECX102Pro30ACardVoltage": ethernetNTECX102Pro30ACardVoltage,
       "ethernetNTECX102Pro30ACardTemperature": ethernetNTECX102Pro30ACardTemperature,
       "ethernetNTECX102Pro30ACardSnmpDyingGaspEnabled": ethernetNTECX102Pro30ACardSnmpDyingGaspEnabled,
       "ethernetNTECX102Pro30ACardRestartAction": ethernetNTECX102Pro30ACardRestartAction,
       "ethernetNTECX102Pro30ACardFineGrainedPmInterval": ethernetNTECX102Pro30ACardFineGrainedPmInterval,
       "ethernetNTECX102Pro30ACardSwitchPortActionPort": ethernetNTECX102Pro30ACardSwitchPortActionPort,
       "ethernetNTECX102Pro30ACardSwitchPortAction": ethernetNTECX102Pro30ACardSwitchPortAction,
       "ge4PortCardTable": ge4PortCardTable,
       "ge4PortCardEntry": ge4PortCardEntry,
       "ge4PortCardEntityIndex": ge4PortCardEntityIndex,
       "ge4PortCardAdminState": ge4PortCardAdminState,
       "ge4PortCardOperationalState": ge4PortCardOperationalState,
       "ge4PortCardSecondaryState": ge4PortCardSecondaryState,
       "ge4PortCardRowStatus": ge4PortCardRowStatus,
       "ge4PortCardAlias": ge4PortCardAlias,
       "ge4PortCardTemperature": ge4PortCardTemperature,
       "ethernetNTEXG116PROCardTable": ethernetNTEXG116PROCardTable,
       "ethernetNTEXG116PROCardEntry": ethernetNTEXG116PROCardEntry,
       "ethernetNTEXG116PROCardEntityIndex": ethernetNTEXG116PROCardEntityIndex,
       "ethernetNTEXG116PROCardAdminState": ethernetNTEXG116PROCardAdminState,
       "ethernetNTEXG116PROCardOperationalState": ethernetNTEXG116PROCardOperationalState,
       "ethernetNTEXG116PROCardSecondaryState": ethernetNTEXG116PROCardSecondaryState,
       "ethernetNTEXG116PROCardVoltage": ethernetNTEXG116PROCardVoltage,
       "ethernetNTEXG116PROCardTemperature": ethernetNTEXG116PROCardTemperature,
       "ethernetNTEXG116PROCardSnmpDyingGaspEnabled": ethernetNTEXG116PROCardSnmpDyingGaspEnabled,
       "ethernetNTEXG116PROCardRestartAction": ethernetNTEXG116PROCardRestartAction,
       "ethernetNTEXG116PROCardFineGrainedPmInterval": ethernetNTEXG116PROCardFineGrainedPmInterval,
       "ethernetNTEXG120PROCardTable": ethernetNTEXG120PROCardTable,
       "ethernetNTEXG120PROCardEntry": ethernetNTEXG120PROCardEntry,
       "ethernetNTEXG120PROCardEntityIndex": ethernetNTEXG120PROCardEntityIndex,
       "ethernetNTEXG120PROCardAdminState": ethernetNTEXG120PROCardAdminState,
       "ethernetNTEXG120PROCardOperationalState": ethernetNTEXG120PROCardOperationalState,
       "ethernetNTEXG120PROCardSecondaryState": ethernetNTEXG120PROCardSecondaryState,
       "ethernetNTEXG120PROCardVoltage": ethernetNTEXG120PROCardVoltage,
       "ethernetNTEXG120PROCardTemperature": ethernetNTEXG120PROCardTemperature,
       "ethernetNTEXG120PROCardSnmpDyingGaspEnabled": ethernetNTEXG120PROCardSnmpDyingGaspEnabled,
       "ethernetNTEXG120PROCardRestartAction": ethernetNTEXG120PROCardRestartAction,
       "ethernetNTEXG120PROCardFineGrainedPmInterval": ethernetNTEXG120PROCardFineGrainedPmInterval,
       "ethernetNTEGE112ProVmCardTable": ethernetNTEGE112ProVmCardTable,
       "ethernetNTEGE112ProVmCardEntry": ethernetNTEGE112ProVmCardEntry,
       "ethernetNTEGE112ProVmCardEntityIndex": ethernetNTEGE112ProVmCardEntityIndex,
       "ethernetNTEGE112ProVmCardAdminState": ethernetNTEGE112ProVmCardAdminState,
       "ethernetNTEGE112ProVmCardOperationalState": ethernetNTEGE112ProVmCardOperationalState,
       "ethernetNTEGE112ProVmCardSecondaryState": ethernetNTEGE112ProVmCardSecondaryState,
       "ethernetNTEGE112ProVmCardVoltage": ethernetNTEGE112ProVmCardVoltage,
       "ethernetNTEGE112ProVmCardTemperature": ethernetNTEGE112ProVmCardTemperature,
       "ethernetNTEGE112ProVmCardSnmpDyingGaspEnabled": ethernetNTEGE112ProVmCardSnmpDyingGaspEnabled,
       "ethernetNTEGE112ProVmCardRestartAction": ethernetNTEGE112ProVmCardRestartAction,
       "ethernetNTEGE112ProVmCardFineGrainedPmInterval": ethernetNTEGE112ProVmCardFineGrainedPmInterval,
       "ethernetNTEGE112ProVmCardSwitchPortActionPort": ethernetNTEGE112ProVmCardSwitchPortActionPort,
       "ethernetNTEGE112ProVmCardSwitchPortAction": ethernetNTEGE112ProVmCardSwitchPortAction,
       "ethernetNTEOSA5401CardTable": ethernetNTEOSA5401CardTable,
       "ethernetNTEOSA5401CardEntry": ethernetNTEOSA5401CardEntry,
       "ethernetNTEOSA5401CardEntityIndex": ethernetNTEOSA5401CardEntityIndex,
       "ethernetNTEOSA5401CardAdminState": ethernetNTEOSA5401CardAdminState,
       "ethernetNTEOSA5401CardOperationalState": ethernetNTEOSA5401CardOperationalState,
       "ethernetNTEOSA5401CardTableRestartAction": ethernetNTEOSA5401CardTableRestartAction,
       "ethernetNTEOSA5405CardTable": ethernetNTEOSA5405CardTable,
       "ethernetNTEOSA5405CardEntry": ethernetNTEOSA5405CardEntry,
       "ethernetNTEOSA5405CardEntityIndex": ethernetNTEOSA5405CardEntityIndex,
       "ethernetNTEOSA5405CardAdminState": ethernetNTEOSA5405CardAdminState,
       "ethernetNTEOSA5405CardOperationalState": ethernetNTEOSA5405CardOperationalState,
       "ethernetNTEOSA5405CardVoltage": ethernetNTEOSA5405CardVoltage,
       "ethernetNTEOSA5405CardTemperature": ethernetNTEOSA5405CardTemperature,
       "ethernetNTEOSA5405CardTableRestartAction": ethernetNTEOSA5405CardTableRestartAction,
       "ethernetCSMCardTable": ethernetCSMCardTable,
       "ethernetCSMCardEntry": ethernetCSMCardEntry,
       "ethernetCSMCardEntityIndex": ethernetCSMCardEntityIndex,
       "ethernetCSMCardAdminState": ethernetCSMCardAdminState,
       "ethernetCSMCardOperationalState": ethernetCSMCardOperationalState,
       "ethernetCSMCardSecondaryState": ethernetCSMCardSecondaryState,
       "ethernetCSMCardVoltage": ethernetCSMCardVoltage,
       "ethernetCSMCardTemperature": ethernetCSMCardTemperature,
       "ethernetCSMCardSnmpDyingGaspEnabled": ethernetCSMCardSnmpDyingGaspEnabled,
       "ethernetCSMCardRestartAction": ethernetCSMCardRestartAction,
       "ethernetCSMCardFineGrainedPmInterval": ethernetCSMCardFineGrainedPmInterval,
       "ethernetCSMCardOscillatorType": ethernetCSMCardOscillatorType,
       "auxPortCardTable": auxPortCardTable,
       "auxPortCardEntry": auxPortCardEntry,
       "auxPortCardEntityIndex": auxPortCardEntityIndex,
       "auxPortCardAdminState": auxPortCardAdminState,
       "auxPortCardOperationalState": auxPortCardOperationalState,
       "auxPortCardSecondaryState": auxPortCardSecondaryState,
       "auxPortCardRowStatus": auxPortCardRowStatus,
       "auxPortCardAlias": auxPortCardAlias,
       "auxPortCardTemperature": auxPortCardTemperature,
       "ethernetNTEGE102ProHCardTable": ethernetNTEGE102ProHCardTable,
       "ethernetNTEGE102ProHCardEntry": ethernetNTEGE102ProHCardEntry,
       "ethernetNTEGE102ProHCardEntityIndex": ethernetNTEGE102ProHCardEntityIndex,
       "ethernetNTEGE102ProHCardAdminState": ethernetNTEGE102ProHCardAdminState,
       "ethernetNTEGE102ProHCardOperationalState": ethernetNTEGE102ProHCardOperationalState,
       "ethernetNTEGE102ProHCardSecondaryState": ethernetNTEGE102ProHCardSecondaryState,
       "ethernetNTEGE102ProHCardVoltage": ethernetNTEGE102ProHCardVoltage,
       "ethernetNTEGE102ProHCardTemperature": ethernetNTEGE102ProHCardTemperature,
       "ethernetNTEGE102ProHCardSnmpDyingGaspEnabled": ethernetNTEGE102ProHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE102ProHCardRestartAction": ethernetNTEGE102ProHCardRestartAction,
       "ethernetNTEGE102ProHCardFineGrainedPmInterval": ethernetNTEGE102ProHCardFineGrainedPmInterval,
       "ethernetNTEGE102ProHCardSwitchPortActionPort": ethernetNTEGE102ProHCardSwitchPortActionPort,
       "ethernetNTEGE102ProHCardSwitchPortAction": ethernetNTEGE102ProHCardSwitchPortAction,
       "ethernetNTEGE102ProHCardPSU1State": ethernetNTEGE102ProHCardPSU1State,
       "ethernetNTEGE102ProHCardPSU2State": ethernetNTEGE102ProHCardPSU2State,
       "ethernetNTEGE102ProHCardFAN1State": ethernetNTEGE102ProHCardFAN1State,
       "ethernetNTEGE102ProHCardFAN2State": ethernetNTEGE102ProHCardFAN2State,
       "ethernetNTEGE102ProHCardPsuType": ethernetNTEGE102ProHCardPsuType,
       "ethernetNTEGE102ProEFMHCardTable": ethernetNTEGE102ProEFMHCardTable,
       "ethernetNTEGE102ProEFMHCardEntry": ethernetNTEGE102ProEFMHCardEntry,
       "ethernetNTEGE102ProEFMHCardEntityIndex": ethernetNTEGE102ProEFMHCardEntityIndex,
       "ethernetNTEGE102ProEFMHCardAdminState": ethernetNTEGE102ProEFMHCardAdminState,
       "ethernetNTEGE102ProEFMHCardOperationalState": ethernetNTEGE102ProEFMHCardOperationalState,
       "ethernetNTEGE102ProEFMHCardSecondaryState": ethernetNTEGE102ProEFMHCardSecondaryState,
       "ethernetNTEGE102ProEFMHCardVoltage": ethernetNTEGE102ProEFMHCardVoltage,
       "ethernetNTEGE102ProEFMHCardTemperature": ethernetNTEGE102ProEFMHCardTemperature,
       "ethernetNTEGE102ProEFMHCardRestartAction": ethernetNTEGE102ProEFMHCardRestartAction,
       "ethernetNTEGE102ProEFMHCardPSU1State": ethernetNTEGE102ProEFMHCardPSU1State,
       "ethernetNTEGE102ProEFMHCardPSU2State": ethernetNTEGE102ProEFMHCardPSU2State,
       "ethernetNTEGE102ProEFMHCardFAN1State": ethernetNTEGE102ProEFMHCardFAN1State,
       "ethernetNTEGE102ProEFMHCardFAN2State": ethernetNTEGE102ProEFMHCardFAN2State,
       "ethernetNTEGE102ProEFMHCardPsuType": ethernetNTEGE102ProEFMHCardPsuType,
       "ethernetNTEGE102ProEFMHCardLLFMode": ethernetNTEGE102ProEFMHCardLLFMode,
       "ethernetNTEGE102ProEFMHCardLLFModeAction": ethernetNTEGE102ProEFMHCardLLFModeAction,
       "ethernetOsa3350MgntCardTable": ethernetOsa3350MgntCardTable,
       "ethernetOsa3350MgntCardEntry": ethernetOsa3350MgntCardEntry,
       "ethernetOsa3350MgntCardEntityIndex": ethernetOsa3350MgntCardEntityIndex,
       "ethernetOsa3350MgntCardAdminState": ethernetOsa3350MgntCardAdminState,
       "ethernetOsa3350MgntCardOperationalState": ethernetOsa3350MgntCardOperationalState,
       "ethernetOsa3350MgntCardSecondaryState": ethernetOsa3350MgntCardSecondaryState,
       "ethernetOsa3350MgntCardRestartAction": ethernetOsa3350MgntCardRestartAction,
       "ethernetOsa3350MgntCardResyncAction": ethernetOsa3350MgntCardResyncAction,
       "ethernetNTEXG116PROHCardTable": ethernetNTEXG116PROHCardTable,
       "ethernetNTEXG116PROHCardEntry": ethernetNTEXG116PROHCardEntry,
       "ethernetNTEXG116PROHCardEntityIndex": ethernetNTEXG116PROHCardEntityIndex,
       "ethernetNTEXG116PROHCardAdminState": ethernetNTEXG116PROHCardAdminState,
       "ethernetNTEXG116PROHCardOperationalState": ethernetNTEXG116PROHCardOperationalState,
       "ethernetNTEXG116PROHCardSecondaryState": ethernetNTEXG116PROHCardSecondaryState,
       "ethernetNTEXG116PROHCardVoltage": ethernetNTEXG116PROHCardVoltage,
       "ethernetNTEXG116PROHCardTemperature": ethernetNTEXG116PROHCardTemperature,
       "ethernetNTEXG116PROHCardSnmpDyingGaspEnabled": ethernetNTEXG116PROHCardSnmpDyingGaspEnabled,
       "ethernetNTEXG116PROHCardRestartAction": ethernetNTEXG116PROHCardRestartAction,
       "ethernetNTEXG116PROHCardFineGrainedPmInterval": ethernetNTEXG116PROHCardFineGrainedPmInterval,
       "ethernetNTEGO102ProSMCardTable": ethernetNTEGO102ProSMCardTable,
       "ethernetNTEGO102ProSMCardEntry": ethernetNTEGO102ProSMCardEntry,
       "ethernetNTEGO102ProSMCardEntityIndex": ethernetNTEGO102ProSMCardEntityIndex,
       "ethernetNTEGO102ProSMCardAdminState": ethernetNTEGO102ProSMCardAdminState,
       "ethernetNTEGO102ProSMCardOperationalState": ethernetNTEGO102ProSMCardOperationalState,
       "ethernetNTEGO102ProSMCardSecondaryState": ethernetNTEGO102ProSMCardSecondaryState,
       "ethernetNTEGO102ProSMCardVoltage": ethernetNTEGO102ProSMCardVoltage,
       "ethernetNTEGO102ProSMCardTemperature": ethernetNTEGO102ProSMCardTemperature,
       "ethernetNTEGO102ProSMCardSnmpDyingGaspEnabled": ethernetNTEGO102ProSMCardSnmpDyingGaspEnabled,
       "ethernetNTEGO102ProSMCardRestartAction": ethernetNTEGO102ProSMCardRestartAction,
       "ethernetNTEGO102ProSMCardFineGrainedPmInterval": ethernetNTEGO102ProSMCardFineGrainedPmInterval,
       "ethernetNTEGO102ProSMCardSwitchPortActionPort": ethernetNTEGO102ProSMCardSwitchPortActionPort,
       "ethernetNTEGO102ProSMCardSwitchPortAction": ethernetNTEGO102ProSMCardSwitchPortAction,
       "ethernetNTEXG118PROSHCardTable": ethernetNTEXG118PROSHCardTable,
       "ethernetNTEXG118PROSHCardEntry": ethernetNTEXG118PROSHCardEntry,
       "ethernetNTEXG118PROSHCardEntityIndex": ethernetNTEXG118PROSHCardEntityIndex,
       "ethernetNTEXG118PROSHCardAdminState": ethernetNTEXG118PROSHCardAdminState,
       "ethernetNTEXG118PROSHCardOperationalState": ethernetNTEXG118PROSHCardOperationalState,
       "ethernetNTEXG118PROSHCardSecondaryState": ethernetNTEXG118PROSHCardSecondaryState,
       "ethernetNTEXG118PROSHCardVoltage": ethernetNTEXG118PROSHCardVoltage,
       "ethernetNTEXG118PROSHCardTemperature": ethernetNTEXG118PROSHCardTemperature,
       "ethernetNTEXG118PROSHCardSnmpDyingGaspEnabled": ethernetNTEXG118PROSHCardSnmpDyingGaspEnabled,
       "ethernetNTEXG118PROSHCardRestartAction": ethernetNTEXG118PROSHCardRestartAction,
       "ethernetNTEXG118PROSHCardFineGrainedPmInterval": ethernetNTEXG118PROSHCardFineGrainedPmInterval,
       "ethernetNTEXG118PROACSHCardTable": ethernetNTEXG118PROACSHCardTable,
       "ethernetNTEXG118PROACSHCardEntry": ethernetNTEXG118PROACSHCardEntry,
       "ethernetNTEXG118PROACSHCardEntityIndex": ethernetNTEXG118PROACSHCardEntityIndex,
       "ethernetNTEXG118PROACSHCardAdminState": ethernetNTEXG118PROACSHCardAdminState,
       "ethernetNTEXG118PROACSHCardOperationalState": ethernetNTEXG118PROACSHCardOperationalState,
       "ethernetNTEXG118PROACSHCardSecondaryState": ethernetNTEXG118PROACSHCardSecondaryState,
       "ethernetNTEXG118PROACSHCardVoltage": ethernetNTEXG118PROACSHCardVoltage,
       "ethernetNTEXG118PROACSHCardTemperature": ethernetNTEXG118PROACSHCardTemperature,
       "ethernetNTEXG118PROACSHCardSnmpDyingGaspEnabled": ethernetNTEXG118PROACSHCardSnmpDyingGaspEnabled,
       "ethernetNTEXG118PROACSHCardRestartAction": ethernetNTEXG118PROACSHCardRestartAction,
       "ethernetNTEXG118PROACSHCardFineGrainedPmInterval": ethernetNTEXG118PROACSHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProVmSHCardTable": ethernetNTEGE114ProVmSHCardTable,
       "ethernetNTEGE114ProVmSHCardEntry": ethernetNTEGE114ProVmSHCardEntry,
       "ethernetNTEGE114ProVmSHCardEntityIndex": ethernetNTEGE114ProVmSHCardEntityIndex,
       "ethernetNTEGE114ProVmSHCardAdminState": ethernetNTEGE114ProVmSHCardAdminState,
       "ethernetNTEGE114ProVmSHCardOperationalState": ethernetNTEGE114ProVmSHCardOperationalState,
       "ethernetNTEGE114ProVmSHCardSecondaryState": ethernetNTEGE114ProVmSHCardSecondaryState,
       "ethernetNTEGE114ProVmSHCardVoltage": ethernetNTEGE114ProVmSHCardVoltage,
       "ethernetNTEGE114ProVmSHCardTemperature": ethernetNTEGE114ProVmSHCardTemperature,
       "ethernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled": ethernetNTEGE114ProVmSHCardSnmpDyingGaspEnabled,
       "ethernetNTEGE114ProVmSHCardRestartAction": ethernetNTEGE114ProVmSHCardRestartAction,
       "ethernetNTEGE114ProVmSHCardFineGrainedPmInterval": ethernetNTEGE114ProVmSHCardFineGrainedPmInterval,
       "ethernetNTEGE114ProVmSHCardSwitchPortActionPort": ethernetNTEGE114ProVmSHCardSwitchPortActionPort,
       "ethernetNTEGE114ProVmSHCardSwitchPortAction": ethernetNTEGE114ProVmSHCardSwitchPortAction,
       "ethernetNTEGE104CardTable": ethernetNTEGE104CardTable,
       "ethernetNTEGE104CardEntry": ethernetNTEGE104CardEntry,
       "ethernetNTEGE104CardEntityIndex": ethernetNTEGE104CardEntityIndex,
       "ethernetNTEGE104CardAdminState": ethernetNTEGE104CardAdminState,
       "ethernetNTEGE104CardOperationalState": ethernetNTEGE104CardOperationalState,
       "ethernetNTEGE104CardSecondaryState": ethernetNTEGE104CardSecondaryState,
       "ethernetNTEGE104CardVoltage": ethernetNTEGE104CardVoltage,
       "ethernetNTEGE104CardTemperature": ethernetNTEGE104CardTemperature,
       "ethernetNTEGE104CardSnmpDyingGaspEnabled": ethernetNTEGE104CardSnmpDyingGaspEnabled,
       "ethernetNTEGE104CardRestartAction": ethernetNTEGE104CardRestartAction,
       "ethernetNTEGE104CardFineGrainedPmInterval": ethernetNTEGE104CardFineGrainedPmInterval,
       "ethernetNTEGE104CardSwitchPortActionPort": ethernetNTEGE104CardSwitchPortActionPort,
       "ethernetNTEGE104CardSwitchPortAction": ethernetNTEGE104CardSwitchPortAction,
       "ethernetNTEXG120PROSHCardTable": ethernetNTEXG120PROSHCardTable,
       "ethernetNTEXG120PROSHCardEntry": ethernetNTEXG120PROSHCardEntry,
       "ethernetNTEXG120PROSHCardEntityIndex": ethernetNTEXG120PROSHCardEntityIndex,
       "ethernetNTEXG120PROSHCardAdminState": ethernetNTEXG120PROSHCardAdminState,
       "ethernetNTEXG120PROSHCardOperationalState": ethernetNTEXG120PROSHCardOperationalState,
       "ethernetNTEXG120PROSHCardSecondaryState": ethernetNTEXG120PROSHCardSecondaryState,
       "ethernetNTEXG120PROSHCardVoltage": ethernetNTEXG120PROSHCardVoltage,
       "ethernetNTEXG120PROSHCardTemperature": ethernetNTEXG120PROSHCardTemperature,
       "ethernetNTEXG120PROSHCardSnmpDyingGaspEnabled": ethernetNTEXG120PROSHCardSnmpDyingGaspEnabled,
       "ethernetNTEXG120PROSHCardRestartAction": ethernetNTEXG120PROSHCardRestartAction,
       "ethernetNTEXG120PROSHCardFineGrainedPmInterval": ethernetNTEXG120PROSHCardFineGrainedPmInterval,
       "mbGnssCardTable": mbGnssCardTable,
       "mbGnssCardEntry": mbGnssCardEntry,
       "mbGnssCardEntityIndex": mbGnssCardEntityIndex,
       "mbGnssCardAdminState": mbGnssCardAdminState,
       "mbGnssCardOperationalState": mbGnssCardOperationalState,
       "mbGnssCardSecondaryState": mbGnssCardSecondaryState,
       "mbGnssCardRowStatus": mbGnssCardRowStatus,
       "mbGnssCardAlias": mbGnssCardAlias,
       "f3IrigCardTable": f3IrigCardTable,
       "f3IrigCardEntry": f3IrigCardEntry,
       "f3IrigCardEntityIndex": f3IrigCardEntityIndex,
       "f3IrigCardAlias": f3IrigCardAlias,
       "f3IrigCardAdminState": f3IrigCardAdminState,
       "f3IrigCardOperationalState": f3IrigCardOperationalState,
       "f3IrigCardSecondaryState": f3IrigCardSecondaryState,
       "f3IrigCardTemperature": f3IrigCardTemperature,
       "f3IrigCardStorageType": f3IrigCardStorageType,
       "f3IrigCardRowStatus": f3IrigCardRowStatus,
       "compositeClockCardTable": compositeClockCardTable,
       "compositeClockCardEntry": compositeClockCardEntry,
       "compositeClockCardEntityIndex": compositeClockCardEntityIndex,
       "compositeClockCardAdminState": compositeClockCardAdminState,
       "compositeClockCardOperationalState": compositeClockCardOperationalState,
       "compositeClockCardSecondaryState": compositeClockCardSecondaryState,
       "compositeClockCardRowStatus": compositeClockCardRowStatus,
       "compositeClockCardAlias": compositeClockCardAlias,
       "f3StorageDeviceTable": f3StorageDeviceTable,
       "f3StorageDeviceEntry": f3StorageDeviceEntry,
       "f3StorageDeviceInternalSsdHealth": f3StorageDeviceInternalSsdHealth,
       "f3StorageDeviceExternalSsdStatus": f3StorageDeviceExternalSsdStatus,
       "f3StorageDeviceWearoutLevel": f3StorageDeviceWearoutLevel,
       "cmEntityConformance": cmEntityConformance,
       "cmEntityCompliances": cmEntityCompliances,
       "cmEntityCompliance": cmEntityCompliance,
       "cmEntityGroups": cmEntityGroups,
       "cmEntityObjectGroup": cmEntityObjectGroup,
       "commonEntityGroup": commonEntityGroup,
       "psuGroup": psuGroup,
       "fanGroup": fanGroup,
       "hubshelfGroup": hubshelfGroup,
       "nteGe206CardGroup": nteGe206CardGroup,
       "nteGe201SyncECardGroup": nteGe201SyncECardGroup,
       "nteGe201NonSyncECardGroup": nteGe201NonSyncECardGroup,
       "nteGe206FCardGroup": nteGe206FCardGroup,
       "nteGe112CardGroup": nteGe112CardGroup,
       "nteGe114CardGroup": nteGe114CardGroup,
       "nteGe206VCardGroup": nteGe206VCardGroup,
       "nteXg210CardGroup": nteXg210CardGroup,
       "pseudoWireCardOcnStmCardGroup": pseudoWireCardOcnStmCardGroup,
       "pseudoWireCardE1T1CardGroup": pseudoWireCardE1T1CardGroup,
       "nteT1804CardGroup": nteT1804CardGroup,
       "nteT3204CardGroup": nteT3204CardGroup,
       "nteGeSyncProbeCardGroup": nteGeSyncProbeCardGroup,
       "xg1XCCCardGroup": xg1XCCCardGroup,
       "xg1SCCCardGroup": xg1SCCCardGroup,
       "ge4ECCCardGroup": ge4ECCCardGroup,
       "ge4SCCCardGroup": ge4SCCCardGroup,
       "ge8SCCCardGroup": ge8SCCCardGroup,
       "nteGe114HCardGroup": nteGe114HCardGroup,
       "nteGe114PHCardGroup": nteGe114PHCardGroup,
       "ethernetOverOCSTMCardGroup": ethernetOverOCSTMCardGroup,
       "ethernet1x10GHighPerCardGroup": ethernet1x10GHighPerCardGroup,
       "ethernetFE36ECardGroup": ethernetFE36ECardGroup,
       "nteGe114SHCardGroup": nteGe114SHCardGroup,
       "nteGe114SCardGroup": nteGe114SCardGroup,
       "ge8ECCCardGroup": ge8ECCCardGroup,
       "neLLDPParamsGroup": neLLDPParamsGroup,
       "nteSh1PcsCardGroup": nteSh1PcsCardGroup,
       "nteOsa5411CardGroup": nteOsa5411CardGroup,
       "nteGe112ProCardGroup": nteGe112ProCardGroup,
       "nteGe112ProMCardGroup": nteGe112ProMCardGroup,
       "nteGe114ProCardGroup": nteGe114ProCardGroup,
       "nteGe114ProCCardGroup": nteGe114ProCCardGroup,
       "nteGe114ProSHCardGroup": nteGe114ProSHCardGroup,
       "nteGe114ProCSHCardGroup": nteGe114ProCSHCardGroup,
       "nteGe114ProHECardGroup": nteGe114ProHECardGroup,
       "nteGe112ProHCardGroup": nteGe112ProHCardGroup,
       "nteXg210CCardGroup": nteXg210CCardGroup,
       "geGE8SCryptoConnectorCardGroup": geGE8SCryptoConnectorCardGroup,
       "nteOsa5420CardGroup": nteOsa5420CardGroup,
       "nteOsa5421CardGroup": nteOsa5421CardGroup,
       "nteGe114GCardGroup": nteGe114GCardGroup,
       "bits16PortCardGroup": bits16PortCardGroup,
       "nteGE114ProVmHCardGroup": nteGE114ProVmHCardGroup,
       "nteGE114ProVmCHCardGroup": nteGE114ProVmCHCardGroup,
       "nteGE114ProVmCSHCardGroup": nteGE114ProVmCSHCardGroup,
       "serverCardGroup": serverCardGroup,
       "pps16PortCardGroup": pps16PortCardGroup,
       "clk16PortCardGroup": clk16PortCardGroup,
       "todPps16PortCardGroup": todPps16PortCardGroup,
       "nteGe101ProCardGroup": nteGe101ProCardGroup,
       "nteGo102ProSCardGroup": nteGo102ProSCardGroup,
       "nteGo102ProSPCardGroup": nteGo102ProSPCardGroup,
       "nteCx101Pro30ACardGroup": nteCx101Pro30ACardGroup,
       "nteCx102Pro30ACardGroup": nteCx102Pro30ACardGroup,
       "ge4PortCardGroup": ge4PortCardGroup,
       "nteXg116ProCardGroup": nteXg116ProCardGroup,
       "nteXg120ProCardGroup": nteXg120ProCardGroup,
       "nteGE112ProVmCardGroup": nteGE112ProVmCardGroup,
       "nteOsa5401CardGroup": nteOsa5401CardGroup,
       "nteOsa5405CardGroup": nteOsa5405CardGroup,
       "csmCardGroup": csmCardGroup,
       "auxPortCardGroup": auxPortCardGroup,
       "nteGe102ProHCardGroup": nteGe102ProHCardGroup,
       "nteGe102ProEFMHCardGroup": nteGe102ProEFMHCardGroup,
       "ethernetOsa3350MgntCardGroup": ethernetOsa3350MgntCardGroup,
       "nteXg116ProHCardGroup": nteXg116ProHCardGroup,
       "nteGo102ProSMCardGroup": nteGo102ProSMCardGroup,
       "nteXg118ProSHCardGroup": nteXg118ProSHCardGroup,
       "nteXg118ProacSHCardGroup": nteXg118ProacSHCardGroup,
       "nteGE114ProVmSHCardGroup": nteGE114ProVmSHCardGroup,
       "nteGE104CardGroup": nteGE104CardGroup,
       "nteXg120ProSHCardGroup": nteXg120ProSHCardGroup,
       "mbGnssCardGroup": mbGnssCardGroup,
       "f3IrigCardGroup": f3IrigCardGroup,
       "compositeClockCardGroup": compositeClockCardGroup}
)
