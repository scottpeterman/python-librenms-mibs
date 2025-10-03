# SNMP MIB module (FS-FIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\FS-FIBER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:48 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

fsFiberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105)
)
if mibBuilder.loadTexts:
    fsFiberMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsFiberMIBObjects_ObjectIdentity = ObjectIdentity
fsFiberMIBObjects = _FsFiberMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1)
)
_FsFiberTable_Object = MibTable
fsFiberTable = _FsFiberTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1)
)
if mibBuilder.loadTexts:
    fsFiberTable.setStatus("current")
_FsFiberEntry_Object = MibTableRow
fsFiberEntry = _FsFiberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1)
)
fsFiberEntry.setIndexNames(
    (0, "FS-FIBER-MIB", "fsFiberPortIndex"),
)
if mibBuilder.loadTexts:
    fsFiberEntry.setStatus("current")
_FsFiberPortIndex_Type = IfIndex
_FsFiberPortIndex_Object = MibTableColumn
fsFiberPortIndex = _FsFiberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 1),
    _FsFiberPortIndex_Type()
)
fsFiberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberPortIndex.setStatus("current")


class _FsFiberPortDescr_Type(DisplayString):
    """Custom type fsFiberPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsFiberPortDescr_Type.__name__ = "DisplayString"
_FsFiberPortDescr_Object = MibTableColumn
fsFiberPortDescr = _FsFiberPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 2),
    _FsFiberPortDescr_Type()
)
fsFiberPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberPortDescr.setStatus("current")


class _FsFiberTransceiverType_Type(Integer32):
    """Custom type fsFiberTransceiverType based on Integer32"""
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
              105)
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
          ("fiber10GBASETXFP", 103),
          ("fiber400GZRPlusQSFPDD", 104),
          ("fiber400GLR4QSFPDD", 105))
    )


_FsFiberTransceiverType_Type.__name__ = "Integer32"
_FsFiberTransceiverType_Object = MibTableColumn
fsFiberTransceiverType = _FsFiberTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 3),
    _FsFiberTransceiverType_Type()
)
fsFiberTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransceiverType.setStatus("current")


class _FsFiberConnectorType_Type(Integer32):
    """Custom type fsFiberConnectorType based on Integer32"""
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
              19)
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
          ("mxc", 19))
    )


_FsFiberConnectorType_Type.__name__ = "Integer32"
_FsFiberConnectorType_Object = MibTableColumn
fsFiberConnectorType = _FsFiberConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 4),
    _FsFiberConnectorType_Type()
)
fsFiberConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberConnectorType.setStatus("current")
_FsFiberWavelength_Type = Integer32
_FsFiberWavelength_Object = MibTableColumn
fsFiberWavelength = _FsFiberWavelength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 5),
    _FsFiberWavelength_Type()
)
fsFiberWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberWavelength.setStatus("current")
_FsFiberTransferDistanceSMF_Type = Integer32
_FsFiberTransferDistanceSMF_Object = MibTableColumn
fsFiberTransferDistanceSMF = _FsFiberTransferDistanceSMF_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 6),
    _FsFiberTransferDistanceSMF_Type()
)
fsFiberTransferDistanceSMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceSMF.setStatus("current")
_FsFiberTransferDistance62point5umOM1_Type = Integer32
_FsFiberTransferDistance62point5umOM1_Object = MibTableColumn
fsFiberTransferDistance62point5umOM1 = _FsFiberTransferDistance62point5umOM1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 7),
    _FsFiberTransferDistance62point5umOM1_Type()
)
fsFiberTransferDistance62point5umOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance62point5umOM1.setStatus("current")
_FsFiberTransferDistance62point5um_Type = Integer32
_FsFiberTransferDistance62point5um_Object = MibTableColumn
fsFiberTransferDistance62point5um = _FsFiberTransferDistance62point5um_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 8),
    _FsFiberTransferDistance62point5um_Type()
)
fsFiberTransferDistance62point5um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance62point5um.setStatus("current")
_FsFiberTransferDistance50umOM2_Type = Integer32
_FsFiberTransferDistance50umOM2_Object = MibTableColumn
fsFiberTransferDistance50umOM2 = _FsFiberTransferDistance50umOM2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 9),
    _FsFiberTransferDistance50umOM2_Type()
)
fsFiberTransferDistance50umOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50umOM2.setStatus("current")
_FsFiberTransferDistance50um_Type = Integer32
_FsFiberTransferDistance50um_Object = MibTableColumn
fsFiberTransferDistance50um = _FsFiberTransferDistance50um_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 10),
    _FsFiberTransferDistance50um_Type()
)
fsFiberTransferDistance50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50um.setStatus("current")
_FsFiberTransferDistance50umOM3_Type = Integer32
_FsFiberTransferDistance50umOM3_Object = MibTableColumn
fsFiberTransferDistance50umOM3 = _FsFiberTransferDistance50umOM3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 11),
    _FsFiberTransferDistance50umOM3_Type()
)
fsFiberTransferDistance50umOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50umOM3.setStatus("current")
_FsFiberTransferDistanceEBW50um_Type = Integer32
_FsFiberTransferDistanceEBW50um_Object = MibTableColumn
fsFiberTransferDistanceEBW50um = _FsFiberTransferDistanceEBW50um_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 12),
    _FsFiberTransferDistanceEBW50um_Type()
)
fsFiberTransferDistanceEBW50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceEBW50um.setStatus("current")
_FsFiberTransferDistanceCopper_Type = Integer32
_FsFiberTransferDistanceCopper_Object = MibTableColumn
fsFiberTransferDistanceCopper = _FsFiberTransferDistanceCopper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 13),
    _FsFiberTransferDistanceCopper_Type()
)
fsFiberTransferDistanceCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceCopper.setStatus("current")
_FsFiberTransferDistanceCableAssembly_Type = Integer32
_FsFiberTransferDistanceCableAssembly_Object = MibTableColumn
fsFiberTransferDistanceCableAssembly = _FsFiberTransferDistanceCableAssembly_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 14),
    _FsFiberTransferDistanceCableAssembly_Type()
)
fsFiberTransferDistanceCableAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceCableAssembly.setStatus("current")
_FsFiberDDMSupportStatus_Type = TruthValue
_FsFiberDDMSupportStatus_Object = MibTableColumn
fsFiberDDMSupportStatus = _FsFiberDDMSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 15),
    _FsFiberDDMSupportStatus_Type()
)
fsFiberDDMSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberDDMSupportStatus.setStatus("current")


class _FsFiberSerialNumber_Type(DisplayString):
    """Custom type fsFiberSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsFiberSerialNumber_Type.__name__ = "DisplayString"
_FsFiberSerialNumber_Object = MibTableColumn
fsFiberSerialNumber = _FsFiberSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 16),
    _FsFiberSerialNumber_Type()
)
fsFiberSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberSerialNumber.setStatus("current")
_FsFiberTemp_Type = Integer32
_FsFiberTemp_Object = MibTableColumn
fsFiberTemp = _FsFiberTemp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 17),
    _FsFiberTemp_Type()
)
fsFiberTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTemp.setStatus("current")


class _FsFiberTempStatus_Type(Integer32):
    """Custom type fsFiberTempStatus based on Integer32"""
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


_FsFiberTempStatus_Type.__name__ = "Integer32"
_FsFiberTempStatus_Object = MibTableColumn
fsFiberTempStatus = _FsFiberTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 18),
    _FsFiberTempStatus_Type()
)
fsFiberTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTempStatus.setStatus("current")
_FsFiberVoltage_Type = Integer32
_FsFiberVoltage_Object = MibTableColumn
fsFiberVoltage = _FsFiberVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 19),
    _FsFiberVoltage_Type()
)
fsFiberVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltage.setStatus("current")


class _FsFiberVoltageStatus_Type(Integer32):
    """Custom type fsFiberVoltageStatus based on Integer32"""
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


_FsFiberVoltageStatus_Type.__name__ = "Integer32"
_FsFiberVoltageStatus_Object = MibTableColumn
fsFiberVoltageStatus = _FsFiberVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 20),
    _FsFiberVoltageStatus_Type()
)
fsFiberVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltageStatus.setStatus("current")
_FsFiberBias_Type = Integer32
_FsFiberBias_Object = MibTableColumn
fsFiberBias = _FsFiberBias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 21),
    _FsFiberBias_Type()
)
fsFiberBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBias.setStatus("current")


class _FsFiberBiasStatus_Type(Integer32):
    """Custom type fsFiberBiasStatus based on Integer32"""
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


_FsFiberBiasStatus_Type.__name__ = "Integer32"
_FsFiberBiasStatus_Object = MibTableColumn
fsFiberBiasStatus = _FsFiberBiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 22),
    _FsFiberBiasStatus_Type()
)
fsFiberBiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBiasStatus.setStatus("current")
_FsFiberChannel1Bias_Type = Integer32
_FsFiberChannel1Bias_Object = MibTableColumn
fsFiberChannel1Bias = _FsFiberChannel1Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 23),
    _FsFiberChannel1Bias_Type()
)
fsFiberChannel1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1Bias.setStatus("current")


class _FsFiberChannel1BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel1BiasStatus based on Integer32"""
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


_FsFiberChannel1BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel1BiasStatus_Object = MibTableColumn
fsFiberChannel1BiasStatus = _FsFiberChannel1BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 24),
    _FsFiberChannel1BiasStatus_Type()
)
fsFiberChannel1BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1BiasStatus.setStatus("current")
_FsFiberChannel2Bias_Type = Integer32
_FsFiberChannel2Bias_Object = MibTableColumn
fsFiberChannel2Bias = _FsFiberChannel2Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 25),
    _FsFiberChannel2Bias_Type()
)
fsFiberChannel2Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2Bias.setStatus("current")


class _FsFiberChannel2BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel2BiasStatus based on Integer32"""
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


_FsFiberChannel2BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel2BiasStatus_Object = MibTableColumn
fsFiberChannel2BiasStatus = _FsFiberChannel2BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 26),
    _FsFiberChannel2BiasStatus_Type()
)
fsFiberChannel2BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2BiasStatus.setStatus("current")
_FsFiberChannel3Bias_Type = Integer32
_FsFiberChannel3Bias_Object = MibTableColumn
fsFiberChannel3Bias = _FsFiberChannel3Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 27),
    _FsFiberChannel3Bias_Type()
)
fsFiberChannel3Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3Bias.setStatus("current")


class _FsFiberChannel3BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel3BiasStatus based on Integer32"""
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


_FsFiberChannel3BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel3BiasStatus_Object = MibTableColumn
fsFiberChannel3BiasStatus = _FsFiberChannel3BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 28),
    _FsFiberChannel3BiasStatus_Type()
)
fsFiberChannel3BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3BiasStatus.setStatus("current")
_FsFiberChannel4Bias_Type = Integer32
_FsFiberChannel4Bias_Object = MibTableColumn
fsFiberChannel4Bias = _FsFiberChannel4Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 29),
    _FsFiberChannel4Bias_Type()
)
fsFiberChannel4Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4Bias.setStatus("current")


class _FsFiberChannel4BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel4BiasStatus based on Integer32"""
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


_FsFiberChannel4BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel4BiasStatus_Object = MibTableColumn
fsFiberChannel4BiasStatus = _FsFiberChannel4BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 30),
    _FsFiberChannel4BiasStatus_Type()
)
fsFiberChannel4BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4BiasStatus.setStatus("current")
_FsFiberRXpowerIntegerpart_Type = Integer32
_FsFiberRXpowerIntegerpart_Object = MibTableColumn
fsFiberRXpowerIntegerpart = _FsFiberRXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 31),
    _FsFiberRXpowerIntegerpart_Type()
)
fsFiberRXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerIntegerpart.setStatus("current")
_FsFiberRXpowerDecimalpart_Type = Integer32
_FsFiberRXpowerDecimalpart_Object = MibTableColumn
fsFiberRXpowerDecimalpart = _FsFiberRXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 32),
    _FsFiberRXpowerDecimalpart_Type()
)
fsFiberRXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerDecimalpart.setStatus("current")


class _FsFiberRXpowertype_Type(Integer32):
    """Custom type fsFiberRXpowertype based on Integer32"""
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


_FsFiberRXpowertype_Type.__name__ = "Integer32"
_FsFiberRXpowertype_Object = MibTableColumn
fsFiberRXpowertype = _FsFiberRXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 33),
    _FsFiberRXpowertype_Type()
)
fsFiberRXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowertype.setStatus("current")


class _FsFiberRXpowerStatus_Type(Integer32):
    """Custom type fsFiberRXpowerStatus based on Integer32"""
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


_FsFiberRXpowerStatus_Type.__name__ = "Integer32"
_FsFiberRXpowerStatus_Object = MibTableColumn
fsFiberRXpowerStatus = _FsFiberRXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 34),
    _FsFiberRXpowerStatus_Type()
)
fsFiberRXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerStatus.setStatus("current")
_FsFiberChannel1RXpowerIntegerpart_Type = Integer32
_FsFiberChannel1RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel1RXpowerIntegerpart = _FsFiberChannel1RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 35),
    _FsFiberChannel1RXpowerIntegerpart_Type()
)
fsFiberChannel1RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerIntegerpart.setStatus("current")
_FsFiberChannel1RXpowerDecimalpart_Type = Integer32
_FsFiberChannel1RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel1RXpowerDecimalpart = _FsFiberChannel1RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 36),
    _FsFiberChannel1RXpowerDecimalpart_Type()
)
fsFiberChannel1RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel1RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel1RXpowertype based on Integer32"""
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


_FsFiberChannel1RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel1RXpowertype_Object = MibTableColumn
fsFiberChannel1RXpowertype = _FsFiberChannel1RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 37),
    _FsFiberChannel1RXpowertype_Type()
)
fsFiberChannel1RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowertype.setStatus("current")


class _FsFiberChannel1RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel1RXpowerStatus based on Integer32"""
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


_FsFiberChannel1RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel1RXpowerStatus_Object = MibTableColumn
fsFiberChannel1RXpowerStatus = _FsFiberChannel1RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 38),
    _FsFiberChannel1RXpowerStatus_Type()
)
fsFiberChannel1RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerStatus.setStatus("current")
_FsFiberChannel2RXpowerIntegerpart_Type = Integer32
_FsFiberChannel2RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel2RXpowerIntegerpart = _FsFiberChannel2RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 39),
    _FsFiberChannel2RXpowerIntegerpart_Type()
)
fsFiberChannel2RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerIntegerpart.setStatus("current")
_FsFiberChannel2RXpowerDecimalpart_Type = Integer32
_FsFiberChannel2RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel2RXpowerDecimalpart = _FsFiberChannel2RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 40),
    _FsFiberChannel2RXpowerDecimalpart_Type()
)
fsFiberChannel2RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel2RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel2RXpowertype based on Integer32"""
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


_FsFiberChannel2RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel2RXpowertype_Object = MibTableColumn
fsFiberChannel2RXpowertype = _FsFiberChannel2RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 41),
    _FsFiberChannel2RXpowertype_Type()
)
fsFiberChannel2RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowertype.setStatus("current")


class _FsFiberChannel2RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel2RXpowerStatus based on Integer32"""
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


_FsFiberChannel2RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel2RXpowerStatus_Object = MibTableColumn
fsFiberChannel2RXpowerStatus = _FsFiberChannel2RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 42),
    _FsFiberChannel2RXpowerStatus_Type()
)
fsFiberChannel2RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerStatus.setStatus("current")
_FsFiberChannel3RXpowerIntegerpart_Type = Integer32
_FsFiberChannel3RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel3RXpowerIntegerpart = _FsFiberChannel3RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 43),
    _FsFiberChannel3RXpowerIntegerpart_Type()
)
fsFiberChannel3RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerIntegerpart.setStatus("current")
_FsFiberChannel3RXpowerDecimalpart_Type = Integer32
_FsFiberChannel3RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel3RXpowerDecimalpart = _FsFiberChannel3RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 44),
    _FsFiberChannel3RXpowerDecimalpart_Type()
)
fsFiberChannel3RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel3RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel3RXpowertype based on Integer32"""
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


_FsFiberChannel3RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel3RXpowertype_Object = MibTableColumn
fsFiberChannel3RXpowertype = _FsFiberChannel3RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 45),
    _FsFiberChannel3RXpowertype_Type()
)
fsFiberChannel3RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowertype.setStatus("current")


class _FsFiberChannel3RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel3RXpowerStatus based on Integer32"""
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


_FsFiberChannel3RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel3RXpowerStatus_Object = MibTableColumn
fsFiberChannel3RXpowerStatus = _FsFiberChannel3RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 46),
    _FsFiberChannel3RXpowerStatus_Type()
)
fsFiberChannel3RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerStatus.setStatus("current")
_FsFiberChannel4RXpowerIntegerpart_Type = Integer32
_FsFiberChannel4RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel4RXpowerIntegerpart = _FsFiberChannel4RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 47),
    _FsFiberChannel4RXpowerIntegerpart_Type()
)
fsFiberChannel4RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerIntegerpart.setStatus("current")
_FsFiberChannel4RXpowerDecimalpart_Type = Integer32
_FsFiberChannel4RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel4RXpowerDecimalpart = _FsFiberChannel4RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 48),
    _FsFiberChannel4RXpowerDecimalpart_Type()
)
fsFiberChannel4RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel4RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel4RXpowertype based on Integer32"""
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


_FsFiberChannel4RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel4RXpowertype_Object = MibTableColumn
fsFiberChannel4RXpowertype = _FsFiberChannel4RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 49),
    _FsFiberChannel4RXpowertype_Type()
)
fsFiberChannel4RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowertype.setStatus("current")


class _FsFiberChannel4RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel4RXpowerStatus based on Integer32"""
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


_FsFiberChannel4RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel4RXpowerStatus_Object = MibTableColumn
fsFiberChannel4RXpowerStatus = _FsFiberChannel4RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 50),
    _FsFiberChannel4RXpowerStatus_Type()
)
fsFiberChannel4RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerStatus.setStatus("current")
_FsFiberTXpowerIntegerpart_Type = Integer32
_FsFiberTXpowerIntegerpart_Object = MibTableColumn
fsFiberTXpowerIntegerpart = _FsFiberTXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 51),
    _FsFiberTXpowerIntegerpart_Type()
)
fsFiberTXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerIntegerpart.setStatus("current")
_FsFiberTXpowerDecimalpart_Type = Integer32
_FsFiberTXpowerDecimalpart_Object = MibTableColumn
fsFiberTXpowerDecimalpart = _FsFiberTXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 52),
    _FsFiberTXpowerDecimalpart_Type()
)
fsFiberTXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerDecimalpart.setStatus("current")


class _FsFiberTXpowerStatus_Type(Integer32):
    """Custom type fsFiberTXpowerStatus based on Integer32"""
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


_FsFiberTXpowerStatus_Type.__name__ = "Integer32"
_FsFiberTXpowerStatus_Object = MibTableColumn
fsFiberTXpowerStatus = _FsFiberTXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 53),
    _FsFiberTXpowerStatus_Type()
)
fsFiberTXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerStatus.setStatus("current")
_FsFiberChannel1TXpowerIntegerpart_Type = Integer32
_FsFiberChannel1TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel1TXpowerIntegerpart = _FsFiberChannel1TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 54),
    _FsFiberChannel1TXpowerIntegerpart_Type()
)
fsFiberChannel1TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerIntegerpart.setStatus("current")
_FsFiberChannel1TXpowerDecimalpart_Type = Integer32
_FsFiberChannel1TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel1TXpowerDecimalpart = _FsFiberChannel1TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 55),
    _FsFiberChannel1TXpowerDecimalpart_Type()
)
fsFiberChannel1TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel1TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel1TXpowerStatus based on Integer32"""
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


_FsFiberChannel1TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel1TXpowerStatus_Object = MibTableColumn
fsFiberChannel1TXpowerStatus = _FsFiberChannel1TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 56),
    _FsFiberChannel1TXpowerStatus_Type()
)
fsFiberChannel1TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerStatus.setStatus("current")
_FsFiberChannel2TXpowerIntegerpart_Type = Integer32
_FsFiberChannel2TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel2TXpowerIntegerpart = _FsFiberChannel2TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 57),
    _FsFiberChannel2TXpowerIntegerpart_Type()
)
fsFiberChannel2TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerIntegerpart.setStatus("current")
_FsFiberChannel2TXpowerDecimalpart_Type = Integer32
_FsFiberChannel2TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel2TXpowerDecimalpart = _FsFiberChannel2TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 58),
    _FsFiberChannel2TXpowerDecimalpart_Type()
)
fsFiberChannel2TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel2TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel2TXpowerStatus based on Integer32"""
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


_FsFiberChannel2TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel2TXpowerStatus_Object = MibTableColumn
fsFiberChannel2TXpowerStatus = _FsFiberChannel2TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 59),
    _FsFiberChannel2TXpowerStatus_Type()
)
fsFiberChannel2TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerStatus.setStatus("current")
_FsFiberChannel3TXpowerIntegerpart_Type = Integer32
_FsFiberChannel3TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel3TXpowerIntegerpart = _FsFiberChannel3TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 60),
    _FsFiberChannel3TXpowerIntegerpart_Type()
)
fsFiberChannel3TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerIntegerpart.setStatus("current")
_FsFiberChannel3TXpowerDecimalpart_Type = Integer32
_FsFiberChannel3TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel3TXpowerDecimalpart = _FsFiberChannel3TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 61),
    _FsFiberChannel3TXpowerDecimalpart_Type()
)
fsFiberChannel3TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel3TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel3TXpowerStatus based on Integer32"""
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


_FsFiberChannel3TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel3TXpowerStatus_Object = MibTableColumn
fsFiberChannel3TXpowerStatus = _FsFiberChannel3TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 62),
    _FsFiberChannel3TXpowerStatus_Type()
)
fsFiberChannel3TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerStatus.setStatus("current")
_FsFiberChannel4TXpowerIntegerpart_Type = Integer32
_FsFiberChannel4TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel4TXpowerIntegerpart = _FsFiberChannel4TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 63),
    _FsFiberChannel4TXpowerIntegerpart_Type()
)
fsFiberChannel4TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerIntegerpart.setStatus("current")
_FsFiberChannel4TXpowerDecimalpart_Type = Integer32
_FsFiberChannel4TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel4TXpowerDecimalpart = _FsFiberChannel4TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 64),
    _FsFiberChannel4TXpowerDecimalpart_Type()
)
fsFiberChannel4TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel4TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel4TXpowerStatus based on Integer32"""
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


_FsFiberChannel4TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel4TXpowerStatus_Object = MibTableColumn
fsFiberChannel4TXpowerStatus = _FsFiberChannel4TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 65),
    _FsFiberChannel4TXpowerStatus_Type()
)
fsFiberChannel4TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerStatus.setStatus("current")
_FsFiberRXpowerSign_Type = Integer32
_FsFiberRXpowerSign_Object = MibTableColumn
fsFiberRXpowerSign = _FsFiberRXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 66),
    _FsFiberRXpowerSign_Type()
)
fsFiberRXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerSign.setStatus("current")
_FsFiberChannel1RXpowerSign_Type = Integer32
_FsFiberChannel1RXpowerSign_Object = MibTableColumn
fsFiberChannel1RXpowerSign = _FsFiberChannel1RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 67),
    _FsFiberChannel1RXpowerSign_Type()
)
fsFiberChannel1RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerSign.setStatus("current")
_FsFiberChannel2RXpowerSign_Type = Integer32
_FsFiberChannel2RXpowerSign_Object = MibTableColumn
fsFiberChannel2RXpowerSign = _FsFiberChannel2RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 68),
    _FsFiberChannel2RXpowerSign_Type()
)
fsFiberChannel2RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerSign.setStatus("current")
_FsFiberChannel3RXpowerSign_Type = Integer32
_FsFiberChannel3RXpowerSign_Object = MibTableColumn
fsFiberChannel3RXpowerSign = _FsFiberChannel3RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 69),
    _FsFiberChannel3RXpowerSign_Type()
)
fsFiberChannel3RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerSign.setStatus("current")
_FsFiberChannel4RXpowerSign_Type = Integer32
_FsFiberChannel4RXpowerSign_Object = MibTableColumn
fsFiberChannel4RXpowerSign = _FsFiberChannel4RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 70),
    _FsFiberChannel4RXpowerSign_Type()
)
fsFiberChannel4RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerSign.setStatus("current")
_FsFiberTXpowerSign_Type = Integer32
_FsFiberTXpowerSign_Object = MibTableColumn
fsFiberTXpowerSign = _FsFiberTXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 71),
    _FsFiberTXpowerSign_Type()
)
fsFiberTXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerSign.setStatus("current")
_FsFiberChannel1TXpowerSign_Type = Integer32
_FsFiberChannel1TXpowerSign_Object = MibTableColumn
fsFiberChannel1TXpowerSign = _FsFiberChannel1TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 72),
    _FsFiberChannel1TXpowerSign_Type()
)
fsFiberChannel1TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerSign.setStatus("current")
_FsFiberChannel2TXpowerSign_Type = Integer32
_FsFiberChannel2TXpowerSign_Object = MibTableColumn
fsFiberChannel2TXpowerSign = _FsFiberChannel2TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 73),
    _FsFiberChannel2TXpowerSign_Type()
)
fsFiberChannel2TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerSign.setStatus("current")
_FsFiberChannel3TXpowerSign_Type = Integer32
_FsFiberChannel3TXpowerSign_Object = MibTableColumn
fsFiberChannel3TXpowerSign = _FsFiberChannel3TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 74),
    _FsFiberChannel3TXpowerSign_Type()
)
fsFiberChannel3TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerSign.setStatus("current")
_FsFiberChannel4TXpowerSign_Type = Integer32
_FsFiberChannel4TXpowerSign_Object = MibTableColumn
fsFiberChannel4TXpowerSign = _FsFiberChannel4TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 75),
    _FsFiberChannel4TXpowerSign_Type()
)
fsFiberChannel4TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerSign.setStatus("current")
_FsFiberRXpower_Type = Integer32
_FsFiberRXpower_Object = MibTableColumn
fsFiberRXpower = _FsFiberRXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 76),
    _FsFiberRXpower_Type()
)
fsFiberRXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpower.setStatus("current")
_FsFiberChannel1RXpower_Type = Integer32
_FsFiberChannel1RXpower_Object = MibTableColumn
fsFiberChannel1RXpower = _FsFiberChannel1RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 77),
    _FsFiberChannel1RXpower_Type()
)
fsFiberChannel1RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpower.setStatus("current")
_FsFiberChannel2RXpower_Type = Integer32
_FsFiberChannel2RXpower_Object = MibTableColumn
fsFiberChannel2RXpower = _FsFiberChannel2RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 78),
    _FsFiberChannel2RXpower_Type()
)
fsFiberChannel2RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpower.setStatus("current")
_FsFiberChannel3RXpower_Type = Integer32
_FsFiberChannel3RXpower_Object = MibTableColumn
fsFiberChannel3RXpower = _FsFiberChannel3RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 79),
    _FsFiberChannel3RXpower_Type()
)
fsFiberChannel3RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpower.setStatus("current")
_FsFiberChannel4RXpower_Type = Integer32
_FsFiberChannel4RXpower_Object = MibTableColumn
fsFiberChannel4RXpower = _FsFiberChannel4RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 80),
    _FsFiberChannel4RXpower_Type()
)
fsFiberChannel4RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpower.setStatus("current")
_FsFiberTXpower_Type = Integer32
_FsFiberTXpower_Object = MibTableColumn
fsFiberTXpower = _FsFiberTXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 81),
    _FsFiberTXpower_Type()
)
fsFiberTXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpower.setStatus("current")
_FsFiberChannel1TXpower_Type = Integer32
_FsFiberChannel1TXpower_Object = MibTableColumn
fsFiberChannel1TXpower = _FsFiberChannel1TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 82),
    _FsFiberChannel1TXpower_Type()
)
fsFiberChannel1TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpower.setStatus("current")
_FsFiberChannel2TXpower_Type = Integer32
_FsFiberChannel2TXpower_Object = MibTableColumn
fsFiberChannel2TXpower = _FsFiberChannel2TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 83),
    _FsFiberChannel2TXpower_Type()
)
fsFiberChannel2TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpower.setStatus("current")
_FsFiberChannel3TXpower_Type = Integer32
_FsFiberChannel3TXpower_Object = MibTableColumn
fsFiberChannel3TXpower = _FsFiberChannel3TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 84),
    _FsFiberChannel3TXpower_Type()
)
fsFiberChannel3TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpower.setStatus("current")
_FsFiberChannel4TXpower_Type = Integer32
_FsFiberChannel4TXpower_Object = MibTableColumn
fsFiberChannel4TXpower = _FsFiberChannel4TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 85),
    _FsFiberChannel4TXpower_Type()
)
fsFiberChannel4TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpower.setStatus("current")


class _FsFiberWavelengthExact_Type(DisplayString):
    """Custom type fsFiberWavelengthExact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsFiberWavelengthExact_Type.__name__ = "DisplayString"
_FsFiberWavelengthExact_Object = MibTableColumn
fsFiberWavelengthExact = _FsFiberWavelengthExact_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 86),
    _FsFiberWavelengthExact_Type()
)
fsFiberWavelengthExact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberWavelengthExact.setStatus("current")
_FsFiberTransferDistance50umOM4_Type = Integer32
_FsFiberTransferDistance50umOM4_Object = MibTableColumn
fsFiberTransferDistance50umOM4 = _FsFiberTransferDistance50umOM4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 87),
    _FsFiberTransferDistance50umOM4_Type()
)
fsFiberTransferDistance50umOM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50umOM4.setStatus("current")
_FsFiberTransferDistanceSMFExt_Type = Integer32
_FsFiberTransferDistanceSMFExt_Object = MibTableColumn
fsFiberTransferDistanceSMFExt = _FsFiberTransferDistanceSMFExt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 88),
    _FsFiberTransferDistanceSMFExt_Type()
)
fsFiberTransferDistanceSMFExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceSMFExt.setStatus("current")
_FsFiberBandWidth_Type = Integer32
_FsFiberBandWidth_Object = MibTableColumn
fsFiberBandWidth = _FsFiberBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 89),
    _FsFiberBandWidth_Type()
)
fsFiberBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBandWidth.setStatus("current")


class _FsFiberFormFactor_Type(Integer32):
    """Custom type fsFiberFormFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("xfp", 1),
          ("sfp", 2),
          ("sfpPlus", 3),
          ("sfp28", 4),
          ("qsfpPlus", 5),
          ("qsfp28", 6))
    )


_FsFiberFormFactor_Type.__name__ = "Integer32"
_FsFiberFormFactor_Object = MibTableColumn
fsFiberFormFactor = _FsFiberFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 90),
    _FsFiberFormFactor_Type()
)
fsFiberFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberFormFactor.setStatus("current")
_FsFiberRXpowerLowWarnThreshold_Type = Integer32
_FsFiberRXpowerLowWarnThreshold_Object = MibTableColumn
fsFiberRXpowerLowWarnThreshold = _FsFiberRXpowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 91),
    _FsFiberRXpowerLowWarnThreshold_Type()
)
fsFiberRXpowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerLowWarnThreshold.setStatus("current")
_FsFiberRXpowerHighWarnThreshold_Type = Integer32
_FsFiberRXpowerHighWarnThreshold_Object = MibTableColumn
fsFiberRXpowerHighWarnThreshold = _FsFiberRXpowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 92),
    _FsFiberRXpowerHighWarnThreshold_Type()
)
fsFiberRXpowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerHighWarnThreshold.setStatus("current")
_FsFiberRXpowerLowAlarmThreshold_Type = Integer32
_FsFiberRXpowerLowAlarmThreshold_Object = MibTableColumn
fsFiberRXpowerLowAlarmThreshold = _FsFiberRXpowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 93),
    _FsFiberRXpowerLowAlarmThreshold_Type()
)
fsFiberRXpowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerLowAlarmThreshold.setStatus("current")
_FsFiberRXpowerHighAlarmThreshold_Type = Integer32
_FsFiberRXpowerHighAlarmThreshold_Object = MibTableColumn
fsFiberRXpowerHighAlarmThreshold = _FsFiberRXpowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 94),
    _FsFiberRXpowerHighAlarmThreshold_Type()
)
fsFiberRXpowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerHighAlarmThreshold.setStatus("current")
_FsFiberTXpowerLowWarnThreshold_Type = Integer32
_FsFiberTXpowerLowWarnThreshold_Object = MibTableColumn
fsFiberTXpowerLowWarnThreshold = _FsFiberTXpowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 95),
    _FsFiberTXpowerLowWarnThreshold_Type()
)
fsFiberTXpowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerLowWarnThreshold.setStatus("current")
_FsFiberTXpowerHighWarnThreshold_Type = Integer32
_FsFiberTXpowerHighWarnThreshold_Object = MibTableColumn
fsFiberTXpowerHighWarnThreshold = _FsFiberTXpowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 96),
    _FsFiberTXpowerHighWarnThreshold_Type()
)
fsFiberTXpowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerHighWarnThreshold.setStatus("current")
_FsFiberTXpowerLowAlarmThreshold_Type = Integer32
_FsFiberTXpowerLowAlarmThreshold_Object = MibTableColumn
fsFiberTXpowerLowAlarmThreshold = _FsFiberTXpowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 97),
    _FsFiberTXpowerLowAlarmThreshold_Type()
)
fsFiberTXpowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerLowAlarmThreshold.setStatus("current")
_FsFiberTXpowerHighAlarmThreshold_Type = Integer32
_FsFiberTXpowerHighAlarmThreshold_Object = MibTableColumn
fsFiberTXpowerHighAlarmThreshold = _FsFiberTXpowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 98),
    _FsFiberTXpowerHighAlarmThreshold_Type()
)
fsFiberTXpowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerHighAlarmThreshold.setStatus("current")
_FsFiberChannel5Bias_Type = Integer32
_FsFiberChannel5Bias_Object = MibTableColumn
fsFiberChannel5Bias = _FsFiberChannel5Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 99),
    _FsFiberChannel5Bias_Type()
)
fsFiberChannel5Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5Bias.setStatus("current")


class _FsFiberChannel5BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel5BiasStatus based on Integer32"""
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


_FsFiberChannel5BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel5BiasStatus_Object = MibTableColumn
fsFiberChannel5BiasStatus = _FsFiberChannel5BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 100),
    _FsFiberChannel5BiasStatus_Type()
)
fsFiberChannel5BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5BiasStatus.setStatus("current")
_FsFiberChannel6Bias_Type = Integer32
_FsFiberChannel6Bias_Object = MibTableColumn
fsFiberChannel6Bias = _FsFiberChannel6Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 101),
    _FsFiberChannel6Bias_Type()
)
fsFiberChannel6Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6Bias.setStatus("current")


class _FsFiberChannel6BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel6BiasStatus based on Integer32"""
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


_FsFiberChannel6BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel6BiasStatus_Object = MibTableColumn
fsFiberChannel6BiasStatus = _FsFiberChannel6BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 102),
    _FsFiberChannel6BiasStatus_Type()
)
fsFiberChannel6BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6BiasStatus.setStatus("current")
_FsFiberChannel7Bias_Type = Integer32
_FsFiberChannel7Bias_Object = MibTableColumn
fsFiberChannel7Bias = _FsFiberChannel7Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 103),
    _FsFiberChannel7Bias_Type()
)
fsFiberChannel7Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7Bias.setStatus("current")


class _FsFiberChannel7BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel7BiasStatus based on Integer32"""
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


_FsFiberChannel7BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel7BiasStatus_Object = MibTableColumn
fsFiberChannel7BiasStatus = _FsFiberChannel7BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 104),
    _FsFiberChannel7BiasStatus_Type()
)
fsFiberChannel7BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7BiasStatus.setStatus("current")
_FsFiberChannel8Bias_Type = Integer32
_FsFiberChannel8Bias_Object = MibTableColumn
fsFiberChannel8Bias = _FsFiberChannel8Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 105),
    _FsFiberChannel8Bias_Type()
)
fsFiberChannel8Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8Bias.setStatus("current")


class _FsFiberChannel8BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel8BiasStatus based on Integer32"""
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


_FsFiberChannel8BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel8BiasStatus_Object = MibTableColumn
fsFiberChannel8BiasStatus = _FsFiberChannel8BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 106),
    _FsFiberChannel8BiasStatus_Type()
)
fsFiberChannel8BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8BiasStatus.setStatus("current")
_FsFiberChannel5RXpowerIntegerpart_Type = Integer32
_FsFiberChannel5RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel5RXpowerIntegerpart = _FsFiberChannel5RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 107),
    _FsFiberChannel5RXpowerIntegerpart_Type()
)
fsFiberChannel5RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5RXpowerIntegerpart.setStatus("current")
_FsFiberChannel5RXpowerDecimalpart_Type = Integer32
_FsFiberChannel5RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel5RXpowerDecimalpart = _FsFiberChannel5RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 108),
    _FsFiberChannel5RXpowerDecimalpart_Type()
)
fsFiberChannel5RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel5RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel5RXpowertype based on Integer32"""
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


_FsFiberChannel5RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel5RXpowertype_Object = MibTableColumn
fsFiberChannel5RXpowertype = _FsFiberChannel5RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 109),
    _FsFiberChannel5RXpowertype_Type()
)
fsFiberChannel5RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5RXpowertype.setStatus("current")


class _FsFiberChannel5RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel5RXpowerStatus based on Integer32"""
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


_FsFiberChannel5RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel5RXpowerStatus_Object = MibTableColumn
fsFiberChannel5RXpowerStatus = _FsFiberChannel5RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 110),
    _FsFiberChannel5RXpowerStatus_Type()
)
fsFiberChannel5RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5RXpowerStatus.setStatus("current")
_FsFiberChannel6RXpowerIntegerpart_Type = Integer32
_FsFiberChannel6RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel6RXpowerIntegerpart = _FsFiberChannel6RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 111),
    _FsFiberChannel6RXpowerIntegerpart_Type()
)
fsFiberChannel6RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6RXpowerIntegerpart.setStatus("current")
_FsFiberChannel6RXpowerDecimalpart_Type = Integer32
_FsFiberChannel6RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel6RXpowerDecimalpart = _FsFiberChannel6RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 112),
    _FsFiberChannel6RXpowerDecimalpart_Type()
)
fsFiberChannel6RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel6RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel6RXpowertype based on Integer32"""
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


_FsFiberChannel6RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel6RXpowertype_Object = MibTableColumn
fsFiberChannel6RXpowertype = _FsFiberChannel6RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 113),
    _FsFiberChannel6RXpowertype_Type()
)
fsFiberChannel6RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6RXpowertype.setStatus("current")


class _FsFiberChannel6RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel6RXpowerStatus based on Integer32"""
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


_FsFiberChannel6RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel6RXpowerStatus_Object = MibTableColumn
fsFiberChannel6RXpowerStatus = _FsFiberChannel6RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 114),
    _FsFiberChannel6RXpowerStatus_Type()
)
fsFiberChannel6RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6RXpowerStatus.setStatus("current")
_FsFiberChannel7RXpowerIntegerpart_Type = Integer32
_FsFiberChannel7RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel7RXpowerIntegerpart = _FsFiberChannel7RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 115),
    _FsFiberChannel7RXpowerIntegerpart_Type()
)
fsFiberChannel7RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7RXpowerIntegerpart.setStatus("current")
_FsFiberChannel7RXpowerDecimalpart_Type = Integer32
_FsFiberChannel7RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel7RXpowerDecimalpart = _FsFiberChannel7RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 116),
    _FsFiberChannel7RXpowerDecimalpart_Type()
)
fsFiberChannel7RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel7RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel7RXpowertype based on Integer32"""
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


_FsFiberChannel7RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel7RXpowertype_Object = MibTableColumn
fsFiberChannel7RXpowertype = _FsFiberChannel7RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 117),
    _FsFiberChannel7RXpowertype_Type()
)
fsFiberChannel7RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7RXpowertype.setStatus("current")


class _FsFiberChannel7RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel7RXpowerStatus based on Integer32"""
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


_FsFiberChannel7RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel7RXpowerStatus_Object = MibTableColumn
fsFiberChannel7RXpowerStatus = _FsFiberChannel7RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 118),
    _FsFiberChannel7RXpowerStatus_Type()
)
fsFiberChannel7RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7RXpowerStatus.setStatus("current")
_FsFiberChannel8RXpowerIntegerpart_Type = Integer32
_FsFiberChannel8RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel8RXpowerIntegerpart = _FsFiberChannel8RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 119),
    _FsFiberChannel8RXpowerIntegerpart_Type()
)
fsFiberChannel8RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8RXpowerIntegerpart.setStatus("current")
_FsFiberChannel8RXpowerDecimalpart_Type = Integer32
_FsFiberChannel8RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel8RXpowerDecimalpart = _FsFiberChannel8RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 120),
    _FsFiberChannel8RXpowerDecimalpart_Type()
)
fsFiberChannel8RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel8RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel8RXpowertype based on Integer32"""
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


_FsFiberChannel8RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel8RXpowertype_Object = MibTableColumn
fsFiberChannel8RXpowertype = _FsFiberChannel8RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 121),
    _FsFiberChannel8RXpowertype_Type()
)
fsFiberChannel8RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8RXpowertype.setStatus("current")


class _FsFiberChannel8RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel8RXpowerStatus based on Integer32"""
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


_FsFiberChannel8RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel8RXpowerStatus_Object = MibTableColumn
fsFiberChannel8RXpowerStatus = _FsFiberChannel8RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 122),
    _FsFiberChannel8RXpowerStatus_Type()
)
fsFiberChannel8RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8RXpowerStatus.setStatus("current")
_FsFiberChannel5TXpowerIntegerpart_Type = Integer32
_FsFiberChannel5TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel5TXpowerIntegerpart = _FsFiberChannel5TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 123),
    _FsFiberChannel5TXpowerIntegerpart_Type()
)
fsFiberChannel5TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5TXpowerIntegerpart.setStatus("current")
_FsFiberChannel5TXpowerDecimalpart_Type = Integer32
_FsFiberChannel5TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel5TXpowerDecimalpart = _FsFiberChannel5TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 124),
    _FsFiberChannel5TXpowerDecimalpart_Type()
)
fsFiberChannel5TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel5TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel5TXpowerStatus based on Integer32"""
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


_FsFiberChannel5TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel5TXpowerStatus_Object = MibTableColumn
fsFiberChannel5TXpowerStatus = _FsFiberChannel5TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 125),
    _FsFiberChannel5TXpowerStatus_Type()
)
fsFiberChannel5TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5TXpowerStatus.setStatus("current")
_FsFiberChannel6TXpowerIntegerpart_Type = Integer32
_FsFiberChannel6TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel6TXpowerIntegerpart = _FsFiberChannel6TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 126),
    _FsFiberChannel6TXpowerIntegerpart_Type()
)
fsFiberChannel6TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6TXpowerIntegerpart.setStatus("current")
_FsFiberChannel6TXpowerDecimalpart_Type = Integer32
_FsFiberChannel6TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel6TXpowerDecimalpart = _FsFiberChannel6TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 127),
    _FsFiberChannel6TXpowerDecimalpart_Type()
)
fsFiberChannel6TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel6TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel6TXpowerStatus based on Integer32"""
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


_FsFiberChannel6TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel6TXpowerStatus_Object = MibTableColumn
fsFiberChannel6TXpowerStatus = _FsFiberChannel6TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 128),
    _FsFiberChannel6TXpowerStatus_Type()
)
fsFiberChannel6TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6TXpowerStatus.setStatus("current")
_FsFiberChannel7TXpowerIntegerpart_Type = Integer32
_FsFiberChannel7TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel7TXpowerIntegerpart = _FsFiberChannel7TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 129),
    _FsFiberChannel7TXpowerIntegerpart_Type()
)
fsFiberChannel7TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7TXpowerIntegerpart.setStatus("current")
_FsFiberChannel7TXpowerDecimalpart_Type = Integer32
_FsFiberChannel7TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel7TXpowerDecimalpart = _FsFiberChannel7TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 130),
    _FsFiberChannel7TXpowerDecimalpart_Type()
)
fsFiberChannel7TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel7TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel7TXpowerStatus based on Integer32"""
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


_FsFiberChannel7TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel7TXpowerStatus_Object = MibTableColumn
fsFiberChannel7TXpowerStatus = _FsFiberChannel7TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 131),
    _FsFiberChannel7TXpowerStatus_Type()
)
fsFiberChannel7TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7TXpowerStatus.setStatus("current")
_FsFiberChannel8TXpowerIntegerpart_Type = Integer32
_FsFiberChannel8TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel8TXpowerIntegerpart = _FsFiberChannel8TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 132),
    _FsFiberChannel8TXpowerIntegerpart_Type()
)
fsFiberChannel8TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8TXpowerIntegerpart.setStatus("current")
_FsFiberChannel8TXpowerDecimalpart_Type = Integer32
_FsFiberChannel8TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel8TXpowerDecimalpart = _FsFiberChannel8TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 133),
    _FsFiberChannel8TXpowerDecimalpart_Type()
)
fsFiberChannel8TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel8TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel8TXpowerStatus based on Integer32"""
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


_FsFiberChannel8TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel8TXpowerStatus_Object = MibTableColumn
fsFiberChannel8TXpowerStatus = _FsFiberChannel8TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 134),
    _FsFiberChannel8TXpowerStatus_Type()
)
fsFiberChannel8TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8TXpowerStatus.setStatus("current")
_FsFiberChannel5RXpowerSign_Type = Integer32
_FsFiberChannel5RXpowerSign_Object = MibTableColumn
fsFiberChannel5RXpowerSign = _FsFiberChannel5RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 135),
    _FsFiberChannel5RXpowerSign_Type()
)
fsFiberChannel5RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5RXpowerSign.setStatus("current")
_FsFiberChannel6RXpowerSign_Type = Integer32
_FsFiberChannel6RXpowerSign_Object = MibTableColumn
fsFiberChannel6RXpowerSign = _FsFiberChannel6RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 136),
    _FsFiberChannel6RXpowerSign_Type()
)
fsFiberChannel6RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6RXpowerSign.setStatus("current")
_FsFiberChannel7RXpowerSign_Type = Integer32
_FsFiberChannel7RXpowerSign_Object = MibTableColumn
fsFiberChannel7RXpowerSign = _FsFiberChannel7RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 137),
    _FsFiberChannel7RXpowerSign_Type()
)
fsFiberChannel7RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7RXpowerSign.setStatus("current")
_FsFiberChannel8RXpowerSign_Type = Integer32
_FsFiberChannel8RXpowerSign_Object = MibTableColumn
fsFiberChannel8RXpowerSign = _FsFiberChannel8RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 138),
    _FsFiberChannel8RXpowerSign_Type()
)
fsFiberChannel8RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8RXpowerSign.setStatus("current")
_FsFiberChannel5TXpowerSign_Type = Integer32
_FsFiberChannel5TXpowerSign_Object = MibTableColumn
fsFiberChannel5TXpowerSign = _FsFiberChannel5TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 139),
    _FsFiberChannel5TXpowerSign_Type()
)
fsFiberChannel5TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5TXpowerSign.setStatus("current")
_FsFiberChannel6TXpowerSign_Type = Integer32
_FsFiberChannel6TXpowerSign_Object = MibTableColumn
fsFiberChannel6TXpowerSign = _FsFiberChannel6TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 140),
    _FsFiberChannel6TXpowerSign_Type()
)
fsFiberChannel6TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6TXpowerSign.setStatus("current")
_FsFiberChannel7TXpowerSign_Type = Integer32
_FsFiberChannel7TXpowerSign_Object = MibTableColumn
fsFiberChannel7TXpowerSign = _FsFiberChannel7TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 141),
    _FsFiberChannel7TXpowerSign_Type()
)
fsFiberChannel7TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7TXpowerSign.setStatus("current")
_FsFiberChannel8TXpowerSign_Type = Integer32
_FsFiberChannel8TXpowerSign_Object = MibTableColumn
fsFiberChannel8TXpowerSign = _FsFiberChannel8TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 142),
    _FsFiberChannel8TXpowerSign_Type()
)
fsFiberChannel8TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8TXpowerSign.setStatus("current")
_FsFiberChannel5RXpower_Type = Integer32
_FsFiberChannel5RXpower_Object = MibTableColumn
fsFiberChannel5RXpower = _FsFiberChannel5RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 143),
    _FsFiberChannel5RXpower_Type()
)
fsFiberChannel5RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5RXpower.setStatus("current")
_FsFiberChannel6RXpower_Type = Integer32
_FsFiberChannel6RXpower_Object = MibTableColumn
fsFiberChannel6RXpower = _FsFiberChannel6RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 144),
    _FsFiberChannel6RXpower_Type()
)
fsFiberChannel6RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6RXpower.setStatus("current")
_FsFiberChannel7RXpower_Type = Integer32
_FsFiberChannel7RXpower_Object = MibTableColumn
fsFiberChannel7RXpower = _FsFiberChannel7RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 145),
    _FsFiberChannel7RXpower_Type()
)
fsFiberChannel7RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7RXpower.setStatus("current")
_FsFiberChannel8RXpower_Type = Integer32
_FsFiberChannel8RXpower_Object = MibTableColumn
fsFiberChannel8RXpower = _FsFiberChannel8RXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 146),
    _FsFiberChannel8RXpower_Type()
)
fsFiberChannel8RXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8RXpower.setStatus("current")
_FsFiberChannel5TXpower_Type = Integer32
_FsFiberChannel5TXpower_Object = MibTableColumn
fsFiberChannel5TXpower = _FsFiberChannel5TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 147),
    _FsFiberChannel5TXpower_Type()
)
fsFiberChannel5TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel5TXpower.setStatus("current")
_FsFiberChannel6TXpower_Type = Integer32
_FsFiberChannel6TXpower_Object = MibTableColumn
fsFiberChannel6TXpower = _FsFiberChannel6TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 148),
    _FsFiberChannel6TXpower_Type()
)
fsFiberChannel6TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel6TXpower.setStatus("current")
_FsFiberChannel7TXpower_Type = Integer32
_FsFiberChannel7TXpower_Object = MibTableColumn
fsFiberChannel7TXpower = _FsFiberChannel7TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 149),
    _FsFiberChannel7TXpower_Type()
)
fsFiberChannel7TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel7TXpower.setStatus("current")
_FsFiberChannel8TXpower_Type = Integer32
_FsFiberChannel8TXpower_Object = MibTableColumn
fsFiberChannel8TXpower = _FsFiberChannel8TXpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 150),
    _FsFiberChannel8TXpower_Type()
)
fsFiberChannel8TXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel8TXpower.setStatus("current")
_FsFiberTransferDistance50umOM5_Type = Integer32
_FsFiberTransferDistance50umOM5_Object = MibTableColumn
fsFiberTransferDistance50umOM5 = _FsFiberTransferDistance50umOM5_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 151),
    _FsFiberTransferDistance50umOM5_Type()
)
fsFiberTransferDistance50umOM5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50umOM5.setStatus("current")


class _FsFiberMode_Type(Integer32):
    """Custom type fsFiberMode based on Integer32"""
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


_FsFiberMode_Type.__name__ = "Integer32"
_FsFiberMode_Object = MibTableColumn
fsFiberMode = _FsFiberMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 152),
    _FsFiberMode_Type()
)
fsFiberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberMode.setStatus("current")
_FsFiberTempLowWarnThreshold_Type = Integer32
_FsFiberTempLowWarnThreshold_Object = MibTableColumn
fsFiberTempLowWarnThreshold = _FsFiberTempLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 153),
    _FsFiberTempLowWarnThreshold_Type()
)
fsFiberTempLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTempLowWarnThreshold.setStatus("current")
_FsFiberTempHighWarnThreshold_Type = Integer32
_FsFiberTempHighWarnThreshold_Object = MibTableColumn
fsFiberTempHighWarnThreshold = _FsFiberTempHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 154),
    _FsFiberTempHighWarnThreshold_Type()
)
fsFiberTempHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTempHighWarnThreshold.setStatus("current")
_FsFiberTempLowAlarmThreshold_Type = Integer32
_FsFiberTempLowAlarmThreshold_Object = MibTableColumn
fsFiberTempLowAlarmThreshold = _FsFiberTempLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 155),
    _FsFiberTempLowAlarmThreshold_Type()
)
fsFiberTempLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTempLowAlarmThreshold.setStatus("current")
_FsFiberTempHighAlarmThreshold_Type = Integer32
_FsFiberTempHighAlarmThreshold_Object = MibTableColumn
fsFiberTempHighAlarmThreshold = _FsFiberTempHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 156),
    _FsFiberTempHighAlarmThreshold_Type()
)
fsFiberTempHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTempHighAlarmThreshold.setStatus("current")
_FsFiberVoltageLowWarnThreshold_Type = Integer32
_FsFiberVoltageLowWarnThreshold_Object = MibTableColumn
fsFiberVoltageLowWarnThreshold = _FsFiberVoltageLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 157),
    _FsFiberVoltageLowWarnThreshold_Type()
)
fsFiberVoltageLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltageLowWarnThreshold.setStatus("current")
_FsFiberVoltageHighWarnThreshold_Type = Integer32
_FsFiberVoltageHighWarnThreshold_Object = MibTableColumn
fsFiberVoltageHighWarnThreshold = _FsFiberVoltageHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 158),
    _FsFiberVoltageHighWarnThreshold_Type()
)
fsFiberVoltageHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltageHighWarnThreshold.setStatus("current")
_FsFiberVoltageLowAlarmThreshold_Type = Integer32
_FsFiberVoltageLowAlarmThreshold_Object = MibTableColumn
fsFiberVoltageLowAlarmThreshold = _FsFiberVoltageLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 159),
    _FsFiberVoltageLowAlarmThreshold_Type()
)
fsFiberVoltageLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltageLowAlarmThreshold.setStatus("current")
_FsFiberVoltageHighAlarmThreshold_Type = Integer32
_FsFiberVoltageHighAlarmThreshold_Object = MibTableColumn
fsFiberVoltageHighAlarmThreshold = _FsFiberVoltageHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 160),
    _FsFiberVoltageHighAlarmThreshold_Type()
)
fsFiberVoltageHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltageHighAlarmThreshold.setStatus("current")
_FsFiberBiasLowWarnThreshold_Type = Integer32
_FsFiberBiasLowWarnThreshold_Object = MibTableColumn
fsFiberBiasLowWarnThreshold = _FsFiberBiasLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 161),
    _FsFiberBiasLowWarnThreshold_Type()
)
fsFiberBiasLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBiasLowWarnThreshold.setStatus("current")
_FsFiberBiasHighWarnThreshold_Type = Integer32
_FsFiberBiasHighWarnThreshold_Object = MibTableColumn
fsFiberBiasHighWarnThreshold = _FsFiberBiasHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 162),
    _FsFiberBiasHighWarnThreshold_Type()
)
fsFiberBiasHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBiasHighWarnThreshold.setStatus("current")
_FsFiberBiasLowAlarmThreshold_Type = Integer32
_FsFiberBiasLowAlarmThreshold_Object = MibTableColumn
fsFiberBiasLowAlarmThreshold = _FsFiberBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 163),
    _FsFiberBiasLowAlarmThreshold_Type()
)
fsFiberBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBiasLowAlarmThreshold.setStatus("current")
_FsFiberBiasHighAlarmThreshold_Type = Integer32
_FsFiberBiasHighAlarmThreshold_Object = MibTableColumn
fsFiberBiasHighAlarmThreshold = _FsFiberBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 164),
    _FsFiberBiasHighAlarmThreshold_Type()
)
fsFiberBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBiasHighAlarmThreshold.setStatus("current")
_FsFiberVendorTable_Object = MibTable
fsFiberVendorTable = _FsFiberVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    fsFiberVendorTable.setStatus("current")
_FsFiberVendorEntry_Object = MibTableRow
fsFiberVendorEntry = _FsFiberVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1)
)
fsFiberVendorEntry.setIndexNames(
    (0, "FS-FIBER-MIB", "fsFiberVendorPortIndex"),
)
if mibBuilder.loadTexts:
    fsFiberVendorEntry.setStatus("current")
_FsFiberVendorPortIndex_Type = IfIndex
_FsFiberVendorPortIndex_Object = MibTableColumn
fsFiberVendorPortIndex = _FsFiberVendorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 1),
    _FsFiberVendorPortIndex_Type()
)
fsFiberVendorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorPortIndex.setStatus("current")
_FsFiberVendorName_Type = DisplayString
_FsFiberVendorName_Object = MibTableColumn
fsFiberVendorName = _FsFiberVendorName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 2),
    _FsFiberVendorName_Type()
)
fsFiberVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorName.setStatus("current")
_FsFiberVendorOUI_Type = DisplayString
_FsFiberVendorOUI_Object = MibTableColumn
fsFiberVendorOUI = _FsFiberVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 3),
    _FsFiberVendorOUI_Type()
)
fsFiberVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorOUI.setStatus("current")
_FsFiberVendorPartNumber_Type = DisplayString
_FsFiberVendorPartNumber_Object = MibTableColumn
fsFiberVendorPartNumber = _FsFiberVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 4),
    _FsFiberVendorPartNumber_Type()
)
fsFiberVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorPartNumber.setStatus("current")
_FsFiberVendorRev_Type = DisplayString
_FsFiberVendorRev_Object = MibTableColumn
fsFiberVendorRev = _FsFiberVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 5),
    _FsFiberVendorRev_Type()
)
fsFiberVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorRev.setStatus("current")
_FsFiberManufacturingDate_Type = DisplayString
_FsFiberManufacturingDate_Object = MibTableColumn
fsFiberManufacturingDate = _FsFiberManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 6),
    _FsFiberManufacturingDate_Type()
)
fsFiberManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberManufacturingDate.setStatus("current")
_FsFiberEncoding_Type = DisplayString
_FsFiberEncoding_Object = MibTableColumn
fsFiberEncoding = _FsFiberEncoding_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 7),
    _FsFiberEncoding_Type()
)
fsFiberEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberEncoding.setStatus("current")
_FsFiberOMCTable_Object = MibTable
fsFiberOMCTable = _FsFiberOMCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    fsFiberOMCTable.setStatus("current")
_FsFiberOMCEntry_Object = MibTableRow
fsFiberOMCEntry = _FsFiberOMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1)
)
fsFiberOMCEntry.setIndexNames(
    (0, "FS-FIBER-MIB", "fsFiberOMCPortIndex"),
)
if mibBuilder.loadTexts:
    fsFiberOMCEntry.setStatus("current")
_FsFiberOMCPortIndex_Type = IfIndex
_FsFiberOMCPortIndex_Object = MibTableColumn
fsFiberOMCPortIndex = _FsFiberOMCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1, 1),
    _FsFiberOMCPortIndex_Type()
)
fsFiberOMCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberOMCPortIndex.setStatus("current")


class _FsFiberOMCRxpower_Type(DisplayString):
    """Custom type fsFiberOMCRxpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberOMCRxpower_Type.__name__ = "DisplayString"
_FsFiberOMCRxpower_Object = MibTableColumn
fsFiberOMCRxpower = _FsFiberOMCRxpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1, 2),
    _FsFiberOMCRxpower_Type()
)
fsFiberOMCRxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberOMCRxpower.setStatus("current")
_FsFiberOMCTxpower_Type = DisplayString
_FsFiberOMCTxpower_Object = MibTableColumn
fsFiberOMCTxpower = _FsFiberOMCTxpower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1, 3),
    _FsFiberOMCTxpower_Type()
)
fsFiberOMCTxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberOMCTxpower.setStatus("current")


class _FsFiberOMCWavelength_Type(DisplayString):
    """Custom type fsFiberOMCWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberOMCWavelength_Type.__name__ = "DisplayString"
_FsFiberOMCWavelength_Object = MibTableColumn
fsFiberOMCWavelength = _FsFiberOMCWavelength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1, 4),
    _FsFiberOMCWavelength_Type()
)
fsFiberOMCWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberOMCWavelength.setStatus("current")
_FsFiberOMCTranslength_Type = DisplayString
_FsFiberOMCTranslength_Object = MibTableColumn
fsFiberOMCTranslength = _FsFiberOMCTranslength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1, 5),
    _FsFiberOMCTranslength_Type()
)
fsFiberOMCTranslength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberOMCTranslength.setStatus("current")


class _FsFiberOMCPortType_Type(DisplayString):
    """Custom type fsFiberOMCPortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberOMCPortType_Type.__name__ = "DisplayString"
_FsFiberOMCPortType_Object = MibTableColumn
fsFiberOMCPortType = _FsFiberOMCPortType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 3, 1, 6),
    _FsFiberOMCPortType_Type()
)
fsFiberOMCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberOMCPortType.setStatus("current")
_FsFiberAntifakeMIBTraps_ObjectIdentity = ObjectIdentity
fsFiberAntifakeMIBTraps = _FsFiberAntifakeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2)
)


class _FsFiberAntifakeIntfNameDesc_Type(DisplayString):
    """Custom type fsFiberAntifakeIntfNameDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberAntifakeIntfNameDesc_Type.__name__ = "DisplayString"
_FsFiberAntifakeIntfNameDesc_Object = MibScalar
fsFiberAntifakeIntfNameDesc = _FsFiberAntifakeIntfNameDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2, 1),
    _FsFiberAntifakeIntfNameDesc_Type()
)
fsFiberAntifakeIntfNameDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberAntifakeIntfNameDesc.setStatus("current")


class _FsFiberAntifakeSerialNumberDesc_Type(DisplayString):
    """Custom type fsFiberAntifakeSerialNumberDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberAntifakeSerialNumberDesc_Type.__name__ = "DisplayString"
_FsFiberAntifakeSerialNumberDesc_Object = MibScalar
fsFiberAntifakeSerialNumberDesc = _FsFiberAntifakeSerialNumberDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2, 2),
    _FsFiberAntifakeSerialNumberDesc_Type()
)
fsFiberAntifakeSerialNumberDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberAntifakeSerialNumberDesc.setStatus("current")
_FsFiberMIBConformance_ObjectIdentity = ObjectIdentity
fsFiberMIBConformance = _FsFiberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3)
)
_FsFiberMIBCompliances_ObjectIdentity = ObjectIdentity
fsFiberMIBCompliances = _FsFiberMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 1)
)
_FsFiberMIBGroups_ObjectIdentity = ObjectIdentity
fsFiberMIBGroups = _FsFiberMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2)
)
_FsFiberEventMIBTraps_ObjectIdentity = ObjectIdentity
fsFiberEventMIBTraps = _FsFiberEventMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4)
)


class _FsFiberEventReason_Type(Integer32):
    """Custom type fsFiberEventReason based on Integer32"""
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
              36)
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
          ("fiberInvalidRXMediaPreFECBERHighWarn", 36))
    )


_FsFiberEventReason_Type.__name__ = "Integer32"
_FsFiberEventReason_Object = MibScalar
fsFiberEventReason = _FsFiberEventReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 1),
    _FsFiberEventReason_Type()
)
fsFiberEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberEventReason.setStatus("current")


class _FsFiberEventDesc_Type(DisplayString):
    """Custom type fsFiberEventDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberEventDesc_Type.__name__ = "DisplayString"
_FsFiberEventDesc_Object = MibScalar
fsFiberEventDesc = _FsFiberEventDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 2),
    _FsFiberEventDesc_Type()
)
fsFiberEventDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberEventDesc.setStatus("current")
_FsFiberAlarmValue_Type = Integer32
_FsFiberAlarmValue_Object = MibScalar
fsFiberAlarmValue = _FsFiberAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 7),
    _FsFiberAlarmValue_Type()
)
fsFiberAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberAlarmValue.setStatus("current")
_FsFiberAlarmThresholdValue_Type = Integer32
_FsFiberAlarmThresholdValue_Object = MibScalar
fsFiberAlarmThresholdValue = _FsFiberAlarmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 8),
    _FsFiberAlarmThresholdValue_Type()
)
fsFiberAlarmThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberAlarmThresholdValue.setStatus("current")

# Managed Objects groups

fsFiberMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2, 1)
)
fsFiberMIBGroup.setObjects(
      *(("FS-FIBER-MIB", "fsFiberPortDescr"),
        ("FS-FIBER-MIB", "fsFiberTransceiverType"),
        ("FS-FIBER-MIB", "fsFiberConnectorType"),
        ("FS-FIBER-MIB", "fsFiberWavelength"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceSMF"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance62point5umOM1"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance62point5um"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50umOM2"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50um"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50umOM3"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceEBW50um"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceCopper"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceCableAssembly"),
        ("FS-FIBER-MIB", "fsFiberDDMSupportStatus"),
        ("FS-FIBER-MIB", "fsFiberSerialNumber"),
        ("FS-FIBER-MIB", "fsFiberTemp"),
        ("FS-FIBER-MIB", "fsFiberTempStatus"),
        ("FS-FIBER-MIB", "fsFiberVoltage"),
        ("FS-FIBER-MIB", "fsFiberVoltageStatus"),
        ("FS-FIBER-MIB", "fsFiberBias"),
        ("FS-FIBER-MIB", "fsFiberBiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel1Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel1BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel2Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel2BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel3Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel3BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel4Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel4BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberRXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberRXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberRXpowertype"),
        ("FS-FIBER-MIB", "fsFiberRXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberTXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberTXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberTXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberRXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberTXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberRXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpower"),
        ("FS-FIBER-MIB", "fsFiberTXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpower"),
        ("FS-FIBER-MIB", "fsFiberWavelengthExact"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50umOM4"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceSMFExt"),
        ("FS-FIBER-MIB", "fsFiberBandWidth"),
        ("FS-FIBER-MIB", "fsFiberFormFactor"),
        ("FS-FIBER-MIB", "fsFiberRXpowerLowWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberRXpowerHighWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberRXpowerLowAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberRXpowerHighAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberTXpowerLowWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberTXpowerHighWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberTXpowerLowAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberTXpowerHighAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberChannel5Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel5BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel6Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel6BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel7Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel7BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel8Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel8BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel5RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel5RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel5RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel5RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel6RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel6RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel6RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel6RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel7RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel7RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel7RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel7RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel8RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel8RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel8RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel8RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel5TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel5TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel5TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel6TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel6TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel6TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel7TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel7TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel7TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel8TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel8TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel8TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel5RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel6RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel7RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel8RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel5TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel6TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel7TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel8TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel5RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel6RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel7RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel8RXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel5TXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel6TXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel7TXpower"),
        ("FS-FIBER-MIB", "fsFiberChannel8TXpower"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50umOM5"),
        ("FS-FIBER-MIB", "fsFiberMode"),
        ("FS-FIBER-MIB", "fsFiberTempLowWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberTempHighWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberTempLowAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberTempHighAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberVoltageLowWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberVoltageHighWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberVoltageLowAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberVoltageHighAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberBiasLowWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberBiasHighWarnThreshold"),
        ("FS-FIBER-MIB", "fsFiberBiasLowAlarmThreshold"),
        ("FS-FIBER-MIB", "fsFiberBiasHighAlarmThreshold"))
)
if mibBuilder.loadTexts:
    fsFiberMIBGroup.setStatus("current")

fsFiberAntifakeIntfNameDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2, 2)
)
fsFiberAntifakeIntfNameDescGroup.setObjects(
    ("FS-FIBER-MIB", "fsFiberAntifakeIntfNameDesc")
)
if mibBuilder.loadTexts:
    fsFiberAntifakeIntfNameDescGroup.setStatus("current")

fsFiberAntifakeSerialNumberDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2, 3)
)
fsFiberAntifakeSerialNumberDescGroup.setObjects(
    ("FS-FIBER-MIB", "fsFiberAntifakeSerialNumberDesc")
)
if mibBuilder.loadTexts:
    fsFiberAntifakeSerialNumberDescGroup.setStatus("current")


# Notification objects

fsFiberAntifakeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2, 3)
)
fsFiberAntifakeTrap.setObjects(
      *(("FS-FIBER-MIB", "fsFiberAntifakeIntfNameDesc"),
        ("FS-FIBER-MIB", "fsFiberAntifakeSerialNumberDesc"))
)
if mibBuilder.loadTexts:
    fsFiberAntifakeTrap.setStatus(
        "current"
    )

fsFiberRemoveEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 3)
)
fsFiberRemoveEventTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    fsFiberRemoveEventTrap.setStatus(
        "current"
    )

fsFiberInsertEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 4)
)
fsFiberInsertEventTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    fsFiberInsertEventTrap.setStatus(
        "current"
    )

fsFiberInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 5)
)
fsFiberInvalidTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("FS-FIBER-MIB", "fsFiberEventReason"),
        ("FS-FIBER-MIB", "fsFiberEventDesc"),
        ("FS-FIBER-MIB", "fsFiberAlarmValue"),
        ("FS-FIBER-MIB", "fsFiberAlarmThresholdValue"))
)
if mibBuilder.loadTexts:
    fsFiberInvalidTrap.setStatus(
        "current"
    )

fsFiberInvalidResumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 6)
)
fsFiberInvalidResumeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("FS-FIBER-MIB", "fsFiberEventReason"),
        ("FS-FIBER-MIB", "fsFiberEventDesc"),
        ("FS-FIBER-MIB", "fsFiberAlarmValue"),
        ("FS-FIBER-MIB", "fsFiberAlarmThresholdValue"))
)
if mibBuilder.loadTexts:
    fsFiberInvalidResumeTrap.setStatus(
        "current"
    )

fsFiberSpeedMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 4, 9)
)
fsFiberSpeedMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    fsFiberSpeedMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsFiberMIBConpliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 1, 1)
)
fsFiberMIBConpliance.setObjects(
      *(("FS-FIBER-MIB", "fsFiberMIBGroup"),
        ("FS-FIBER-MIB", "fsFiberAntifakeIntfNameDescGroup"),
        ("FS-FIBER-MIB", "fsFiberAntifakeSerialNumberDescGroup"))
)
if mibBuilder.loadTexts:
    fsFiberMIBConpliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-FIBER-MIB",
    **{"fsFiberMIB": fsFiberMIB,
       "fsFiberMIBObjects": fsFiberMIBObjects,
       "fsFiberTable": fsFiberTable,
       "fsFiberEntry": fsFiberEntry,
       "fsFiberPortIndex": fsFiberPortIndex,
       "fsFiberPortDescr": fsFiberPortDescr,
       "fsFiberTransceiverType": fsFiberTransceiverType,
       "fsFiberConnectorType": fsFiberConnectorType,
       "fsFiberWavelength": fsFiberWavelength,
       "fsFiberTransferDistanceSMF": fsFiberTransferDistanceSMF,
       "fsFiberTransferDistance62point5umOM1": fsFiberTransferDistance62point5umOM1,
       "fsFiberTransferDistance62point5um": fsFiberTransferDistance62point5um,
       "fsFiberTransferDistance50umOM2": fsFiberTransferDistance50umOM2,
       "fsFiberTransferDistance50um": fsFiberTransferDistance50um,
       "fsFiberTransferDistance50umOM3": fsFiberTransferDistance50umOM3,
       "fsFiberTransferDistanceEBW50um": fsFiberTransferDistanceEBW50um,
       "fsFiberTransferDistanceCopper": fsFiberTransferDistanceCopper,
       "fsFiberTransferDistanceCableAssembly": fsFiberTransferDistanceCableAssembly,
       "fsFiberDDMSupportStatus": fsFiberDDMSupportStatus,
       "fsFiberSerialNumber": fsFiberSerialNumber,
       "fsFiberTemp": fsFiberTemp,
       "fsFiberTempStatus": fsFiberTempStatus,
       "fsFiberVoltage": fsFiberVoltage,
       "fsFiberVoltageStatus": fsFiberVoltageStatus,
       "fsFiberBias": fsFiberBias,
       "fsFiberBiasStatus": fsFiberBiasStatus,
       "fsFiberChannel1Bias": fsFiberChannel1Bias,
       "fsFiberChannel1BiasStatus": fsFiberChannel1BiasStatus,
       "fsFiberChannel2Bias": fsFiberChannel2Bias,
       "fsFiberChannel2BiasStatus": fsFiberChannel2BiasStatus,
       "fsFiberChannel3Bias": fsFiberChannel3Bias,
       "fsFiberChannel3BiasStatus": fsFiberChannel3BiasStatus,
       "fsFiberChannel4Bias": fsFiberChannel4Bias,
       "fsFiberChannel4BiasStatus": fsFiberChannel4BiasStatus,
       "fsFiberRXpowerIntegerpart": fsFiberRXpowerIntegerpart,
       "fsFiberRXpowerDecimalpart": fsFiberRXpowerDecimalpart,
       "fsFiberRXpowertype": fsFiberRXpowertype,
       "fsFiberRXpowerStatus": fsFiberRXpowerStatus,
       "fsFiberChannel1RXpowerIntegerpart": fsFiberChannel1RXpowerIntegerpart,
       "fsFiberChannel1RXpowerDecimalpart": fsFiberChannel1RXpowerDecimalpart,
       "fsFiberChannel1RXpowertype": fsFiberChannel1RXpowertype,
       "fsFiberChannel1RXpowerStatus": fsFiberChannel1RXpowerStatus,
       "fsFiberChannel2RXpowerIntegerpart": fsFiberChannel2RXpowerIntegerpart,
       "fsFiberChannel2RXpowerDecimalpart": fsFiberChannel2RXpowerDecimalpart,
       "fsFiberChannel2RXpowertype": fsFiberChannel2RXpowertype,
       "fsFiberChannel2RXpowerStatus": fsFiberChannel2RXpowerStatus,
       "fsFiberChannel3RXpowerIntegerpart": fsFiberChannel3RXpowerIntegerpart,
       "fsFiberChannel3RXpowerDecimalpart": fsFiberChannel3RXpowerDecimalpart,
       "fsFiberChannel3RXpowertype": fsFiberChannel3RXpowertype,
       "fsFiberChannel3RXpowerStatus": fsFiberChannel3RXpowerStatus,
       "fsFiberChannel4RXpowerIntegerpart": fsFiberChannel4RXpowerIntegerpart,
       "fsFiberChannel4RXpowerDecimalpart": fsFiberChannel4RXpowerDecimalpart,
       "fsFiberChannel4RXpowertype": fsFiberChannel4RXpowertype,
       "fsFiberChannel4RXpowerStatus": fsFiberChannel4RXpowerStatus,
       "fsFiberTXpowerIntegerpart": fsFiberTXpowerIntegerpart,
       "fsFiberTXpowerDecimalpart": fsFiberTXpowerDecimalpart,
       "fsFiberTXpowerStatus": fsFiberTXpowerStatus,
       "fsFiberChannel1TXpowerIntegerpart": fsFiberChannel1TXpowerIntegerpart,
       "fsFiberChannel1TXpowerDecimalpart": fsFiberChannel1TXpowerDecimalpart,
       "fsFiberChannel1TXpowerStatus": fsFiberChannel1TXpowerStatus,
       "fsFiberChannel2TXpowerIntegerpart": fsFiberChannel2TXpowerIntegerpart,
       "fsFiberChannel2TXpowerDecimalpart": fsFiberChannel2TXpowerDecimalpart,
       "fsFiberChannel2TXpowerStatus": fsFiberChannel2TXpowerStatus,
       "fsFiberChannel3TXpowerIntegerpart": fsFiberChannel3TXpowerIntegerpart,
       "fsFiberChannel3TXpowerDecimalpart": fsFiberChannel3TXpowerDecimalpart,
       "fsFiberChannel3TXpowerStatus": fsFiberChannel3TXpowerStatus,
       "fsFiberChannel4TXpowerIntegerpart": fsFiberChannel4TXpowerIntegerpart,
       "fsFiberChannel4TXpowerDecimalpart": fsFiberChannel4TXpowerDecimalpart,
       "fsFiberChannel4TXpowerStatus": fsFiberChannel4TXpowerStatus,
       "fsFiberRXpowerSign": fsFiberRXpowerSign,
       "fsFiberChannel1RXpowerSign": fsFiberChannel1RXpowerSign,
       "fsFiberChannel2RXpowerSign": fsFiberChannel2RXpowerSign,
       "fsFiberChannel3RXpowerSign": fsFiberChannel3RXpowerSign,
       "fsFiberChannel4RXpowerSign": fsFiberChannel4RXpowerSign,
       "fsFiberTXpowerSign": fsFiberTXpowerSign,
       "fsFiberChannel1TXpowerSign": fsFiberChannel1TXpowerSign,
       "fsFiberChannel2TXpowerSign": fsFiberChannel2TXpowerSign,
       "fsFiberChannel3TXpowerSign": fsFiberChannel3TXpowerSign,
       "fsFiberChannel4TXpowerSign": fsFiberChannel4TXpowerSign,
       "fsFiberRXpower": fsFiberRXpower,
       "fsFiberChannel1RXpower": fsFiberChannel1RXpower,
       "fsFiberChannel2RXpower": fsFiberChannel2RXpower,
       "fsFiberChannel3RXpower": fsFiberChannel3RXpower,
       "fsFiberChannel4RXpower": fsFiberChannel4RXpower,
       "fsFiberTXpower": fsFiberTXpower,
       "fsFiberChannel1TXpower": fsFiberChannel1TXpower,
       "fsFiberChannel2TXpower": fsFiberChannel2TXpower,
       "fsFiberChannel3TXpower": fsFiberChannel3TXpower,
       "fsFiberChannel4TXpower": fsFiberChannel4TXpower,
       "fsFiberWavelengthExact": fsFiberWavelengthExact,
       "fsFiberTransferDistance50umOM4": fsFiberTransferDistance50umOM4,
       "fsFiberTransferDistanceSMFExt": fsFiberTransferDistanceSMFExt,
       "fsFiberBandWidth": fsFiberBandWidth,
       "fsFiberFormFactor": fsFiberFormFactor,
       "fsFiberRXpowerLowWarnThreshold": fsFiberRXpowerLowWarnThreshold,
       "fsFiberRXpowerHighWarnThreshold": fsFiberRXpowerHighWarnThreshold,
       "fsFiberRXpowerLowAlarmThreshold": fsFiberRXpowerLowAlarmThreshold,
       "fsFiberRXpowerHighAlarmThreshold": fsFiberRXpowerHighAlarmThreshold,
       "fsFiberTXpowerLowWarnThreshold": fsFiberTXpowerLowWarnThreshold,
       "fsFiberTXpowerHighWarnThreshold": fsFiberTXpowerHighWarnThreshold,
       "fsFiberTXpowerLowAlarmThreshold": fsFiberTXpowerLowAlarmThreshold,
       "fsFiberTXpowerHighAlarmThreshold": fsFiberTXpowerHighAlarmThreshold,
       "fsFiberChannel5Bias": fsFiberChannel5Bias,
       "fsFiberChannel5BiasStatus": fsFiberChannel5BiasStatus,
       "fsFiberChannel6Bias": fsFiberChannel6Bias,
       "fsFiberChannel6BiasStatus": fsFiberChannel6BiasStatus,
       "fsFiberChannel7Bias": fsFiberChannel7Bias,
       "fsFiberChannel7BiasStatus": fsFiberChannel7BiasStatus,
       "fsFiberChannel8Bias": fsFiberChannel8Bias,
       "fsFiberChannel8BiasStatus": fsFiberChannel8BiasStatus,
       "fsFiberChannel5RXpowerIntegerpart": fsFiberChannel5RXpowerIntegerpart,
       "fsFiberChannel5RXpowerDecimalpart": fsFiberChannel5RXpowerDecimalpart,
       "fsFiberChannel5RXpowertype": fsFiberChannel5RXpowertype,
       "fsFiberChannel5RXpowerStatus": fsFiberChannel5RXpowerStatus,
       "fsFiberChannel6RXpowerIntegerpart": fsFiberChannel6RXpowerIntegerpart,
       "fsFiberChannel6RXpowerDecimalpart": fsFiberChannel6RXpowerDecimalpart,
       "fsFiberChannel6RXpowertype": fsFiberChannel6RXpowertype,
       "fsFiberChannel6RXpowerStatus": fsFiberChannel6RXpowerStatus,
       "fsFiberChannel7RXpowerIntegerpart": fsFiberChannel7RXpowerIntegerpart,
       "fsFiberChannel7RXpowerDecimalpart": fsFiberChannel7RXpowerDecimalpart,
       "fsFiberChannel7RXpowertype": fsFiberChannel7RXpowertype,
       "fsFiberChannel7RXpowerStatus": fsFiberChannel7RXpowerStatus,
       "fsFiberChannel8RXpowerIntegerpart": fsFiberChannel8RXpowerIntegerpart,
       "fsFiberChannel8RXpowerDecimalpart": fsFiberChannel8RXpowerDecimalpart,
       "fsFiberChannel8RXpowertype": fsFiberChannel8RXpowertype,
       "fsFiberChannel8RXpowerStatus": fsFiberChannel8RXpowerStatus,
       "fsFiberChannel5TXpowerIntegerpart": fsFiberChannel5TXpowerIntegerpart,
       "fsFiberChannel5TXpowerDecimalpart": fsFiberChannel5TXpowerDecimalpart,
       "fsFiberChannel5TXpowerStatus": fsFiberChannel5TXpowerStatus,
       "fsFiberChannel6TXpowerIntegerpart": fsFiberChannel6TXpowerIntegerpart,
       "fsFiberChannel6TXpowerDecimalpart": fsFiberChannel6TXpowerDecimalpart,
       "fsFiberChannel6TXpowerStatus": fsFiberChannel6TXpowerStatus,
       "fsFiberChannel7TXpowerIntegerpart": fsFiberChannel7TXpowerIntegerpart,
       "fsFiberChannel7TXpowerDecimalpart": fsFiberChannel7TXpowerDecimalpart,
       "fsFiberChannel7TXpowerStatus": fsFiberChannel7TXpowerStatus,
       "fsFiberChannel8TXpowerIntegerpart": fsFiberChannel8TXpowerIntegerpart,
       "fsFiberChannel8TXpowerDecimalpart": fsFiberChannel8TXpowerDecimalpart,
       "fsFiberChannel8TXpowerStatus": fsFiberChannel8TXpowerStatus,
       "fsFiberChannel5RXpowerSign": fsFiberChannel5RXpowerSign,
       "fsFiberChannel6RXpowerSign": fsFiberChannel6RXpowerSign,
       "fsFiberChannel7RXpowerSign": fsFiberChannel7RXpowerSign,
       "fsFiberChannel8RXpowerSign": fsFiberChannel8RXpowerSign,
       "fsFiberChannel5TXpowerSign": fsFiberChannel5TXpowerSign,
       "fsFiberChannel6TXpowerSign": fsFiberChannel6TXpowerSign,
       "fsFiberChannel7TXpowerSign": fsFiberChannel7TXpowerSign,
       "fsFiberChannel8TXpowerSign": fsFiberChannel8TXpowerSign,
       "fsFiberChannel5RXpower": fsFiberChannel5RXpower,
       "fsFiberChannel6RXpower": fsFiberChannel6RXpower,
       "fsFiberChannel7RXpower": fsFiberChannel7RXpower,
       "fsFiberChannel8RXpower": fsFiberChannel8RXpower,
       "fsFiberChannel5TXpower": fsFiberChannel5TXpower,
       "fsFiberChannel6TXpower": fsFiberChannel6TXpower,
       "fsFiberChannel7TXpower": fsFiberChannel7TXpower,
       "fsFiberChannel8TXpower": fsFiberChannel8TXpower,
       "fsFiberTransferDistance50umOM5": fsFiberTransferDistance50umOM5,
       "fsFiberMode": fsFiberMode,
       "fsFiberTempLowWarnThreshold": fsFiberTempLowWarnThreshold,
       "fsFiberTempHighWarnThreshold": fsFiberTempHighWarnThreshold,
       "fsFiberTempLowAlarmThreshold": fsFiberTempLowAlarmThreshold,
       "fsFiberTempHighAlarmThreshold": fsFiberTempHighAlarmThreshold,
       "fsFiberVoltageLowWarnThreshold": fsFiberVoltageLowWarnThreshold,
       "fsFiberVoltageHighWarnThreshold": fsFiberVoltageHighWarnThreshold,
       "fsFiberVoltageLowAlarmThreshold": fsFiberVoltageLowAlarmThreshold,
       "fsFiberVoltageHighAlarmThreshold": fsFiberVoltageHighAlarmThreshold,
       "fsFiberBiasLowWarnThreshold": fsFiberBiasLowWarnThreshold,
       "fsFiberBiasHighWarnThreshold": fsFiberBiasHighWarnThreshold,
       "fsFiberBiasLowAlarmThreshold": fsFiberBiasLowAlarmThreshold,
       "fsFiberBiasHighAlarmThreshold": fsFiberBiasHighAlarmThreshold,
       "fsFiberVendorTable": fsFiberVendorTable,
       "fsFiberVendorEntry": fsFiberVendorEntry,
       "fsFiberVendorPortIndex": fsFiberVendorPortIndex,
       "fsFiberVendorName": fsFiberVendorName,
       "fsFiberVendorOUI": fsFiberVendorOUI,
       "fsFiberVendorPartNumber": fsFiberVendorPartNumber,
       "fsFiberVendorRev": fsFiberVendorRev,
       "fsFiberManufacturingDate": fsFiberManufacturingDate,
       "fsFiberEncoding": fsFiberEncoding,
       "fsFiberOMCTable": fsFiberOMCTable,
       "fsFiberOMCEntry": fsFiberOMCEntry,
       "fsFiberOMCPortIndex": fsFiberOMCPortIndex,
       "fsFiberOMCRxpower": fsFiberOMCRxpower,
       "fsFiberOMCTxpower": fsFiberOMCTxpower,
       "fsFiberOMCWavelength": fsFiberOMCWavelength,
       "fsFiberOMCTranslength": fsFiberOMCTranslength,
       "fsFiberOMCPortType": fsFiberOMCPortType,
       "fsFiberAntifakeMIBTraps": fsFiberAntifakeMIBTraps,
       "fsFiberAntifakeIntfNameDesc": fsFiberAntifakeIntfNameDesc,
       "fsFiberAntifakeSerialNumberDesc": fsFiberAntifakeSerialNumberDesc,
       "fsFiberAntifakeTrap": fsFiberAntifakeTrap,
       "fsFiberMIBConformance": fsFiberMIBConformance,
       "fsFiberMIBCompliances": fsFiberMIBCompliances,
       "fsFiberMIBConpliance": fsFiberMIBConpliance,
       "fsFiberMIBGroups": fsFiberMIBGroups,
       "fsFiberMIBGroup": fsFiberMIBGroup,
       "fsFiberAntifakeIntfNameDescGroup": fsFiberAntifakeIntfNameDescGroup,
       "fsFiberAntifakeSerialNumberDescGroup": fsFiberAntifakeSerialNumberDescGroup,
       "fsFiberEventMIBTraps": fsFiberEventMIBTraps,
       "fsFiberEventReason": fsFiberEventReason,
       "fsFiberEventDesc": fsFiberEventDesc,
       "fsFiberRemoveEventTrap": fsFiberRemoveEventTrap,
       "fsFiberInsertEventTrap": fsFiberInsertEventTrap,
       "fsFiberInvalidTrap": fsFiberInvalidTrap,
       "fsFiberInvalidResumeTrap": fsFiberInvalidResumeTrap,
       "fsFiberAlarmValue": fsFiberAlarmValue,
       "fsFiberAlarmThresholdValue": fsFiberAlarmThresholdValue,
       "fsFiberSpeedMismatch": fsFiberSpeedMismatch}
)
