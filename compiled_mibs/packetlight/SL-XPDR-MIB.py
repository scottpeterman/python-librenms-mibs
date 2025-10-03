# SNMP MIB module (SL-XPDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-XPDR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:59 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slXpdr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TsMaskBits(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class XpdrServiceType(TextualConvention, Integer32):
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
              81,
              82,
              83,
              84,
              85,
              86,
              87,
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
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              120,
              121,
              170,
              171,
              1701)
        )
    )
    namedValues = NamedValues(
        *(("ds3Sts1", 1),
          ("fe", 2),
          ("escon", 3),
          ("dvbVideo", 4),
          ("fc1gFicon", 5),
          ("gbE", 6),
          ("fc2g", 7),
          ("oc3Stm1", 8),
          ("oc12Stm4", 9),
          ("oc48Stm16", 10),
          ("other", 11),
          ("fc4g", 12),
          ("infiniband25G", 13),
          ("otn27g", 14),
          ("oc24gpon", 15),
          ("smpteSdi", 16),
          ("copperFe", 17),
          ("copperGbe", 18),
          ("mux2GbE", 19),
          ("mux4GbE", 20),
          ("xpdr5G", 21),
          ("ficon1g", 22),
          ("ficon2g", 23),
          ("stm1", 24),
          ("stm4", 25),
          ("stm16", 26),
          ("gpon248", 27),
          ("ficon4g", 28),
          ("eth10m", 29),
          ("xfp10oc192", 30),
          ("xfp10stm64", 31),
          ("xfp10GbEWan", 32),
          ("xfp10GbELan", 33),
          ("xfp10otu2", 34),
          ("xfp10GFC", 35),
          ("xfp10GbEWanStm64", 36),
          ("mux1GbE", 37),
          ("mux1GbERegen", 38),
          ("mux2GbERegen", 39),
          ("mux4GbERegen", 40),
          ("fc8g", 41),
          ("ficon8g", 42),
          ("mux10GbE", 43),
          ("syncEgbE", 44),
          ("noPm10GbE", 45),
          ("totu2", 46),
          ("otu1e", 50),
          ("otu2e", 51),
          ("otu1f", 52),
          ("otu2f", 53),
          ("oc192ToOtu2", 54),
          ("stm64ToOtu2", 55),
          ("gbe10WanToOtu2", 56),
          ("gbe10LanToOtu2A", 57),
          ("gbe10LanToOtu1e", 58),
          ("gbe10LanToOtu2e", 59),
          ("gbe10LanToOtu2B", 60),
          ("fc10LanToOtu1f", 61),
          ("fc10LanToOtu2f", 62),
          ("fc8LanToOtu2", 63),
          ("otu3", 64),
          ("oc768", 65),
          ("stm256", 66),
          ("otu4", 67),
          ("gbe40lan", 68),
          ("gbe100lan", 69),
          ("fc16g", 70),
          ("smpteHdSdi", 71),
          ("smpteSdSdi", 72),
          ("smpte3gSdi", 73),
          ("smpte3dSdi", 74),
          ("smpteHdSdiNtsc", 75),
          ("smpte3gSdiNtsc", 76),
          ("fc16gNoIsl", 77),
          ("fc32g", 78),
          ("cpri1", 81),
          ("cpri2", 82),
          ("cpri3", 83),
          ("cpri4", 84),
          ("cpri5", 85),
          ("cpri6", 86),
          ("cpri7", 87),
          ("enc10GbELan", 91),
          ("enc1GbELan", 92),
          ("encfc1g", 93),
          ("encfc2g", 94),
          ("encfc4g", 95),
          ("encfc8g", 96),
          ("encfc16g", 97),
          ("encfc10g", 98),
          ("enc1GbE10g", 99),
          ("encGbe40lan", 100),
          ("encGbe100lan", 101),
          ("encOtu2", 102),
          ("encOtu2e", 103),
          ("encOtu3", 104),
          ("encOtu4", 105),
          ("encOc192", 106),
          ("encStm64", 107),
          ("encfc32g", 108),
          ("encfc16gNoIsl", 110),
          ("encCpri1", 111),
          ("encCpri2", 112),
          ("encCpri3", 113),
          ("encCpri4", 114),
          ("encCpri5", 115),
          ("encCpri6", 116),
          ("encCpri7", 117),
          ("enc10GbENoPm", 118),
          ("otuc2", 120),
          ("encOtuc2", 121),
          ("copper10m", 170),
          ("copper10mAn", 171),
          ("copperFeAn", 1701))
    )



# MIB Managed Objects in the order of their OIDs

_SlXpdrConn_ObjectIdentity = ObjectIdentity
slXpdrConn = _SlXpdrConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1)
)
_XpdrConnConfigTable_Object = MibTable
xpdrConnConfigTable = _XpdrConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    xpdrConnConfigTable.setStatus("current")
_XpdrConnConfigEntry_Object = MibTableRow
xpdrConnConfigEntry = _XpdrConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1)
)
xpdrConnConfigEntry.setIndexNames(
    (0, "SL-XPDR-MIB", "xpdrConnConfigIf1"),
    (0, "SL-XPDR-MIB", "xpdrConnConfigIf2"),
)
if mibBuilder.loadTexts:
    xpdrConnConfigEntry.setStatus("current")
_XpdrConnConfigIf1_Type = InterfaceIndex
_XpdrConnConfigIf1_Object = MibTableColumn
xpdrConnConfigIf1 = _XpdrConnConfigIf1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 1),
    _XpdrConnConfigIf1_Type()
)
xpdrConnConfigIf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrConnConfigIf1.setStatus("current")
_XpdrConnConfigIf2_Type = InterfaceIndex
_XpdrConnConfigIf2_Object = MibTableColumn
xpdrConnConfigIf2 = _XpdrConnConfigIf2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 2),
    _XpdrConnConfigIf2_Type()
)
xpdrConnConfigIf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrConnConfigIf2.setStatus("current")
_XpdrConnConfigRateControlAdmin_Type = Integer32
_XpdrConnConfigRateControlAdmin_Object = MibTableColumn
xpdrConnConfigRateControlAdmin = _XpdrConnConfigRateControlAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 3),
    _XpdrConnConfigRateControlAdmin_Type()
)
xpdrConnConfigRateControlAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnConfigRateControlAdmin.setStatus("current")
_XpdrConnConfigRateControlOper_Type = Integer32
_XpdrConnConfigRateControlOper_Object = MibTableColumn
xpdrConnConfigRateControlOper = _XpdrConnConfigRateControlOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 4),
    _XpdrConnConfigRateControlOper_Type()
)
xpdrConnConfigRateControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrConnConfigRateControlOper.setStatus("current")
_XpdrConnConfigLosPropagation_Type = TruthValue
_XpdrConnConfigLosPropagation_Object = MibTableColumn
xpdrConnConfigLosPropagation = _XpdrConnConfigLosPropagation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 5),
    _XpdrConnConfigLosPropagation_Type()
)
xpdrConnConfigLosPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnConfigLosPropagation.setStatus("current")
_XpdrServiceType_Type = XpdrServiceType
_XpdrServiceType_Object = MibTableColumn
xpdrServiceType = _XpdrServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 6),
    _XpdrServiceType_Type()
)
xpdrServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrServiceType.setStatus("current")
_XpdrConnAddMask_Type = Integer32
_XpdrConnAddMask_Object = MibTableColumn
xpdrConnAddMask = _XpdrConnAddMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 7),
    _XpdrConnAddMask_Type()
)
xpdrConnAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnAddMask.setStatus("current")


class _XpdrMuxInbandAdmin_Type(Integer32):
    """Custom type xpdrMuxInbandAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("standby", 3))
    )


_XpdrMuxInbandAdmin_Type.__name__ = "Integer32"
_XpdrMuxInbandAdmin_Object = MibTableColumn
xpdrMuxInbandAdmin = _XpdrMuxInbandAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 8),
    _XpdrMuxInbandAdmin_Type()
)
xpdrMuxInbandAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrMuxInbandAdmin.setStatus("current")


class _XpdrMuxInbandOper_Type(Integer32):
    """Custom type xpdrMuxInbandOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("standby", 3))
    )


_XpdrMuxInbandOper_Type.__name__ = "Integer32"
_XpdrMuxInbandOper_Object = MibTableColumn
xpdrMuxInbandOper = _XpdrMuxInbandOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 9),
    _XpdrMuxInbandOper_Type()
)
xpdrMuxInbandOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrMuxInbandOper.setStatus("current")


class _XpdrDirection_Type(Integer32):
    """Custom type xpdrDirection based on Integer32"""
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
        *(("bidirectional", 1),
          ("unidirectionalTx", 2),
          ("unidirectionalRx", 3),
          ("loopback", 4))
    )


_XpdrDirection_Type.__name__ = "Integer32"
_XpdrDirection_Object = MibTableColumn
xpdrDirection = _XpdrDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 10),
    _XpdrDirection_Type()
)
xpdrDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrDirection.setStatus("current")
_XpdrConnConfigCpriRateControl_Type = TruthValue
_XpdrConnConfigCpriRateControl_Object = MibTableColumn
xpdrConnConfigCpriRateControl = _XpdrConnConfigCpriRateControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 11),
    _XpdrConnConfigCpriRateControl_Type()
)
xpdrConnConfigCpriRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnConfigCpriRateControl.setStatus("current")
_XpdrFaultPropagationDelay_Type = Integer32
_XpdrFaultPropagationDelay_Object = MibTableColumn
xpdrFaultPropagationDelay = _XpdrFaultPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 12),
    _XpdrFaultPropagationDelay_Type()
)
xpdrFaultPropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrFaultPropagationDelay.setStatus("current")
_XpdrFecMode_Type = Integer32
_XpdrFecMode_Object = MibTableColumn
xpdrFecMode = _XpdrFecMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 13),
    _XpdrFecMode_Type()
)
xpdrFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrFecMode.setStatus("current")
_XpdrConnAddMask1_Type = TsMaskBits
_XpdrConnAddMask1_Object = MibTableColumn
xpdrConnAddMask1 = _XpdrConnAddMask1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 14),
    _XpdrConnAddMask1_Type()
)
xpdrConnAddMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnAddMask1.setStatus("current")
_XpdrConnAddMask2_Type = TsMaskBits
_XpdrConnAddMask2_Object = MibTableColumn
xpdrConnAddMask2 = _XpdrConnAddMask2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 15),
    _XpdrConnAddMask2_Type()
)
xpdrConnAddMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnAddMask2.setStatus("current")
_XpdrCryptoUser_Type = DisplayString
_XpdrCryptoUser_Object = MibTableColumn
xpdrCryptoUser = _XpdrCryptoUser_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 16),
    _XpdrCryptoUser_Type()
)
xpdrCryptoUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrCryptoUser.setStatus("current")
_OduXcConnConfigTable_Object = MibTable
oduXcConnConfigTable = _OduXcConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    oduXcConnConfigTable.setStatus("current")
_OduXcConnConfigEntry_Object = MibTableRow
oduXcConnConfigEntry = _OduXcConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1)
)
oduXcConnConfigEntry.setIndexNames(
    (0, "SL-XPDR-MIB", "oduXcConnConfigP1"),
    (0, "SL-XPDR-MIB", "oduXcConnConfigP2"),
)
if mibBuilder.loadTexts:
    oduXcConnConfigEntry.setStatus("current")
_OduXcConnConfigP1_Type = Integer32
_OduXcConnConfigP1_Object = MibTableColumn
oduXcConnConfigP1 = _OduXcConnConfigP1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 1),
    _OduXcConnConfigP1_Type()
)
oduXcConnConfigP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigP1.setStatus("current")
_OduXcConnConfigP2_Type = Integer32
_OduXcConnConfigP2_Object = MibTableColumn
oduXcConnConfigP2 = _OduXcConnConfigP2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 2),
    _OduXcConnConfigP2_Type()
)
oduXcConnConfigP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigP2.setStatus("current")
_OduXcConnConfigProtected_Type = TruthValue
_OduXcConnConfigProtected_Object = MibTableColumn
oduXcConnConfigProtected = _OduXcConnConfigProtected_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 3),
    _OduXcConnConfigProtected_Type()
)
oduXcConnConfigProtected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigProtected.setStatus("current")
_OduXcConnConfigRowStatus_Type = RowStatus
_OduXcConnConfigRowStatus_Object = MibTableColumn
oduXcConnConfigRowStatus = _OduXcConnConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 4),
    _OduXcConnConfigRowStatus_Type()
)
oduXcConnConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigRowStatus.setStatus("current")
_TribXcConnConfigTable_Object = MibTable
tribXcConnConfigTable = _TribXcConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    tribXcConnConfigTable.setStatus("current")
_TribXcConnConfigEntry_Object = MibTableRow
tribXcConnConfigEntry = _TribXcConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1)
)
tribXcConnConfigEntry.setIndexNames(
    (0, "SL-XPDR-MIB", "tribXcConnConfigP1"),
    (0, "SL-XPDR-MIB", "tribXcConnConfigP2"),
)
if mibBuilder.loadTexts:
    tribXcConnConfigEntry.setStatus("current")
_TribXcConnConfigP1_Type = Integer32
_TribXcConnConfigP1_Object = MibTableColumn
tribXcConnConfigP1 = _TribXcConnConfigP1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 1),
    _TribXcConnConfigP1_Type()
)
tribXcConnConfigP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tribXcConnConfigP1.setStatus("current")
_TribXcConnConfigP2_Type = Integer32
_TribXcConnConfigP2_Object = MibTableColumn
tribXcConnConfigP2 = _TribXcConnConfigP2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 2),
    _TribXcConnConfigP2_Type()
)
tribXcConnConfigP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tribXcConnConfigP2.setStatus("current")
_TribXcConnServiceType_Type = XpdrServiceType
_TribXcConnServiceType_Object = MibTableColumn
tribXcConnServiceType = _TribXcConnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 3),
    _TribXcConnServiceType_Type()
)
tribXcConnServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribXcConnServiceType.setStatus("current")
_TribXcConnMask1_Type = TsMaskBits
_TribXcConnMask1_Object = MibTableColumn
tribXcConnMask1 = _TribXcConnMask1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 4),
    _TribXcConnMask1_Type()
)
tribXcConnMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribXcConnMask1.setStatus("current")
_TribXcConnMask2_Type = TsMaskBits
_TribXcConnMask2_Object = MibTableColumn
tribXcConnMask2 = _TribXcConnMask2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 5),
    _TribXcConnMask2_Type()
)
tribXcConnMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribXcConnMask2.setStatus("current")
_TribXcConnConfigProtected_Type = TruthValue
_TribXcConnConfigProtected_Object = MibTableColumn
tribXcConnConfigProtected = _TribXcConnConfigProtected_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 6),
    _TribXcConnConfigProtected_Type()
)
tribXcConnConfigProtected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tribXcConnConfigProtected.setStatus("current")
_TribXcConnConfigRowStatus_Type = RowStatus
_TribXcConnConfigRowStatus_Object = MibTableColumn
tribXcConnConfigRowStatus = _TribXcConnConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 7),
    _TribXcConnConfigRowStatus_Type()
)
tribXcConnConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tribXcConnConfigRowStatus.setStatus("current")


class _SmmOwnerMode_Type(Integer32):
    """Custom type smmOwnerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gui", 1),
          ("ems", 2))
    )


_SmmOwnerMode_Type.__name__ = "Integer32"
_SmmOwnerMode_Object = MibScalar
smmOwnerMode = _SmmOwnerMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 4),
    _SmmOwnerMode_Type()
)
smmOwnerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smmOwnerMode.setStatus("current")
_SlXpdrLastChange_ObjectIdentity = ObjectIdentity
slXpdrLastChange = _SlXpdrLastChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 6)
)
_SlXpdrTraps_ObjectIdentity = ObjectIdentity
slXpdrTraps = _SlXpdrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7)
)
_SlXpdrTraps0_ObjectIdentity = ObjectIdentity
slXpdrTraps0 = _SlXpdrTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0)
)

# Managed Objects groups


# Notification objects

xpdrConnConfigTableChange0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0, 1)
)
if mibBuilder.loadTexts:
    xpdrConnConfigTableChange0.setStatus(
        "current"
    )

xpdrConnConfigTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 1)
)
if mibBuilder.loadTexts:
    xpdrConnConfigTableChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-XPDR-MIB",
    **{"TsMaskBits": TsMaskBits,
       "XpdrServiceType": XpdrServiceType,
       "slXpdr": slXpdr,
       "slXpdrConn": slXpdrConn,
       "xpdrConnConfigTable": xpdrConnConfigTable,
       "xpdrConnConfigEntry": xpdrConnConfigEntry,
       "xpdrConnConfigIf1": xpdrConnConfigIf1,
       "xpdrConnConfigIf2": xpdrConnConfigIf2,
       "xpdrConnConfigRateControlAdmin": xpdrConnConfigRateControlAdmin,
       "xpdrConnConfigRateControlOper": xpdrConnConfigRateControlOper,
       "xpdrConnConfigLosPropagation": xpdrConnConfigLosPropagation,
       "xpdrServiceType": xpdrServiceType,
       "xpdrConnAddMask": xpdrConnAddMask,
       "xpdrMuxInbandAdmin": xpdrMuxInbandAdmin,
       "xpdrMuxInbandOper": xpdrMuxInbandOper,
       "xpdrDirection": xpdrDirection,
       "xpdrConnConfigCpriRateControl": xpdrConnConfigCpriRateControl,
       "xpdrFaultPropagationDelay": xpdrFaultPropagationDelay,
       "xpdrFecMode": xpdrFecMode,
       "xpdrConnAddMask1": xpdrConnAddMask1,
       "xpdrConnAddMask2": xpdrConnAddMask2,
       "xpdrCryptoUser": xpdrCryptoUser,
       "oduXcConnConfigTable": oduXcConnConfigTable,
       "oduXcConnConfigEntry": oduXcConnConfigEntry,
       "oduXcConnConfigP1": oduXcConnConfigP1,
       "oduXcConnConfigP2": oduXcConnConfigP2,
       "oduXcConnConfigProtected": oduXcConnConfigProtected,
       "oduXcConnConfigRowStatus": oduXcConnConfigRowStatus,
       "tribXcConnConfigTable": tribXcConnConfigTable,
       "tribXcConnConfigEntry": tribXcConnConfigEntry,
       "tribXcConnConfigP1": tribXcConnConfigP1,
       "tribXcConnConfigP2": tribXcConnConfigP2,
       "tribXcConnServiceType": tribXcConnServiceType,
       "tribXcConnMask1": tribXcConnMask1,
       "tribXcConnMask2": tribXcConnMask2,
       "tribXcConnConfigProtected": tribXcConnConfigProtected,
       "tribXcConnConfigRowStatus": tribXcConnConfigRowStatus,
       "smmOwnerMode": smmOwnerMode,
       "slXpdrLastChange": slXpdrLastChange,
       "slXpdrTraps": slXpdrTraps,
       "slXpdrTraps0": slXpdrTraps0,
       "xpdrConnConfigTableChange0": xpdrConnConfigTableChange0,
       "xpdrConnConfigTableChange": xpdrConnConfigTableChange}
)
