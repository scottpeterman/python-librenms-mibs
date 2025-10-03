# SNMP MIB module (RUIJIE-FIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruijie\RUIJIE-FIBER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:17 2025
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieFiberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105)
)
if mibBuilder.loadTexts:
    ruijieFiberMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieFiberMIBObjects_ObjectIdentity = ObjectIdentity
ruijieFiberMIBObjects = _RuijieFiberMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1)
)
_RuijieFiberTable_Object = MibTable
ruijieFiberTable = _RuijieFiberTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieFiberTable.setStatus("current")
_RuijieFiberEntry_Object = MibTableRow
ruijieFiberEntry = _RuijieFiberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1)
)
ruijieFiberEntry.setIndexNames(
    (0, "RUIJIE-FIBER-MIB", "ruijieFiberPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieFiberEntry.setStatus("current")
_RuijieFiberPortIndex_Type = IfIndex
_RuijieFiberPortIndex_Object = MibTableColumn
ruijieFiberPortIndex = _RuijieFiberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 1),
    _RuijieFiberPortIndex_Type()
)
ruijieFiberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberPortIndex.setStatus("current")


class _RuijieFiberPortDescr_Type(DisplayString):
    """Custom type ruijieFiberPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieFiberPortDescr_Type.__name__ = "DisplayString"
_RuijieFiberPortDescr_Object = MibTableColumn
ruijieFiberPortDescr = _RuijieFiberPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 2),
    _RuijieFiberPortDescr_Type()
)
ruijieFiberPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberPortDescr.setStatus("current")


class _RuijieFiberTransceiverType_Type(Integer32):
    """Custom type ruijieFiberTransceiverType based on Integer32"""
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
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fiber100BASEGTSFP", 2),
          ("fiber100BASESXSFP", 3),
          ("fiber100BASELXSFP", 4),
          ("fiber100BASELHSFP", 5),
          ("fiber100BASEZXSFP", 6),
          ("fiber100CopperSFP", 7),
          ("fiber1000BASEGTSFP", 8),
          ("fiber1000BASESXSFP", 9),
          ("fiber1000BASELXSFP", 10),
          ("fiber1000BASELHSFP", 11),
          ("fiber1000BASEZXSFP", 12),
          ("fiber1000CopperSFP", 13),
          ("fiber10GCopperSFPPlus", 14),
          ("fiber10GBASESRSFPPlus", 15),
          ("fiber10GBASELRSFPPlus", 16),
          ("fiber10GBASEERSFPPlus", 17),
          ("fiber10GBASEZRSFPPlus", 18),
          ("fiber10GCopperXFP", 19),
          ("fiber10GBASESRXFP", 20),
          ("fiber10GBASELRXFP", 21),
          ("fiber10GBASEERXFP", 22),
          ("fiber10GBASEZRXFP", 23),
          ("fiber40GActiveCableQSFPPlus", 24),
          ("fiber40GLR4QSFPPlus", 25),
          ("fiber40GCopperQSFPPlus", 26),
          ("fiber40GSR4QSFPPlus", 27),
          ("fiber2500CopperSFP", 28),
          ("fiberFC16G", 29),
          ("fiberFC8G", 30),
          ("fiberFC4G", 31),
          ("fiberFC2G", 32),
          ("fiber10GActiveCableSFPPlus", 33),
          ("fiber40GER4QSFPPlus", 34),
          ("fiber40GZR4QSFPPlus", 35),
          ("fiber100GCABLEQSFP28", 36),
          ("fiber100GLR4QSFP28", 37),
          ("fiber100GSR4QSFP28", 38),
          ("fiber100GER4QSFP28", 39),
          ("fiber100GZR4QSFP28", 40),
          ("fiber100GCR4QSFP28", 41),
          ("fiber100GPSM4QSFP28", 42),
          ("fiber25GSRSFP28", 43),
          ("fiber25GLRSFP28", 44),
          ("fiber25GERSFP28", 45),
          ("fiber25GZRSFP28", 46),
          ("fiber25GCOPPERSFP28", 47),
          ("fiber25GACTIVECABLESFP28", 48),
          ("fiber100GiLR4QSFP28", 49),
          ("fiber10GBASELRMSFPPlus", 50),
          ("fiber40GLSR4QSFPPlus", 51),
          ("fiber40GSWDM4QSFPPlus", 52),
          ("fiber40GiLR4QSFPPlus", 53),
          ("fiber40GPSM4QSFPPlus", 54),
          ("fiber40GSR4BiDiQSFPPlus", 55),
          ("fiber100GSWDM4QSFP28", 56),
          ("fiber100GPAM4BiDiQSFP28", 57),
          ("fiber100GER4LiteQSFP28", 58),
          ("fiber100G4WDM40QSFP28", 59),
          ("fiber100GDWDM2QSFP28", 60),
          ("fiber40GZRQSFPPlus", 61),
          ("fiber100GZRQSFP28", 62),
          ("fiber100GCWDM4QSFP28", 63),
          ("fiber10GPASSIVECOPPERSFPPlus", 64),
          ("fiber10GACTIVECOPPERSFPPlus", 65),
          ("fiber10GLOOPBACKSFPPlus", 66),
          ("fiber40GPASSIVECOPPERQSFPPlus", 67),
          ("fiber40GACTIVECOPPERQSFPPlus", 68),
          ("fiber40GLOOPBACKQSFPPlus", 69),
          ("fiber100GPASSIVECOPPERQSFP28", 70),
          ("fiber100GACTIVECOPPERQSFP28", 71),
          ("fiber100GLOOPBACKQSFP28", 72),
          ("fiber25GPASSIVECOPPERSFP28", 73),
          ("fiber25GACTIVECOPPERSFP28", 74),
          ("fiber25GLOOPBACKSFP28", 75),
          ("fiber200GSR4QSFP56", 76),
          ("fiber200GFR4QSFP56", 77),
          ("fiber200GPASSIVECOPPERQSFP56", 78),
          ("fiber200GACTIVECOPPERQSFP56", 79),
          ("fiber400GSR8QSFPDD", 80),
          ("fiber400GDR4QSFPDD", 81),
          ("fiber400GFR4QSFPDD", 82),
          ("fiber400GPASSIVECOPPERQSFPDD", 83),
          ("fiber400GACTIVECABLEQSFPDD", 84),
          ("fiber400GLR8QSFPDD", 85),
          ("fiber200GLOOPBACKQSFP56", 86),
          ("fiber400GACTIVECOPPERQSFPDD", 87),
          ("fiber400GLOOPBACKQSFPDD", 88),
          ("fiber100GPASSIVECOPPERDSFP", 89),
          ("fiber100GACTIVECOPPERDSFP", 90),
          ("fiber100GACTIVECABLEDSFP", 91),
          ("fiber100GLOOPBACKDSFP", 92),
          ("fiber100GDR1QSFP28", 93),
          ("fiber100GFR1QSFP28", 94),
          ("fiber400GZRQSFPDD", 95),
          ("fiber2500BASESXSFP", 96),
          ("fiber2500BASELXSFP", 97),
          ("fiber200GACTIVECABLEQSFP56", 98),
          ("fiber40GLX4QSFPPlus", 99),
          ("fiber10GBASELR8SFX", 100),
          ("fiber1000BASELX8SFG", 101),
          ("fiber10GCOPPER8SFX", 102),
          ("fiber10GBASETSFPPlus", 103),
          ("fiber400GZRPlusQSFPDD", 104),
          ("fiber400GLR4TENQSFPDD", 105),
          ("fiber400GLR4SIXQSFPDD", 106),
          ("fiber400GSR4QSFPDD", 107),
          ("fiber100GLR1QSFP28", 108),
          ("fiber400GVR4QSFPDD", 109),
          ("fiber400GSR4QSFP112", 110),
          ("fiber400GDR4QSFP112", 111),
          ("fiber400GFR4QSFP112", 112),
          ("fiber400GLR4TENQSFP112", 113),
          ("fiber400GLR4SIXQSFP112", 114),
          ("fiber400GPASSIVECOPPERQSFP112", 115),
          ("fiber400GACTIVECOPPERQSFP112", 116),
          ("fiber400GACTIVECABLEQSFP112", 117),
          ("fiber400GLOOPBACKQSFP112", 118),
          ("fiber101001000BASEGTSFP", 119),
          ("fiber2500BASELX8SFM", 120),
          ("fiber1000BASELH2CHCCSFP", 121),
          ("fiber1000BASELH2CHCSFP", 122),
          ("fiber1000BASELXCSFP", 123),
          ("fiber10GBASELR16SFXP", 124),
          ("fiber2500BASELX16SFMP", 125),
          ("fiber1000BASELX16SFGP", 126),
          ("fiber400GVR4QSFP112", 127),
          ("fiber10GCOPPER16SFXP", 128),
          ("fiber400GDR4QSFP112L", 129),
          ("fiber400GSR8QSFP112", 130),
          ("fiber1000BASELXSGSFP", 131),
          ("fiber1000BASELXSGCSFP", 132),
          ("fiber800GVR8OSFP112", 133),
          ("fiber800G2VR4OSFP112", 134),
          ("fiber800GSR8OSFP112", 135),
          ("fiber800G2SR4OSFP112", 136),
          ("fiber800GDR8OSFP112", 137),
          ("fiber800G2DR4OSFP112", 138),
          ("fiber800GDR8OSFP112L", 139),
          ("fiber800G2DR4OSFP112L", 140),
          ("fiber800GDR8TWOOSFP112", 141),
          ("fiber800G2FR4OSFP112", 142),
          ("fiber800GPASSIVECOPPEROSFP112", 143),
          ("fiber800GACTIVECOPPEROSFP112", 144),
          ("fiber800GACTIVECABLEOSFP112", 145),
          ("fiber800GLOOPBACKOSFP112", 146),
          ("fiber100GPASSIVECOPPERQSFP56", 147),
          ("fiber100GACTIVECABLEQSFP56", 148))
    )


_RuijieFiberTransceiverType_Type.__name__ = "Integer32"
_RuijieFiberTransceiverType_Object = MibTableColumn
ruijieFiberTransceiverType = _RuijieFiberTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 3),
    _RuijieFiberTransceiverType_Type()
)
ruijieFiberTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransceiverType.setStatus("current")


class _RuijieFiberConnectorType_Type(Integer32):
    """Custom type ruijieFiberConnectorType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("meaningless", 0),
          ("unknownorunspecified", 1),
          ("vendorspecific", 2),
          ("sc", 3),
          ("fiberChannelStyle1CopperConnector", 4),
          ("fiberChannelStyle2CopperConnector", 5),
          ("bncortnc", 6),
          ("fiberChannelCoaxialHeaders", 7),
          ("fiberJack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalPigtail", 13),
          ("hssdcII", 14),
          ("copperPigtail", 15),
          ("mpo", 16),
          ("rj45", 17),
          ("noSeparableConnector", 18),
          ("mxc", 19),
          ("CSOpticalConnector", 20),
          ("SNOpticalConnector", 21))
    )


_RuijieFiberConnectorType_Type.__name__ = "Integer32"
_RuijieFiberConnectorType_Object = MibTableColumn
ruijieFiberConnectorType = _RuijieFiberConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 4),
    _RuijieFiberConnectorType_Type()
)
ruijieFiberConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberConnectorType.setStatus("current")
_RuijieFiberWavelength_Type = Integer32
_RuijieFiberWavelength_Object = MibTableColumn
ruijieFiberWavelength = _RuijieFiberWavelength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 5),
    _RuijieFiberWavelength_Type()
)
ruijieFiberWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberWavelength.setStatus("current")
_RuijieFiberTransferDistanceSMF_Type = Integer32
_RuijieFiberTransferDistanceSMF_Object = MibTableColumn
ruijieFiberTransferDistanceSMF = _RuijieFiberTransferDistanceSMF_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 6),
    _RuijieFiberTransferDistanceSMF_Type()
)
ruijieFiberTransferDistanceSMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistanceSMF.setStatus("current")
_RuijieFiberTransferDistance62point5umOM1_Type = Integer32
_RuijieFiberTransferDistance62point5umOM1_Object = MibTableColumn
ruijieFiberTransferDistance62point5umOM1 = _RuijieFiberTransferDistance62point5umOM1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 7),
    _RuijieFiberTransferDistance62point5umOM1_Type()
)
ruijieFiberTransferDistance62point5umOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance62point5umOM1.setStatus("current")
_RuijieFiberTransferDistance62point5um_Type = Integer32
_RuijieFiberTransferDistance62point5um_Object = MibTableColumn
ruijieFiberTransferDistance62point5um = _RuijieFiberTransferDistance62point5um_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 8),
    _RuijieFiberTransferDistance62point5um_Type()
)
ruijieFiberTransferDistance62point5um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance62point5um.setStatus("current")
_RuijieFiberTransferDistance50umOM2_Type = Integer32
_RuijieFiberTransferDistance50umOM2_Object = MibTableColumn
ruijieFiberTransferDistance50umOM2 = _RuijieFiberTransferDistance50umOM2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 9),
    _RuijieFiberTransferDistance50umOM2_Type()
)
ruijieFiberTransferDistance50umOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance50umOM2.setStatus("current")
_RuijieFiberTransferDistance50um_Type = Integer32
_RuijieFiberTransferDistance50um_Object = MibTableColumn
ruijieFiberTransferDistance50um = _RuijieFiberTransferDistance50um_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 10),
    _RuijieFiberTransferDistance50um_Type()
)
ruijieFiberTransferDistance50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance50um.setStatus("current")
_RuijieFiberTransferDistance50umOM3_Type = Integer32
_RuijieFiberTransferDistance50umOM3_Object = MibTableColumn
ruijieFiberTransferDistance50umOM3 = _RuijieFiberTransferDistance50umOM3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 11),
    _RuijieFiberTransferDistance50umOM3_Type()
)
ruijieFiberTransferDistance50umOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance50umOM3.setStatus("current")
_RuijieFiberTransferDistanceEBW50um_Type = Integer32
_RuijieFiberTransferDistanceEBW50um_Object = MibTableColumn
ruijieFiberTransferDistanceEBW50um = _RuijieFiberTransferDistanceEBW50um_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 12),
    _RuijieFiberTransferDistanceEBW50um_Type()
)
ruijieFiberTransferDistanceEBW50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistanceEBW50um.setStatus("current")
_RuijieFiberTransferDistanceCopper_Type = Integer32
_RuijieFiberTransferDistanceCopper_Object = MibTableColumn
ruijieFiberTransferDistanceCopper = _RuijieFiberTransferDistanceCopper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 13),
    _RuijieFiberTransferDistanceCopper_Type()
)
ruijieFiberTransferDistanceCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistanceCopper.setStatus("current")
_RuijieFiberTransferDistanceCableAssembly_Type = Integer32
_RuijieFiberTransferDistanceCableAssembly_Object = MibTableColumn
ruijieFiberTransferDistanceCableAssembly = _RuijieFiberTransferDistanceCableAssembly_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 14),
    _RuijieFiberTransferDistanceCableAssembly_Type()
)
ruijieFiberTransferDistanceCableAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistanceCableAssembly.setStatus("current")
_RuijieFiberDDMSupportStatus_Type = TruthValue
_RuijieFiberDDMSupportStatus_Object = MibTableColumn
ruijieFiberDDMSupportStatus = _RuijieFiberDDMSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 15),
    _RuijieFiberDDMSupportStatus_Type()
)
ruijieFiberDDMSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberDDMSupportStatus.setStatus("current")


class _RuijieFiberSerialNumber_Type(DisplayString):
    """Custom type ruijieFiberSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieFiberSerialNumber_Type.__name__ = "DisplayString"
_RuijieFiberSerialNumber_Object = MibTableColumn
ruijieFiberSerialNumber = _RuijieFiberSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 16),
    _RuijieFiberSerialNumber_Type()
)
ruijieFiberSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberSerialNumber.setStatus("current")
_RuijieFiberTemp_Type = Integer32
_RuijieFiberTemp_Object = MibTableColumn
ruijieFiberTemp = _RuijieFiberTemp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 17),
    _RuijieFiberTemp_Type()
)
ruijieFiberTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTemp.setStatus("current")


class _RuijieFiberTempStatus_Type(Integer32):
    """Custom type ruijieFiberTempStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberTempStatus_Type.__name__ = "Integer32"
_RuijieFiberTempStatus_Object = MibTableColumn
ruijieFiberTempStatus = _RuijieFiberTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 18),
    _RuijieFiberTempStatus_Type()
)
ruijieFiberTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTempStatus.setStatus("current")
_RuijieFiberVoltage_Type = Integer32
_RuijieFiberVoltage_Object = MibTableColumn
ruijieFiberVoltage = _RuijieFiberVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 19),
    _RuijieFiberVoltage_Type()
)
ruijieFiberVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVoltage.setStatus("current")


class _RuijieFiberVoltageStatus_Type(Integer32):
    """Custom type ruijieFiberVoltageStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberVoltageStatus_Type.__name__ = "Integer32"
_RuijieFiberVoltageStatus_Object = MibTableColumn
ruijieFiberVoltageStatus = _RuijieFiberVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 20),
    _RuijieFiberVoltageStatus_Type()
)
ruijieFiberVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVoltageStatus.setStatus("current")
_RuijieFiberBias_Type = Integer32
_RuijieFiberBias_Object = MibTableColumn
ruijieFiberBias = _RuijieFiberBias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 21),
    _RuijieFiberBias_Type()
)
ruijieFiberBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBias.setStatus("current")


class _RuijieFiberBiasStatus_Type(Integer32):
    """Custom type ruijieFiberBiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberBiasStatus_Type.__name__ = "Integer32"
_RuijieFiberBiasStatus_Object = MibTableColumn
ruijieFiberBiasStatus = _RuijieFiberBiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 22),
    _RuijieFiberBiasStatus_Type()
)
ruijieFiberBiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBiasStatus.setStatus("current")
_RuijieFiberChannel1Bias_Type = Integer32
_RuijieFiberChannel1Bias_Object = MibTableColumn
ruijieFiberChannel1Bias = _RuijieFiberChannel1Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 23),
    _RuijieFiberChannel1Bias_Type()
)
ruijieFiberChannel1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1Bias.setStatus("current")


class _RuijieFiberChannel1BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel1BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel1BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel1BiasStatus_Object = MibTableColumn
ruijieFiberChannel1BiasStatus = _RuijieFiberChannel1BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 24),
    _RuijieFiberChannel1BiasStatus_Type()
)
ruijieFiberChannel1BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1BiasStatus.setStatus("current")
_RuijieFiberChannel2Bias_Type = Integer32
_RuijieFiberChannel2Bias_Object = MibTableColumn
ruijieFiberChannel2Bias = _RuijieFiberChannel2Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 25),
    _RuijieFiberChannel2Bias_Type()
)
ruijieFiberChannel2Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2Bias.setStatus("current")


class _RuijieFiberChannel2BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel2BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel2BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel2BiasStatus_Object = MibTableColumn
ruijieFiberChannel2BiasStatus = _RuijieFiberChannel2BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 26),
    _RuijieFiberChannel2BiasStatus_Type()
)
ruijieFiberChannel2BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2BiasStatus.setStatus("current")
_RuijieFiberChannel3Bias_Type = Integer32
_RuijieFiberChannel3Bias_Object = MibTableColumn
ruijieFiberChannel3Bias = _RuijieFiberChannel3Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 27),
    _RuijieFiberChannel3Bias_Type()
)
ruijieFiberChannel3Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3Bias.setStatus("current")


class _RuijieFiberChannel3BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel3BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel3BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel3BiasStatus_Object = MibTableColumn
ruijieFiberChannel3BiasStatus = _RuijieFiberChannel3BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 28),
    _RuijieFiberChannel3BiasStatus_Type()
)
ruijieFiberChannel3BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3BiasStatus.setStatus("current")
_RuijieFiberChannel4Bias_Type = Integer32
_RuijieFiberChannel4Bias_Object = MibTableColumn
ruijieFiberChannel4Bias = _RuijieFiberChannel4Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 29),
    _RuijieFiberChannel4Bias_Type()
)
ruijieFiberChannel4Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4Bias.setStatus("current")


class _RuijieFiberChannel4BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel4BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel4BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel4BiasStatus_Object = MibTableColumn
ruijieFiberChannel4BiasStatus = _RuijieFiberChannel4BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 30),
    _RuijieFiberChannel4BiasStatus_Type()
)
ruijieFiberChannel4BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4BiasStatus.setStatus("current")
_RuijieFiberRXpowerIntegerpart_Type = Integer32
_RuijieFiberRXpowerIntegerpart_Object = MibTableColumn
ruijieFiberRXpowerIntegerpart = _RuijieFiberRXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 31),
    _RuijieFiberRXpowerIntegerpart_Type()
)
ruijieFiberRXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerIntegerpart.setStatus("current")
_RuijieFiberRXpowerDecimalpart_Type = Integer32
_RuijieFiberRXpowerDecimalpart_Object = MibTableColumn
ruijieFiberRXpowerDecimalpart = _RuijieFiberRXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 32),
    _RuijieFiberRXpowerDecimalpart_Type()
)
ruijieFiberRXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerDecimalpart.setStatus("current")


class _RuijieFiberRXpowertype_Type(Integer32):
    """Custom type ruijieFiberRXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberRXpowertype_Type.__name__ = "Integer32"
_RuijieFiberRXpowertype_Object = MibTableColumn
ruijieFiberRXpowertype = _RuijieFiberRXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 33),
    _RuijieFiberRXpowertype_Type()
)
ruijieFiberRXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowertype.setStatus("current")


class _RuijieFiberRXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberRXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberRXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberRXpowerStatus_Object = MibTableColumn
ruijieFiberRXpowerStatus = _RuijieFiberRXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 34),
    _RuijieFiberRXpowerStatus_Type()
)
ruijieFiberRXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerStatus.setStatus("current")
_RuijieFiberChannel1RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel1RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel1RXpowerIntegerpart = _RuijieFiberChannel1RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 35),
    _RuijieFiberChannel1RXpowerIntegerpart_Type()
)
ruijieFiberChannel1RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel1RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel1RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel1RXpowerDecimalpart = _RuijieFiberChannel1RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 36),
    _RuijieFiberChannel1RXpowerDecimalpart_Type()
)
ruijieFiberChannel1RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel1RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel1RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel1RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel1RXpowertype_Object = MibTableColumn
ruijieFiberChannel1RXpowertype = _RuijieFiberChannel1RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 37),
    _RuijieFiberChannel1RXpowertype_Type()
)
ruijieFiberChannel1RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1RXpowertype.setStatus("current")


class _RuijieFiberChannel1RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel1RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel1RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel1RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel1RXpowerStatus = _RuijieFiberChannel1RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 38),
    _RuijieFiberChannel1RXpowerStatus_Type()
)
ruijieFiberChannel1RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1RXpowerStatus.setStatus("current")
_RuijieFiberChannel2RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel2RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel2RXpowerIntegerpart = _RuijieFiberChannel2RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 39),
    _RuijieFiberChannel2RXpowerIntegerpart_Type()
)
ruijieFiberChannel2RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel2RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel2RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel2RXpowerDecimalpart = _RuijieFiberChannel2RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 40),
    _RuijieFiberChannel2RXpowerDecimalpart_Type()
)
ruijieFiberChannel2RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel2RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel2RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel2RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel2RXpowertype_Object = MibTableColumn
ruijieFiberChannel2RXpowertype = _RuijieFiberChannel2RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 41),
    _RuijieFiberChannel2RXpowertype_Type()
)
ruijieFiberChannel2RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2RXpowertype.setStatus("current")


class _RuijieFiberChannel2RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel2RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel2RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel2RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel2RXpowerStatus = _RuijieFiberChannel2RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 42),
    _RuijieFiberChannel2RXpowerStatus_Type()
)
ruijieFiberChannel2RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2RXpowerStatus.setStatus("current")
_RuijieFiberChannel3RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel3RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel3RXpowerIntegerpart = _RuijieFiberChannel3RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 43),
    _RuijieFiberChannel3RXpowerIntegerpart_Type()
)
ruijieFiberChannel3RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel3RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel3RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel3RXpowerDecimalpart = _RuijieFiberChannel3RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 44),
    _RuijieFiberChannel3RXpowerDecimalpart_Type()
)
ruijieFiberChannel3RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel3RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel3RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel3RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel3RXpowertype_Object = MibTableColumn
ruijieFiberChannel3RXpowertype = _RuijieFiberChannel3RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 45),
    _RuijieFiberChannel3RXpowertype_Type()
)
ruijieFiberChannel3RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3RXpowertype.setStatus("current")


class _RuijieFiberChannel3RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel3RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel3RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel3RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel3RXpowerStatus = _RuijieFiberChannel3RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 46),
    _RuijieFiberChannel3RXpowerStatus_Type()
)
ruijieFiberChannel3RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3RXpowerStatus.setStatus("current")
_RuijieFiberChannel4RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel4RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel4RXpowerIntegerpart = _RuijieFiberChannel4RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 47),
    _RuijieFiberChannel4RXpowerIntegerpart_Type()
)
ruijieFiberChannel4RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel4RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel4RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel4RXpowerDecimalpart = _RuijieFiberChannel4RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 48),
    _RuijieFiberChannel4RXpowerDecimalpart_Type()
)
ruijieFiberChannel4RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel4RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel4RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel4RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel4RXpowertype_Object = MibTableColumn
ruijieFiberChannel4RXpowertype = _RuijieFiberChannel4RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 49),
    _RuijieFiberChannel4RXpowertype_Type()
)
ruijieFiberChannel4RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4RXpowertype.setStatus("current")


class _RuijieFiberChannel4RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel4RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel4RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel4RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel4RXpowerStatus = _RuijieFiberChannel4RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 50),
    _RuijieFiberChannel4RXpowerStatus_Type()
)
ruijieFiberChannel4RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4RXpowerStatus.setStatus("current")
_RuijieFiberTXpowerIntegerpart_Type = Integer32
_RuijieFiberTXpowerIntegerpart_Object = MibTableColumn
ruijieFiberTXpowerIntegerpart = _RuijieFiberTXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 51),
    _RuijieFiberTXpowerIntegerpart_Type()
)
ruijieFiberTXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerIntegerpart.setStatus("current")
_RuijieFiberTXpowerDecimalpart_Type = Integer32
_RuijieFiberTXpowerDecimalpart_Object = MibTableColumn
ruijieFiberTXpowerDecimalpart = _RuijieFiberTXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 52),
    _RuijieFiberTXpowerDecimalpart_Type()
)
ruijieFiberTXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerDecimalpart.setStatus("current")


class _RuijieFiberTXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberTXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberTXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberTXpowerStatus_Object = MibTableColumn
ruijieFiberTXpowerStatus = _RuijieFiberTXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 53),
    _RuijieFiberTXpowerStatus_Type()
)
ruijieFiberTXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerStatus.setStatus("current")
_RuijieFiberChannel1TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel1TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel1TXpowerIntegerpart = _RuijieFiberChannel1TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 54),
    _RuijieFiberChannel1TXpowerIntegerpart_Type()
)
ruijieFiberChannel1TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel1TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel1TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel1TXpowerDecimalpart = _RuijieFiberChannel1TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 55),
    _RuijieFiberChannel1TXpowerDecimalpart_Type()
)
ruijieFiberChannel1TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel1TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel1TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel1TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel1TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel1TXpowerStatus = _RuijieFiberChannel1TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 56),
    _RuijieFiberChannel1TXpowerStatus_Type()
)
ruijieFiberChannel1TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1TXpowerStatus.setStatus("current")
_RuijieFiberChannel2TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel2TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel2TXpowerIntegerpart = _RuijieFiberChannel2TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 57),
    _RuijieFiberChannel2TXpowerIntegerpart_Type()
)
ruijieFiberChannel2TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel2TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel2TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel2TXpowerDecimalpart = _RuijieFiberChannel2TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 58),
    _RuijieFiberChannel2TXpowerDecimalpart_Type()
)
ruijieFiberChannel2TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel2TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel2TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel2TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel2TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel2TXpowerStatus = _RuijieFiberChannel2TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 59),
    _RuijieFiberChannel2TXpowerStatus_Type()
)
ruijieFiberChannel2TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2TXpowerStatus.setStatus("current")
_RuijieFiberChannel3TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel3TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel3TXpowerIntegerpart = _RuijieFiberChannel3TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 60),
    _RuijieFiberChannel3TXpowerIntegerpart_Type()
)
ruijieFiberChannel3TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel3TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel3TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel3TXpowerDecimalpart = _RuijieFiberChannel3TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 61),
    _RuijieFiberChannel3TXpowerDecimalpart_Type()
)
ruijieFiberChannel3TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel3TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel3TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel3TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel3TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel3TXpowerStatus = _RuijieFiberChannel3TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 62),
    _RuijieFiberChannel3TXpowerStatus_Type()
)
ruijieFiberChannel3TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3TXpowerStatus.setStatus("current")
_RuijieFiberChannel4TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel4TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel4TXpowerIntegerpart = _RuijieFiberChannel4TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 63),
    _RuijieFiberChannel4TXpowerIntegerpart_Type()
)
ruijieFiberChannel4TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel4TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel4TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel4TXpowerDecimalpart = _RuijieFiberChannel4TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 64),
    _RuijieFiberChannel4TXpowerDecimalpart_Type()
)
ruijieFiberChannel4TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel4TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel4TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel4TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel4TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel4TXpowerStatus = _RuijieFiberChannel4TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 65),
    _RuijieFiberChannel4TXpowerStatus_Type()
)
ruijieFiberChannel4TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4TXpowerStatus.setStatus("current")
_RuijieFiberRXpowerSign_Type = Integer32
_RuijieFiberRXpowerSign_Object = MibTableColumn
ruijieFiberRXpowerSign = _RuijieFiberRXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 66),
    _RuijieFiberRXpowerSign_Type()
)
ruijieFiberRXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerSign.setStatus("current")
_RuijieFiberChannel1RXpowerSign_Type = Integer32
_RuijieFiberChannel1RXpowerSign_Object = MibTableColumn
ruijieFiberChannel1RXpowerSign = _RuijieFiberChannel1RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 67),
    _RuijieFiberChannel1RXpowerSign_Type()
)
ruijieFiberChannel1RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1RXpowerSign.setStatus("current")
_RuijieFiberChannel2RXpowerSign_Type = Integer32
_RuijieFiberChannel2RXpowerSign_Object = MibTableColumn
ruijieFiberChannel2RXpowerSign = _RuijieFiberChannel2RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 68),
    _RuijieFiberChannel2RXpowerSign_Type()
)
ruijieFiberChannel2RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2RXpowerSign.setStatus("current")
_RuijieFiberChannel3RXpowerSign_Type = Integer32
_RuijieFiberChannel3RXpowerSign_Object = MibTableColumn
ruijieFiberChannel3RXpowerSign = _RuijieFiberChannel3RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 69),
    _RuijieFiberChannel3RXpowerSign_Type()
)
ruijieFiberChannel3RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3RXpowerSign.setStatus("current")
_RuijieFiberChannel4RXpowerSign_Type = Integer32
_RuijieFiberChannel4RXpowerSign_Object = MibTableColumn
ruijieFiberChannel4RXpowerSign = _RuijieFiberChannel4RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 70),
    _RuijieFiberChannel4RXpowerSign_Type()
)
ruijieFiberChannel4RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4RXpowerSign.setStatus("current")
_RuijieFiberTXpowerSign_Type = Integer32
_RuijieFiberTXpowerSign_Object = MibTableColumn
ruijieFiberTXpowerSign = _RuijieFiberTXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 71),
    _RuijieFiberTXpowerSign_Type()
)
ruijieFiberTXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerSign.setStatus("current")
_RuijieFiberChannel1TXpowerSign_Type = Integer32
_RuijieFiberChannel1TXpowerSign_Object = MibTableColumn
ruijieFiberChannel1TXpowerSign = _RuijieFiberChannel1TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 72),
    _RuijieFiberChannel1TXpowerSign_Type()
)
ruijieFiberChannel1TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1TXpowerSign.setStatus("current")
_RuijieFiberChannel2TXpowerSign_Type = Integer32
_RuijieFiberChannel2TXpowerSign_Object = MibTableColumn
ruijieFiberChannel2TXpowerSign = _RuijieFiberChannel2TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 73),
    _RuijieFiberChannel2TXpowerSign_Type()
)
ruijieFiberChannel2TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2TXpowerSign.setStatus("current")
_RuijieFiberChannel3TXpowerSign_Type = Integer32
_RuijieFiberChannel3TXpowerSign_Object = MibTableColumn
ruijieFiberChannel3TXpowerSign = _RuijieFiberChannel3TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 74),
    _RuijieFiberChannel3TXpowerSign_Type()
)
ruijieFiberChannel3TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3TXpowerSign.setStatus("current")
_RuijieFiberChannel4TXpowerSign_Type = Integer32
_RuijieFiberChannel4TXpowerSign_Object = MibTableColumn
ruijieFiberChannel4TXpowerSign = _RuijieFiberChannel4TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 75),
    _RuijieFiberChannel4TXpowerSign_Type()
)
ruijieFiberChannel4TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4TXpowerSign.setStatus("current")
_RuijieFiberRXpower_Type = Integer32
_RuijieFiberRXpower_Object = MibTableColumn
ruijieFiberRXpower = _RuijieFiberRXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 76),
    _RuijieFiberRXpower_Type()
)
ruijieFiberRXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpower.setStatus("current")
_RuijieFiberChannel1RXpower_Type = Integer32
_RuijieFiberChannel1RXpower_Object = MibTableColumn
ruijieFiberChannel1RXpower = _RuijieFiberChannel1RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 77),
    _RuijieFiberChannel1RXpower_Type()
)
ruijieFiberChannel1RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1RXpower.setStatus("current")
_RuijieFiberChannel2RXpower_Type = Integer32
_RuijieFiberChannel2RXpower_Object = MibTableColumn
ruijieFiberChannel2RXpower = _RuijieFiberChannel2RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 78),
    _RuijieFiberChannel2RXpower_Type()
)
ruijieFiberChannel2RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2RXpower.setStatus("current")
_RuijieFiberChannel3RXpower_Type = Integer32
_RuijieFiberChannel3RXpower_Object = MibTableColumn
ruijieFiberChannel3RXpower = _RuijieFiberChannel3RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 79),
    _RuijieFiberChannel3RXpower_Type()
)
ruijieFiberChannel3RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3RXpower.setStatus("current")
_RuijieFiberChannel4RXpower_Type = Integer32
_RuijieFiberChannel4RXpower_Object = MibTableColumn
ruijieFiberChannel4RXpower = _RuijieFiberChannel4RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 80),
    _RuijieFiberChannel4RXpower_Type()
)
ruijieFiberChannel4RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4RXpower.setStatus("current")
_RuijieFiberTXpower_Type = Integer32
_RuijieFiberTXpower_Object = MibTableColumn
ruijieFiberTXpower = _RuijieFiberTXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 81),
    _RuijieFiberTXpower_Type()
)
ruijieFiberTXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpower.setStatus("current")
_RuijieFiberChannel1TXpower_Type = Integer32
_RuijieFiberChannel1TXpower_Object = MibTableColumn
ruijieFiberChannel1TXpower = _RuijieFiberChannel1TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 82),
    _RuijieFiberChannel1TXpower_Type()
)
ruijieFiberChannel1TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel1TXpower.setStatus("current")
_RuijieFiberChannel2TXpower_Type = Integer32
_RuijieFiberChannel2TXpower_Object = MibTableColumn
ruijieFiberChannel2TXpower = _RuijieFiberChannel2TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 83),
    _RuijieFiberChannel2TXpower_Type()
)
ruijieFiberChannel2TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel2TXpower.setStatus("current")
_RuijieFiberChannel3TXpower_Type = Integer32
_RuijieFiberChannel3TXpower_Object = MibTableColumn
ruijieFiberChannel3TXpower = _RuijieFiberChannel3TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 84),
    _RuijieFiberChannel3TXpower_Type()
)
ruijieFiberChannel3TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel3TXpower.setStatus("current")
_RuijieFiberChannel4TXpower_Type = Integer32
_RuijieFiberChannel4TXpower_Object = MibTableColumn
ruijieFiberChannel4TXpower = _RuijieFiberChannel4TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 85),
    _RuijieFiberChannel4TXpower_Type()
)
ruijieFiberChannel4TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel4TXpower.setStatus("current")


class _RuijieFiberWavelengthExact_Type(DisplayString):
    """Custom type ruijieFiberWavelengthExact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieFiberWavelengthExact_Type.__name__ = "DisplayString"
_RuijieFiberWavelengthExact_Object = MibTableColumn
ruijieFiberWavelengthExact = _RuijieFiberWavelengthExact_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 86),
    _RuijieFiberWavelengthExact_Type()
)
ruijieFiberWavelengthExact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberWavelengthExact.setStatus("current")
_RuijieFiberTransferDistance50umOM4_Type = Integer32
_RuijieFiberTransferDistance50umOM4_Object = MibTableColumn
ruijieFiberTransferDistance50umOM4 = _RuijieFiberTransferDistance50umOM4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 87),
    _RuijieFiberTransferDistance50umOM4_Type()
)
ruijieFiberTransferDistance50umOM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance50umOM4.setStatus("current")
_RuijieFiberTransferDistanceSMFExt_Type = Integer32
_RuijieFiberTransferDistanceSMFExt_Object = MibTableColumn
ruijieFiberTransferDistanceSMFExt = _RuijieFiberTransferDistanceSMFExt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 88),
    _RuijieFiberTransferDistanceSMFExt_Type()
)
ruijieFiberTransferDistanceSMFExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistanceSMFExt.setStatus("current")
_RuijieFiberBandWidth_Type = Integer32
_RuijieFiberBandWidth_Object = MibTableColumn
ruijieFiberBandWidth = _RuijieFiberBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 89),
    _RuijieFiberBandWidth_Type()
)
ruijieFiberBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBandWidth.setStatus("current")


class _RuijieFiberFormFactor_Type(Integer32):
    """Custom type ruijieFiberFormFactor based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("xfp", 1),
          ("sfp", 2),
          ("sfpPlus", 3),
          ("sfp28", 4),
          ("qsfpPlus", 5),
          ("qsfp28", 6),
          ("qsfp56", 7),
          ("qsfpDD", 8),
          ("dsfp", 9),
          ("qsfp112", 10))
    )


_RuijieFiberFormFactor_Type.__name__ = "Integer32"
_RuijieFiberFormFactor_Object = MibTableColumn
ruijieFiberFormFactor = _RuijieFiberFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 90),
    _RuijieFiberFormFactor_Type()
)
ruijieFiberFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberFormFactor.setStatus("current")
_RuijieFiberRXpowerLowWarnThreshold_Type = Integer32
_RuijieFiberRXpowerLowWarnThreshold_Object = MibTableColumn
ruijieFiberRXpowerLowWarnThreshold = _RuijieFiberRXpowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 91),
    _RuijieFiberRXpowerLowWarnThreshold_Type()
)
ruijieFiberRXpowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerLowWarnThreshold.setStatus("current")
_RuijieFiberRXpowerHighWarnThreshold_Type = Integer32
_RuijieFiberRXpowerHighWarnThreshold_Object = MibTableColumn
ruijieFiberRXpowerHighWarnThreshold = _RuijieFiberRXpowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 92),
    _RuijieFiberRXpowerHighWarnThreshold_Type()
)
ruijieFiberRXpowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerHighWarnThreshold.setStatus("current")
_RuijieFiberRXpowerLowAlarmThreshold_Type = Integer32
_RuijieFiberRXpowerLowAlarmThreshold_Object = MibTableColumn
ruijieFiberRXpowerLowAlarmThreshold = _RuijieFiberRXpowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 93),
    _RuijieFiberRXpowerLowAlarmThreshold_Type()
)
ruijieFiberRXpowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerLowAlarmThreshold.setStatus("current")
_RuijieFiberRXpowerHighAlarmThreshold_Type = Integer32
_RuijieFiberRXpowerHighAlarmThreshold_Object = MibTableColumn
ruijieFiberRXpowerHighAlarmThreshold = _RuijieFiberRXpowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 94),
    _RuijieFiberRXpowerHighAlarmThreshold_Type()
)
ruijieFiberRXpowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberRXpowerHighAlarmThreshold.setStatus("current")
_RuijieFiberTXpowerLowWarnThreshold_Type = Integer32
_RuijieFiberTXpowerLowWarnThreshold_Object = MibTableColumn
ruijieFiberTXpowerLowWarnThreshold = _RuijieFiberTXpowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 95),
    _RuijieFiberTXpowerLowWarnThreshold_Type()
)
ruijieFiberTXpowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerLowWarnThreshold.setStatus("current")
_RuijieFiberTXpowerHighWarnThreshold_Type = Integer32
_RuijieFiberTXpowerHighWarnThreshold_Object = MibTableColumn
ruijieFiberTXpowerHighWarnThreshold = _RuijieFiberTXpowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 96),
    _RuijieFiberTXpowerHighWarnThreshold_Type()
)
ruijieFiberTXpowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerHighWarnThreshold.setStatus("current")
_RuijieFiberTXpowerLowAlarmThreshold_Type = Integer32
_RuijieFiberTXpowerLowAlarmThreshold_Object = MibTableColumn
ruijieFiberTXpowerLowAlarmThreshold = _RuijieFiberTXpowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 97),
    _RuijieFiberTXpowerLowAlarmThreshold_Type()
)
ruijieFiberTXpowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerLowAlarmThreshold.setStatus("current")
_RuijieFiberTXpowerHighAlarmThreshold_Type = Integer32
_RuijieFiberTXpowerHighAlarmThreshold_Object = MibTableColumn
ruijieFiberTXpowerHighAlarmThreshold = _RuijieFiberTXpowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 98),
    _RuijieFiberTXpowerHighAlarmThreshold_Type()
)
ruijieFiberTXpowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTXpowerHighAlarmThreshold.setStatus("current")
_RuijieFiberChannel5Bias_Type = Integer32
_RuijieFiberChannel5Bias_Object = MibTableColumn
ruijieFiberChannel5Bias = _RuijieFiberChannel5Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 99),
    _RuijieFiberChannel5Bias_Type()
)
ruijieFiberChannel5Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5Bias.setStatus("current")


class _RuijieFiberChannel5BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel5BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel5BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel5BiasStatus_Object = MibTableColumn
ruijieFiberChannel5BiasStatus = _RuijieFiberChannel5BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 100),
    _RuijieFiberChannel5BiasStatus_Type()
)
ruijieFiberChannel5BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5BiasStatus.setStatus("current")
_RuijieFiberChannel6Bias_Type = Integer32
_RuijieFiberChannel6Bias_Object = MibTableColumn
ruijieFiberChannel6Bias = _RuijieFiberChannel6Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 101),
    _RuijieFiberChannel6Bias_Type()
)
ruijieFiberChannel6Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6Bias.setStatus("current")


class _RuijieFiberChannel6BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel6BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel6BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel6BiasStatus_Object = MibTableColumn
ruijieFiberChannel6BiasStatus = _RuijieFiberChannel6BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 102),
    _RuijieFiberChannel6BiasStatus_Type()
)
ruijieFiberChannel6BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6BiasStatus.setStatus("current")
_RuijieFiberChannel7Bias_Type = Integer32
_RuijieFiberChannel7Bias_Object = MibTableColumn
ruijieFiberChannel7Bias = _RuijieFiberChannel7Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 103),
    _RuijieFiberChannel7Bias_Type()
)
ruijieFiberChannel7Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7Bias.setStatus("current")


class _RuijieFiberChannel7BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel7BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel7BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel7BiasStatus_Object = MibTableColumn
ruijieFiberChannel7BiasStatus = _RuijieFiberChannel7BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 104),
    _RuijieFiberChannel7BiasStatus_Type()
)
ruijieFiberChannel7BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7BiasStatus.setStatus("current")
_RuijieFiberChannel8Bias_Type = Integer32
_RuijieFiberChannel8Bias_Object = MibTableColumn
ruijieFiberChannel8Bias = _RuijieFiberChannel8Bias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 105),
    _RuijieFiberChannel8Bias_Type()
)
ruijieFiberChannel8Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8Bias.setStatus("current")


class _RuijieFiberChannel8BiasStatus_Type(Integer32):
    """Custom type ruijieFiberChannel8BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel8BiasStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel8BiasStatus_Object = MibTableColumn
ruijieFiberChannel8BiasStatus = _RuijieFiberChannel8BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 106),
    _RuijieFiberChannel8BiasStatus_Type()
)
ruijieFiberChannel8BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8BiasStatus.setStatus("current")
_RuijieFiberChannel5RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel5RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel5RXpowerIntegerpart = _RuijieFiberChannel5RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 107),
    _RuijieFiberChannel5RXpowerIntegerpart_Type()
)
ruijieFiberChannel5RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel5RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel5RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel5RXpowerDecimalpart = _RuijieFiberChannel5RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 108),
    _RuijieFiberChannel5RXpowerDecimalpart_Type()
)
ruijieFiberChannel5RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel5RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel5RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel5RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel5RXpowertype_Object = MibTableColumn
ruijieFiberChannel5RXpowertype = _RuijieFiberChannel5RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 109),
    _RuijieFiberChannel5RXpowertype_Type()
)
ruijieFiberChannel5RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5RXpowertype.setStatus("current")


class _RuijieFiberChannel5RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel5RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel5RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel5RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel5RXpowerStatus = _RuijieFiberChannel5RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 110),
    _RuijieFiberChannel5RXpowerStatus_Type()
)
ruijieFiberChannel5RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5RXpowerStatus.setStatus("current")
_RuijieFiberChannel6RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel6RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel6RXpowerIntegerpart = _RuijieFiberChannel6RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 111),
    _RuijieFiberChannel6RXpowerIntegerpart_Type()
)
ruijieFiberChannel6RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel6RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel6RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel6RXpowerDecimalpart = _RuijieFiberChannel6RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 112),
    _RuijieFiberChannel6RXpowerDecimalpart_Type()
)
ruijieFiberChannel6RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel6RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel6RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel6RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel6RXpowertype_Object = MibTableColumn
ruijieFiberChannel6RXpowertype = _RuijieFiberChannel6RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 113),
    _RuijieFiberChannel6RXpowertype_Type()
)
ruijieFiberChannel6RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6RXpowertype.setStatus("current")


class _RuijieFiberChannel6RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel6RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel6RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel6RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel6RXpowerStatus = _RuijieFiberChannel6RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 114),
    _RuijieFiberChannel6RXpowerStatus_Type()
)
ruijieFiberChannel6RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6RXpowerStatus.setStatus("current")
_RuijieFiberChannel7RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel7RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel7RXpowerIntegerpart = _RuijieFiberChannel7RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 115),
    _RuijieFiberChannel7RXpowerIntegerpart_Type()
)
ruijieFiberChannel7RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel7RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel7RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel7RXpowerDecimalpart = _RuijieFiberChannel7RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 116),
    _RuijieFiberChannel7RXpowerDecimalpart_Type()
)
ruijieFiberChannel7RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel7RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel7RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel7RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel7RXpowertype_Object = MibTableColumn
ruijieFiberChannel7RXpowertype = _RuijieFiberChannel7RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 117),
    _RuijieFiberChannel7RXpowertype_Type()
)
ruijieFiberChannel7RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7RXpowertype.setStatus("current")


class _RuijieFiberChannel7RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel7RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel7RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel7RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel7RXpowerStatus = _RuijieFiberChannel7RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 118),
    _RuijieFiberChannel7RXpowerStatus_Type()
)
ruijieFiberChannel7RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7RXpowerStatus.setStatus("current")
_RuijieFiberChannel8RXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel8RXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel8RXpowerIntegerpart = _RuijieFiberChannel8RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 119),
    _RuijieFiberChannel8RXpowerIntegerpart_Type()
)
ruijieFiberChannel8RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8RXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel8RXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel8RXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel8RXpowerDecimalpart = _RuijieFiberChannel8RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 120),
    _RuijieFiberChannel8RXpowerDecimalpart_Type()
)
ruijieFiberChannel8RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8RXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel8RXpowertype_Type(Integer32):
    """Custom type ruijieFiberChannel8RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_RuijieFiberChannel8RXpowertype_Type.__name__ = "Integer32"
_RuijieFiberChannel8RXpowertype_Object = MibTableColumn
ruijieFiberChannel8RXpowertype = _RuijieFiberChannel8RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 121),
    _RuijieFiberChannel8RXpowertype_Type()
)
ruijieFiberChannel8RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8RXpowertype.setStatus("current")


class _RuijieFiberChannel8RXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel8RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel8RXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel8RXpowerStatus_Object = MibTableColumn
ruijieFiberChannel8RXpowerStatus = _RuijieFiberChannel8RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 122),
    _RuijieFiberChannel8RXpowerStatus_Type()
)
ruijieFiberChannel8RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8RXpowerStatus.setStatus("current")
_RuijieFiberChannel5TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel5TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel5TXpowerIntegerpart = _RuijieFiberChannel5TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 123),
    _RuijieFiberChannel5TXpowerIntegerpart_Type()
)
ruijieFiberChannel5TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel5TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel5TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel5TXpowerDecimalpart = _RuijieFiberChannel5TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 124),
    _RuijieFiberChannel5TXpowerDecimalpart_Type()
)
ruijieFiberChannel5TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel5TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel5TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel5TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel5TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel5TXpowerStatus = _RuijieFiberChannel5TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 125),
    _RuijieFiberChannel5TXpowerStatus_Type()
)
ruijieFiberChannel5TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5TXpowerStatus.setStatus("current")
_RuijieFiberChannel6TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel6TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel6TXpowerIntegerpart = _RuijieFiberChannel6TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 126),
    _RuijieFiberChannel6TXpowerIntegerpart_Type()
)
ruijieFiberChannel6TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel6TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel6TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel6TXpowerDecimalpart = _RuijieFiberChannel6TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 127),
    _RuijieFiberChannel6TXpowerDecimalpart_Type()
)
ruijieFiberChannel6TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel6TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel6TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel6TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel6TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel6TXpowerStatus = _RuijieFiberChannel6TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 128),
    _RuijieFiberChannel6TXpowerStatus_Type()
)
ruijieFiberChannel6TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6TXpowerStatus.setStatus("current")
_RuijieFiberChannel7TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel7TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel7TXpowerIntegerpart = _RuijieFiberChannel7TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 129),
    _RuijieFiberChannel7TXpowerIntegerpart_Type()
)
ruijieFiberChannel7TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel7TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel7TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel7TXpowerDecimalpart = _RuijieFiberChannel7TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 130),
    _RuijieFiberChannel7TXpowerDecimalpart_Type()
)
ruijieFiberChannel7TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel7TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel7TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel7TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel7TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel7TXpowerStatus = _RuijieFiberChannel7TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 131),
    _RuijieFiberChannel7TXpowerStatus_Type()
)
ruijieFiberChannel7TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7TXpowerStatus.setStatus("current")
_RuijieFiberChannel8TXpowerIntegerpart_Type = Integer32
_RuijieFiberChannel8TXpowerIntegerpart_Object = MibTableColumn
ruijieFiberChannel8TXpowerIntegerpart = _RuijieFiberChannel8TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 132),
    _RuijieFiberChannel8TXpowerIntegerpart_Type()
)
ruijieFiberChannel8TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8TXpowerIntegerpart.setStatus("current")
_RuijieFiberChannel8TXpowerDecimalpart_Type = Integer32
_RuijieFiberChannel8TXpowerDecimalpart_Object = MibTableColumn
ruijieFiberChannel8TXpowerDecimalpart = _RuijieFiberChannel8TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 133),
    _RuijieFiberChannel8TXpowerDecimalpart_Type()
)
ruijieFiberChannel8TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8TXpowerDecimalpart.setStatus("current")


class _RuijieFiberChannel8TXpowerStatus_Type(Integer32):
    """Custom type ruijieFiberChannel8TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RuijieFiberChannel8TXpowerStatus_Type.__name__ = "Integer32"
_RuijieFiberChannel8TXpowerStatus_Object = MibTableColumn
ruijieFiberChannel8TXpowerStatus = _RuijieFiberChannel8TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 134),
    _RuijieFiberChannel8TXpowerStatus_Type()
)
ruijieFiberChannel8TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8TXpowerStatus.setStatus("current")
_RuijieFiberChannel5RXpowerSign_Type = Integer32
_RuijieFiberChannel5RXpowerSign_Object = MibTableColumn
ruijieFiberChannel5RXpowerSign = _RuijieFiberChannel5RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 135),
    _RuijieFiberChannel5RXpowerSign_Type()
)
ruijieFiberChannel5RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5RXpowerSign.setStatus("current")
_RuijieFiberChannel6RXpowerSign_Type = Integer32
_RuijieFiberChannel6RXpowerSign_Object = MibTableColumn
ruijieFiberChannel6RXpowerSign = _RuijieFiberChannel6RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 136),
    _RuijieFiberChannel6RXpowerSign_Type()
)
ruijieFiberChannel6RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6RXpowerSign.setStatus("current")
_RuijieFiberChannel7RXpowerSign_Type = Integer32
_RuijieFiberChannel7RXpowerSign_Object = MibTableColumn
ruijieFiberChannel7RXpowerSign = _RuijieFiberChannel7RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 137),
    _RuijieFiberChannel7RXpowerSign_Type()
)
ruijieFiberChannel7RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7RXpowerSign.setStatus("current")
_RuijieFiberChannel8RXpowerSign_Type = Integer32
_RuijieFiberChannel8RXpowerSign_Object = MibTableColumn
ruijieFiberChannel8RXpowerSign = _RuijieFiberChannel8RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 138),
    _RuijieFiberChannel8RXpowerSign_Type()
)
ruijieFiberChannel8RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8RXpowerSign.setStatus("current")
_RuijieFiberChannel5TXpowerSign_Type = Integer32
_RuijieFiberChannel5TXpowerSign_Object = MibTableColumn
ruijieFiberChannel5TXpowerSign = _RuijieFiberChannel5TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 139),
    _RuijieFiberChannel5TXpowerSign_Type()
)
ruijieFiberChannel5TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5TXpowerSign.setStatus("current")
_RuijieFiberChannel6TXpowerSign_Type = Integer32
_RuijieFiberChannel6TXpowerSign_Object = MibTableColumn
ruijieFiberChannel6TXpowerSign = _RuijieFiberChannel6TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 140),
    _RuijieFiberChannel6TXpowerSign_Type()
)
ruijieFiberChannel6TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6TXpowerSign.setStatus("current")
_RuijieFiberChannel7TXpowerSign_Type = Integer32
_RuijieFiberChannel7TXpowerSign_Object = MibTableColumn
ruijieFiberChannel7TXpowerSign = _RuijieFiberChannel7TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 141),
    _RuijieFiberChannel7TXpowerSign_Type()
)
ruijieFiberChannel7TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7TXpowerSign.setStatus("current")
_RuijieFiberChannel8TXpowerSign_Type = Integer32
_RuijieFiberChannel8TXpowerSign_Object = MibTableColumn
ruijieFiberChannel8TXpowerSign = _RuijieFiberChannel8TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 142),
    _RuijieFiberChannel8TXpowerSign_Type()
)
ruijieFiberChannel8TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8TXpowerSign.setStatus("current")
_RuijieFiberChannel5RXpower_Type = Integer32
_RuijieFiberChannel5RXpower_Object = MibTableColumn
ruijieFiberChannel5RXpower = _RuijieFiberChannel5RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 143),
    _RuijieFiberChannel5RXpower_Type()
)
ruijieFiberChannel5RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5RXpower.setStatus("current")
_RuijieFiberChannel6RXpower_Type = Integer32
_RuijieFiberChannel6RXpower_Object = MibTableColumn
ruijieFiberChannel6RXpower = _RuijieFiberChannel6RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 144),
    _RuijieFiberChannel6RXpower_Type()
)
ruijieFiberChannel6RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6RXpower.setStatus("current")
_RuijieFiberChannel7RXpower_Type = Integer32
_RuijieFiberChannel7RXpower_Object = MibTableColumn
ruijieFiberChannel7RXpower = _RuijieFiberChannel7RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 145),
    _RuijieFiberChannel7RXpower_Type()
)
ruijieFiberChannel7RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7RXpower.setStatus("current")
_RuijieFiberChannel8RXpower_Type = Integer32
_RuijieFiberChannel8RXpower_Object = MibTableColumn
ruijieFiberChannel8RXpower = _RuijieFiberChannel8RXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 146),
    _RuijieFiberChannel8RXpower_Type()
)
ruijieFiberChannel8RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8RXpower.setStatus("current")
_RuijieFiberChannel5TXpower_Type = Integer32
_RuijieFiberChannel5TXpower_Object = MibTableColumn
ruijieFiberChannel5TXpower = _RuijieFiberChannel5TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 147),
    _RuijieFiberChannel5TXpower_Type()
)
ruijieFiberChannel5TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel5TXpower.setStatus("current")
_RuijieFiberChannel6TXpower_Type = Integer32
_RuijieFiberChannel6TXpower_Object = MibTableColumn
ruijieFiberChannel6TXpower = _RuijieFiberChannel6TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 148),
    _RuijieFiberChannel6TXpower_Type()
)
ruijieFiberChannel6TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel6TXpower.setStatus("current")
_RuijieFiberChannel7TXpower_Type = Integer32
_RuijieFiberChannel7TXpower_Object = MibTableColumn
ruijieFiberChannel7TXpower = _RuijieFiberChannel7TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 149),
    _RuijieFiberChannel7TXpower_Type()
)
ruijieFiberChannel7TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel7TXpower.setStatus("current")
_RuijieFiberChannel8TXpower_Type = Integer32
_RuijieFiberChannel8TXpower_Object = MibTableColumn
ruijieFiberChannel8TXpower = _RuijieFiberChannel8TXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 150),
    _RuijieFiberChannel8TXpower_Type()
)
ruijieFiberChannel8TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannel8TXpower.setStatus("current")
_RuijieFiberTransferDistance50umOM5_Type = Integer32
_RuijieFiberTransferDistance50umOM5_Object = MibTableColumn
ruijieFiberTransferDistance50umOM5 = _RuijieFiberTransferDistance50umOM5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 151),
    _RuijieFiberTransferDistance50umOM5_Type()
)
ruijieFiberTransferDistance50umOM5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransferDistance50umOM5.setStatus("current")


class _RuijieFiberMode_Type(Integer32):
    """Custom type ruijieFiberMode based on Integer32"""
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
        *(("unknown", 0),
          ("copper", 1),
          ("singleMode", 2),
          ("multiMode", 3))
    )


_RuijieFiberMode_Type.__name__ = "Integer32"
_RuijieFiberMode_Object = MibTableColumn
ruijieFiberMode = _RuijieFiberMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 152),
    _RuijieFiberMode_Type()
)
ruijieFiberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberMode.setStatus("current")
_RuijieFiberTempLowWarnThreshold_Type = Integer32
_RuijieFiberTempLowWarnThreshold_Object = MibTableColumn
ruijieFiberTempLowWarnThreshold = _RuijieFiberTempLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 153),
    _RuijieFiberTempLowWarnThreshold_Type()
)
ruijieFiberTempLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTempLowWarnThreshold.setStatus("current")
_RuijieFiberTempHighWarnThreshold_Type = Integer32
_RuijieFiberTempHighWarnThreshold_Object = MibTableColumn
ruijieFiberTempHighWarnThreshold = _RuijieFiberTempHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 154),
    _RuijieFiberTempHighWarnThreshold_Type()
)
ruijieFiberTempHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTempHighWarnThreshold.setStatus("current")
_RuijieFiberTempLowAlarmThreshold_Type = Integer32
_RuijieFiberTempLowAlarmThreshold_Object = MibTableColumn
ruijieFiberTempLowAlarmThreshold = _RuijieFiberTempLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 155),
    _RuijieFiberTempLowAlarmThreshold_Type()
)
ruijieFiberTempLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTempLowAlarmThreshold.setStatus("current")
_RuijieFiberTempHighAlarmThreshold_Type = Integer32
_RuijieFiberTempHighAlarmThreshold_Object = MibTableColumn
ruijieFiberTempHighAlarmThreshold = _RuijieFiberTempHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 156),
    _RuijieFiberTempHighAlarmThreshold_Type()
)
ruijieFiberTempHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTempHighAlarmThreshold.setStatus("current")
_RuijieFiberVoltageLowWarnThreshold_Type = Integer32
_RuijieFiberVoltageLowWarnThreshold_Object = MibTableColumn
ruijieFiberVoltageLowWarnThreshold = _RuijieFiberVoltageLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 157),
    _RuijieFiberVoltageLowWarnThreshold_Type()
)
ruijieFiberVoltageLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVoltageLowWarnThreshold.setStatus("current")
_RuijieFiberVoltageHighWarnThreshold_Type = Integer32
_RuijieFiberVoltageHighWarnThreshold_Object = MibTableColumn
ruijieFiberVoltageHighWarnThreshold = _RuijieFiberVoltageHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 158),
    _RuijieFiberVoltageHighWarnThreshold_Type()
)
ruijieFiberVoltageHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVoltageHighWarnThreshold.setStatus("current")
_RuijieFiberVoltageLowAlarmThreshold_Type = Integer32
_RuijieFiberVoltageLowAlarmThreshold_Object = MibTableColumn
ruijieFiberVoltageLowAlarmThreshold = _RuijieFiberVoltageLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 159),
    _RuijieFiberVoltageLowAlarmThreshold_Type()
)
ruijieFiberVoltageLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVoltageLowAlarmThreshold.setStatus("current")
_RuijieFiberVoltageHighAlarmThreshold_Type = Integer32
_RuijieFiberVoltageHighAlarmThreshold_Object = MibTableColumn
ruijieFiberVoltageHighAlarmThreshold = _RuijieFiberVoltageHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 160),
    _RuijieFiberVoltageHighAlarmThreshold_Type()
)
ruijieFiberVoltageHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVoltageHighAlarmThreshold.setStatus("current")
_RuijieFiberBiasLowWarnThreshold_Type = Integer32
_RuijieFiberBiasLowWarnThreshold_Object = MibTableColumn
ruijieFiberBiasLowWarnThreshold = _RuijieFiberBiasLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 161),
    _RuijieFiberBiasLowWarnThreshold_Type()
)
ruijieFiberBiasLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBiasLowWarnThreshold.setStatus("current")
_RuijieFiberBiasHighWarnThreshold_Type = Integer32
_RuijieFiberBiasHighWarnThreshold_Object = MibTableColumn
ruijieFiberBiasHighWarnThreshold = _RuijieFiberBiasHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 162),
    _RuijieFiberBiasHighWarnThreshold_Type()
)
ruijieFiberBiasHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBiasHighWarnThreshold.setStatus("current")
_RuijieFiberBiasLowAlarmThreshold_Type = Integer32
_RuijieFiberBiasLowAlarmThreshold_Object = MibTableColumn
ruijieFiberBiasLowAlarmThreshold = _RuijieFiberBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 163),
    _RuijieFiberBiasLowAlarmThreshold_Type()
)
ruijieFiberBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBiasLowAlarmThreshold.setStatus("current")
_RuijieFiberBiasHighAlarmThreshold_Type = Integer32
_RuijieFiberBiasHighAlarmThreshold_Object = MibTableColumn
ruijieFiberBiasHighAlarmThreshold = _RuijieFiberBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 164),
    _RuijieFiberBiasHighAlarmThreshold_Type()
)
ruijieFiberBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberBiasHighAlarmThreshold.setStatus("current")


class _RuijieFiberTransceiverTypeStr_Type(DisplayString):
    """Custom type ruijieFiberTransceiverTypeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieFiberTransceiverTypeStr_Type.__name__ = "DisplayString"
_RuijieFiberTransceiverTypeStr_Object = MibTableColumn
ruijieFiberTransceiverTypeStr = _RuijieFiberTransceiverTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 165),
    _RuijieFiberTransceiverTypeStr_Type()
)
ruijieFiberTransceiverTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberTransceiverTypeStr.setStatus("current")


class _RuijieFiberConnectorTypeStr_Type(DisplayString):
    """Custom type ruijieFiberConnectorTypeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieFiberConnectorTypeStr_Type.__name__ = "DisplayString"
_RuijieFiberConnectorTypeStr_Object = MibTableColumn
ruijieFiberConnectorTypeStr = _RuijieFiberConnectorTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 1, 1, 166),
    _RuijieFiberConnectorTypeStr_Type()
)
ruijieFiberConnectorTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberConnectorTypeStr.setStatus("current")
_RuijieFiberVendorTable_Object = MibTable
ruijieFiberVendorTable = _RuijieFiberVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieFiberVendorTable.setStatus("current")
_RuijieFiberVendorEntry_Object = MibTableRow
ruijieFiberVendorEntry = _RuijieFiberVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1)
)
ruijieFiberVendorEntry.setIndexNames(
    (0, "RUIJIE-FIBER-MIB", "ruijieFiberVendorPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieFiberVendorEntry.setStatus("current")
_RuijieFiberVendorPortIndex_Type = IfIndex
_RuijieFiberVendorPortIndex_Object = MibTableColumn
ruijieFiberVendorPortIndex = _RuijieFiberVendorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 1),
    _RuijieFiberVendorPortIndex_Type()
)
ruijieFiberVendorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVendorPortIndex.setStatus("current")
_RuijieFiberVendorName_Type = DisplayString
_RuijieFiberVendorName_Object = MibTableColumn
ruijieFiberVendorName = _RuijieFiberVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 2),
    _RuijieFiberVendorName_Type()
)
ruijieFiberVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVendorName.setStatus("current")
_RuijieFiberVendorOUI_Type = DisplayString
_RuijieFiberVendorOUI_Object = MibTableColumn
ruijieFiberVendorOUI = _RuijieFiberVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 3),
    _RuijieFiberVendorOUI_Type()
)
ruijieFiberVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVendorOUI.setStatus("current")
_RuijieFiberVendorPartNumber_Type = DisplayString
_RuijieFiberVendorPartNumber_Object = MibTableColumn
ruijieFiberVendorPartNumber = _RuijieFiberVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 4),
    _RuijieFiberVendorPartNumber_Type()
)
ruijieFiberVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVendorPartNumber.setStatus("current")
_RuijieFiberVendorRev_Type = DisplayString
_RuijieFiberVendorRev_Object = MibTableColumn
ruijieFiberVendorRev = _RuijieFiberVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 5),
    _RuijieFiberVendorRev_Type()
)
ruijieFiberVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberVendorRev.setStatus("current")
_RuijieFiberManufacturingDate_Type = DisplayString
_RuijieFiberManufacturingDate_Object = MibTableColumn
ruijieFiberManufacturingDate = _RuijieFiberManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 6),
    _RuijieFiberManufacturingDate_Type()
)
ruijieFiberManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberManufacturingDate.setStatus("current")
_RuijieFiberEncoding_Type = DisplayString
_RuijieFiberEncoding_Object = MibTableColumn
ruijieFiberEncoding = _RuijieFiberEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 2, 1, 7),
    _RuijieFiberEncoding_Type()
)
ruijieFiberEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberEncoding.setStatus("current")
_RuijieFiberOMCTable_Object = MibTable
ruijieFiberOMCTable = _RuijieFiberOMCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieFiberOMCTable.setStatus("current")
_RuijieFiberOMCEntry_Object = MibTableRow
ruijieFiberOMCEntry = _RuijieFiberOMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1)
)
ruijieFiberOMCEntry.setIndexNames(
    (0, "RUIJIE-FIBER-MIB", "ruijieFiberOMCPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieFiberOMCEntry.setStatus("current")
_RuijieFiberOMCPortIndex_Type = IfIndex
_RuijieFiberOMCPortIndex_Object = MibTableColumn
ruijieFiberOMCPortIndex = _RuijieFiberOMCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1, 1),
    _RuijieFiberOMCPortIndex_Type()
)
ruijieFiberOMCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberOMCPortIndex.setStatus("current")


class _RuijieFiberOMCRxpower_Type(DisplayString):
    """Custom type ruijieFiberOMCRxpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFiberOMCRxpower_Type.__name__ = "DisplayString"
_RuijieFiberOMCRxpower_Object = MibTableColumn
ruijieFiberOMCRxpower = _RuijieFiberOMCRxpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1, 2),
    _RuijieFiberOMCRxpower_Type()
)
ruijieFiberOMCRxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberOMCRxpower.setStatus("current")
_RuijieFiberOMCTxpower_Type = DisplayString
_RuijieFiberOMCTxpower_Object = MibTableColumn
ruijieFiberOMCTxpower = _RuijieFiberOMCTxpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1, 3),
    _RuijieFiberOMCTxpower_Type()
)
ruijieFiberOMCTxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberOMCTxpower.setStatus("current")


class _RuijieFiberOMCWavelength_Type(DisplayString):
    """Custom type ruijieFiberOMCWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFiberOMCWavelength_Type.__name__ = "DisplayString"
_RuijieFiberOMCWavelength_Object = MibTableColumn
ruijieFiberOMCWavelength = _RuijieFiberOMCWavelength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1, 4),
    _RuijieFiberOMCWavelength_Type()
)
ruijieFiberOMCWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberOMCWavelength.setStatus("current")
_RuijieFiberOMCTranslength_Type = DisplayString
_RuijieFiberOMCTranslength_Object = MibTableColumn
ruijieFiberOMCTranslength = _RuijieFiberOMCTranslength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1, 5),
    _RuijieFiberOMCTranslength_Type()
)
ruijieFiberOMCTranslength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberOMCTranslength.setStatus("current")


class _RuijieFiberOMCPortType_Type(DisplayString):
    """Custom type ruijieFiberOMCPortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFiberOMCPortType_Type.__name__ = "DisplayString"
_RuijieFiberOMCPortType_Object = MibTableColumn
ruijieFiberOMCPortType = _RuijieFiberOMCPortType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 3, 1, 6),
    _RuijieFiberOMCPortType_Type()
)
ruijieFiberOMCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberOMCPortType.setStatus("current")
_RuijieFiberChannelTable_Object = MibTable
ruijieFiberChannelTable = _RuijieFiberChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieFiberChannelTable.setStatus("current")
_RuijieFiberChannelEntry_Object = MibTableRow
ruijieFiberChannelEntry = _RuijieFiberChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1)
)
ruijieFiberChannelEntry.setIndexNames(
    (0, "RUIJIE-FIBER-MIB", "ruijieFiberChannelPortIndex"),
    (0, "RUIJIE-FIBER-MIB", "ruijieFiberChannelIndex"),
)
if mibBuilder.loadTexts:
    ruijieFiberChannelEntry.setStatus("current")
_RuijieFiberChannelPortIndex_Type = IfIndex
_RuijieFiberChannelPortIndex_Object = MibTableColumn
ruijieFiberChannelPortIndex = _RuijieFiberChannelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 1),
    _RuijieFiberChannelPortIndex_Type()
)
ruijieFiberChannelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelPortIndex.setStatus("current")


class _RuijieFiberChannelIndex_Type(Integer32):
    """Custom type ruijieFiberChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieFiberChannelIndex_Type.__name__ = "Integer32"
_RuijieFiberChannelIndex_Object = MibTableColumn
ruijieFiberChannelIndex = _RuijieFiberChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 2),
    _RuijieFiberChannelIndex_Type()
)
ruijieFiberChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelIndex.setStatus("current")
_RuijieFiberChannelBias_Type = Integer32
_RuijieFiberChannelBias_Object = MibTableColumn
ruijieFiberChannelBias = _RuijieFiberChannelBias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 3),
    _RuijieFiberChannelBias_Type()
)
ruijieFiberChannelBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelBias.setStatus("current")
_RuijieFiberChannelBiasStatus_Type = Integer32
_RuijieFiberChannelBiasStatus_Object = MibTableColumn
ruijieFiberChannelBiasStatus = _RuijieFiberChannelBiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 4),
    _RuijieFiberChannelBiasStatus_Type()
)
ruijieFiberChannelBiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelBiasStatus.setStatus("current")
_RuijieFiberChannelRXpower_Type = Integer32
_RuijieFiberChannelRXpower_Object = MibTableColumn
ruijieFiberChannelRXpower = _RuijieFiberChannelRXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 5),
    _RuijieFiberChannelRXpower_Type()
)
ruijieFiberChannelRXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelRXpower.setStatus("current")
_RuijieFiberChannelRXpowertype_Type = Integer32
_RuijieFiberChannelRXpowertype_Object = MibTableColumn
ruijieFiberChannelRXpowertype = _RuijieFiberChannelRXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 6),
    _RuijieFiberChannelRXpowertype_Type()
)
ruijieFiberChannelRXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelRXpowertype.setStatus("current")
_RuijieFiberChannelRXpowerStatus_Type = Integer32
_RuijieFiberChannelRXpowerStatus_Object = MibTableColumn
ruijieFiberChannelRXpowerStatus = _RuijieFiberChannelRXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 7),
    _RuijieFiberChannelRXpowerStatus_Type()
)
ruijieFiberChannelRXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelRXpowerStatus.setStatus("current")
_RuijieFiberChannelTXpower_Type = Integer32
_RuijieFiberChannelTXpower_Object = MibTableColumn
ruijieFiberChannelTXpower = _RuijieFiberChannelTXpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 8),
    _RuijieFiberChannelTXpower_Type()
)
ruijieFiberChannelTXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelTXpower.setStatus("current")
_RuijieFiberChannelTXpowerStatus_Type = Integer32
_RuijieFiberChannelTXpowerStatus_Object = MibTableColumn
ruijieFiberChannelTXpowerStatus = _RuijieFiberChannelTXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 9),
    _RuijieFiberChannelTXpowerStatus_Type()
)
ruijieFiberChannelTXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelTXpowerStatus.setStatus("current")


class _RuijieFiberChannelAPR_Type(Integer32):
    """Custom type ruijieFiberChannelAPR based on Integer32"""
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
          ("off", 1),
          ("on", 2))
    )


_RuijieFiberChannelAPR_Type.__name__ = "Integer32"
_RuijieFiberChannelAPR_Object = MibTableColumn
ruijieFiberChannelAPR = _RuijieFiberChannelAPR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 1, 4, 1, 10),
    _RuijieFiberChannelAPR_Type()
)
ruijieFiberChannelAPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFiberChannelAPR.setStatus("current")
_RuijieFiberAntifakeMIBTraps_ObjectIdentity = ObjectIdentity
ruijieFiberAntifakeMIBTraps = _RuijieFiberAntifakeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 2)
)


class _RuijieFiberAntifakeIntfNameDesc_Type(DisplayString):
    """Custom type ruijieFiberAntifakeIntfNameDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFiberAntifakeIntfNameDesc_Type.__name__ = "DisplayString"
_RuijieFiberAntifakeIntfNameDesc_Object = MibScalar
ruijieFiberAntifakeIntfNameDesc = _RuijieFiberAntifakeIntfNameDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 2, 1),
    _RuijieFiberAntifakeIntfNameDesc_Type()
)
ruijieFiberAntifakeIntfNameDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieFiberAntifakeIntfNameDesc.setStatus("current")


class _RuijieFiberAntifakeSerialNumberDesc_Type(DisplayString):
    """Custom type ruijieFiberAntifakeSerialNumberDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFiberAntifakeSerialNumberDesc_Type.__name__ = "DisplayString"
_RuijieFiberAntifakeSerialNumberDesc_Object = MibScalar
ruijieFiberAntifakeSerialNumberDesc = _RuijieFiberAntifakeSerialNumberDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 2, 2),
    _RuijieFiberAntifakeSerialNumberDesc_Type()
)
ruijieFiberAntifakeSerialNumberDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieFiberAntifakeSerialNumberDesc.setStatus("current")
_RuijieFiberMIBConformance_ObjectIdentity = ObjectIdentity
ruijieFiberMIBConformance = _RuijieFiberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3)
)
_RuijieFiberMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieFiberMIBCompliances = _RuijieFiberMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3, 1)
)
_RuijieFiberMIBGroups_ObjectIdentity = ObjectIdentity
ruijieFiberMIBGroups = _RuijieFiberMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3, 2)
)
_RuijieFiberEventMIBTraps_ObjectIdentity = ObjectIdentity
ruijieFiberEventMIBTraps = _RuijieFiberEventMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4)
)


class _RuijieFiberEventReason_Type(Integer32):
    """Custom type ruijieFiberEventReason based on Integer32"""
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
              61)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fiberInvalidTxHigh", 2),
          ("fiberInvalidTxLow", 3),
          ("fiberInvalidRxHigh", 4),
          ("fiberInvalidRxLow", 5),
          ("fiberInvalidI2CFail", 6),
          ("fiberInvalidNotSupp", 7),
          ("fiberInvalidTemperatureLow", 8),
          ("fiberInvalidTemperatureHigh", 9),
          ("fiberInvalidVoltageLow", 10),
          ("fiberInvalidVoltageHigh", 11),
          ("fiberInvalidTXBiasLow", 12),
          ("fiberInvalidTXBiasHigh", 13),
          ("fiberInvalidRXLossSignal", 14),
          ("fiberInvalidRXCDRLossLock", 15),
          ("fiberInvalidTXLossSignal", 16),
          ("fiberInvalidTXCDRLossLock", 17),
          ("fiberInvalidTXFault", 18),
          ("fiberInvalidCheckSumError", 19),
          ("fiberInvalidModuleNotReady", 20),
          ("fiberInvalidRXNotReady", 21),
          ("fiberInvalidTxHighWarn", 22),
          ("fiberInvalidTxLowWarn", 23),
          ("fiberInvalidRxHighWarn", 24),
          ("fiberInvalidRxLowWarn", 25),
          ("fiberInvalidTemperatureLowWarn", 26),
          ("fiberInvalidTemperatureHighWarn", 27),
          ("fiberInvalidVoltageLowWarn", 28),
          ("fiberInvalidVoltageHighWarn", 29),
          ("fiberInvalidTXBiasLowWarn", 30),
          ("fiberInvalidTXBiasHighWarn", 31),
          ("fiberInvalidRXTotalPowerLowAlarm", 32),
          ("fiberInvalidRXMediaPreFECBERHighAlarm", 33),
          ("fiberInvalidColorGrayFiberAlarm", 34),
          ("fiberInvalidRXTotalPowerLowWarn", 35),
          ("fiberInvalidRXMediaPreFECBERHighWarn", 36),
          ("fiberInvalidTXERHighAlarm", 37),
          ("fiberInvalidTXERLowAlarm", 38),
          ("fiberInvalidRXERHighAlarm", 39),
          ("fiberInvalidRXERLowAlarm", 40),
          ("fiberInvalidTXERHighRelativeWarn", 41),
          ("fiberInvalidTXERLowRelativeWarn", 42),
          ("fiberInvalidRXERHighRelativeWarn", 43),
          ("fiberInvalidRXERLowRelativeWarn", 44),
          ("fiberInvalidAbnormalLuminescence", 45),
          ("fiberInvalidInbandLinkDisconnect", 46),
          ("fiberInvalidPLLLossLock", 47),
          ("fiberInvalidMCUTemperatureLowAlarm", 48),
          ("fiberInvalidMCUTemperatureHighAlarm", 49),
          ("fiberInvalidMCUTemperatureLowWarn", 50),
          ("fiberInvalidMCUTemperatureHighWarn", 51),
          ("fiberInvalidResetByColdBoot", 52),
          ("fiberInvalidResetByHotBoot", 53),
          ("fiberInvalidResetByReinsert", 54),
          ("fiberInvalidResetByError", 55),
          ("fiberInvalidResetByCLI", 56),
          ("fiberInvalidUPCFault", 57),
          ("fiberInvalidPortNotReady", 58),
          ("fiberInvalidPeerOff", 59),
          ("fiberInvalidBFFailure", 60),
          ("fiberInvalidTFFailure", 61))
    )


_RuijieFiberEventReason_Type.__name__ = "Integer32"
_RuijieFiberEventReason_Object = MibScalar
ruijieFiberEventReason = _RuijieFiberEventReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 1),
    _RuijieFiberEventReason_Type()
)
ruijieFiberEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieFiberEventReason.setStatus("current")


class _RuijieFiberEventDesc_Type(DisplayString):
    """Custom type ruijieFiberEventDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFiberEventDesc_Type.__name__ = "DisplayString"
_RuijieFiberEventDesc_Object = MibScalar
ruijieFiberEventDesc = _RuijieFiberEventDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 2),
    _RuijieFiberEventDesc_Type()
)
ruijieFiberEventDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieFiberEventDesc.setStatus("current")
_RuijieFiberAlarmValue_Type = Integer32
_RuijieFiberAlarmValue_Object = MibScalar
ruijieFiberAlarmValue = _RuijieFiberAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 7),
    _RuijieFiberAlarmValue_Type()
)
ruijieFiberAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieFiberAlarmValue.setStatus("current")
_RuijieFiberAlarmThresholdValue_Type = Integer32
_RuijieFiberAlarmThresholdValue_Object = MibScalar
ruijieFiberAlarmThresholdValue = _RuijieFiberAlarmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 8),
    _RuijieFiberAlarmThresholdValue_Type()
)
ruijieFiberAlarmThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieFiberAlarmThresholdValue.setStatus("current")

# Managed Objects groups

ruijieFiberMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3, 2, 1)
)
ruijieFiberMIBGroup.setObjects(
      *(("RUIJIE-FIBER-MIB", "ruijieFiberPortDescr"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransceiverType"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberConnectorType"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberWavelength"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistanceSMF"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance62point5umOM1"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance62point5um"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance50umOM2"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance50um"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance50umOM3"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistanceEBW50um"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistanceCopper"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistanceCableAssembly"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberDDMSupportStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberSerialNumber"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTemp"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTempStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberVoltage"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberVoltageStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel1TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel2TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel3TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel4TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberWavelengthExact"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance50umOM4"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistanceSMFExt"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBandWidth"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberFormFactor"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerLowWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerHighWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerLowAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberRXpowerHighAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerLowWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerHighWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerLowAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTXpowerHighAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8Bias"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8BiasStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8RXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8RXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8RXpowertype"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8RXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8TXpowerIntegerpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8TXpowerDecimalpart"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8TXpowerStatus"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8RXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8TXpowerSign"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8RXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel5TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel6TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel7TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberChannel8TXpower"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransferDistance50umOM5"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberMode"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTempLowWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTempHighWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTempLowAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTempHighAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberVoltageLowWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberVoltageHighWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberVoltageLowAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberVoltageHighAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBiasLowWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBiasHighWarnThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBiasLowAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberBiasHighAlarmThreshold"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberTransceiverTypeStr"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberConnectorTypeStr"))
)
if mibBuilder.loadTexts:
    ruijieFiberMIBGroup.setStatus("current")

ruijieFiberAntifakeIntfNameDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3, 2, 2)
)
ruijieFiberAntifakeIntfNameDescGroup.setObjects(
    ("RUIJIE-FIBER-MIB", "ruijieFiberAntifakeIntfNameDesc")
)
if mibBuilder.loadTexts:
    ruijieFiberAntifakeIntfNameDescGroup.setStatus("current")

ruijieFiberAntifakeSerialNumberDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3, 2, 3)
)
ruijieFiberAntifakeSerialNumberDescGroup.setObjects(
    ("RUIJIE-FIBER-MIB", "ruijieFiberAntifakeSerialNumberDesc")
)
if mibBuilder.loadTexts:
    ruijieFiberAntifakeSerialNumberDescGroup.setStatus("current")


# Notification objects

ruijieFiberAntifakeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 2, 3)
)
ruijieFiberAntifakeTrap.setObjects(
      *(("RUIJIE-FIBER-MIB", "ruijieFiberAntifakeIntfNameDesc"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAntifakeSerialNumberDesc"))
)
if mibBuilder.loadTexts:
    ruijieFiberAntifakeTrap.setStatus(
        "current"
    )

ruijieFiberRemoveEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 3)
)
ruijieFiberRemoveEventTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ruijieFiberRemoveEventTrap.setStatus(
        "current"
    )

ruijieFiberInsertEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 4)
)
ruijieFiberInsertEventTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ruijieFiberInsertEventTrap.setStatus(
        "current"
    )

ruijieFiberInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 5)
)
ruijieFiberInvalidTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberEventReason"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberEventDesc"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAlarmValue"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAlarmThresholdValue"))
)
if mibBuilder.loadTexts:
    ruijieFiberInvalidTrap.setStatus(
        "current"
    )

ruijieFiberInvalidResumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 6)
)
ruijieFiberInvalidResumeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberEventReason"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberEventDesc"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAlarmValue"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAlarmThresholdValue"))
)
if mibBuilder.loadTexts:
    ruijieFiberInvalidResumeTrap.setStatus(
        "current"
    )

ruijieFiberSpeedMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 9)
)
ruijieFiberSpeedMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ruijieFiberSpeedMismatch.setStatus(
        "current"
    )

ruijieFiberUnCertified = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 10)
)
ruijieFiberUnCertified.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ruijieFiberUnCertified.setStatus(
        "current"
    )

ruijieFiberUnCertifiedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 4, 11)
)
ruijieFiberUnCertifiedClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ruijieFiberUnCertifiedClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieFiberMIBConpliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 105, 3, 1, 1)
)
ruijieFiberMIBConpliance.setObjects(
      *(("RUIJIE-FIBER-MIB", "ruijieFiberMIBGroup"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAntifakeIntfNameDescGroup"),
        ("RUIJIE-FIBER-MIB", "ruijieFiberAntifakeSerialNumberDescGroup"))
)
if mibBuilder.loadTexts:
    ruijieFiberMIBConpliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-FIBER-MIB",
    **{"ruijieFiberMIB": ruijieFiberMIB,
       "ruijieFiberMIBObjects": ruijieFiberMIBObjects,
       "ruijieFiberTable": ruijieFiberTable,
       "ruijieFiberEntry": ruijieFiberEntry,
       "ruijieFiberPortIndex": ruijieFiberPortIndex,
       "ruijieFiberPortDescr": ruijieFiberPortDescr,
       "ruijieFiberTransceiverType": ruijieFiberTransceiverType,
       "ruijieFiberConnectorType": ruijieFiberConnectorType,
       "ruijieFiberWavelength": ruijieFiberWavelength,
       "ruijieFiberTransferDistanceSMF": ruijieFiberTransferDistanceSMF,
       "ruijieFiberTransferDistance62point5umOM1": ruijieFiberTransferDistance62point5umOM1,
       "ruijieFiberTransferDistance62point5um": ruijieFiberTransferDistance62point5um,
       "ruijieFiberTransferDistance50umOM2": ruijieFiberTransferDistance50umOM2,
       "ruijieFiberTransferDistance50um": ruijieFiberTransferDistance50um,
       "ruijieFiberTransferDistance50umOM3": ruijieFiberTransferDistance50umOM3,
       "ruijieFiberTransferDistanceEBW50um": ruijieFiberTransferDistanceEBW50um,
       "ruijieFiberTransferDistanceCopper": ruijieFiberTransferDistanceCopper,
       "ruijieFiberTransferDistanceCableAssembly": ruijieFiberTransferDistanceCableAssembly,
       "ruijieFiberDDMSupportStatus": ruijieFiberDDMSupportStatus,
       "ruijieFiberSerialNumber": ruijieFiberSerialNumber,
       "ruijieFiberTemp": ruijieFiberTemp,
       "ruijieFiberTempStatus": ruijieFiberTempStatus,
       "ruijieFiberVoltage": ruijieFiberVoltage,
       "ruijieFiberVoltageStatus": ruijieFiberVoltageStatus,
       "ruijieFiberBias": ruijieFiberBias,
       "ruijieFiberBiasStatus": ruijieFiberBiasStatus,
       "ruijieFiberChannel1Bias": ruijieFiberChannel1Bias,
       "ruijieFiberChannel1BiasStatus": ruijieFiberChannel1BiasStatus,
       "ruijieFiberChannel2Bias": ruijieFiberChannel2Bias,
       "ruijieFiberChannel2BiasStatus": ruijieFiberChannel2BiasStatus,
       "ruijieFiberChannel3Bias": ruijieFiberChannel3Bias,
       "ruijieFiberChannel3BiasStatus": ruijieFiberChannel3BiasStatus,
       "ruijieFiberChannel4Bias": ruijieFiberChannel4Bias,
       "ruijieFiberChannel4BiasStatus": ruijieFiberChannel4BiasStatus,
       "ruijieFiberRXpowerIntegerpart": ruijieFiberRXpowerIntegerpart,
       "ruijieFiberRXpowerDecimalpart": ruijieFiberRXpowerDecimalpart,
       "ruijieFiberRXpowertype": ruijieFiberRXpowertype,
       "ruijieFiberRXpowerStatus": ruijieFiberRXpowerStatus,
       "ruijieFiberChannel1RXpowerIntegerpart": ruijieFiberChannel1RXpowerIntegerpart,
       "ruijieFiberChannel1RXpowerDecimalpart": ruijieFiberChannel1RXpowerDecimalpart,
       "ruijieFiberChannel1RXpowertype": ruijieFiberChannel1RXpowertype,
       "ruijieFiberChannel1RXpowerStatus": ruijieFiberChannel1RXpowerStatus,
       "ruijieFiberChannel2RXpowerIntegerpart": ruijieFiberChannel2RXpowerIntegerpart,
       "ruijieFiberChannel2RXpowerDecimalpart": ruijieFiberChannel2RXpowerDecimalpart,
       "ruijieFiberChannel2RXpowertype": ruijieFiberChannel2RXpowertype,
       "ruijieFiberChannel2RXpowerStatus": ruijieFiberChannel2RXpowerStatus,
       "ruijieFiberChannel3RXpowerIntegerpart": ruijieFiberChannel3RXpowerIntegerpart,
       "ruijieFiberChannel3RXpowerDecimalpart": ruijieFiberChannel3RXpowerDecimalpart,
       "ruijieFiberChannel3RXpowertype": ruijieFiberChannel3RXpowertype,
       "ruijieFiberChannel3RXpowerStatus": ruijieFiberChannel3RXpowerStatus,
       "ruijieFiberChannel4RXpowerIntegerpart": ruijieFiberChannel4RXpowerIntegerpart,
       "ruijieFiberChannel4RXpowerDecimalpart": ruijieFiberChannel4RXpowerDecimalpart,
       "ruijieFiberChannel4RXpowertype": ruijieFiberChannel4RXpowertype,
       "ruijieFiberChannel4RXpowerStatus": ruijieFiberChannel4RXpowerStatus,
       "ruijieFiberTXpowerIntegerpart": ruijieFiberTXpowerIntegerpart,
       "ruijieFiberTXpowerDecimalpart": ruijieFiberTXpowerDecimalpart,
       "ruijieFiberTXpowerStatus": ruijieFiberTXpowerStatus,
       "ruijieFiberChannel1TXpowerIntegerpart": ruijieFiberChannel1TXpowerIntegerpart,
       "ruijieFiberChannel1TXpowerDecimalpart": ruijieFiberChannel1TXpowerDecimalpart,
       "ruijieFiberChannel1TXpowerStatus": ruijieFiberChannel1TXpowerStatus,
       "ruijieFiberChannel2TXpowerIntegerpart": ruijieFiberChannel2TXpowerIntegerpart,
       "ruijieFiberChannel2TXpowerDecimalpart": ruijieFiberChannel2TXpowerDecimalpart,
       "ruijieFiberChannel2TXpowerStatus": ruijieFiberChannel2TXpowerStatus,
       "ruijieFiberChannel3TXpowerIntegerpart": ruijieFiberChannel3TXpowerIntegerpart,
       "ruijieFiberChannel3TXpowerDecimalpart": ruijieFiberChannel3TXpowerDecimalpart,
       "ruijieFiberChannel3TXpowerStatus": ruijieFiberChannel3TXpowerStatus,
       "ruijieFiberChannel4TXpowerIntegerpart": ruijieFiberChannel4TXpowerIntegerpart,
       "ruijieFiberChannel4TXpowerDecimalpart": ruijieFiberChannel4TXpowerDecimalpart,
       "ruijieFiberChannel4TXpowerStatus": ruijieFiberChannel4TXpowerStatus,
       "ruijieFiberRXpowerSign": ruijieFiberRXpowerSign,
       "ruijieFiberChannel1RXpowerSign": ruijieFiberChannel1RXpowerSign,
       "ruijieFiberChannel2RXpowerSign": ruijieFiberChannel2RXpowerSign,
       "ruijieFiberChannel3RXpowerSign": ruijieFiberChannel3RXpowerSign,
       "ruijieFiberChannel4RXpowerSign": ruijieFiberChannel4RXpowerSign,
       "ruijieFiberTXpowerSign": ruijieFiberTXpowerSign,
       "ruijieFiberChannel1TXpowerSign": ruijieFiberChannel1TXpowerSign,
       "ruijieFiberChannel2TXpowerSign": ruijieFiberChannel2TXpowerSign,
       "ruijieFiberChannel3TXpowerSign": ruijieFiberChannel3TXpowerSign,
       "ruijieFiberChannel4TXpowerSign": ruijieFiberChannel4TXpowerSign,
       "ruijieFiberRXpower": ruijieFiberRXpower,
       "ruijieFiberChannel1RXpower": ruijieFiberChannel1RXpower,
       "ruijieFiberChannel2RXpower": ruijieFiberChannel2RXpower,
       "ruijieFiberChannel3RXpower": ruijieFiberChannel3RXpower,
       "ruijieFiberChannel4RXpower": ruijieFiberChannel4RXpower,
       "ruijieFiberTXpower": ruijieFiberTXpower,
       "ruijieFiberChannel1TXpower": ruijieFiberChannel1TXpower,
       "ruijieFiberChannel2TXpower": ruijieFiberChannel2TXpower,
       "ruijieFiberChannel3TXpower": ruijieFiberChannel3TXpower,
       "ruijieFiberChannel4TXpower": ruijieFiberChannel4TXpower,
       "ruijieFiberWavelengthExact": ruijieFiberWavelengthExact,
       "ruijieFiberTransferDistance50umOM4": ruijieFiberTransferDistance50umOM4,
       "ruijieFiberTransferDistanceSMFExt": ruijieFiberTransferDistanceSMFExt,
       "ruijieFiberBandWidth": ruijieFiberBandWidth,
       "ruijieFiberFormFactor": ruijieFiberFormFactor,
       "ruijieFiberRXpowerLowWarnThreshold": ruijieFiberRXpowerLowWarnThreshold,
       "ruijieFiberRXpowerHighWarnThreshold": ruijieFiberRXpowerHighWarnThreshold,
       "ruijieFiberRXpowerLowAlarmThreshold": ruijieFiberRXpowerLowAlarmThreshold,
       "ruijieFiberRXpowerHighAlarmThreshold": ruijieFiberRXpowerHighAlarmThreshold,
       "ruijieFiberTXpowerLowWarnThreshold": ruijieFiberTXpowerLowWarnThreshold,
       "ruijieFiberTXpowerHighWarnThreshold": ruijieFiberTXpowerHighWarnThreshold,
       "ruijieFiberTXpowerLowAlarmThreshold": ruijieFiberTXpowerLowAlarmThreshold,
       "ruijieFiberTXpowerHighAlarmThreshold": ruijieFiberTXpowerHighAlarmThreshold,
       "ruijieFiberChannel5Bias": ruijieFiberChannel5Bias,
       "ruijieFiberChannel5BiasStatus": ruijieFiberChannel5BiasStatus,
       "ruijieFiberChannel6Bias": ruijieFiberChannel6Bias,
       "ruijieFiberChannel6BiasStatus": ruijieFiberChannel6BiasStatus,
       "ruijieFiberChannel7Bias": ruijieFiberChannel7Bias,
       "ruijieFiberChannel7BiasStatus": ruijieFiberChannel7BiasStatus,
       "ruijieFiberChannel8Bias": ruijieFiberChannel8Bias,
       "ruijieFiberChannel8BiasStatus": ruijieFiberChannel8BiasStatus,
       "ruijieFiberChannel5RXpowerIntegerpart": ruijieFiberChannel5RXpowerIntegerpart,
       "ruijieFiberChannel5RXpowerDecimalpart": ruijieFiberChannel5RXpowerDecimalpart,
       "ruijieFiberChannel5RXpowertype": ruijieFiberChannel5RXpowertype,
       "ruijieFiberChannel5RXpowerStatus": ruijieFiberChannel5RXpowerStatus,
       "ruijieFiberChannel6RXpowerIntegerpart": ruijieFiberChannel6RXpowerIntegerpart,
       "ruijieFiberChannel6RXpowerDecimalpart": ruijieFiberChannel6RXpowerDecimalpart,
       "ruijieFiberChannel6RXpowertype": ruijieFiberChannel6RXpowertype,
       "ruijieFiberChannel6RXpowerStatus": ruijieFiberChannel6RXpowerStatus,
       "ruijieFiberChannel7RXpowerIntegerpart": ruijieFiberChannel7RXpowerIntegerpart,
       "ruijieFiberChannel7RXpowerDecimalpart": ruijieFiberChannel7RXpowerDecimalpart,
       "ruijieFiberChannel7RXpowertype": ruijieFiberChannel7RXpowertype,
       "ruijieFiberChannel7RXpowerStatus": ruijieFiberChannel7RXpowerStatus,
       "ruijieFiberChannel8RXpowerIntegerpart": ruijieFiberChannel8RXpowerIntegerpart,
       "ruijieFiberChannel8RXpowerDecimalpart": ruijieFiberChannel8RXpowerDecimalpart,
       "ruijieFiberChannel8RXpowertype": ruijieFiberChannel8RXpowertype,
       "ruijieFiberChannel8RXpowerStatus": ruijieFiberChannel8RXpowerStatus,
       "ruijieFiberChannel5TXpowerIntegerpart": ruijieFiberChannel5TXpowerIntegerpart,
       "ruijieFiberChannel5TXpowerDecimalpart": ruijieFiberChannel5TXpowerDecimalpart,
       "ruijieFiberChannel5TXpowerStatus": ruijieFiberChannel5TXpowerStatus,
       "ruijieFiberChannel6TXpowerIntegerpart": ruijieFiberChannel6TXpowerIntegerpart,
       "ruijieFiberChannel6TXpowerDecimalpart": ruijieFiberChannel6TXpowerDecimalpart,
       "ruijieFiberChannel6TXpowerStatus": ruijieFiberChannel6TXpowerStatus,
       "ruijieFiberChannel7TXpowerIntegerpart": ruijieFiberChannel7TXpowerIntegerpart,
       "ruijieFiberChannel7TXpowerDecimalpart": ruijieFiberChannel7TXpowerDecimalpart,
       "ruijieFiberChannel7TXpowerStatus": ruijieFiberChannel7TXpowerStatus,
       "ruijieFiberChannel8TXpowerIntegerpart": ruijieFiberChannel8TXpowerIntegerpart,
       "ruijieFiberChannel8TXpowerDecimalpart": ruijieFiberChannel8TXpowerDecimalpart,
       "ruijieFiberChannel8TXpowerStatus": ruijieFiberChannel8TXpowerStatus,
       "ruijieFiberChannel5RXpowerSign": ruijieFiberChannel5RXpowerSign,
       "ruijieFiberChannel6RXpowerSign": ruijieFiberChannel6RXpowerSign,
       "ruijieFiberChannel7RXpowerSign": ruijieFiberChannel7RXpowerSign,
       "ruijieFiberChannel8RXpowerSign": ruijieFiberChannel8RXpowerSign,
       "ruijieFiberChannel5TXpowerSign": ruijieFiberChannel5TXpowerSign,
       "ruijieFiberChannel6TXpowerSign": ruijieFiberChannel6TXpowerSign,
       "ruijieFiberChannel7TXpowerSign": ruijieFiberChannel7TXpowerSign,
       "ruijieFiberChannel8TXpowerSign": ruijieFiberChannel8TXpowerSign,
       "ruijieFiberChannel5RXpower": ruijieFiberChannel5RXpower,
       "ruijieFiberChannel6RXpower": ruijieFiberChannel6RXpower,
       "ruijieFiberChannel7RXpower": ruijieFiberChannel7RXpower,
       "ruijieFiberChannel8RXpower": ruijieFiberChannel8RXpower,
       "ruijieFiberChannel5TXpower": ruijieFiberChannel5TXpower,
       "ruijieFiberChannel6TXpower": ruijieFiberChannel6TXpower,
       "ruijieFiberChannel7TXpower": ruijieFiberChannel7TXpower,
       "ruijieFiberChannel8TXpower": ruijieFiberChannel8TXpower,
       "ruijieFiberTransferDistance50umOM5": ruijieFiberTransferDistance50umOM5,
       "ruijieFiberMode": ruijieFiberMode,
       "ruijieFiberTempLowWarnThreshold": ruijieFiberTempLowWarnThreshold,
       "ruijieFiberTempHighWarnThreshold": ruijieFiberTempHighWarnThreshold,
       "ruijieFiberTempLowAlarmThreshold": ruijieFiberTempLowAlarmThreshold,
       "ruijieFiberTempHighAlarmThreshold": ruijieFiberTempHighAlarmThreshold,
       "ruijieFiberVoltageLowWarnThreshold": ruijieFiberVoltageLowWarnThreshold,
       "ruijieFiberVoltageHighWarnThreshold": ruijieFiberVoltageHighWarnThreshold,
       "ruijieFiberVoltageLowAlarmThreshold": ruijieFiberVoltageLowAlarmThreshold,
       "ruijieFiberVoltageHighAlarmThreshold": ruijieFiberVoltageHighAlarmThreshold,
       "ruijieFiberBiasLowWarnThreshold": ruijieFiberBiasLowWarnThreshold,
       "ruijieFiberBiasHighWarnThreshold": ruijieFiberBiasHighWarnThreshold,
       "ruijieFiberBiasLowAlarmThreshold": ruijieFiberBiasLowAlarmThreshold,
       "ruijieFiberBiasHighAlarmThreshold": ruijieFiberBiasHighAlarmThreshold,
       "ruijieFiberTransceiverTypeStr": ruijieFiberTransceiverTypeStr,
       "ruijieFiberConnectorTypeStr": ruijieFiberConnectorTypeStr,
       "ruijieFiberVendorTable": ruijieFiberVendorTable,
       "ruijieFiberVendorEntry": ruijieFiberVendorEntry,
       "ruijieFiberVendorPortIndex": ruijieFiberVendorPortIndex,
       "ruijieFiberVendorName": ruijieFiberVendorName,
       "ruijieFiberVendorOUI": ruijieFiberVendorOUI,
       "ruijieFiberVendorPartNumber": ruijieFiberVendorPartNumber,
       "ruijieFiberVendorRev": ruijieFiberVendorRev,
       "ruijieFiberManufacturingDate": ruijieFiberManufacturingDate,
       "ruijieFiberEncoding": ruijieFiberEncoding,
       "ruijieFiberOMCTable": ruijieFiberOMCTable,
       "ruijieFiberOMCEntry": ruijieFiberOMCEntry,
       "ruijieFiberOMCPortIndex": ruijieFiberOMCPortIndex,
       "ruijieFiberOMCRxpower": ruijieFiberOMCRxpower,
       "ruijieFiberOMCTxpower": ruijieFiberOMCTxpower,
       "ruijieFiberOMCWavelength": ruijieFiberOMCWavelength,
       "ruijieFiberOMCTranslength": ruijieFiberOMCTranslength,
       "ruijieFiberOMCPortType": ruijieFiberOMCPortType,
       "ruijieFiberChannelTable": ruijieFiberChannelTable,
       "ruijieFiberChannelEntry": ruijieFiberChannelEntry,
       "ruijieFiberChannelPortIndex": ruijieFiberChannelPortIndex,
       "ruijieFiberChannelIndex": ruijieFiberChannelIndex,
       "ruijieFiberChannelBias": ruijieFiberChannelBias,
       "ruijieFiberChannelBiasStatus": ruijieFiberChannelBiasStatus,
       "ruijieFiberChannelRXpower": ruijieFiberChannelRXpower,
       "ruijieFiberChannelRXpowertype": ruijieFiberChannelRXpowertype,
       "ruijieFiberChannelRXpowerStatus": ruijieFiberChannelRXpowerStatus,
       "ruijieFiberChannelTXpower": ruijieFiberChannelTXpower,
       "ruijieFiberChannelTXpowerStatus": ruijieFiberChannelTXpowerStatus,
       "ruijieFiberChannelAPR": ruijieFiberChannelAPR,
       "ruijieFiberAntifakeMIBTraps": ruijieFiberAntifakeMIBTraps,
       "ruijieFiberAntifakeIntfNameDesc": ruijieFiberAntifakeIntfNameDesc,
       "ruijieFiberAntifakeSerialNumberDesc": ruijieFiberAntifakeSerialNumberDesc,
       "ruijieFiberAntifakeTrap": ruijieFiberAntifakeTrap,
       "ruijieFiberMIBConformance": ruijieFiberMIBConformance,
       "ruijieFiberMIBCompliances": ruijieFiberMIBCompliances,
       "ruijieFiberMIBConpliance": ruijieFiberMIBConpliance,
       "ruijieFiberMIBGroups": ruijieFiberMIBGroups,
       "ruijieFiberMIBGroup": ruijieFiberMIBGroup,
       "ruijieFiberAntifakeIntfNameDescGroup": ruijieFiberAntifakeIntfNameDescGroup,
       "ruijieFiberAntifakeSerialNumberDescGroup": ruijieFiberAntifakeSerialNumberDescGroup,
       "ruijieFiberEventMIBTraps": ruijieFiberEventMIBTraps,
       "ruijieFiberEventReason": ruijieFiberEventReason,
       "ruijieFiberEventDesc": ruijieFiberEventDesc,
       "ruijieFiberRemoveEventTrap": ruijieFiberRemoveEventTrap,
       "ruijieFiberInsertEventTrap": ruijieFiberInsertEventTrap,
       "ruijieFiberInvalidTrap": ruijieFiberInvalidTrap,
       "ruijieFiberInvalidResumeTrap": ruijieFiberInvalidResumeTrap,
       "ruijieFiberAlarmValue": ruijieFiberAlarmValue,
       "ruijieFiberAlarmThresholdValue": ruijieFiberAlarmThresholdValue,
       "ruijieFiberSpeedMismatch": ruijieFiberSpeedMismatch,
       "ruijieFiberUnCertified": ruijieFiberUnCertified,
       "ruijieFiberUnCertifiedClear": ruijieFiberUnCertifiedClear}
)
