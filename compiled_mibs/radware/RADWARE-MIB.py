# SNMP MIB module (RADWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radware\RADWARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:51 2025
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )





class FeatureStatus(Integer32):
    """Custom type FeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class BitFlag(Integer32):
    """Custom type BitFlag based on Integer32"""




class VrId(Integer32):
    """Custom type VrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )





class RouteTag(OctetString):
    """Custom type RouteTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2





class RsIfType(Integer32):
    """Custom type RsIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(23,
              32,
              500,
              1000,
              1001,
              1002,
              1003,
              1010,
              1011,
              1100)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 23),
          ("frameRelay", 32),
          ("virtualNet", 500),
          ("rndWan", 1000),
          ("cod", 1001),
          ("backup", 1002),
          ("fr1490", 1003),
          ("b1isdn", 1010),
          ("b2isdn", 1011),
          ("unknown", 1100))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rnd_ObjectIdentity = ObjectIdentity
rnd = _Rnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89)
)
_RndMng_ObjectIdentity = ObjectIdentity
rndMng = _RndMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 1)
)


class _RndSysId_Type(Integer32):
    """Custom type rndSysId based on Integer32"""
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
              62)
        )
    )
    namedValues = NamedValues(
        *(("reb", 1),
          ("ceb", 2),
          ("ceblb", 3),
          ("xeb", 4),
          ("xeb1", 5),
          ("rebsx", 6),
          ("rtb", 7),
          ("ltb", 8),
          ("lte", 9),
          ("iprouter", 10),
          ("ielb", 11),
          ("leb", 12),
          ("openGate12", 13),
          ("openGate4", 14),
          ("ran", 15),
          ("itlb", 16),
          ("gatelinx", 17),
          ("openGate2", 18),
          ("ogRanTR", 19),
          ("stc", 20),
          ("ftc", 21),
          ("armon", 22),
          ("fccs1004", 23),
          ("fccs1012", 24),
          ("rdapter", 25),
          ("ogvan", 26),
          ("wanGate", 27),
          ("ogRubE", 28),
          ("ogRubT", 29),
          ("elX", 30),
          ("vGate4", 31),
          ("mrt", 32),
          ("ogSrubET", 33),
          ("vanXS", 34),
          ("lre", 35),
          ("vGate2", 36),
          ("serverDispatcher4", 37),
          ("serverDispatcher2", 38),
          ("vGate2Fast", 39),
          ("serverDispatcher2Fast", 40),
          ("prt", 41),
          ("mlm", 42),
          ("prt11", 43),
          ("quickOffice", 44),
          ("apollo", 45),
          ("radware", 62))
    )


_RndSysId_Type.__name__ = "Integer32"
_RndSysId_Object = MibScalar
rndSysId = _RndSysId_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 1),
    _RndSysId_Type()
)
rndSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndSysId.setStatus("mandatory")


class _RndAction_Type(Integer32):
    """Custom type rndAction based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("sendNetworkTab", 2),
          ("deleteNetworkTab", 3),
          ("sendRoutingTab", 4),
          ("deleteRoutingTab", 5),
          ("sendLanTab", 6),
          ("deleteLanTab", 7),
          ("deleteArpTab", 8),
          ("sendArpTab", 9),
          ("deleteRouteTab", 10),
          ("sendRouteTab", 11),
          ("backupSPFRoutingTab", 12),
          ("backupIPRoutingTab", 13),
          ("backupNetworkTab", 14),
          ("backupLanTab", 15),
          ("backupArpTab", 16),
          ("backupIPXRipTab", 17),
          ("backupIPXSAPTab", 18),
          ("resetCDB", 19),
          ("eraseCDB", 20),
          ("deleteZeroHopRoutingAllocTab", 21),
          ("shutdown", 22))
    )


_RndAction_Type.__name__ = "Integer32"
_RndAction_Object = MibScalar
rndAction = _RndAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 2),
    _RndAction_Type()
)
rndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAction.setStatus("mandatory")
_RndFileName_Type = OctetString
_RndFileName_Object = MibScalar
rndFileName = _RndFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 3),
    _RndFileName_Type()
)
rndFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFileName.setStatus("mandatory")


class _RemoveViewTablePermissionReductionCheck_Type(Integer32):
    """Custom type removeViewTablePermissionReductionCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoveViewTablePermissionReductionCheck_Type.__name__ = "Integer32"
_RemoveViewTablePermissionReductionCheck_Object = MibScalar
removeViewTablePermissionReductionCheck = _RemoveViewTablePermissionReductionCheck_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 4),
    _RemoveViewTablePermissionReductionCheck_Type()
)
removeViewTablePermissionReductionCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removeViewTablePermissionReductionCheck.setStatus("mandatory")


class _RsConfigurationAuditStatus_Type(Integer32):
    """Custom type rsConfigurationAuditStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsConfigurationAuditStatus_Type.__name__ = "Integer32"
_RsConfigurationAuditStatus_Object = MibScalar
rsConfigurationAuditStatus = _RsConfigurationAuditStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 5),
    _RsConfigurationAuditStatus_Type()
)
rsConfigurationAuditStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsConfigurationAuditStatus.setStatus("mandatory")


class _RdwrPrintToLogAndCli_Type(DisplayString):
    """Custom type rdwrPrintToLogAndCli based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_RdwrPrintToLogAndCli_Type.__name__ = "DisplayString"
_RdwrPrintToLogAndCli_Object = MibScalar
rdwrPrintToLogAndCli = _RdwrPrintToLogAndCli_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 6),
    _RdwrPrintToLogAndCli_Type()
)
rdwrPrintToLogAndCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrPrintToLogAndCli.setStatus("mandatory")


class _RdwrClearTheLogFile_Type(Integer32):
    """Custom type rdwrClearTheLogFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSysLog", 1)
    )


_RdwrClearTheLogFile_Type.__name__ = "Integer32"
_RdwrClearTheLogFile_Object = MibScalar
rdwrClearTheLogFile = _RdwrClearTheLogFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 7),
    _RdwrClearTheLogFile_Type()
)
rdwrClearTheLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClearTheLogFile.setStatus("mandatory")


class _RdwrAutoRowGenerationStatus_Type(Integer32):
    """Custom type rdwrAutoRowGenerationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RdwrAutoRowGenerationStatus_Type.__name__ = "Integer32"
_RdwrAutoRowGenerationStatus_Object = MibScalar
rdwrAutoRowGenerationStatus = _RdwrAutoRowGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 8),
    _RdwrAutoRowGenerationStatus_Type()
)
rdwrAutoRowGenerationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrAutoRowGenerationStatus.setStatus("mandatory")


class _RsConfigurationAuditingType_Type(Integer32):
    """Custom type rsConfigurationAuditingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("extended", 2))
    )


_RsConfigurationAuditingType_Type.__name__ = "Integer32"
_RsConfigurationAuditingType_Object = MibScalar
rsConfigurationAuditingType = _RsConfigurationAuditingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 9),
    _RsConfigurationAuditingType_Type()
)
rsConfigurationAuditingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsConfigurationAuditingType.setStatus("mandatory")
_RndDeviceParams_ObjectIdentity = ObjectIdentity
rndDeviceParams = _RndDeviceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2)
)


class _RndBridgeType_Type(Integer32):
    """Custom type rndBridgeType based on Integer32"""
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
              48)
        )
    )
    namedValues = NamedValues(
        *(("reb", 1),
          ("ceb", 2),
          ("ceblb", 3),
          ("xeb", 4),
          ("xeb1", 5),
          ("rebsx", 6),
          ("rtb", 7),
          ("ltb", 8),
          ("tre", 9),
          ("rtre", 10),
          ("xtb", 11),
          ("ete", 12),
          ("rete", 13),
          ("ielb", 30),
          ("leb", 31),
          ("openGate12", 32),
          ("openGate4", 33),
          ("ran", 34),
          ("itlb", 35),
          ("gatelinx", 36),
          ("openGate2", 37),
          ("ogRanTR", 38),
          ("rdapter", 39),
          ("ogVan", 40),
          ("wanGate", 41),
          ("ogRubE", 42),
          ("ogRubT", 43),
          ("wanGateI", 44),
          ("vGate4", 45),
          ("lre", 46),
          ("mrt", 47),
          ("vGate2", 48))
    )


_RndBridgeType_Type.__name__ = "Integer32"
_RndBridgeType_Object = MibScalar
rndBridgeType = _RndBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 1),
    _RndBridgeType_Type()
)
rndBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBridgeType.setStatus("mandatory")
_RndInactiveArpTimeOut_Type = Integer32
_RndInactiveArpTimeOut_Object = MibScalar
rndInactiveArpTimeOut = _RndInactiveArpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 2),
    _RndInactiveArpTimeOut_Type()
)
rndInactiveArpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndInactiveArpTimeOut.setStatus("mandatory")
_RndBridgeAlarm_ObjectIdentity = ObjectIdentity
rndBridgeAlarm = _RndBridgeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 3)
)
_RndErrorDesc_Type = DisplayString
_RndErrorDesc_Object = MibScalar
rndErrorDesc = _RndErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 1),
    _RndErrorDesc_Type()
)
rndErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorDesc.setStatus("mandatory")
_RndErrorSeverity_Type = Integer32
_RndErrorSeverity_Object = MibScalar
rndErrorSeverity = _RndErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 2),
    _RndErrorSeverity_Type()
)
rndErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorSeverity.setStatus("mandatory")
_RndBrgVersion_Type = DisplayString
_RndBrgVersion_Object = MibScalar
rndBrgVersion = _RndBrgVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 4),
    _RndBrgVersion_Type()
)
rndBrgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBrgVersion.setStatus("mandatory")
_RndBrgFeatures_Type = OctetString
_RndBrgFeatures_Object = MibScalar
rndBrgFeatures = _RndBrgFeatures_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 5),
    _RndBrgFeatures_Type()
)
rndBrgFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgFeatures.setStatus("mandatory")
_RndBrgLicense_Type = OctetString
_RndBrgLicense_Object = MibScalar
rndBrgLicense = _RndBrgLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 6),
    _RndBrgLicense_Type()
)
rndBrgLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBrgLicense.setStatus("mandatory")
_RndIpHost_ObjectIdentity = ObjectIdentity
rndIpHost = _RndIpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 7)
)


class _RndICMPTransmitionEnable_Type(Integer32):
    """Custom type rndICMPTransmitionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RndICMPTransmitionEnable_Type.__name__ = "Integer32"
_RndICMPTransmitionEnable_Object = MibScalar
rndICMPTransmitionEnable = _RndICMPTransmitionEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 1),
    _RndICMPTransmitionEnable_Type()
)
rndICMPTransmitionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndICMPTransmitionEnable.setStatus("mandatory")
_RndCommunityTable_Object = MibTable
rndCommunityTable = _RndCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2)
)
if mibBuilder.loadTexts:
    rndCommunityTable.setStatus("mandatory")
_RndCommunityEntry_Object = MibTableRow
rndCommunityEntry = _RndCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1)
)
rndCommunityEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndCommunityMngStationAddr"),
    (1, "RADWARE-MIB", "rndCommunityString"),
)
if mibBuilder.loadTexts:
    rndCommunityEntry.setStatus("mandatory")
_RndCommunityMngStationAddr_Type = IpAddress
_RndCommunityMngStationAddr_Object = MibTableColumn
rndCommunityMngStationAddr = _RndCommunityMngStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 1),
    _RndCommunityMngStationAddr_Type()
)
rndCommunityMngStationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityMngStationAddr.setStatus("mandatory")


class _RndCommunityString_Type(DisplayString):
    """Custom type rndCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndCommunityString_Type.__name__ = "DisplayString"
_RndCommunityString_Object = MibTableColumn
rndCommunityString = _RndCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 2),
    _RndCommunityString_Type()
)
rndCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityString.setStatus("mandatory")


class _RndCommunityAccess_Type(Integer32):
    """Custom type rndCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("super", 3))
    )


_RndCommunityAccess_Type.__name__ = "Integer32"
_RndCommunityAccess_Object = MibTableColumn
rndCommunityAccess = _RndCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 3),
    _RndCommunityAccess_Type()
)
rndCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityAccess.setStatus("mandatory")


class _RndCommunityTrapsEnable_Type(Integer32):
    """Custom type rndCommunityTrapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapsEnable", 1),
          ("trapsDisable", 2))
    )


_RndCommunityTrapsEnable_Type.__name__ = "Integer32"
_RndCommunityTrapsEnable_Object = MibTableColumn
rndCommunityTrapsEnable = _RndCommunityTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 4),
    _RndCommunityTrapsEnable_Type()
)
rndCommunityTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityTrapsEnable.setStatus("mandatory")


class _RndCommunityStatus_Type(Integer32):
    """Custom type rndCommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("invalid", 2))
    )


_RndCommunityStatus_Type.__name__ = "Integer32"
_RndCommunityStatus_Object = MibTableColumn
rndCommunityStatus = _RndCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 5),
    _RndCommunityStatus_Type()
)
rndCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityStatus.setStatus("mandatory")


class _RndManagedTime_Type(DisplayString):
    """Custom type rndManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RndManagedTime_Type.__name__ = "DisplayString"
_RndManagedTime_Object = MibScalar
rndManagedTime = _RndManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 8),
    _RndManagedTime_Type()
)
rndManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedTime.setStatus("mandatory")


class _RndManagedDate_Type(DisplayString):
    """Custom type rndManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 8),
    )


_RndManagedDate_Type.__name__ = "DisplayString"
_RndManagedDate_Object = MibScalar
rndManagedDate = _RndManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 9),
    _RndManagedDate_Type()
)
rndManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedDate.setStatus("mandatory")
_GenGroup_ObjectIdentity = ObjectIdentity
genGroup = _GenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 11)
)
_GenGroupHWVersion_Type = DisplayString
_GenGroupHWVersion_Object = MibScalar
genGroupHWVersion = _GenGroupHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 1),
    _GenGroupHWVersion_Type()
)
genGroupHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWVersion.setStatus("mandatory")


class _GenGroupConfigurationSymbol_Type(DisplayString):
    """Custom type genGroupConfigurationSymbol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_GenGroupConfigurationSymbol_Type.__name__ = "DisplayString"
_GenGroupConfigurationSymbol_Object = MibScalar
genGroupConfigurationSymbol = _GenGroupConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 2),
    _GenGroupConfigurationSymbol_Type()
)
genGroupConfigurationSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupConfigurationSymbol.setStatus("mandatory")


class _GenGroupHWStatus_Type(Integer32):
    """Custom type genGroupHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("hardwareProblems", 2),
          ("notSupported", 255))
    )


_GenGroupHWStatus_Type.__name__ = "Integer32"
_GenGroupHWStatus_Object = MibScalar
genGroupHWStatus = _GenGroupHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 3),
    _GenGroupHWStatus_Type()
)
genGroupHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWStatus.setStatus("mandatory")


class _RndSerialNumber_Type(DisplayString):
    """Custom type rndSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RndSerialNumber_Type.__name__ = "DisplayString"
_RndSerialNumber_Object = MibScalar
rndSerialNumber = _RndSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 12),
    _RndSerialNumber_Type()
)
rndSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSerialNumber.setStatus("mandatory")


class _RndApsoluteOSVersion_Type(DisplayString):
    """Custom type rndApsoluteOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RndApsoluteOSVersion_Type.__name__ = "DisplayString"
_RndApsoluteOSVersion_Object = MibScalar
rndApsoluteOSVersion = _RndApsoluteOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13),
    _RndApsoluteOSVersion_Type()
)
rndApsoluteOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndApsoluteOSVersion.setStatus("mandatory")


class _RdwrDeviceType_Type(DisplayString):
    """Custom type rdwrDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDeviceType_Type.__name__ = "DisplayString"
_RdwrDeviceType_Object = MibScalar
rdwrDeviceType = _RdwrDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 14),
    _RdwrDeviceType_Type()
)
rdwrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceType.setStatus("mandatory")
_RdwrDeviceNumberOfPorts_Type = Integer32
_RdwrDeviceNumberOfPorts_Object = MibScalar
rdwrDeviceNumberOfPorts = _RdwrDeviceNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 15),
    _RdwrDeviceNumberOfPorts_Type()
)
rdwrDeviceNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceNumberOfPorts.setStatus("mandatory")


class _RdwrDevicePortsConfig_Type(DisplayString):
    """Custom type rdwrDevicePortsConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDevicePortsConfig_Type.__name__ = "DisplayString"
_RdwrDevicePortsConfig_Object = MibScalar
rdwrDevicePortsConfig = _RdwrDevicePortsConfig_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16),
    _RdwrDevicePortsConfig_Type()
)
rdwrDevicePortsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDevicePortsConfig.setStatus("mandatory")


class _RdwrDeviceThroughput_Type(DisplayString):
    """Custom type rdwrDeviceThroughput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDeviceThroughput_Type.__name__ = "DisplayString"
_RdwrDeviceThroughput_Object = MibScalar
rdwrDeviceThroughput = _RdwrDeviceThroughput_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 17),
    _RdwrDeviceThroughput_Type()
)
rdwrDeviceThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceThroughput.setStatus("mandatory")


class _RdwrDeviceNetworkDriver_Type(DisplayString):
    """Custom type rdwrDeviceNetworkDriver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDeviceNetworkDriver_Type.__name__ = "DisplayString"
_RdwrDeviceNetworkDriver_Object = MibScalar
rdwrDeviceNetworkDriver = _RdwrDeviceNetworkDriver_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 18),
    _RdwrDeviceNetworkDriver_Type()
)
rdwrDeviceNetworkDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceNetworkDriver.setStatus("mandatory")
_RdwrDeviceCPUsNumber_Type = Integer32
_RdwrDeviceCPUsNumber_Object = MibScalar
rdwrDeviceCPUsNumber = _RdwrDeviceCPUsNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 19),
    _RdwrDeviceCPUsNumber_Type()
)
rdwrDeviceCPUsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceCPUsNumber.setStatus("mandatory")


class _RdwrDeviceActiveBoot_Type(DisplayString):
    """Custom type rdwrDeviceActiveBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDeviceActiveBoot_Type.__name__ = "DisplayString"
_RdwrDeviceActiveBoot_Object = MibScalar
rdwrDeviceActiveBoot = _RdwrDeviceActiveBoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 20),
    _RdwrDeviceActiveBoot_Type()
)
rdwrDeviceActiveBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceActiveBoot.setStatus("mandatory")


class _RdwrDeviceSecondaryBoot_Type(DisplayString):
    """Custom type rdwrDeviceSecondaryBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDeviceSecondaryBoot_Type.__name__ = "DisplayString"
_RdwrDeviceSecondaryBoot_Object = MibScalar
rdwrDeviceSecondaryBoot = _RdwrDeviceSecondaryBoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 21),
    _RdwrDeviceSecondaryBoot_Type()
)
rdwrDeviceSecondaryBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDeviceSecondaryBoot.setStatus("mandatory")
_RndInterface_ObjectIdentity = ObjectIdentity
rndInterface = _RndInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 4)
)
_RndIfTable_Object = MibTable
rndIfTable = _RndIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1)
)
if mibBuilder.loadTexts:
    rndIfTable.setStatus("mandatory")
_RndIfEntry_Object = MibTableRow
rndIfEntry = _RndIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1)
)
rndIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndIfIndex"),
)
if mibBuilder.loadTexts:
    rndIfEntry.setStatus("mandatory")
_RndIfIndex_Type = Integer32
_RndIfIndex_Object = MibTableColumn
rndIfIndex = _RndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 1),
    _RndIfIndex_Type()
)
rndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfIndex.setStatus("mandatory")
_RndIfBoardNum_Type = Integer32
_RndIfBoardNum_Object = MibTableColumn
rndIfBoardNum = _RndIfBoardNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 2),
    _RndIfBoardNum_Type()
)
rndIfBoardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfBoardNum.setStatus("mandatory")
_RndIfNetAddress_Type = IpAddress
_RndIfNetAddress_Object = MibTableColumn
rndIfNetAddress = _RndIfNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 3),
    _RndIfNetAddress_Type()
)
rndIfNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfNetAddress.setStatus("mandatory")


class _RndIfStatus_Type(Integer32):
    """Custom type rndIfStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("okSingleBrg", 2),
          ("okMultiBrg", 3),
          ("connctFault", 4),
          ("rxFault", 5),
          ("txFault", 6),
          ("channelLoopback", 7),
          ("rxClockFault", 8),
          ("t1Alarm", 9))
    )


_RndIfStatus_Type.__name__ = "Integer32"
_RndIfStatus_Object = MibTableColumn
rndIfStatus = _RndIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 4),
    _RndIfStatus_Type()
)
rndIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfStatus.setStatus("mandatory")


class _RndIfClockType_Type(Integer32):
    """Custom type rndIfClockType based on Integer32"""
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
        *(("external", 1),
          ("internal", 2),
          ("t1", 3),
          ("g703", 4))
    )


_RndIfClockType_Type.__name__ = "Integer32"
_RndIfClockType_Object = MibTableColumn
rndIfClockType = _RndIfClockType_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 5),
    _RndIfClockType_Type()
)
rndIfClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfClockType.setStatus("mandatory")
_RndIfBaudRate_Type = Integer32
_RndIfBaudRate_Object = MibTableColumn
rndIfBaudRate = _RndIfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 6),
    _RndIfBaudRate_Type()
)
rndIfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfBaudRate.setStatus("mandatory")
_RndIfCost_Type = Integer32
_RndIfCost_Object = MibTableColumn
rndIfCost = _RndIfCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 7),
    _RndIfCost_Type()
)
rndIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfCost.setStatus("mandatory")


class _RndIfCompression_Type(Integer32):
    """Custom type rndIfCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RndIfCompression_Type.__name__ = "Integer32"
_RndIfCompression_Object = MibTableColumn
rndIfCompression = _RndIfCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 8),
    _RndIfCompression_Type()
)
rndIfCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfCompression.setStatus("mandatory")


class _RndIfCompressionStatus_Type(Integer32):
    """Custom type rndIfCompressionStatus based on Integer32"""
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
        *(("not-inserted", 1),
          ("active", 2),
          ("not-active", 3),
          ("disable", 4))
    )


_RndIfCompressionStatus_Type.__name__ = "Integer32"
_RndIfCompressionStatus_Object = MibTableColumn
rndIfCompressionStatus = _RndIfCompressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 9),
    _RndIfCompressionStatus_Type()
)
rndIfCompressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfCompressionStatus.setStatus("mandatory")
_RndIfCompressionRate_Type = Integer32
_RndIfCompressionRate_Object = MibTableColumn
rndIfCompressionRate = _RndIfCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 10),
    _RndIfCompressionRate_Type()
)
rndIfCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfCompressionRate.setStatus("mandatory")


class _RndIfLATCompression_Type(Integer32):
    """Custom type rndIfLATCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RndIfLATCompression_Type.__name__ = "Integer32"
_RndIfLATCompression_Object = MibTableColumn
rndIfLATCompression = _RndIfLATCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 11),
    _RndIfLATCompression_Type()
)
rndIfLATCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfLATCompression.setStatus("mandatory")


class _RndIfCompressionType_Type(Integer32):
    """Custom type rndIfCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lowSpeed", 2),
          ("highSpeed", 3))
    )


_RndIfCompressionType_Type.__name__ = "Integer32"
_RndIfCompressionType_Object = MibTableColumn
rndIfCompressionType = _RndIfCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 12),
    _RndIfCompressionType_Type()
)
rndIfCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfCompressionType.setStatus("mandatory")


class _RndIfFilterMode_Type(Integer32):
    """Custom type rndIfFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destinationOnly", 1),
          ("sourceAndDestination", 2),
          ("none", 3))
    )


_RndIfFilterMode_Type.__name__ = "Integer32"
_RndIfFilterMode_Object = MibTableColumn
rndIfFilterMode = _RndIfFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 13),
    _RndIfFilterMode_Type()
)
rndIfFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfFilterMode.setStatus("mandatory")


class _RndIfChannelType_Type(Integer32):
    """Custom type rndIfChannelType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wanChannel", 1),
          ("ogRanPort", 2),
          ("routerToBridge", 3),
          ("spsFramRelay", 4),
          ("dialBackup", 5),
          ("snar", 6),
          ("lan", 7),
          ("spsX25", 8),
          ("frameRelay1490", 9),
          ("frameRelay1490CAR", 10),
          ("frameRelayCAR", 11),
          ("ppp", 12))
    )


_RndIfChannelType_Type.__name__ = "Integer32"
_RndIfChannelType_Object = MibTableColumn
rndIfChannelType = _RndIfChannelType_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 14),
    _RndIfChannelType_Type()
)
rndIfChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfChannelType.setStatus("mandatory")


class _RndIfBridge_Type(Integer32):
    """Custom type rndIfBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RndIfBridge_Type.__name__ = "Integer32"
_RndIfBridge_Object = MibTableColumn
rndIfBridge = _RndIfBridge_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 15),
    _RndIfBridge_Type()
)
rndIfBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfBridge.setStatus("mandatory")


class _RndHighPriorityIf_Type(Integer32):
    """Custom type rndHighPriorityIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RndHighPriorityIf_Type.__name__ = "Integer32"
_RndHighPriorityIf_Object = MibTableColumn
rndHighPriorityIf = _RndHighPriorityIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 16),
    _RndHighPriorityIf_Type()
)
rndHighPriorityIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndHighPriorityIf.setStatus("mandatory")


class _RndWanHeader_Type(Integer32):
    """Custom type rndWanHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("short", 2))
    )


_RndWanHeader_Type.__name__ = "Integer32"
_RndWanHeader_Object = MibTableColumn
rndWanHeader = _RndWanHeader_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 17),
    _RndWanHeader_Type()
)
rndWanHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndWanHeader.setStatus("mandatory")


class _RndDuplexMode_Type(Integer32):
    """Custom type rndDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_RndDuplexMode_Type.__name__ = "Integer32"
_RndDuplexMode_Object = MibTableColumn
rndDuplexMode = _RndDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 18),
    _RndDuplexMode_Type()
)
rndDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDuplexMode.setStatus("mandatory")
_RndIPX_ObjectIdentity = ObjectIdentity
rndIPX = _RndIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12)
)
_RndFACS_ObjectIdentity = ObjectIdentity
rndFACS = _RndFACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 16)
)


class _RndFACSDefaultAction_Type(Integer32):
    """Custom type rndFACSDefaultAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              129)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("enable", 3),
          ("disable", 4),
          ("blockAndReport", 129))
    )


_RndFACSDefaultAction_Type.__name__ = "Integer32"
_RndFACSDefaultAction_Object = MibScalar
rndFACSDefaultAction = _RndFACSDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 1),
    _RndFACSDefaultAction_Type()
)
rndFACSDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSDefaultAction.setStatus("mandatory")
_RndFACSActTable_Object = MibTable
rndFACSActTable = _RndFACSActTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2)
)
if mibBuilder.loadTexts:
    rndFACSActTable.setStatus("mandatory")
_RndFACSActEntry_Object = MibTableRow
rndFACSActEntry = _RndFACSActEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1)
)
rndFACSActEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndFACSActType"),
    (0, "RADWARE-MIB", "rndFACSActIfIndex"),
)
if mibBuilder.loadTexts:
    rndFACSActEntry.setStatus("mandatory")


class _RndFACSActType_Type(Integer32):
    """Custom type rndFACSActType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2),
          ("activeDB", 4),
          ("tempDB", 5))
    )


_RndFACSActType_Type.__name__ = "Integer32"
_RndFACSActType_Object = MibTableColumn
rndFACSActType = _RndFACSActType_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1, 1),
    _RndFACSActType_Type()
)
rndFACSActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSActType.setStatus("mandatory")
_RndFACSActIfIndex_Type = Integer32
_RndFACSActIfIndex_Object = MibTableColumn
rndFACSActIfIndex = _RndFACSActIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1, 2),
    _RndFACSActIfIndex_Type()
)
rndFACSActIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSActIfIndex.setStatus("mandatory")


class _RndFACSAction_Type(Integer32):
    """Custom type rndFACSAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eraseIP", 2),
          ("eraseDECnet", 3),
          ("eraseIPX", 4),
          ("eraseBrg", 5),
          ("replaceIP", 6),
          ("replaceIPX", 8),
          ("replaceBrg", 9),
          ("backupIP", 10),
          ("backupIPX", 12),
          ("backupBrg", 13))
    )


_RndFACSAction_Type.__name__ = "Integer32"
_RndFACSAction_Object = MibTableColumn
rndFACSAction = _RndFACSAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1, 3),
    _RndFACSAction_Type()
)
rndFACSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSAction.setStatus("mandatory")
_RndFACSTable_Object = MibTable
rndFACSTable = _RndFACSTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3)
)
if mibBuilder.loadTexts:
    rndFACSTable.setStatus("mandatory")
_RndFACSEntry_Object = MibTableRow
rndFACSEntry = _RndFACSEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1)
)
rndFACSEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndFACSIfIndex"),
    (0, "RADWARE-MIB", "rndFACSProtocolType"),
    (0, "RADWARE-MIB", "rndFACSType"),
    (0, "RADWARE-MIB", "rndFACSIndex"),
)
if mibBuilder.loadTexts:
    rndFACSEntry.setStatus("mandatory")
_RndFACSIfIndex_Type = Integer32
_RndFACSIfIndex_Object = MibTableColumn
rndFACSIfIndex = _RndFACSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 1),
    _RndFACSIfIndex_Type()
)
rndFACSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSIfIndex.setStatus("mandatory")


class _RndFACSProtocolType_Type(Integer32):
    """Custom type rndFACSProtocolType based on Integer32"""
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
        *(("ip", 1),
          ("ipx", 2),
          ("dec", 3),
          ("bridge", 4))
    )


_RndFACSProtocolType_Type.__name__ = "Integer32"
_RndFACSProtocolType_Object = MibTableColumn
rndFACSProtocolType = _RndFACSProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 2),
    _RndFACSProtocolType_Type()
)
rndFACSProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSProtocolType.setStatus("mandatory")


class _RndFACSType_Type(Integer32):
    """Custom type rndFACSType based on Integer32"""
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
        *(("tx", 1),
          ("rx", 2),
          ("cod", 3),
          ("activeDB", 4),
          ("tempDB", 5))
    )


_RndFACSType_Type.__name__ = "Integer32"
_RndFACSType_Object = MibTableColumn
rndFACSType = _RndFACSType_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 3),
    _RndFACSType_Type()
)
rndFACSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSType.setStatus("mandatory")
_RndFACSIndex_Type = Integer32
_RndFACSIndex_Object = MibTableColumn
rndFACSIndex = _RndFACSIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 4),
    _RndFACSIndex_Type()
)
rndFACSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSIndex.setStatus("mandatory")
_RndFACSSrcAdd_Type = OctetString
_RndFACSSrcAdd_Object = MibTableColumn
rndFACSSrcAdd = _RndFACSSrcAdd_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 5),
    _RndFACSSrcAdd_Type()
)
rndFACSSrcAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSSrcAdd.setStatus("mandatory")
_RndFACSSrcAddMask_Type = OctetString
_RndFACSSrcAddMask_Object = MibTableColumn
rndFACSSrcAddMask = _RndFACSSrcAddMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 6),
    _RndFACSSrcAddMask_Type()
)
rndFACSSrcAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSSrcAddMask.setStatus("mandatory")
_RndFACSDesAdd_Type = OctetString
_RndFACSDesAdd_Object = MibTableColumn
rndFACSDesAdd = _RndFACSDesAdd_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 7),
    _RndFACSDesAdd_Type()
)
rndFACSDesAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSDesAdd.setStatus("mandatory")
_RndFACSDesAddMask_Type = OctetString
_RndFACSDesAddMask_Object = MibTableColumn
rndFACSDesAddMask = _RndFACSDesAddMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 8),
    _RndFACSDesAddMask_Type()
)
rndFACSDesAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSDesAddMask.setStatus("mandatory")


class _RndFACSOperation_Type(Integer32):
    """Custom type rndFACSOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              129)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("permit", 3),
          ("deny", 4),
          ("blockZHRP", 5),
          ("blockAndReport", 129))
    )


_RndFACSOperation_Type.__name__ = "Integer32"
_RndFACSOperation_Object = MibTableColumn
rndFACSOperation = _RndFACSOperation_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 9),
    _RndFACSOperation_Type()
)
rndFACSOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSOperation.setStatus("mandatory")


class _RndFACSNetFiltering_Type(Integer32):
    """Custom type rndFACSNetFiltering based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("l2multicast", 2),
          ("arp", 3),
          ("icmp", 4),
          ("ip", 5),
          ("udp", 6),
          ("tcp", 7),
          ("decnet", 8),
          ("ipx", 9))
    )


_RndFACSNetFiltering_Type.__name__ = "Integer32"
_RndFACSNetFiltering_Object = MibTableColumn
rndFACSNetFiltering = _RndFACSNetFiltering_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 10),
    _RndFACSNetFiltering_Type()
)
rndFACSNetFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSNetFiltering.setStatus("mandatory")
_RndFACSSoketNum_Type = Integer32
_RndFACSSoketNum_Object = MibTableColumn
rndFACSSoketNum = _RndFACSSoketNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 11),
    _RndFACSSoketNum_Type()
)
rndFACSSoketNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSSoketNum.setStatus("mandatory")
_RndFACSMask1Id_Type = Integer32
_RndFACSMask1Id_Object = MibTableColumn
rndFACSMask1Id = _RndFACSMask1Id_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 12),
    _RndFACSMask1Id_Type()
)
rndFACSMask1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSMask1Id.setStatus("mandatory")
_RndFACSMask2Id_Type = Integer32
_RndFACSMask2Id_Object = MibTableColumn
rndFACSMask2Id = _RndFACSMask2Id_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 13),
    _RndFACSMask2Id_Type()
)
rndFACSMask2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSMask2Id.setStatus("mandatory")


class _RndFACSStatus_Type(Integer32):
    """Custom type rndFACSStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RndFACSStatus_Type.__name__ = "Integer32"
_RndFACSStatus_Object = MibTableColumn
rndFACSStatus = _RndFACSStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 14),
    _RndFACSStatus_Type()
)
rndFACSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSStatus.setStatus("mandatory")
_RndBootP_ObjectIdentity = ObjectIdentity
rndBootP = _RndBootP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 24)
)


class _RndBootPServerAddress_Type(IpAddress):
    """Custom type rndBootPServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_RndBootPServerAddress_Type.__name__ = "IpAddress"
_RndBootPServerAddress_Object = MibScalar
rndBootPServerAddress = _RndBootPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 24, 1),
    _RndBootPServerAddress_Type()
)
rndBootPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPServerAddress.setStatus("mandatory")
_RndBootPRelaySecThreshold_Type = Integer32
_RndBootPRelaySecThreshold_Object = MibScalar
rndBootPRelaySecThreshold = _RndBootPRelaySecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 24, 2),
    _RndBootPRelaySecThreshold_Type()
)
rndBootPRelaySecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPRelaySecThreshold.setStatus("mandatory")
_IpSpec_ObjectIdentity = ObjectIdentity
ipSpec = _IpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26)
)
_RsIpAddrTable_Object = MibTable
rsIpAddrTable = _RsIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1)
)
if mibBuilder.loadTexts:
    rsIpAddrTable.setStatus("mandatory")
_RsIpAddrEntry_Object = MibTableRow
rsIpAddrEntry = _RsIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1)
)
rsIpAddrEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    rsIpAddrEntry.setStatus("mandatory")
_RsIpAdEntAddr_Type = IpAddress
_RsIpAdEntAddr_Object = MibTableColumn
rsIpAdEntAddr = _RsIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 1),
    _RsIpAdEntAddr_Type()
)
rsIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntAddr.setStatus("mandatory")
_RsIpAdEntIfIndex_Type = Integer32
_RsIpAdEntIfIndex_Object = MibTableColumn
rsIpAdEntIfIndex = _RsIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 2),
    _RsIpAdEntIfIndex_Type()
)
rsIpAdEntIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntIfIndex.setStatus("mandatory")
_RsIpAdEntNetMask_Type = IpAddress
_RsIpAdEntNetMask_Object = MibTableColumn
rsIpAdEntNetMask = _RsIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 3),
    _RsIpAdEntNetMask_Type()
)
rsIpAdEntNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntNetMask.setStatus("mandatory")


class _RsIpAdEntForwardIpBroadcast_Type(Integer32):
    """Custom type rsIpAdEntForwardIpBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsIpAdEntForwardIpBroadcast_Type.__name__ = "Integer32"
_RsIpAdEntForwardIpBroadcast_Object = MibTableColumn
rsIpAdEntForwardIpBroadcast = _RsIpAdEntForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 4),
    _RsIpAdEntForwardIpBroadcast_Type()
)
rsIpAdEntForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntForwardIpBroadcast.setStatus("mandatory")


class _RsIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type rsIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_RsIpAdEntReasmMaxSize_Object = MibTableColumn
rsIpAdEntReasmMaxSize = _RsIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 5),
    _RsIpAdEntReasmMaxSize_Type()
)
rsIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntReasmMaxSize.setStatus("mandatory")


class _RsIpAdEntStatus_Type(Integer32):
    """Custom type rsIpAdEntStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RsIpAdEntStatus_Type.__name__ = "Integer32"
_RsIpAdEntStatus_Object = MibTableColumn
rsIpAdEntStatus = _RsIpAdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 6),
    _RsIpAdEntStatus_Type()
)
rsIpAdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntStatus.setStatus("mandatory")


class _RsIpAdEntBcastAddr_Type(Integer32):
    """Custom type rsIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RsIpAdEntBcastAddr_Type.__name__ = "Integer32"
_RsIpAdEntBcastAddr_Object = MibTableColumn
rsIpAdEntBcastAddr = _RsIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 7),
    _RsIpAdEntBcastAddr_Type()
)
rsIpAdEntBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntBcastAddr.setStatus("mandatory")
_RsIpAdEntVlanTag_Type = Integer32
_RsIpAdEntVlanTag_Object = MibTableColumn
rsIpAdEntVlanTag = _RsIpAdEntVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 8),
    _RsIpAdEntVlanTag_Type()
)
rsIpAdEntVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntVlanTag.setStatus("mandatory")


class _RsIpAdEntOneIpMode_Type(Integer32):
    """Custom type rsIpAdEntOneIpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsIpAdEntOneIpMode_Type.__name__ = "Integer32"
_RsIpAdEntOneIpMode_Object = MibTableColumn
rsIpAdEntOneIpMode = _RsIpAdEntOneIpMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 9),
    _RsIpAdEntOneIpMode_Type()
)
rsIpAdEntOneIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntOneIpMode.setStatus("mandatory")


class _RsIpAdEntType_Type(Integer32):
    """Custom type rsIpAdEntType based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("pppoe", 3),
          ("pptp", 4))
    )


_RsIpAdEntType_Type.__name__ = "Integer32"
_RsIpAdEntType_Object = MibTableColumn
rsIpAdEntType = _RsIpAdEntType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 10),
    _RsIpAdEntType_Type()
)
rsIpAdEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntType.setStatus("mandatory")
_RsIpAdEntPeerAddr_Type = IpAddress
_RsIpAdEntPeerAddr_Object = MibTableColumn
rsIpAdEntPeerAddr = _RsIpAdEntPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 11),
    _RsIpAdEntPeerAddr_Type()
)
rsIpAdEntPeerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntPeerAddr.setStatus("mandatory")


class _RsIpAdEntPeerAddrStatus_Type(Integer32):
    """Custom type rsIpAdEntPeerAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("relevant", 1),
          ("nonrelevant", 2))
    )


_RsIpAdEntPeerAddrStatus_Type.__name__ = "Integer32"
_RsIpAdEntPeerAddrStatus_Object = MibTableColumn
rsIpAdEntPeerAddrStatus = _RsIpAdEntPeerAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 12),
    _RsIpAdEntPeerAddrStatus_Type()
)
rsIpAdEntPeerAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntPeerAddrStatus.setStatus("mandatory")
_IcmpSpec_ObjectIdentity = ObjectIdentity
icmpSpec = _IcmpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 2)
)


class _RsIcmpGenErrMsgEnable_Type(Integer32):
    """Custom type rsIcmpGenErrMsgEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsIcmpGenErrMsgEnable_Type.__name__ = "Integer32"
_RsIcmpGenErrMsgEnable_Object = MibScalar
rsIcmpGenErrMsgEnable = _RsIcmpGenErrMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 1),
    _RsIcmpGenErrMsgEnable_Type()
)
rsIcmpGenErrMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpGenErrMsgEnable.setStatus("mandatory")
_RsIcmpRdTable_Object = MibTable
rsIcmpRdTable = _RsIcmpRdTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2)
)
if mibBuilder.loadTexts:
    rsIcmpRdTable.setStatus("mandatory")
_RsIcmpRdEntry_Object = MibTableRow
rsIcmpRdEntry = _RsIcmpRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1)
)
rsIcmpRdEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIcmpRdIpAddr"),
)
if mibBuilder.loadTexts:
    rsIcmpRdEntry.setStatus("mandatory")
_RsIcmpRdIpAddr_Type = IpAddress
_RsIcmpRdIpAddr_Object = MibTableColumn
rsIcmpRdIpAddr = _RsIcmpRdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 1),
    _RsIcmpRdIpAddr_Type()
)
rsIcmpRdIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIcmpRdIpAddr.setStatus("mandatory")


class _RsIcmpRdIpAdvertAddr_Type(IpAddress):
    """Custom type rsIcmpRdIpAdvertAddr based on IpAddress"""
    defaultHexValue = "E0000001"


_RsIcmpRdIpAdvertAddr_Type.__name__ = "IpAddress"
_RsIcmpRdIpAdvertAddr_Object = MibTableColumn
rsIcmpRdIpAdvertAddr = _RsIcmpRdIpAdvertAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 2),
    _RsIcmpRdIpAdvertAddr_Type()
)
rsIcmpRdIpAdvertAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdIpAdvertAddr.setStatus("mandatory")


class _RsIcmpRdMaxAdvertInterval_Type(Integer32):
    """Custom type rsIcmpRdMaxAdvertInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_RsIcmpRdMaxAdvertInterval_Type.__name__ = "Integer32"
_RsIcmpRdMaxAdvertInterval_Object = MibTableColumn
rsIcmpRdMaxAdvertInterval = _RsIcmpRdMaxAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 3),
    _RsIcmpRdMaxAdvertInterval_Type()
)
rsIcmpRdMaxAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdMaxAdvertInterval.setStatus("mandatory")


class _RsIcmpRdMinAdvertInterval_Type(Integer32):
    """Custom type rsIcmpRdMinAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_RsIcmpRdMinAdvertInterval_Type.__name__ = "Integer32"
_RsIcmpRdMinAdvertInterval_Object = MibTableColumn
rsIcmpRdMinAdvertInterval = _RsIcmpRdMinAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 4),
    _RsIcmpRdMinAdvertInterval_Type()
)
rsIcmpRdMinAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdMinAdvertInterval.setStatus("mandatory")


class _RsIcmpRdAdvertLifetime_Type(Integer32):
    """Custom type rsIcmpRdAdvertLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_RsIcmpRdAdvertLifetime_Type.__name__ = "Integer32"
_RsIcmpRdAdvertLifetime_Object = MibTableColumn
rsIcmpRdAdvertLifetime = _RsIcmpRdAdvertLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 5),
    _RsIcmpRdAdvertLifetime_Type()
)
rsIcmpRdAdvertLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdAdvertLifetime.setStatus("mandatory")


class _RsIcmpRdAdvertise_Type(Integer32):
    """Custom type rsIcmpRdAdvertise based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsIcmpRdAdvertise_Type.__name__ = "Integer32"
_RsIcmpRdAdvertise_Object = MibTableColumn
rsIcmpRdAdvertise = _RsIcmpRdAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 6),
    _RsIcmpRdAdvertise_Type()
)
rsIcmpRdAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdAdvertise.setStatus("mandatory")


class _RsIcmpRdPreferenceLevel_Type(Integer32):
    """Custom type rsIcmpRdPreferenceLevel based on Integer32"""
    defaultValue = 0


_RsIcmpRdPreferenceLevel_Type.__name__ = "Integer32"
_RsIcmpRdPreferenceLevel_Object = MibTableColumn
rsIcmpRdPreferenceLevel = _RsIcmpRdPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 7),
    _RsIcmpRdPreferenceLevel_Type()
)
rsIcmpRdPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdPreferenceLevel.setStatus("mandatory")
_RsIcmpRdEntStatus_Type = Integer32
_RsIcmpRdEntStatus_Object = MibTableColumn
rsIcmpRdEntStatus = _RsIcmpRdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 8),
    _RsIcmpRdEntStatus_Type()
)
rsIcmpRdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdEntStatus.setStatus("mandatory")
_Rip2Spec_ObjectIdentity = ObjectIdentity
rip2Spec = _Rip2Spec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 3)
)
_RsRip2IfConfTable_Object = MibTable
rsRip2IfConfTable = _RsRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1)
)
if mibBuilder.loadTexts:
    rsRip2IfConfTable.setStatus("mandatory")
_RsRip2IfConfEntry_Object = MibTableRow
rsRip2IfConfEntry = _RsRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1)
)
rsRip2IfConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    rsRip2IfConfEntry.setStatus("mandatory")
_RsRip2IfConfAddress_Type = IpAddress
_RsRip2IfConfAddress_Object = MibTableColumn
rsRip2IfConfAddress = _RsRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 1),
    _RsRip2IfConfAddress_Type()
)
rsRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRip2IfConfAddress.setStatus("mandatory")


class _RsRip2IfConfVirtualDis_Type(Integer32):
    """Custom type rsRip2IfConfVirtualDis based on Integer32"""
    defaultValue = 1


_RsRip2IfConfVirtualDis_Type.__name__ = "Integer32"
_RsRip2IfConfVirtualDis_Object = MibTableColumn
rsRip2IfConfVirtualDis = _RsRip2IfConfVirtualDis_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 2),
    _RsRip2IfConfVirtualDis_Type()
)
rsRip2IfConfVirtualDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRip2IfConfVirtualDis.setStatus("mandatory")


class _RsRip2IfConfAutoSend_Type(Integer32):
    """Custom type rsRip2IfConfAutoSend based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsRip2IfConfAutoSend_Type.__name__ = "Integer32"
_RsRip2IfConfAutoSend_Object = MibTableColumn
rsRip2IfConfAutoSend = _RsRip2IfConfAutoSend_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 3),
    _RsRip2IfConfAutoSend_Type()
)
rsRip2IfConfAutoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRip2IfConfAutoSend.setStatus("mandatory")
_RdwrRip2IfConfTable_Object = MibTable
rdwrRip2IfConfTable = _RdwrRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2)
)
if mibBuilder.loadTexts:
    rdwrRip2IfConfTable.setStatus("mandatory")
_RdwrRip2IfConfEntry_Object = MibTableRow
rdwrRip2IfConfEntry = _RdwrRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1)
)
rdwrRip2IfConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    rdwrRip2IfConfEntry.setStatus("mandatory")
_RdwrRip2IfConfAddress_Type = IpAddress
_RdwrRip2IfConfAddress_Object = MibTableColumn
rdwrRip2IfConfAddress = _RdwrRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 1),
    _RdwrRip2IfConfAddress_Type()
)
rdwrRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRip2IfConfAddress.setStatus("mandatory")
_RdwrRip2IfConfDomain_Type = RouteTag
_RdwrRip2IfConfDomain_Object = MibTableColumn
rdwrRip2IfConfDomain = _RdwrRip2IfConfDomain_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 2),
    _RdwrRip2IfConfDomain_Type()
)
rdwrRip2IfConfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfDomain.setStatus("deprecated")


class _RdwrRip2IfConfAuthType_Type(Integer32):
    """Custom type rdwrRip2IfConfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", 1),
          ("simplePassword", 2))
    )


_RdwrRip2IfConfAuthType_Type.__name__ = "Integer32"
_RdwrRip2IfConfAuthType_Object = MibTableColumn
rdwrRip2IfConfAuthType = _RdwrRip2IfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 3),
    _RdwrRip2IfConfAuthType_Type()
)
rdwrRip2IfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfAuthType.setStatus("mandatory")


class _RdwrRip2IfConfAuthKey_Type(OctetString):
    """Custom type rdwrRip2IfConfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RdwrRip2IfConfAuthKey_Type.__name__ = "OctetString"
_RdwrRip2IfConfAuthKey_Object = MibTableColumn
rdwrRip2IfConfAuthKey = _RdwrRip2IfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 4),
    _RdwrRip2IfConfAuthKey_Type()
)
rdwrRip2IfConfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfAuthKey.setStatus("mandatory")


class _RdwrRip2IfConfSend_Type(Integer32):
    """Custom type rdwrRip2IfConfSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("doNotSend", 1),
          ("ripVersion1", 2),
          ("rip1Compatible", 3),
          ("ripVersion2", 4),
          ("ripV1Demand", 5),
          ("ripV2Demand", 6))
    )


_RdwrRip2IfConfSend_Type.__name__ = "Integer32"
_RdwrRip2IfConfSend_Object = MibTableColumn
rdwrRip2IfConfSend = _RdwrRip2IfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 5),
    _RdwrRip2IfConfSend_Type()
)
rdwrRip2IfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfSend.setStatus("mandatory")


class _RdwrRip2IfConfReceive_Type(Integer32):
    """Custom type rdwrRip2IfConfReceive based on Integer32"""
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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3),
          ("doNotRecieve", 4))
    )


_RdwrRip2IfConfReceive_Type.__name__ = "Integer32"
_RdwrRip2IfConfReceive_Object = MibTableColumn
rdwrRip2IfConfReceive = _RdwrRip2IfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 6),
    _RdwrRip2IfConfReceive_Type()
)
rdwrRip2IfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfReceive.setStatus("mandatory")


class _RdwrRip2IfConfDefaultMetric_Type(Integer32):
    """Custom type rdwrRip2IfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RdwrRip2IfConfDefaultMetric_Type.__name__ = "Integer32"
_RdwrRip2IfConfDefaultMetric_Object = MibTableColumn
rdwrRip2IfConfDefaultMetric = _RdwrRip2IfConfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 7),
    _RdwrRip2IfConfDefaultMetric_Type()
)
rdwrRip2IfConfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfDefaultMetric.setStatus("mandatory")


class _RdwrRip2IfConfStatus_Type(Integer32):
    """Custom type rdwrRip2IfConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RdwrRip2IfConfStatus_Type.__name__ = "Integer32"
_RdwrRip2IfConfStatus_Object = MibTableColumn
rdwrRip2IfConfStatus = _RdwrRip2IfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 8),
    _RdwrRip2IfConfStatus_Type()
)
rdwrRip2IfConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfStatus.setStatus("mandatory")
_RdwrRip2IfConfSrcAddress_Type = IpAddress
_RdwrRip2IfConfSrcAddress_Object = MibTableColumn
rdwrRip2IfConfSrcAddress = _RdwrRip2IfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 9),
    _RdwrRip2IfConfSrcAddress_Type()
)
rdwrRip2IfConfSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfSrcAddress.setStatus("mandatory")


class _RdwrRip2IfConfVirtualDis_Type(Integer32):
    """Custom type rdwrRip2IfConfVirtualDis based on Integer32"""
    defaultValue = 1


_RdwrRip2IfConfVirtualDis_Type.__name__ = "Integer32"
_RdwrRip2IfConfVirtualDis_Object = MibTableColumn
rdwrRip2IfConfVirtualDis = _RdwrRip2IfConfVirtualDis_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 10),
    _RdwrRip2IfConfVirtualDis_Type()
)
rdwrRip2IfConfVirtualDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfVirtualDis.setStatus("mandatory")


class _RdwrRip2IfConfAutoSend_Type(Integer32):
    """Custom type rdwrRip2IfConfAutoSend based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RdwrRip2IfConfAutoSend_Type.__name__ = "Integer32"
_RdwrRip2IfConfAutoSend_Object = MibTableColumn
rdwrRip2IfConfAutoSend = _RdwrRip2IfConfAutoSend_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 2, 1, 11),
    _RdwrRip2IfConfAutoSend_Type()
)
rdwrRip2IfConfAutoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRip2IfConfAutoSend.setStatus("mandatory")
_ArpSpec_ObjectIdentity = ObjectIdentity
arpSpec = _ArpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 4)
)
_RsArpDeleteTable_Type = Integer32
_RsArpDeleteTable_Object = MibScalar
rsArpDeleteTable = _RsArpDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 1),
    _RsArpDeleteTable_Type()
)
rsArpDeleteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpDeleteTable.setStatus("mandatory")


class _RsArpInactiveTimeOut_Type(Integer32):
    """Custom type rsArpInactiveTimeOut based on Integer32"""
    defaultValue = 60000


_RsArpInactiveTimeOut_Type.__name__ = "Integer32"
_RsArpInactiveTimeOut_Object = MibScalar
rsArpInactiveTimeOut = _RsArpInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 2),
    _RsArpInactiveTimeOut_Type()
)
rsArpInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpInactiveTimeOut.setStatus("mandatory")


class _RsArpProxy_Type(Integer32):
    """Custom type rsArpProxy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsArpProxy_Type.__name__ = "Integer32"
_RsArpProxy_Object = MibScalar
rsArpProxy = _RsArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 3),
    _RsArpProxy_Type()
)
rsArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpProxy.setStatus("mandatory")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 5)
)


class _RsTftpRetryTimeOut_Type(Integer32):
    """Custom type rsTftpRetryTimeOut based on Integer32"""
    defaultValue = 15


_RsTftpRetryTimeOut_Type.__name__ = "Integer32"
_RsTftpRetryTimeOut_Object = MibScalar
rsTftpRetryTimeOut = _RsTftpRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 1),
    _RsTftpRetryTimeOut_Type()
)
rsTftpRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTftpRetryTimeOut.setStatus("mandatory")


class _RsTftpTotalTimeOut_Type(Integer32):
    """Custom type rsTftpTotalTimeOut based on Integer32"""
    defaultValue = 60


_RsTftpTotalTimeOut_Type.__name__ = "Integer32"
_RsTftpTotalTimeOut_Object = MibScalar
rsTftpTotalTimeOut = _RsTftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 2),
    _RsTftpTotalTimeOut_Type()
)
rsTftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTftpTotalTimeOut.setStatus("mandatory")
_RsSendConfigFile_Type = DisplayString
_RsSendConfigFile_Object = MibScalar
rsSendConfigFile = _RsSendConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 3),
    _RsSendConfigFile_Type()
)
rsSendConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSendConfigFile.setStatus("mandatory")
_RsGetConfigFile_Type = DisplayString
_RsGetConfigFile_Object = MibScalar
rsGetConfigFile = _RsGetConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 4),
    _RsGetConfigFile_Type()
)
rsGetConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigFile.setStatus("mandatory")
_RsLoadSoftware_Type = DisplayString
_RsLoadSoftware_Object = MibScalar
rsLoadSoftware = _RsLoadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 5),
    _RsLoadSoftware_Type()
)
rsLoadSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLoadSoftware.setStatus("mandatory")
_RsFileServerAddress_Type = IpAddress
_RsFileServerAddress_Object = MibScalar
rsFileServerAddress = _RsFileServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 6),
    _RsFileServerAddress_Type()
)
rsFileServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileServerAddress.setStatus("mandatory")
_RsGetConfigFileAppend_Type = DisplayString
_RsGetConfigFileAppend_Object = MibScalar
rsGetConfigFileAppend = _RsGetConfigFileAppend_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 8),
    _RsGetConfigFileAppend_Type()
)
rsGetConfigFileAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigFileAppend.setStatus("mandatory")
_RsGetConfigFileAppendReboot_Type = DisplayString
_RsGetConfigFileAppendReboot_Object = MibScalar
rsGetConfigFileAppendReboot = _RsGetConfigFileAppendReboot_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 9),
    _RsGetConfigFileAppendReboot_Type()
)
rsGetConfigFileAppendReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigFileAppendReboot.setStatus("mandatory")
_RsGetConfigErrorLog_Type = DisplayString
_RsGetConfigErrorLog_Object = MibScalar
rsGetConfigErrorLog = _RsGetConfigErrorLog_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 10),
    _RsGetConfigErrorLog_Type()
)
rsGetConfigErrorLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigErrorLog.setStatus("mandatory")
_RsSendConfigFileBer_Type = DisplayString
_RsSendConfigFileBer_Object = MibScalar
rsSendConfigFileBer = _RsSendConfigFileBer_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 11),
    _RsSendConfigFileBer_Type()
)
rsSendConfigFileBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSendConfigFileBer.setStatus("mandatory")


class _RsIncludePrivateKeys_Type(FeatureStatus):
    """Custom type rsIncludePrivateKeys based on FeatureStatus"""
    defaultValue = 2


_RsIncludePrivateKeys_Type.__name__ = "FeatureStatus"
_RsIncludePrivateKeys_Object = MibScalar
rsIncludePrivateKeys = _RsIncludePrivateKeys_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 12),
    _RsIncludePrivateKeys_Type()
)
rsIncludePrivateKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIncludePrivateKeys.setStatus("mandatory")


class _RsGetConfigFileType_Type(Integer32):
    """Custom type rsGetConfigFileType based on Integer32"""
    defaultValue = 0

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
        *(("regular", 0),
          ("active-active", 1),
          ("active-backup", 2),
          ("for-peer", 3))
    )


_RsGetConfigFileType_Type.__name__ = "Integer32"
_RsGetConfigFileType_Object = MibScalar
rsGetConfigFileType = _RsGetConfigFileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 13),
    _RsGetConfigFileType_Type()
)
rsGetConfigFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigFileType.setStatus("mandatory")
_IpRedundancy_ObjectIdentity = ObjectIdentity
ipRedundancy = _IpRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 6)
)


class _IpRedundAdminStatus_Type(Integer32):
    """Custom type ipRedundAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("vrrp", 3))
    )


_IpRedundAdminStatus_Type.__name__ = "Integer32"
_IpRedundAdminStatus_Object = MibScalar
ipRedundAdminStatus = _IpRedundAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 1),
    _IpRedundAdminStatus_Type()
)
ipRedundAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundAdminStatus.setStatus("mandatory")


class _IpRedundOperStatus_Type(Integer32):
    """Custom type ipRedundOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpRedundOperStatus_Type.__name__ = "Integer32"
_IpRedundOperStatus_Object = MibScalar
ipRedundOperStatus = _IpRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 2),
    _IpRedundOperStatus_Type()
)
ipRedundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundOperStatus.setStatus("mandatory")
_IpRedundRoutersTable_Object = MibTable
ipRedundRoutersTable = _IpRedundRoutersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3)
)
if mibBuilder.loadTexts:
    ipRedundRoutersTable.setStatus("mandatory")
_IpRedundRoutersEntry_Object = MibTableRow
ipRedundRoutersEntry = _IpRedundRoutersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1)
)
ipRedundRoutersEntry.setIndexNames(
    (0, "RADWARE-MIB", "ipRedundRoutersIfAddr"),
    (0, "RADWARE-MIB", "ipRedundRoutersMainRouterAddr"),
)
if mibBuilder.loadTexts:
    ipRedundRoutersEntry.setStatus("mandatory")
_IpRedundRoutersIfAddr_Type = IpAddress
_IpRedundRoutersIfAddr_Object = MibTableColumn
ipRedundRoutersIfAddr = _IpRedundRoutersIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 1),
    _IpRedundRoutersIfAddr_Type()
)
ipRedundRoutersIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersIfAddr.setStatus("mandatory")
_IpRedundRoutersMainRouterAddr_Type = IpAddress
_IpRedundRoutersMainRouterAddr_Object = MibTableColumn
ipRedundRoutersMainRouterAddr = _IpRedundRoutersMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 2),
    _IpRedundRoutersMainRouterAddr_Type()
)
ipRedundRoutersMainRouterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersMainRouterAddr.setStatus("mandatory")


class _IpRedundRoutersOperStatus_Type(Integer32):
    """Custom type ipRedundRoutersOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpRedundRoutersOperStatus_Type.__name__ = "Integer32"
_IpRedundRoutersOperStatus_Object = MibTableColumn
ipRedundRoutersOperStatus = _IpRedundRoutersOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 3),
    _IpRedundRoutersOperStatus_Type()
)
ipRedundRoutersOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersOperStatus.setStatus("mandatory")


class _IpRedundRoutersPollInterval_Type(Integer32):
    """Custom type ipRedundRoutersPollInterval based on Integer32"""
    defaultValue = 3


_IpRedundRoutersPollInterval_Type.__name__ = "Integer32"
_IpRedundRoutersPollInterval_Object = MibTableColumn
ipRedundRoutersPollInterval = _IpRedundRoutersPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 4),
    _IpRedundRoutersPollInterval_Type()
)
ipRedundRoutersPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersPollInterval.setStatus("mandatory")


class _IpRedundRoutersTimeout_Type(Integer32):
    """Custom type ipRedundRoutersTimeout based on Integer32"""
    defaultValue = 12


_IpRedundRoutersTimeout_Type.__name__ = "Integer32"
_IpRedundRoutersTimeout_Object = MibTableColumn
ipRedundRoutersTimeout = _IpRedundRoutersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 5),
    _IpRedundRoutersTimeout_Type()
)
ipRedundRoutersTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersTimeout.setStatus("mandatory")


class _IpRedundRoutersStatus_Type(Integer32):
    """Custom type ipRedundRoutersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_IpRedundRoutersStatus_Type.__name__ = "Integer32"
_IpRedundRoutersStatus_Object = MibTableColumn
ipRedundRoutersStatus = _IpRedundRoutersStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 6),
    _IpRedundRoutersStatus_Type()
)
ipRedundRoutersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersStatus.setStatus("mandatory")


class _RdwrRedunForceDownPorts_Type(Integer32):
    """Custom type rdwrRedunForceDownPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_RdwrRedunForceDownPorts_Type.__name__ = "Integer32"
_RdwrRedunForceDownPorts_Object = MibScalar
rdwrRedunForceDownPorts = _RdwrRedunForceDownPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 4),
    _RdwrRedunForceDownPorts_Type()
)
rdwrRedunForceDownPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrRedunForceDownPorts.setStatus("mandatory")
_RdwrRedundancyInfoTable_Object = MibTable
rdwrRedundancyInfoTable = _RdwrRedundancyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5)
)
if mibBuilder.loadTexts:
    rdwrRedundancyInfoTable.setStatus("mandatory")
_RdwrRedundancyInfoEntry_Object = MibTableRow
rdwrRedundancyInfoEntry = _RdwrRedundancyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1)
)
rdwrRedundancyInfoEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrRedundancyInfoIdx"),
)
if mibBuilder.loadTexts:
    rdwrRedundancyInfoEntry.setStatus("mandatory")
_RdwrRedundancyInfoIdx_Type = Integer32
_RdwrRedundancyInfoIdx_Object = MibTableColumn
rdwrRedundancyInfoIdx = _RdwrRedundancyInfoIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 1),
    _RdwrRedundancyInfoIdx_Type()
)
rdwrRedundancyInfoIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoIdx.setStatus("mandatory")
_RdwrRedundancyInfoInterface_Type = Integer32
_RdwrRedundancyInfoInterface_Object = MibTableColumn
rdwrRedundancyInfoInterface = _RdwrRedundancyInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 2),
    _RdwrRedundancyInfoInterface_Type()
)
rdwrRedundancyInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoInterface.setStatus("mandatory")
_RdwrRedundancyInfoVRID_Type = Integer32
_RdwrRedundancyInfoVRID_Object = MibTableColumn
rdwrRedundancyInfoVRID = _RdwrRedundancyInfoVRID_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 3),
    _RdwrRedundancyInfoVRID_Type()
)
rdwrRedundancyInfoVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoVRID.setStatus("mandatory")


class _RdwrRedundancyInfoMode_Type(Integer32):
    """Custom type rdwrRedundancyInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("not-used", 2),
          ("vrrp", 3))
    )


_RdwrRedundancyInfoMode_Type.__name__ = "Integer32"
_RdwrRedundancyInfoMode_Object = MibTableColumn
rdwrRedundancyInfoMode = _RdwrRedundancyInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 4),
    _RdwrRedundancyInfoMode_Type()
)
rdwrRedundancyInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoMode.setStatus("mandatory")
_RdwrRedundancyInfoMyAddress_Type = IpAddress
_RdwrRedundancyInfoMyAddress_Object = MibTableColumn
rdwrRedundancyInfoMyAddress = _RdwrRedundancyInfoMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 5),
    _RdwrRedundancyInfoMyAddress_Type()
)
rdwrRedundancyInfoMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoMyAddress.setStatus("mandatory")
_RdwrRedundancyInfoNeighborAddress_Type = IpAddress
_RdwrRedundancyInfoNeighborAddress_Object = MibTableColumn
rdwrRedundancyInfoNeighborAddress = _RdwrRedundancyInfoNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 6),
    _RdwrRedundancyInfoNeighborAddress_Type()
)
rdwrRedundancyInfoNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoNeighborAddress.setStatus("mandatory")


class _RdwrRedundancyInfoStatus_Type(Integer32):
    """Custom type rdwrRedundancyInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_RdwrRedundancyInfoStatus_Type.__name__ = "Integer32"
_RdwrRedundancyInfoStatus_Object = MibTableColumn
rdwrRedundancyInfoStatus = _RdwrRedundancyInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 5, 1, 7),
    _RdwrRedundancyInfoStatus_Type()
)
rdwrRedundancyInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrRedundancyInfoStatus.setStatus("mandatory")
_IpRouteLeaking_ObjectIdentity = ObjectIdentity
ipRouteLeaking = _IpRouteLeaking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 7)
)


class _IpLeakStaticToRip_Type(Integer32):
    """Custom type ipLeakStaticToRip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakStaticToRip_Type.__name__ = "Integer32"
_IpLeakStaticToRip_Object = MibScalar
ipLeakStaticToRip = _IpLeakStaticToRip_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 1),
    _IpLeakStaticToRip_Type()
)
ipLeakStaticToRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakStaticToRip.setStatus("mandatory")


class _IpLeakStaticToOspf_Type(Integer32):
    """Custom type ipLeakStaticToOspf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakStaticToOspf_Type.__name__ = "Integer32"
_IpLeakStaticToOspf_Object = MibScalar
ipLeakStaticToOspf = _IpLeakStaticToOspf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 2),
    _IpLeakStaticToOspf_Type()
)
ipLeakStaticToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakStaticToOspf.setStatus("mandatory")


class _IpLeakOspfToRip_Type(Integer32):
    """Custom type ipLeakOspfToRip based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakOspfToRip_Type.__name__ = "Integer32"
_IpLeakOspfToRip_Object = MibScalar
ipLeakOspfToRip = _IpLeakOspfToRip_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 3),
    _IpLeakOspfToRip_Type()
)
ipLeakOspfToRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakOspfToRip.setStatus("mandatory")


class _IpLeakRipToOspf_Type(Integer32):
    """Custom type ipLeakRipToOspf based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakRipToOspf_Type.__name__ = "Integer32"
_IpLeakRipToOspf_Object = MibScalar
ipLeakRipToOspf = _IpLeakRipToOspf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 4),
    _IpLeakRipToOspf_Type()
)
ipLeakRipToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakRipToOspf.setStatus("mandatory")


class _IpLeakExtDirectToOspf_Type(Integer32):
    """Custom type ipLeakExtDirectToOspf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakExtDirectToOspf_Type.__name__ = "Integer32"
_IpLeakExtDirectToOspf_Object = MibScalar
ipLeakExtDirectToOspf = _IpLeakExtDirectToOspf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 5),
    _IpLeakExtDirectToOspf_Type()
)
ipLeakExtDirectToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakExtDirectToOspf.setStatus("mandatory")


class _IpLeakOverrideOSPFLeakonFailure_Type(Integer32):
    """Custom type ipLeakOverrideOSPFLeakonFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakOverrideOSPFLeakonFailure_Type.__name__ = "Integer32"
_IpLeakOverrideOSPFLeakonFailure_Object = MibScalar
ipLeakOverrideOSPFLeakonFailure = _IpLeakOverrideOSPFLeakonFailure_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 6),
    _IpLeakOverrideOSPFLeakonFailure_Type()
)
ipLeakOverrideOSPFLeakonFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakOverrideOSPFLeakonFailure.setStatus("mandatory")


class _IpLeakAdvertiseOSPFAccordingtoPortRules_Type(Integer32):
    """Custom type ipLeakAdvertiseOSPFAccordingtoPortRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpLeakAdvertiseOSPFAccordingtoPortRules_Type.__name__ = "Integer32"
_IpLeakAdvertiseOSPFAccordingtoPortRules_Object = MibScalar
ipLeakAdvertiseOSPFAccordingtoPortRules = _IpLeakAdvertiseOSPFAccordingtoPortRules_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 7),
    _IpLeakAdvertiseOSPFAccordingtoPortRules_Type()
)
ipLeakAdvertiseOSPFAccordingtoPortRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakAdvertiseOSPFAccordingtoPortRules.setStatus("mandatory")
_IpRipFilter_ObjectIdentity = ObjectIdentity
ipRipFilter = _IpRipFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 8)
)
_RsIpRipFilterGlbTable_Object = MibTable
rsIpRipFilterGlbTable = _RsIpRipFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1)
)
if mibBuilder.loadTexts:
    rsIpRipFilterGlbTable.setStatus("mandatory")
_RsIpRipFilterGlbEntry_Object = MibTableRow
rsIpRipFilterGlbEntry = _RsIpRipFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1)
)
rsIpRipFilterGlbEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpRipFilterGlbType"),
    (0, "RADWARE-MIB", "rsIpRipFilterGlbNumber"),
)
if mibBuilder.loadTexts:
    rsIpRipFilterGlbEntry.setStatus("mandatory")


class _RsIpRipFilterGlbType_Type(Integer32):
    """Custom type rsIpRipFilterGlbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RsIpRipFilterGlbType_Type.__name__ = "Integer32"
_RsIpRipFilterGlbType_Object = MibTableColumn
rsIpRipFilterGlbType = _RsIpRipFilterGlbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 1),
    _RsIpRipFilterGlbType_Type()
)
rsIpRipFilterGlbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbType.setStatus("mandatory")
_RsIpRipFilterGlbNumber_Type = Integer32
_RsIpRipFilterGlbNumber_Object = MibTableColumn
rsIpRipFilterGlbNumber = _RsIpRipFilterGlbNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 2),
    _RsIpRipFilterGlbNumber_Type()
)
rsIpRipFilterGlbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbNumber.setStatus("mandatory")


class _RsIpRipFilterGlbStatus_Type(Integer32):
    """Custom type rsIpRipFilterGlbStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("underCreation", 3))
    )


_RsIpRipFilterGlbStatus_Type.__name__ = "Integer32"
_RsIpRipFilterGlbStatus_Object = MibTableColumn
rsIpRipFilterGlbStatus = _RsIpRipFilterGlbStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 3),
    _RsIpRipFilterGlbStatus_Type()
)
rsIpRipFilterGlbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbStatus.setStatus("mandatory")


class _RsIpRipFilterGlbIpAddr_Type(IpAddress):
    """Custom type rsIpRipFilterGlbIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpRipFilterGlbIpAddr_Type.__name__ = "IpAddress"
_RsIpRipFilterGlbIpAddr_Object = MibTableColumn
rsIpRipFilterGlbIpAddr = _RsIpRipFilterGlbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 4),
    _RsIpRipFilterGlbIpAddr_Type()
)
rsIpRipFilterGlbIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbIpAddr.setStatus("mandatory")


class _RsIpRipFilterGlbNetworkMaskBits_Type(Integer32):
    """Custom type rsIpRipFilterGlbNetworkMaskBits based on Integer32"""
    defaultValue = 0


_RsIpRipFilterGlbNetworkMaskBits_Type.__name__ = "Integer32"
_RsIpRipFilterGlbNetworkMaskBits_Object = MibTableColumn
rsIpRipFilterGlbNetworkMaskBits = _RsIpRipFilterGlbNetworkMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 5),
    _RsIpRipFilterGlbNetworkMaskBits_Type()
)
rsIpRipFilterGlbNetworkMaskBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbNetworkMaskBits.setStatus("mandatory")


class _RsIpRipFilterGlbMatchBits_Type(Integer32):
    """Custom type rsIpRipFilterGlbMatchBits based on Integer32"""
    defaultValue = 32


_RsIpRipFilterGlbMatchBits_Type.__name__ = "Integer32"
_RsIpRipFilterGlbMatchBits_Object = MibTableColumn
rsIpRipFilterGlbMatchBits = _RsIpRipFilterGlbMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 6),
    _RsIpRipFilterGlbMatchBits_Type()
)
rsIpRipFilterGlbMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbMatchBits.setStatus("mandatory")


class _RsIpRipFilterGlbAction_Type(Integer32):
    """Custom type rsIpRipFilterGlbAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RsIpRipFilterGlbAction_Type.__name__ = "Integer32"
_RsIpRipFilterGlbAction_Object = MibTableColumn
rsIpRipFilterGlbAction = _RsIpRipFilterGlbAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 7),
    _RsIpRipFilterGlbAction_Type()
)
rsIpRipFilterGlbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbAction.setStatus("mandatory")
_RsIpRipFilterLclTable_Object = MibTable
rsIpRipFilterLclTable = _RsIpRipFilterLclTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2)
)
if mibBuilder.loadTexts:
    rsIpRipFilterLclTable.setStatus("mandatory")
_RsIpRipFilterLclEntry_Object = MibTableRow
rsIpRipFilterLclEntry = _RsIpRipFilterLclEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1)
)
rsIpRipFilterLclEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpRipFilterLclIpIntf"),
    (0, "RADWARE-MIB", "rsIpRipFilterLclType"),
    (0, "RADWARE-MIB", "rsIpRipFilterLclNumber"),
)
if mibBuilder.loadTexts:
    rsIpRipFilterLclEntry.setStatus("mandatory")
_RsIpRipFilterLclIpIntf_Type = IpAddress
_RsIpRipFilterLclIpIntf_Object = MibTableColumn
rsIpRipFilterLclIpIntf = _RsIpRipFilterLclIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 1),
    _RsIpRipFilterLclIpIntf_Type()
)
rsIpRipFilterLclIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclIpIntf.setStatus("mandatory")


class _RsIpRipFilterLclType_Type(Integer32):
    """Custom type rsIpRipFilterLclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RsIpRipFilterLclType_Type.__name__ = "Integer32"
_RsIpRipFilterLclType_Object = MibTableColumn
rsIpRipFilterLclType = _RsIpRipFilterLclType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 2),
    _RsIpRipFilterLclType_Type()
)
rsIpRipFilterLclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclType.setStatus("mandatory")
_RsIpRipFilterLclNumber_Type = Integer32
_RsIpRipFilterLclNumber_Object = MibTableColumn
rsIpRipFilterLclNumber = _RsIpRipFilterLclNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 3),
    _RsIpRipFilterLclNumber_Type()
)
rsIpRipFilterLclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclNumber.setStatus("mandatory")


class _RsIpRipFilterLclStatus_Type(Integer32):
    """Custom type rsIpRipFilterLclStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("underCreation", 3))
    )


_RsIpRipFilterLclStatus_Type.__name__ = "Integer32"
_RsIpRipFilterLclStatus_Object = MibTableColumn
rsIpRipFilterLclStatus = _RsIpRipFilterLclStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 4),
    _RsIpRipFilterLclStatus_Type()
)
rsIpRipFilterLclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclStatus.setStatus("mandatory")


class _RsIpRipFilterLclIpAddr_Type(IpAddress):
    """Custom type rsIpRipFilterLclIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpRipFilterLclIpAddr_Type.__name__ = "IpAddress"
_RsIpRipFilterLclIpAddr_Object = MibTableColumn
rsIpRipFilterLclIpAddr = _RsIpRipFilterLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 5),
    _RsIpRipFilterLclIpAddr_Type()
)
rsIpRipFilterLclIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclIpAddr.setStatus("mandatory")


class _RsIpRipFilterLclNetworkMaskBits_Type(Integer32):
    """Custom type rsIpRipFilterLclNetworkMaskBits based on Integer32"""
    defaultValue = 0


_RsIpRipFilterLclNetworkMaskBits_Type.__name__ = "Integer32"
_RsIpRipFilterLclNetworkMaskBits_Object = MibTableColumn
rsIpRipFilterLclNetworkMaskBits = _RsIpRipFilterLclNetworkMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 6),
    _RsIpRipFilterLclNetworkMaskBits_Type()
)
rsIpRipFilterLclNetworkMaskBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclNetworkMaskBits.setStatus("mandatory")


class _RsIpRipFilterLclMatchBits_Type(Integer32):
    """Custom type rsIpRipFilterLclMatchBits based on Integer32"""
    defaultValue = 32


_RsIpRipFilterLclMatchBits_Type.__name__ = "Integer32"
_RsIpRipFilterLclMatchBits_Object = MibTableColumn
rsIpRipFilterLclMatchBits = _RsIpRipFilterLclMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 7),
    _RsIpRipFilterLclMatchBits_Type()
)
rsIpRipFilterLclMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclMatchBits.setStatus("mandatory")


class _RsIpRipFilterLclAction_Type(Integer32):
    """Custom type rsIpRipFilterLclAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RsIpRipFilterLclAction_Type.__name__ = "Integer32"
_RsIpRipFilterLclAction_Object = MibTableColumn
rsIpRipFilterLclAction = _RsIpRipFilterLclAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 8),
    _RsIpRipFilterLclAction_Type()
)
rsIpRipFilterLclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclAction.setStatus("mandatory")


class _RsRipEnable_Type(Integer32):
    """Custom type rsRipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsRipEnable_Type.__name__ = "Integer32"
_RsRipEnable_Object = MibScalar
rsRipEnable = _RsRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 9),
    _RsRipEnable_Type()
)
rsRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRipEnable.setStatus("mandatory")
_LreBoxAgentIP_Type = IpAddress
_LreBoxAgentIP_Object = MibScalar
lreBoxAgentIP = _LreBoxAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 10),
    _LreBoxAgentIP_Type()
)
lreBoxAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreBoxAgentIP.setStatus("mandatory")
_IpIfTable_Object = MibTable
ipIfTable = _IpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11)
)
if mibBuilder.loadTexts:
    ipIfTable.setStatus("mandatory")
_IpIfEntry_Object = MibTableRow
ipIfEntry = _IpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1)
)
ipIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "ipIfAddr"),
)
if mibBuilder.loadTexts:
    ipIfEntry.setStatus("mandatory")
_IpIfAddr_Type = Ipv6Address
_IpIfAddr_Object = MibTableColumn
ipIfAddr = _IpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 1),
    _IpIfAddr_Type()
)
ipIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfAddr.setStatus("mandatory")


class _IpIfPrefix_Type(Integer32):
    """Custom type ipIfPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpIfPrefix_Type.__name__ = "Integer32"
_IpIfPrefix_Object = MibTableColumn
ipIfPrefix = _IpIfPrefix_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 2),
    _IpIfPrefix_Type()
)
ipIfPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfPrefix.setStatus("mandatory")
_IpIfIndex_Type = Integer32
_IpIfIndex_Object = MibTableColumn
ipIfIndex = _IpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 3),
    _IpIfIndex_Type()
)
ipIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfIndex.setStatus("mandatory")


class _IpIfFwdBroadcast_Type(Integer32):
    """Custom type ipIfFwdBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IpIfFwdBroadcast_Type.__name__ = "Integer32"
_IpIfFwdBroadcast_Object = MibTableColumn
ipIfFwdBroadcast = _IpIfFwdBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 4),
    _IpIfFwdBroadcast_Type()
)
ipIfFwdBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfFwdBroadcast.setStatus("mandatory")


class _IpIfBcastAddr_Type(Integer32):
    """Custom type ipIfBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IpIfBcastAddr_Type.__name__ = "Integer32"
_IpIfBcastAddr_Object = MibTableColumn
ipIfBcastAddr = _IpIfBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 5),
    _IpIfBcastAddr_Type()
)
ipIfBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfBcastAddr.setStatus("mandatory")
_IpIfVlanTag_Type = Integer32
_IpIfVlanTag_Object = MibTableColumn
ipIfVlanTag = _IpIfVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 6),
    _IpIfVlanTag_Type()
)
ipIfVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfVlanTag.setStatus("mandatory")


class _IpIfLabel_Type(DisplayString):
    """Custom type ipIfLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpIfLabel_Type.__name__ = "DisplayString"
_IpIfLabel_Object = MibTableColumn
ipIfLabel = _IpIfLabel_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 7),
    _IpIfLabel_Type()
)
ipIfLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfLabel.setStatus("mandatory")
_IpIfEntryStatus_Type = RowStatus
_IpIfEntryStatus_Object = MibTableColumn
ipIfEntryStatus = _IpIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 8),
    _IpIfEntryStatus_Type()
)
ipIfEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfEntryStatus.setStatus("mandatory")
_IpIfBackupAddr_Type = Ipv6Address
_IpIfBackupAddr_Object = MibTableColumn
ipIfBackupAddr = _IpIfBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11, 1, 9),
    _IpIfBackupAddr_Type()
)
ipIfBackupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfBackupAddr.setStatus("mandatory")
_IpSpecRouteTable_Object = MibTable
ipSpecRouteTable = _IpSpecRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12)
)
if mibBuilder.loadTexts:
    ipSpecRouteTable.setStatus("mandatory")
_IpSpecRouteEntry_Object = MibTableRow
ipSpecRouteEntry = _IpSpecRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1)
)
ipSpecRouteEntry.setIndexNames(
    (0, "RADWARE-MIB", "ipSpecRouteDest"),
    (0, "RADWARE-MIB", "ipSpecRoutePfxLen"),
    (0, "RADWARE-MIB", "ipSpecRouteNextHop"),
)
if mibBuilder.loadTexts:
    ipSpecRouteEntry.setStatus("mandatory")
_IpSpecRouteDest_Type = Ipv6Address
_IpSpecRouteDest_Object = MibTableColumn
ipSpecRouteDest = _IpSpecRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 1),
    _IpSpecRouteDest_Type()
)
ipSpecRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSpecRouteDest.setStatus("mandatory")


class _IpSpecRoutePfxLen_Type(Integer32):
    """Custom type ipSpecRoutePfxLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpSpecRoutePfxLen_Type.__name__ = "Integer32"
_IpSpecRoutePfxLen_Object = MibTableColumn
ipSpecRoutePfxLen = _IpSpecRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 2),
    _IpSpecRoutePfxLen_Type()
)
ipSpecRoutePfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSpecRoutePfxLen.setStatus("mandatory")
_IpSpecRouteNextHop_Type = Ipv6Address
_IpSpecRouteNextHop_Object = MibTableColumn
ipSpecRouteNextHop = _IpSpecRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 3),
    _IpSpecRouteNextHop_Type()
)
ipSpecRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSpecRouteNextHop.setStatus("mandatory")


class _IpSpecRouteMetric_Type(Integer32):
    """Custom type ipSpecRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_IpSpecRouteMetric_Type.__name__ = "Integer32"
_IpSpecRouteMetric_Object = MibTableColumn
ipSpecRouteMetric = _IpSpecRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 4),
    _IpSpecRouteMetric_Type()
)
ipSpecRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSpecRouteMetric.setStatus("mandatory")
_IpSpecRoutePort_Type = Integer32
_IpSpecRoutePort_Object = MibTableColumn
ipSpecRoutePort = _IpSpecRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 5),
    _IpSpecRoutePort_Type()
)
ipSpecRoutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSpecRoutePort.setStatus("mandatory")


class _IpSpecRouteLabel_Type(DisplayString):
    """Custom type ipSpecRouteLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpSpecRouteLabel_Type.__name__ = "DisplayString"
_IpSpecRouteLabel_Object = MibTableColumn
ipSpecRouteLabel = _IpSpecRouteLabel_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 6),
    _IpSpecRouteLabel_Type()
)
ipSpecRouteLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSpecRouteLabel.setStatus("mandatory")
_IpSpecRouteStatus_Type = RowStatus
_IpSpecRouteStatus_Object = MibTableColumn
ipSpecRouteStatus = _IpSpecRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 7),
    _IpSpecRouteStatus_Type()
)
ipSpecRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSpecRouteStatus.setStatus("mandatory")
_Ip6NetToMediaTable_Object = MibTable
ip6NetToMediaTable = _Ip6NetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 13)
)
if mibBuilder.loadTexts:
    ip6NetToMediaTable.setStatus("mandatory")
_Ip6NetToMediaEntry_Object = MibTableRow
ip6NetToMediaEntry = _Ip6NetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 13, 1)
)
ip6NetToMediaEntry.setIndexNames(
    (0, "RADWARE-MIB", "ip6NetToMediaIfIndex"),
    (0, "RADWARE-MIB", "ip6NetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ip6NetToMediaEntry.setStatus("mandatory")
_Ip6NetToMediaIfIndex_Type = Integer32
_Ip6NetToMediaIfIndex_Object = MibTableColumn
ip6NetToMediaIfIndex = _Ip6NetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 13, 1, 1),
    _Ip6NetToMediaIfIndex_Type()
)
ip6NetToMediaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip6NetToMediaIfIndex.setStatus("mandatory")
_Ip6NetToMediaPhysAddress_Type = PhysAddress
_Ip6NetToMediaPhysAddress_Object = MibTableColumn
ip6NetToMediaPhysAddress = _Ip6NetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 13, 1, 2),
    _Ip6NetToMediaPhysAddress_Type()
)
ip6NetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip6NetToMediaPhysAddress.setStatus("mandatory")
_Ip6NetToMediaNetAddress_Type = Ipv6Address
_Ip6NetToMediaNetAddress_Object = MibTableColumn
ip6NetToMediaNetAddress = _Ip6NetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 13, 1, 3),
    _Ip6NetToMediaNetAddress_Type()
)
ip6NetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip6NetToMediaNetAddress.setStatus("mandatory")


class _Ip6NetToMediaType_Type(Integer32):
    """Custom type ip6NetToMediaType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_Ip6NetToMediaType_Type.__name__ = "Integer32"
_Ip6NetToMediaType_Object = MibTableColumn
ip6NetToMediaType = _Ip6NetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 13, 1, 4),
    _Ip6NetToMediaType_Type()
)
ip6NetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip6NetToMediaType.setStatus("mandatory")
_NdSpec_ObjectIdentity = ObjectIdentity
ndSpec = _NdSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 14)
)


class _RsNetNdInactiveTimeOut_Type(Integer32):
    """Custom type rsNetNdInactiveTimeOut based on Integer32"""
    defaultValue = 60000


_RsNetNdInactiveTimeOut_Type.__name__ = "Integer32"
_RsNetNdInactiveTimeOut_Object = MibScalar
rsNetNdInactiveTimeOut = _RsNetNdInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 14, 1),
    _RsNetNdInactiveTimeOut_Type()
)
rsNetNdInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsNetNdInactiveTimeOut.setStatus("mandatory")
_VirtualLan_ObjectIdentity = ObjectIdentity
virtualLan = _VirtualLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 27)
)
_VirtualLanTable_Object = MibTable
virtualLanTable = _VirtualLanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1)
)
if mibBuilder.loadTexts:
    virtualLanTable.setStatus("mandatory")
_VirtualLanEntry_Object = MibTableRow
virtualLanEntry = _VirtualLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1)
)
virtualLanEntry.setIndexNames(
    (0, "RADWARE-MIB", "vlIfIndex"),
)
if mibBuilder.loadTexts:
    virtualLanEntry.setStatus("mandatory")
_VlIfIndex_Type = Integer32
_VlIfIndex_Object = MibTableColumn
vlIfIndex = _VlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 1),
    _VlIfIndex_Type()
)
vlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlIfIndex.setStatus("mandatory")


class _VlProto_Type(Integer32):
    """Custom type vlProto based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ip", 2),
          ("ipmulticast", 3),
          ("ipxRaw", 4),
          ("ipxET", 5),
          ("ipxLLC", 6),
          ("ipxSNAP", 7),
          ("decNET", 8),
          ("decLAT", 9),
          ("netBios", 10),
          ("appleTalk", 11),
          ("xns", 12),
          ("sna", 13),
          ("userDefined", 14))
    )


_VlProto_Type.__name__ = "Integer32"
_VlProto_Object = MibTableColumn
vlProto = _VlProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 2),
    _VlProto_Type()
)
vlProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlProto.setStatus("mandatory")
_VlAutoConfigEnable_Type = TruthValue
_VlAutoConfigEnable_Object = MibTableColumn
vlAutoConfigEnable = _VlAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 3),
    _VlAutoConfigEnable_Type()
)
vlAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlAutoConfigEnable.setStatus("mandatory")
_VlStatus_Type = RowStatus
_VlStatus_Object = MibTableColumn
vlStatus = _VlStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 4),
    _VlStatus_Type()
)
vlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlStatus.setStatus("mandatory")


class _VlType_Type(Integer32):
    """Custom type vlType based on Integer32"""
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
        *(("regular", 1),
          ("specBroadcast", 2),
          ("specArpReq", 3),
          ("specBroadcastAndUnicast", 4),
          ("specArpReqAndUnicast", 5))
    )


_VlType_Type.__name__ = "Integer32"
_VlType_Object = MibTableColumn
vlType = _VlType_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 5),
    _VlType_Type()
)
vlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlType.setStatus("mandatory")
_VirtualLanPortsTable_Object = MibTable
virtualLanPortsTable = _VirtualLanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2)
)
if mibBuilder.loadTexts:
    virtualLanPortsTable.setStatus("mandatory")
_VirtualLanPortEntry_Object = MibTableRow
virtualLanPortEntry = _VirtualLanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1)
)
virtualLanPortEntry.setIndexNames(
    (0, "RADWARE-MIB", "vLIfIndex"),
    (0, "RADWARE-MIB", "vLPortIfIndex"),
)
if mibBuilder.loadTexts:
    virtualLanPortEntry.setStatus("mandatory")
_VLIfIndex_Type = Integer32
_VLIfIndex_Object = MibTableColumn
vLIfIndex = _VLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 1),
    _VLIfIndex_Type()
)
vLIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLIfIndex.setStatus("mandatory")
_VLPortIfIndex_Type = Integer32
_VLPortIfIndex_Object = MibTableColumn
vLPortIfIndex = _VLPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 2),
    _VLPortIfIndex_Type()
)
vLPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLPortIfIndex.setStatus("mandatory")


class _VLPortType_Type(Integer32):
    """Custom type vLPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_VLPortType_Type.__name__ = "Integer32"
_VLPortType_Object = MibTableColumn
vLPortType = _VLPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 3),
    _VLPortType_Type()
)
vLPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLPortType.setStatus("mandatory")
_VLPortStatus_Type = RowStatus
_VLPortStatus_Object = MibTableColumn
vLPortStatus = _VLPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 4),
    _VLPortStatus_Type()
)
vLPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLPortStatus.setStatus("mandatory")
_VirtualLanAutoConfTable_Object = MibTable
virtualLanAutoConfTable = _VirtualLanAutoConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3)
)
if mibBuilder.loadTexts:
    virtualLanAutoConfTable.setStatus("mandatory")
_VirtualLanAutoConfEntry_Object = MibTableRow
virtualLanAutoConfEntry = _VirtualLanAutoConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1)
)
virtualLanAutoConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "vlAutoConfPortIfIndex"),
    (0, "RADWARE-MIB", "vlAutoConfProto"),
)
if mibBuilder.loadTexts:
    virtualLanAutoConfEntry.setStatus("mandatory")
_VlAutoConfPortIfIndex_Type = Integer32
_VlAutoConfPortIfIndex_Object = MibTableColumn
vlAutoConfPortIfIndex = _VlAutoConfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1, 1),
    _VlAutoConfPortIfIndex_Type()
)
vlAutoConfPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlAutoConfPortIfIndex.setStatus("mandatory")


class _VlAutoConfProto_Type(Integer32):
    """Custom type vlAutoConfProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ip", 2)
    )


_VlAutoConfProto_Type.__name__ = "Integer32"
_VlAutoConfProto_Object = MibTableColumn
vlAutoConfProto = _VlAutoConfProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1, 2),
    _VlAutoConfProto_Type()
)
vlAutoConfProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlAutoConfProto.setStatus("mandatory")
_VlAutoConfStatus_Type = RowStatus
_VlAutoConfStatus_Object = MibTableColumn
vlAutoConfStatus = _VlAutoConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1, 3),
    _VlAutoConfStatus_Type()
)
vlAutoConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlAutoConfStatus.setStatus("mandatory")


class _VirtualLanAutoConfAgingTimeout_Type(Integer32):
    """Custom type virtualLanAutoConfAgingTimeout based on Integer32"""
    defaultValue = 3600


_VirtualLanAutoConfAgingTimeout_Type.__name__ = "Integer32"
_VirtualLanAutoConfAgingTimeout_Object = MibScalar
virtualLanAutoConfAgingTimeout = _VirtualLanAutoConfAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 4),
    _VirtualLanAutoConfAgingTimeout_Type()
)
virtualLanAutoConfAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualLanAutoConfAgingTimeout.setStatus("mandatory")
_VirtualLanProtocolVlan_ObjectIdentity = ObjectIdentity
virtualLanProtocolVlan = _VirtualLanProtocolVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 27, 5)
)


class _VirtualLanUserEtherType_Type(OctetString):
    """Custom type virtualLanUserEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_VirtualLanUserEtherType_Type.__name__ = "OctetString"
_VirtualLanUserEtherType_Object = MibScalar
virtualLanUserEtherType = _VirtualLanUserEtherType_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 5, 1),
    _VirtualLanUserEtherType_Type()
)
virtualLanUserEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualLanUserEtherType.setStatus("mandatory")


class _VirtualLanUserMask_Type(OctetString):
    """Custom type virtualLanUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_VirtualLanUserMask_Type.__name__ = "OctetString"
_VirtualLanUserMask_Object = MibScalar
virtualLanUserMask = _VirtualLanUserMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 5, 2),
    _VirtualLanUserMask_Type()
)
virtualLanUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualLanUserMask.setStatus("mandatory")
_RsConf_ObjectIdentity = ObjectIdentity
rsConf = _RsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 28)
)
_RsIfConfTable_Object = MibTable
rsIfConfTable = _RsIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1)
)
if mibBuilder.loadTexts:
    rsIfConfTable.setStatus("mandatory")
_RsIfConfEntry_Object = MibTableRow
rsIfConfEntry = _RsIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1)
)
rsIfConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIfConfIndex"),
)
if mibBuilder.loadTexts:
    rsIfConfEntry.setStatus("mandatory")
_RsIfConfIndex_Type = Integer32
_RsIfConfIndex_Object = MibTableColumn
rsIfConfIndex = _RsIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 1),
    _RsIfConfIndex_Type()
)
rsIfConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfConfIndex.setStatus("mandatory")
_RsIfConfType_Type = RsIfType
_RsIfConfType_Object = MibTableColumn
rsIfConfType = _RsIfConfType_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 2),
    _RsIfConfType_Type()
)
rsIfConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfConfType.setStatus("mandatory")
_RsIfConfName_Type = DisplayString
_RsIfConfName_Object = MibTableColumn
rsIfConfName = _RsIfConfName_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 3),
    _RsIfConfName_Type()
)
rsIfConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfConfName.setStatus("mandatory")
_RsIfConfStatus_Type = RowStatus
_RsIfConfStatus_Object = MibTableColumn
rsIfConfStatus = _RsIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 4),
    _RsIfConfStatus_Type()
)
rsIfConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfConfStatus.setStatus("mandatory")
_RsTunning_ObjectIdentity = ObjectIdentity
rsTunning = _RsTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29)
)
_RsHighPriority_Type = Integer32
_RsHighPriority_Object = MibScalar
rsHighPriority = _RsHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 1),
    _RsHighPriority_Type()
)
rsHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsHighPriority.setStatus("mandatory")
_RsLowPriority_Type = Integer32
_RsLowPriority_Object = MibScalar
rsLowPriority = _RsLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 2),
    _RsLowPriority_Type()
)
rsLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLowPriority.setStatus("mandatory")
_RsDbgLevel_Type = Integer32
_RsDbgLevel_Object = MibScalar
rsDbgLevel = _RsDbgLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 3),
    _RsDbgLevel_Type()
)
rsDbgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDbgLevel.setStatus("mandatory")
_RsDiagnostic_Type = DisplayString
_RsDiagnostic_Object = MibScalar
rsDiagnostic = _RsDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4),
    _RsDiagnostic_Type()
)
rsDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiagnostic.setStatus("mandatory")
_RsConfirmMessagTab_Type = Integer32
_RsConfirmMessagTab_Object = MibScalar
rsConfirmMessagTab = _RsConfirmMessagTab_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 5),
    _RsConfirmMessagTab_Type()
)
rsConfirmMessagTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsConfirmMessagTab.setStatus("mandatory")
_EventMessageTable_Object = MibTable
eventMessageTable = _EventMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6)
)
if mibBuilder.loadTexts:
    eventMessageTable.setStatus("mandatory")
_EventMessageEntry_Object = MibTableRow
eventMessageEntry = _EventMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1)
)
eventMessageEntry.setIndexNames(
    (0, "RADWARE-MIB", "eventNum"),
)
if mibBuilder.loadTexts:
    eventMessageEntry.setStatus("mandatory")
_EventNum_Type = Integer32
_EventNum_Object = MibTableColumn
eventNum = _EventNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1, 1),
    _EventNum_Type()
)
eventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNum.setStatus("mandatory")
_EventDesc_Type = DisplayString
_EventDesc_Object = MibTableColumn
eventDesc = _EventDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1, 2),
    _EventDesc_Type()
)
eventDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDesc.setStatus("mandatory")
_ReaTunning_ObjectIdentity = ObjectIdentity
reaTunning = _ReaTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 7)
)
_ReaIpRemoteAgingTime_Type = Integer32
_ReaIpRemoteAgingTime_Object = MibScalar
reaIpRemoteAgingTime = _ReaIpRemoteAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 1),
    _ReaIpRemoteAgingTime_Type()
)
reaIpRemoteAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpRemoteAgingTime.setStatus("mandatory")
_ReaFftHashMaxChain_Type = Integer32
_ReaFftHashMaxChain_Object = MibScalar
reaFftHashMaxChain = _ReaFftHashMaxChain_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 2),
    _ReaFftHashMaxChain_Type()
)
reaFftHashMaxChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaFftHashMaxChain.setStatus("mandatory")


class _ReaMltcstBitOn_Type(Integer32):
    """Custom type reaMltcstBitOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ReaMltcstBitOn_Type.__name__ = "Integer32"
_ReaMltcstBitOn_Object = MibScalar
reaMltcstBitOn = _ReaMltcstBitOn_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 3),
    _ReaMltcstBitOn_Type()
)
reaMltcstBitOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaMltcstBitOn.setStatus("mandatory")


class _ReaIpForwardEnable_Type(Integer32):
    """Custom type reaIpForwardEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaIpForwardEnable_Type.__name__ = "Integer32"
_ReaIpForwardEnable_Object = MibScalar
reaIpForwardEnable = _ReaIpForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 4),
    _ReaIpForwardEnable_Type()
)
reaIpForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpForwardEnable.setStatus("mandatory")


class _ReaIpxForwardEnable_Type(Integer32):
    """Custom type reaIpxForwardEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaIpxForwardEnable_Type.__name__ = "Integer32"
_ReaIpxForwardEnable_Object = MibScalar
reaIpxForwardEnable = _ReaIpxForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 5),
    _ReaIpxForwardEnable_Type()
)
reaIpxForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpxForwardEnable.setStatus("mandatory")


class _ReaBridgeEnable_Type(Integer32):
    """Custom type reaBridgeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaBridgeEnable_Type.__name__ = "Integer32"
_ReaBridgeEnable_Object = MibScalar
reaBridgeEnable = _ReaBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 6),
    _ReaBridgeEnable_Type()
)
reaBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaBridgeEnable.setStatus("mandatory")


class _ReaFacsEnable_Type(Integer32):
    """Custom type reaFacsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaFacsEnable_Type.__name__ = "Integer32"
_ReaFacsEnable_Object = MibScalar
reaFacsEnable = _ReaFacsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 7),
    _ReaFacsEnable_Type()
)
reaFacsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaFacsEnable.setStatus("mandatory")
_ReaIpForwardDatagrams_Type = Counter32
_ReaIpForwardDatagrams_Object = MibScalar
reaIpForwardDatagrams = _ReaIpForwardDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 8),
    _ReaIpForwardDatagrams_Type()
)
reaIpForwardDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpForwardDatagrams.setStatus("mandatory")
_ReaIpInDiscards_Type = Counter32
_ReaIpInDiscards_Object = MibScalar
reaIpInDiscards = _ReaIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 9),
    _ReaIpInDiscards_Type()
)
reaIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpInDiscards.setStatus("mandatory")
_ReaIpxForwardDatagrams_Type = Counter32
_ReaIpxForwardDatagrams_Object = MibScalar
reaIpxForwardDatagrams = _ReaIpxForwardDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 10),
    _ReaIpxForwardDatagrams_Type()
)
reaIpxForwardDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxForwardDatagrams.setStatus("mandatory")
_ReaIpxInDiscards_Type = Counter32
_ReaIpxInDiscards_Object = MibScalar
reaIpxInDiscards = _ReaIpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 11),
    _ReaIpxInDiscards_Type()
)
reaIpxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxInDiscards.setStatus("mandatory")
_ReaBridgeFftTable_Object = MibTable
reaBridgeFftTable = _ReaBridgeFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12)
)
if mibBuilder.loadTexts:
    reaBridgeFftTable.setStatus("mandatory")
_ReaBridgeFftEntry_Object = MibTableRow
reaBridgeFftEntry = _ReaBridgeFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1)
)
reaBridgeFftEntry.setIndexNames(
    (0, "RADWARE-MIB", "reaBrgFftEntryNum"),
)
if mibBuilder.loadTexts:
    reaBridgeFftEntry.setStatus("mandatory")
_ReaBrgFftEntryNum_Type = Integer32
_ReaBrgFftEntryNum_Object = MibTableColumn
reaBrgFftEntryNum = _ReaBrgFftEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 1),
    _ReaBrgFftEntryNum_Type()
)
reaBrgFftEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftEntryNum.setStatus("mandatory")
_ReaBrgFftMacAddr_Type = PhysAddress
_ReaBrgFftMacAddr_Object = MibTableColumn
reaBrgFftMacAddr = _ReaBrgFftMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 2),
    _ReaBrgFftMacAddr_Type()
)
reaBrgFftMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftMacAddr.setStatus("mandatory")
_ReaBrgFftReNum_Type = Integer32
_ReaBrgFftReNum_Object = MibTableColumn
reaBrgFftReNum = _ReaBrgFftReNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 3),
    _ReaBrgFftReNum_Type()
)
reaBrgFftReNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftReNum.setStatus("mandatory")
_ReaBrgFftPortNum_Type = Integer32
_ReaBrgFftPortNum_Object = MibTableColumn
reaBrgFftPortNum = _ReaBrgFftPortNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 4),
    _ReaBrgFftPortNum_Type()
)
reaBrgFftPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftPortNum.setStatus("mandatory")
_ReaBrgFftFacsSrcIndex_Type = Integer32
_ReaBrgFftFacsSrcIndex_Object = MibTableColumn
reaBrgFftFacsSrcIndex = _ReaBrgFftFacsSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 5),
    _ReaBrgFftFacsSrcIndex_Type()
)
reaBrgFftFacsSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftFacsSrcIndex.setStatus("mandatory")
_ReaBrgFftFacsDstIndex_Type = Integer32
_ReaBrgFftFacsDstIndex_Object = MibTableColumn
reaBrgFftFacsDstIndex = _ReaBrgFftFacsDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 6),
    _ReaBrgFftFacsDstIndex_Type()
)
reaBrgFftFacsDstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftFacsDstIndex.setStatus("mandatory")
_ReaBrgDiscards_Type = Counter32
_ReaBrgDiscards_Object = MibScalar
reaBrgDiscards = _ReaBrgDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 13),
    _ReaBrgDiscards_Type()
)
reaBrgDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgDiscards.setStatus("mandatory")
_ReaBrgForwards_Type = Counter32
_ReaBrgForwards_Object = MibScalar
reaBrgForwards = _ReaBrgForwards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 14),
    _ReaBrgForwards_Type()
)
reaBrgForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgForwards.setStatus("mandatory")
_ReaIpFftTable_Object = MibTable
reaIpFftTable = _ReaIpFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15)
)
if mibBuilder.loadTexts:
    reaIpFftTable.setStatus("mandatory")
_ReaIpFftEntry_Object = MibTableRow
reaIpFftEntry = _ReaIpFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1)
)
reaIpFftEntry.setIndexNames(
    (0, "RADWARE-MIB", "reaIpFftEntryNum"),
)
if mibBuilder.loadTexts:
    reaIpFftEntry.setStatus("mandatory")
_ReaIpFftEntryNum_Type = Integer32
_ReaIpFftEntryNum_Object = MibTableColumn
reaIpFftEntryNum = _ReaIpFftEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 1),
    _ReaIpFftEntryNum_Type()
)
reaIpFftEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftEntryNum.setStatus("mandatory")
_ReaIpFftDstIpAddr_Type = IpAddress
_ReaIpFftDstIpAddr_Object = MibTableColumn
reaIpFftDstIpAddr = _ReaIpFftDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 2),
    _ReaIpFftDstIpAddr_Type()
)
reaIpFftDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftDstIpAddr.setStatus("mandatory")
_ReaIpFftDstIpMask_Type = IpAddress
_ReaIpFftDstIpMask_Object = MibTableColumn
reaIpFftDstIpMask = _ReaIpFftDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 3),
    _ReaIpFftDstIpMask_Type()
)
reaIpFftDstIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftDstIpMask.setStatus("mandatory")


class _ReaIpFftRangeType_Type(Integer32):
    """Custom type reaIpFftRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("remote", 2))
    )


_ReaIpFftRangeType_Type.__name__ = "Integer32"
_ReaIpFftRangeType_Object = MibTableColumn
reaIpFftRangeType = _ReaIpFftRangeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 4),
    _ReaIpFftRangeType_Type()
)
reaIpFftRangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftRangeType.setStatus("mandatory")
_ReaIpFftSrcMacAddr_Type = PhysAddress
_ReaIpFftSrcMacAddr_Object = MibTableColumn
reaIpFftSrcMacAddr = _ReaIpFftSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 5),
    _ReaIpFftSrcMacAddr_Type()
)
reaIpFftSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftSrcMacAddr.setStatus("mandatory")
_ReaIpFftDstMacAddr_Type = PhysAddress
_ReaIpFftDstMacAddr_Object = MibTableColumn
reaIpFftDstMacAddr = _ReaIpFftDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 6),
    _ReaIpFftDstMacAddr_Type()
)
reaIpFftDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftDstMacAddr.setStatus("mandatory")
_ReaIpFftReNum_Type = Integer32
_ReaIpFftReNum_Object = MibTableColumn
reaIpFftReNum = _ReaIpFftReNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 7),
    _ReaIpFftReNum_Type()
)
reaIpFftReNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftReNum.setStatus("mandatory")
_ReaIpFftPortNum_Type = Integer32
_ReaIpFftPortNum_Object = MibTableColumn
reaIpFftPortNum = _ReaIpFftPortNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 8),
    _ReaIpFftPortNum_Type()
)
reaIpFftPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftPortNum.setStatus("mandatory")
_ReaIpFftFacsSrcIndex_Type = Integer32
_ReaIpFftFacsSrcIndex_Object = MibTableColumn
reaIpFftFacsSrcIndex = _ReaIpFftFacsSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 9),
    _ReaIpFftFacsSrcIndex_Type()
)
reaIpFftFacsSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftFacsSrcIndex.setStatus("mandatory")
_ReaIpFftFacsDstIndex_Type = Integer32
_ReaIpFftFacsDstIndex_Object = MibTableColumn
reaIpFftFacsDstIndex = _ReaIpFftFacsDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 10),
    _ReaIpFftFacsDstIndex_Type()
)
reaIpFftFacsDstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftFacsDstIndex.setStatus("mandatory")


class _ReaIpFftApplFlags_Type(OctetString):
    """Custom type reaIpFftApplFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ReaIpFftApplFlags_Type.__name__ = "OctetString"
_ReaIpFftApplFlags_Object = MibTableColumn
reaIpFftApplFlags = _ReaIpFftApplFlags_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 11),
    _ReaIpFftApplFlags_Type()
)
reaIpFftApplFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftApplFlags.setStatus("mandatory")
_ReaIpxFftTable_Object = MibTable
reaIpxFftTable = _ReaIpxFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16)
)
if mibBuilder.loadTexts:
    reaIpxFftTable.setStatus("mandatory")
_ReaIpxFftEntry_Object = MibTableRow
reaIpxFftEntry = _ReaIpxFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1)
)
reaIpxFftEntry.setIndexNames(
    (0, "RADWARE-MIB", "reaIpxFftEntryNum"),
)
if mibBuilder.loadTexts:
    reaIpxFftEntry.setStatus("mandatory")
_ReaIpxFftEntryNum_Type = Integer32
_ReaIpxFftEntryNum_Object = MibTableColumn
reaIpxFftEntryNum = _ReaIpxFftEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 1),
    _ReaIpxFftEntryNum_Type()
)
reaIpxFftEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftEntryNum.setStatus("mandatory")
_ReaIpxFftDstNetid_Type = Integer32
_ReaIpxFftDstNetid_Object = MibTableColumn
reaIpxFftDstNetid = _ReaIpxFftDstNetid_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 2),
    _ReaIpxFftDstNetid_Type()
)
reaIpxFftDstNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftDstNetid.setStatus("mandatory")


class _ReaIpxFftRangeType_Type(Integer32):
    """Custom type reaIpxFftRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("remote", 2))
    )


_ReaIpxFftRangeType_Type.__name__ = "Integer32"
_ReaIpxFftRangeType_Object = MibTableColumn
reaIpxFftRangeType = _ReaIpxFftRangeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 3),
    _ReaIpxFftRangeType_Type()
)
reaIpxFftRangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftRangeType.setStatus("mandatory")
_ReaIpxFftSrcMacAddr_Type = PhysAddress
_ReaIpxFftSrcMacAddr_Object = MibTableColumn
reaIpxFftSrcMacAddr = _ReaIpxFftSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 4),
    _ReaIpxFftSrcMacAddr_Type()
)
reaIpxFftSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftSrcMacAddr.setStatus("mandatory")
_ReaIpxFftDstMacAddr_Type = PhysAddress
_ReaIpxFftDstMacAddr_Object = MibTableColumn
reaIpxFftDstMacAddr = _ReaIpxFftDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 5),
    _ReaIpxFftDstMacAddr_Type()
)
reaIpxFftDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftDstMacAddr.setStatus("mandatory")
_ReaIpxFftReNum_Type = Integer32
_ReaIpxFftReNum_Object = MibTableColumn
reaIpxFftReNum = _ReaIpxFftReNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 6),
    _ReaIpxFftReNum_Type()
)
reaIpxFftReNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftReNum.setStatus("mandatory")
_ReaIpxFftPortNum_Type = Integer32
_ReaIpxFftPortNum_Object = MibTableColumn
reaIpxFftPortNum = _ReaIpxFftPortNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 7),
    _ReaIpxFftPortNum_Type()
)
reaIpxFftPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftPortNum.setStatus("mandatory")
_ReaIpxFftFacsSrcIndex_Type = Integer32
_ReaIpxFftFacsSrcIndex_Object = MibTableColumn
reaIpxFftFacsSrcIndex = _ReaIpxFftFacsSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 8),
    _ReaIpxFftFacsSrcIndex_Type()
)
reaIpxFftFacsSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftFacsSrcIndex.setStatus("mandatory")
_ReaIpxFftFacsDstIndex_Type = Integer32
_ReaIpxFftFacsDstIndex_Object = MibTableColumn
reaIpxFftFacsDstIndex = _ReaIpxFftFacsDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 9),
    _ReaIpxFftFacsDstIndex_Type()
)
reaIpxFftFacsDstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftFacsDstIndex.setStatus("mandatory")
_LreVnResposibilityTable_Object = MibTable
lreVnResposibilityTable = _LreVnResposibilityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17)
)
if mibBuilder.loadTexts:
    lreVnResposibilityTable.setStatus("mandatory")
_LreVnResposibilityEntry_Object = MibTableRow
lreVnResposibilityEntry = _LreVnResposibilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17, 1)
)
lreVnResposibilityEntry.setIndexNames(
    (0, "RADWARE-MIB", "lreVnRespVn"),
)
if mibBuilder.loadTexts:
    lreVnResposibilityEntry.setStatus("mandatory")
_LreVnRespVn_Type = Integer32
_LreVnRespVn_Object = MibTableColumn
lreVnRespVn = _LreVnRespVn_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17, 1, 1),
    _LreVnRespVn_Type()
)
lreVnRespVn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreVnRespVn.setStatus("mandatory")
_LreVnRespStatus_Type = RowStatus
_LreVnRespStatus_Object = MibTableColumn
lreVnRespStatus = _LreVnRespStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17, 1, 2),
    _LreVnRespStatus_Type()
)
lreVnRespStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreVnRespStatus.setStatus("mandatory")


class _ReaSrcViolationEnable_Type(Integer32):
    """Custom type reaSrcViolationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaSrcViolationEnable_Type.__name__ = "Integer32"
_ReaSrcViolationEnable_Object = MibScalar
reaSrcViolationEnable = _ReaSrcViolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 18),
    _ReaSrcViolationEnable_Type()
)
reaSrcViolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaSrcViolationEnable.setStatus("mandatory")


class _ReaSrcViolationTrapEnable_Type(Integer32):
    """Custom type reaSrcViolationTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaSrcViolationTrapEnable_Type.__name__ = "Integer32"
_ReaSrcViolationTrapEnable_Object = MibScalar
reaSrcViolationTrapEnable = _ReaSrcViolationTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 19),
    _ReaSrcViolationTrapEnable_Type()
)
reaSrcViolationTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaSrcViolationTrapEnable.setStatus("mandatory")


class _ReaSrcAddrValidationEnable_Type(Integer32):
    """Custom type reaSrcAddrValidationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ReaSrcAddrValidationEnable_Type.__name__ = "Integer32"
_ReaSrcAddrValidationEnable_Object = MibScalar
reaSrcAddrValidationEnable = _ReaSrcAddrValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 20),
    _ReaSrcAddrValidationEnable_Type()
)
reaSrcAddrValidationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaSrcAddrValidationEnable.setStatus("mandatory")
_ReaRsQueueDiscards_Type = Counter32
_ReaRsQueueDiscards_Object = MibScalar
reaRsQueueDiscards = _ReaRsQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 21),
    _ReaRsQueueDiscards_Type()
)
reaRsQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaRsQueueDiscards.setStatus("mandatory")
_ReaBufFree_Type = Integer32
_ReaBufFree_Object = MibScalar
reaBufFree = _ReaBufFree_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 22),
    _ReaBufFree_Type()
)
reaBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBufFree.setStatus("mandatory")


class _LreResetDstMacBit46_Type(Integer32):
    """Custom type lreResetDstMacBit46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LreResetDstMacBit46_Type.__name__ = "Integer32"
_LreResetDstMacBit46_Object = MibScalar
lreResetDstMacBit46 = _LreResetDstMacBit46_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 23),
    _LreResetDstMacBit46_Type()
)
lreResetDstMacBit46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreResetDstMacBit46.setStatus("mandatory")


class _LreQueSourceSelect_Type(Integer32):
    """Custom type lreQueSourceSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vNET", 1),
          ("dstMac", 2))
    )


_LreQueSourceSelect_Type.__name__ = "Integer32"
_LreQueSourceSelect_Object = MibScalar
lreQueSourceSelect = _LreQueSourceSelect_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 24),
    _LreQueSourceSelect_Type()
)
lreQueSourceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreQueSourceSelect.setStatus("mandatory")


class _LreResetDstMacBit47_Type(Integer32):
    """Custom type lreResetDstMacBit47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LreResetDstMacBit47_Type.__name__ = "Integer32"
_LreResetDstMacBit47_Object = MibScalar
lreResetDstMacBit47 = _LreResetDstMacBit47_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 25),
    _LreResetDstMacBit47_Type()
)
lreResetDstMacBit47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreResetDstMacBit47.setStatus("mandatory")
_RsMaxEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxEntriesTuning = _RsMaxEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8)
)
_RsMaxBridgeForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxBridgeForwardingEntriesTuning = _RsMaxBridgeForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1)
)
_RsMaxBrgFrwEntries_Type = Integer32
_RsMaxBrgFrwEntries_Object = MibScalar
rsMaxBrgFrwEntries = _RsMaxBrgFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1, 1),
    _RsMaxBrgFrwEntries_Type()
)
rsMaxBrgFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxBrgFrwEntries.setStatus("mandatory")
_RsMaxBrgFrwEntriesAfterReset_Type = Integer32
_RsMaxBrgFrwEntriesAfterReset_Object = MibScalar
rsMaxBrgFrwEntriesAfterReset = _RsMaxBrgFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1, 2),
    _RsMaxBrgFrwEntriesAfterReset_Type()
)
rsMaxBrgFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxBrgFrwEntriesAfterReset.setStatus("mandatory")
_RsMaxIpForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpForwardingEntriesTuning = _RsMaxIpForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2)
)
_RsMaxIpFrwEntries_Type = Integer32
_RsMaxIpFrwEntries_Object = MibScalar
rsMaxIpFrwEntries = _RsMaxIpFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2, 1),
    _RsMaxIpFrwEntries_Type()
)
rsMaxIpFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpFrwEntries.setStatus("mandatory")
_RsMaxIpFrwEntriesAfterReset_Type = Integer32
_RsMaxIpFrwEntriesAfterReset_Object = MibScalar
rsMaxIpFrwEntriesAfterReset = _RsMaxIpFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2, 2),
    _RsMaxIpFrwEntriesAfterReset_Type()
)
rsMaxIpFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpFrwEntriesAfterReset.setStatus("mandatory")
_RsMaxArpEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxArpEntriesTuning = _RsMaxArpEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3)
)
_RsMaxArpEntries_Type = Integer32
_RsMaxArpEntries_Object = MibScalar
rsMaxArpEntries = _RsMaxArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3, 1),
    _RsMaxArpEntries_Type()
)
rsMaxArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxArpEntries.setStatus("mandatory")
_RsMaxArpEntriesAfterReset_Type = Integer32
_RsMaxArpEntriesAfterReset_Object = MibScalar
rsMaxArpEntriesAfterReset = _RsMaxArpEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3, 2),
    _RsMaxArpEntriesAfterReset_Type()
)
rsMaxArpEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxArpEntriesAfterReset.setStatus("mandatory")
_RsMaxIpxForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxForwardingEntriesTuning = _RsMaxIpxForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4)
)
_RsMaxIpxFrwEntries_Type = Integer32
_RsMaxIpxFrwEntries_Object = MibScalar
rsMaxIpxFrwEntries = _RsMaxIpxFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4, 1),
    _RsMaxIpxFrwEntries_Type()
)
rsMaxIpxFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxFrwEntries.setStatus("mandatory")
_RsMaxIpxFrwEntriesAfterReset_Type = Integer32
_RsMaxIpxFrwEntriesAfterReset_Object = MibScalar
rsMaxIpxFrwEntriesAfterReset = _RsMaxIpxFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4, 2),
    _RsMaxIpxFrwEntriesAfterReset_Type()
)
rsMaxIpxFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxFrwEntriesAfterReset.setStatus("mandatory")
_RsMaxIpxSapEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxSapEntriesTuning = _RsMaxIpxSapEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5)
)
_RsMaxIpxSapEntries_Type = Integer32
_RsMaxIpxSapEntries_Object = MibScalar
rsMaxIpxSapEntries = _RsMaxIpxSapEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5, 1),
    _RsMaxIpxSapEntries_Type()
)
rsMaxIpxSapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxSapEntries.setStatus("mandatory")
_RsMaxIpxSapEntriesAfterReset_Type = Integer32
_RsMaxIpxSapEntriesAfterReset_Object = MibScalar
rsMaxIpxSapEntriesAfterReset = _RsMaxIpxSapEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5, 2),
    _RsMaxIpxSapEntriesAfterReset_Type()
)
rsMaxIpxSapEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxSapEntriesAfterReset.setStatus("mandatory")
_RsMaxDspClntEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxDspClntEntriesTuning = _RsMaxDspClntEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6)
)
_RsMaxDspClntEntries_Type = Integer32
_RsMaxDspClntEntries_Object = MibScalar
rsMaxDspClntEntries = _RsMaxDspClntEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6, 1),
    _RsMaxDspClntEntries_Type()
)
rsMaxDspClntEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDspClntEntries.setStatus("mandatory")
_RsMaxDspClntEntriesAfterReset_Type = Integer32
_RsMaxDspClntEntriesAfterReset_Object = MibScalar
rsMaxDspClntEntriesAfterReset = _RsMaxDspClntEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6, 2),
    _RsMaxDspClntEntriesAfterReset_Type()
)
rsMaxDspClntEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDspClntEntriesAfterReset.setStatus("mandatory")
_RsMaxZeroHopRoutEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxZeroHopRoutEntriesTuning = _RsMaxZeroHopRoutEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 7)
)
_RsMaxZhrConns_Type = Integer32
_RsMaxZhrConns_Object = MibScalar
rsMaxZhrConns = _RsMaxZhrConns_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 7, 1),
    _RsMaxZhrConns_Type()
)
rsMaxZhrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxZhrConns.setStatus("mandatory")
_RsMaxZhrConnsAfterReset_Type = Integer32
_RsMaxZhrConnsAfterReset_Object = MibScalar
rsMaxZhrConnsAfterReset = _RsMaxZhrConnsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 7, 2),
    _RsMaxZhrConnsAfterReset_Type()
)
rsMaxZhrConnsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxZhrConnsAfterReset.setStatus("mandatory")
_RsMaxDspFrmEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxDspFrmEntriesTuning = _RsMaxDspFrmEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 8)
)
_RsMaxDspFrmEntries_Type = Integer32
_RsMaxDspFrmEntries_Object = MibScalar
rsMaxDspFrmEntries = _RsMaxDspFrmEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 8, 1),
    _RsMaxDspFrmEntries_Type()
)
rsMaxDspFrmEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDspFrmEntries.setStatus("mandatory")
_RsMaxDspFrmEntriesAfterReset_Type = Integer32
_RsMaxDspFrmEntriesAfterReset_Object = MibScalar
rsMaxDspFrmEntriesAfterReset = _RsMaxDspFrmEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 8, 2),
    _RsMaxDspFrmEntriesAfterReset_Type()
)
rsMaxDspFrmEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDspFrmEntriesAfterReset.setStatus("mandatory")
_RsMaxRoutingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxRoutingEntriesTuning = _RsMaxRoutingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9)
)
_RsMaxRoutingEntries_Type = Integer32
_RsMaxRoutingEntries_Object = MibScalar
rsMaxRoutingEntries = _RsMaxRoutingEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 1),
    _RsMaxRoutingEntries_Type()
)
rsMaxRoutingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxRoutingEntries.setStatus("mandatory")
_RsMaxRoutingEntriesAfterReset_Type = Integer32
_RsMaxRoutingEntriesAfterReset_Object = MibScalar
rsMaxRoutingEntriesAfterReset = _RsMaxRoutingEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 2),
    _RsMaxRoutingEntriesAfterReset_Type()
)
rsMaxRoutingEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxRoutingEntriesAfterReset.setStatus("mandatory")
_RsMaxRadiusEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxRadiusEntriesTuning = _RsMaxRadiusEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10)
)
_RsMaxRadiusUsersEntries_Type = Integer32
_RsMaxRadiusUsersEntries_Object = MibScalar
rsMaxRadiusUsersEntries = _RsMaxRadiusUsersEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 1),
    _RsMaxRadiusUsersEntries_Type()
)
rsMaxRadiusUsersEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxRadiusUsersEntries.setStatus("mandatory")
_RsMaxRadiusUsersEntriesAfterReset_Type = Integer32
_RsMaxRadiusUsersEntriesAfterReset_Object = MibScalar
rsMaxRadiusUsersEntriesAfterReset = _RsMaxRadiusUsersEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 2),
    _RsMaxRadiusUsersEntriesAfterReset_Type()
)
rsMaxRadiusUsersEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxRadiusUsersEntriesAfterReset.setStatus("mandatory")
_RsMaxRadiusNasAuthEntries_Type = Integer32
_RsMaxRadiusNasAuthEntries_Object = MibScalar
rsMaxRadiusNasAuthEntries = _RsMaxRadiusNasAuthEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 3),
    _RsMaxRadiusNasAuthEntries_Type()
)
rsMaxRadiusNasAuthEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxRadiusNasAuthEntries.setStatus("mandatory")
_RsMaxRadiusNasAuthEntriesAfterReset_Type = Integer32
_RsMaxRadiusNasAuthEntriesAfterReset_Object = MibScalar
rsMaxRadiusNasAuthEntriesAfterReset = _RsMaxRadiusNasAuthEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 4),
    _RsMaxRadiusNasAuthEntriesAfterReset_Type()
)
rsMaxRadiusNasAuthEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxRadiusNasAuthEntriesAfterReset.setStatus("mandatory")


class _RsTuneCheckMemory_Type(Integer32):
    """Custom type rsTuneCheckMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enoughMemory", 1),
          ("notEnoughMemory", 2))
    )


_RsTuneCheckMemory_Type.__name__ = "Integer32"
_RsTuneCheckMemory_Object = MibScalar
rsTuneCheckMemory = _RsTuneCheckMemory_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 9),
    _RsTuneCheckMemory_Type()
)
rsTuneCheckMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTuneCheckMemory.setStatus("mandatory")
_RsTuneLastCheckResult_Type = Integer32
_RsTuneLastCheckResult_Object = MibScalar
rsTuneLastCheckResult = _RsTuneLastCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 10),
    _RsTuneLastCheckResult_Type()
)
rsTuneLastCheckResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTuneLastCheckResult.setStatus("mandatory")
_StpSpec_ObjectIdentity = ObjectIdentity
stpSpec = _StpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 30)
)


class _RsStpMode_Type(Integer32):
    """Custom type rsStpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("per-vlan", 2))
    )


_RsStpMode_Type.__name__ = "Integer32"
_RsStpMode_Object = MibScalar
rsStpMode = _RsStpMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 1),
    _RsStpMode_Type()
)
rsStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpMode.setStatus("mandatory")


class _RsStpDefaultBridgePriority_Type(Integer32):
    """Custom type rsStpDefaultBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_RsStpDefaultBridgePriority_Type.__name__ = "Integer32"
_RsStpDefaultBridgePriority_Object = MibScalar
rsStpDefaultBridgePriority = _RsStpDefaultBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 2),
    _RsStpDefaultBridgePriority_Type()
)
rsStpDefaultBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpDefaultBridgePriority.setStatus("mandatory")


class _RsStpDefaultHelloTime_Type(Integer32):
    """Custom type rsStpDefaultHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsStpDefaultHelloTime_Type.__name__ = "Integer32"
_RsStpDefaultHelloTime_Object = MibScalar
rsStpDefaultHelloTime = _RsStpDefaultHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 3),
    _RsStpDefaultHelloTime_Type()
)
rsStpDefaultHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpDefaultHelloTime.setStatus("mandatory")


class _RsStpDefaultMaxAgingTime_Type(Integer32):
    """Custom type rsStpDefaultMaxAgingTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_RsStpDefaultMaxAgingTime_Type.__name__ = "Integer32"
_RsStpDefaultMaxAgingTime_Object = MibScalar
rsStpDefaultMaxAgingTime = _RsStpDefaultMaxAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 4),
    _RsStpDefaultMaxAgingTime_Type()
)
rsStpDefaultMaxAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpDefaultMaxAgingTime.setStatus("mandatory")


class _RsStpDefaultForwardDelayTime_Type(Integer32):
    """Custom type rsStpDefaultForwardDelayTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_RsStpDefaultForwardDelayTime_Type.__name__ = "Integer32"
_RsStpDefaultForwardDelayTime_Object = MibScalar
rsStpDefaultForwardDelayTime = _RsStpDefaultForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 5),
    _RsStpDefaultForwardDelayTime_Type()
)
rsStpDefaultForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpDefaultForwardDelayTime.setStatus("mandatory")


class _RsStpDefaultPortPriority_Type(Integer32):
    """Custom type rsStpDefaultPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_RsStpDefaultPortPriority_Type.__name__ = "Integer32"
_RsStpDefaultPortPriority_Object = MibScalar
rsStpDefaultPortPriority = _RsStpDefaultPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 6),
    _RsStpDefaultPortPriority_Type()
)
rsStpDefaultPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpDefaultPortPriority.setStatus("mandatory")
_RsStpInstancesTable_Object = MibTable
rsStpInstancesTable = _RsStpInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7)
)
if mibBuilder.loadTexts:
    rsStpInstancesTable.setStatus("mandatory")
_RsStpInstanceEntry_Object = MibTableRow
rsStpInstanceEntry = _RsStpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1)
)
rsStpInstanceEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsStpInstanceVlanId"),
)
if mibBuilder.loadTexts:
    rsStpInstanceEntry.setStatus("mandatory")
_RsStpInstanceVlanId_Type = Integer32
_RsStpInstanceVlanId_Object = MibTableColumn
rsStpInstanceVlanId = _RsStpInstanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 1),
    _RsStpInstanceVlanId_Type()
)
rsStpInstanceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpInstanceVlanId.setStatus("mandatory")


class _RsStpInstanceBridgePriority_Type(Integer32):
    """Custom type rsStpInstanceBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_RsStpInstanceBridgePriority_Type.__name__ = "Integer32"
_RsStpInstanceBridgePriority_Object = MibTableColumn
rsStpInstanceBridgePriority = _RsStpInstanceBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 2),
    _RsStpInstanceBridgePriority_Type()
)
rsStpInstanceBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpInstanceBridgePriority.setStatus("mandatory")


class _RsStpInstanceHelloTime_Type(Integer32):
    """Custom type rsStpInstanceHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsStpInstanceHelloTime_Type.__name__ = "Integer32"
_RsStpInstanceHelloTime_Object = MibTableColumn
rsStpInstanceHelloTime = _RsStpInstanceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 3),
    _RsStpInstanceHelloTime_Type()
)
rsStpInstanceHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpInstanceHelloTime.setStatus("mandatory")


class _RsStpInstanceMaxAgingTime_Type(Integer32):
    """Custom type rsStpInstanceMaxAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_RsStpInstanceMaxAgingTime_Type.__name__ = "Integer32"
_RsStpInstanceMaxAgingTime_Object = MibTableColumn
rsStpInstanceMaxAgingTime = _RsStpInstanceMaxAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 4),
    _RsStpInstanceMaxAgingTime_Type()
)
rsStpInstanceMaxAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpInstanceMaxAgingTime.setStatus("mandatory")


class _RsStpInstanceForwardDelayTime_Type(Integer32):
    """Custom type rsStpInstanceForwardDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_RsStpInstanceForwardDelayTime_Type.__name__ = "Integer32"
_RsStpInstanceForwardDelayTime_Object = MibTableColumn
rsStpInstanceForwardDelayTime = _RsStpInstanceForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 5),
    _RsStpInstanceForwardDelayTime_Type()
)
rsStpInstanceForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpInstanceForwardDelayTime.setStatus("mandatory")
_RsStpInstanceEnabled_Type = FeatureStatus
_RsStpInstanceEnabled_Object = MibTableColumn
rsStpInstanceEnabled = _RsStpInstanceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 6),
    _RsStpInstanceEnabled_Type()
)
rsStpInstanceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpInstanceEnabled.setStatus("mandatory")
_RsStpInstanceRootId_Type = DisplayString
_RsStpInstanceRootId_Object = MibTableColumn
rsStpInstanceRootId = _RsStpInstanceRootId_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 7),
    _RsStpInstanceRootId_Type()
)
rsStpInstanceRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpInstanceRootId.setStatus("mandatory")
_RsStpInstanceRootPathCost_Type = Integer32
_RsStpInstanceRootPathCost_Object = MibTableColumn
rsStpInstanceRootPathCost = _RsStpInstanceRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 8),
    _RsStpInstanceRootPathCost_Type()
)
rsStpInstanceRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpInstanceRootPathCost.setStatus("mandatory")
_RsStpInstanceDesignatedBridgeId_Type = DisplayString
_RsStpInstanceDesignatedBridgeId_Object = MibTableColumn
rsStpInstanceDesignatedBridgeId = _RsStpInstanceDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 9),
    _RsStpInstanceDesignatedBridgeId_Type()
)
rsStpInstanceDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpInstanceDesignatedBridgeId.setStatus("mandatory")
_RsStpInstanceDesignatedPortId_Type = Integer32
_RsStpInstanceDesignatedPortId_Object = MibTableColumn
rsStpInstanceDesignatedPortId = _RsStpInstanceDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 7, 1, 10),
    _RsStpInstanceDesignatedPortId_Type()
)
rsStpInstanceDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpInstanceDesignatedPortId.setStatus("mandatory")
_RsStpPortTable_Object = MibTable
rsStpPortTable = _RsStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8)
)
if mibBuilder.loadTexts:
    rsStpPortTable.setStatus("mandatory")
_RsStpPortEntry_Object = MibTableRow
rsStpPortEntry = _RsStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1)
)
rsStpPortEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsStpPortId"),
)
if mibBuilder.loadTexts:
    rsStpPortEntry.setStatus("mandatory")
_RsStpPortId_Type = Integer32
_RsStpPortId_Object = MibTableColumn
rsStpPortId = _RsStpPortId_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 1),
    _RsStpPortId_Type()
)
rsStpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpPortId.setStatus("mandatory")
_RsStpPortVlanId_Type = Integer32
_RsStpPortVlanId_Object = MibTableColumn
rsStpPortVlanId = _RsStpPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 2),
    _RsStpPortVlanId_Type()
)
rsStpPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpPortVlanId.setStatus("mandatory")


class _RsStpPortPriority_Type(Integer32):
    """Custom type rsStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_RsStpPortPriority_Type.__name__ = "Integer32"
_RsStpPortPriority_Object = MibTableColumn
rsStpPortPriority = _RsStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 3),
    _RsStpPortPriority_Type()
)
rsStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpPortPriority.setStatus("mandatory")


class _RsStpPortPathCost_Type(Integer32):
    """Custom type rsStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsStpPortPathCost_Type.__name__ = "Integer32"
_RsStpPortPathCost_Object = MibTableColumn
rsStpPortPathCost = _RsStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 4),
    _RsStpPortPathCost_Type()
)
rsStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpPortPathCost.setStatus("mandatory")
_RsStpPortModeFast_Type = FeatureStatus
_RsStpPortModeFast_Object = MibTableColumn
rsStpPortModeFast = _RsStpPortModeFast_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 5),
    _RsStpPortModeFast_Type()
)
rsStpPortModeFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpPortModeFast.setStatus("mandatory")
_RsStpPortEnabled_Type = FeatureStatus
_RsStpPortEnabled_Object = MibTableColumn
rsStpPortEnabled = _RsStpPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 6),
    _RsStpPortEnabled_Type()
)
rsStpPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpPortEnabled.setStatus("mandatory")


class _RsStpPortState_Type(Integer32):
    """Custom type rsStpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("learning", 2),
          ("forwarding", 3))
    )


_RsStpPortState_Type.__name__ = "Integer32"
_RsStpPortState_Object = MibTableColumn
rsStpPortState = _RsStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 7),
    _RsStpPortState_Type()
)
rsStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpPortState.setStatus("mandatory")


class _RsStpPortRole_Type(Integer32):
    """Custom type rsStpPortRole based on Integer32"""
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
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backup", 5))
    )


_RsStpPortRole_Type.__name__ = "Integer32"
_RsStpPortRole_Object = MibTableColumn
rsStpPortRole = _RsStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 89, 30, 8, 1, 8),
    _RsStpPortRole_Type()
)
rsStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpPortRole.setStatus("mandatory")
_RndApplications_ObjectIdentity = ObjectIdentity
rndApplications = _RndApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35)
)
_RsServerDispatcher_ObjectIdentity = ObjectIdentity
rsServerDispatcher = _RsServerDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1)
)
_RsWSDServerStatTable_Object = MibTable
rsWSDServerStatTable = _RsWSDServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12)
)
if mibBuilder.loadTexts:
    rsWSDServerStatTable.setStatus("mandatory")
_RsWSDServerStatEntry_Object = MibTableRow
rsWSDServerStatEntry = _RsWSDServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1)
)
rsWSDServerStatEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDSerStatName"),
)
if mibBuilder.loadTexts:
    rsWSDServerStatEntry.setStatus("mandatory")


class _RsWSDSerStatName_Type(DisplayString):
    """Custom type rsWSDSerStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsWSDSerStatName_Type.__name__ = "DisplayString"
_RsWSDSerStatName_Object = MibTableColumn
rsWSDSerStatName = _RsWSDSerStatName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 1),
    _RsWSDSerStatName_Type()
)
rsWSDSerStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatName.setStatus("mandatory")
_RsWSDSerStatAttUsersNum_Type = Integer32
_RsWSDSerStatAttUsersNum_Object = MibTableColumn
rsWSDSerStatAttUsersNum = _RsWSDSerStatAttUsersNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 2),
    _RsWSDSerStatAttUsersNum_Type()
)
rsWSDSerStatAttUsersNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatAttUsersNum.setStatus("mandatory")
_RsWSDSerStatPeakLoad_Type = Integer32
_RsWSDSerStatPeakLoad_Object = MibTableColumn
rsWSDSerStatPeakLoad = _RsWSDSerStatPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 3),
    _RsWSDSerStatPeakLoad_Type()
)
rsWSDSerStatPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatPeakLoad.setStatus("mandatory")
_RsWSDSerStatFramesRate_Type = Integer32
_RsWSDSerStatFramesRate_Object = MibTableColumn
rsWSDSerStatFramesRate = _RsWSDSerStatFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 4),
    _RsWSDSerStatFramesRate_Type()
)
rsWSDSerStatFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatFramesRate.setStatus("mandatory")
_RsWSDSerStatFramesLoad_Type = Counter32
_RsWSDSerStatFramesLoad_Object = MibTableColumn
rsWSDSerStatFramesLoad = _RsWSDSerStatFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 5),
    _RsWSDSerStatFramesLoad_Type()
)
rsWSDSerStatFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatFramesLoad.setStatus("mandatory")
_RsWSDSerStatRecoveryTime_Type = Integer32
_RsWSDSerStatRecoveryTime_Object = MibTableColumn
rsWSDSerStatRecoveryTime = _RsWSDSerStatRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 6),
    _RsWSDSerStatRecoveryTime_Type()
)
rsWSDSerStatRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatRecoveryTime.setStatus("mandatory")
_RsWSDSerStatWarmUpTime_Type = Integer32
_RsWSDSerStatWarmUpTime_Object = MibTableColumn
rsWSDSerStatWarmUpTime = _RsWSDSerStatWarmUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 7),
    _RsWSDSerStatWarmUpTime_Type()
)
rsWSDSerStatWarmUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatWarmUpTime.setStatus("mandatory")
_RsWSDSerStatConnectionLimit_Type = Integer32
_RsWSDSerStatConnectionLimit_Object = MibTableColumn
rsWSDSerStatConnectionLimit = _RsWSDSerStatConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 8),
    _RsWSDSerStatConnectionLimit_Type()
)
rsWSDSerStatConnectionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatConnectionLimit.setStatus("mandatory")


class _RsWSDSerStatAdminStatus_Type(Integer32):
    """Custom type rsWSDSerStatAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("connectionsShutdown", 2),
          ("sessionsShutdown", 3))
    )


_RsWSDSerStatAdminStatus_Type.__name__ = "Integer32"
_RsWSDSerStatAdminStatus_Object = MibTableColumn
rsWSDSerStatAdminStatus = _RsWSDSerStatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 9),
    _RsWSDSerStatAdminStatus_Type()
)
rsWSDSerStatAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatAdminStatus.setStatus("mandatory")
_RsWSDSerStatConnectionLimitReached_Type = Integer32
_RsWSDSerStatConnectionLimitReached_Object = MibTableColumn
rsWSDSerStatConnectionLimitReached = _RsWSDSerStatConnectionLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 10),
    _RsWSDSerStatConnectionLimitReached_Type()
)
rsWSDSerStatConnectionLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatConnectionLimitReached.setStatus("mandatory")
_WsdRedundTable_Object = MibTable
wsdRedundTable = _WsdRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16)
)
if mibBuilder.loadTexts:
    wsdRedundTable.setStatus("mandatory")
_WsdRedundEntry_Object = MibTableRow
wsdRedundEntry = _WsdRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1)
)
wsdRedundEntry.setIndexNames(
    (0, "RADWARE-MIB", "wsdRedundFarmAddr"),
    (0, "RADWARE-MIB", "wsdRedundMainWsdAddr"),
)
if mibBuilder.loadTexts:
    wsdRedundEntry.setStatus("mandatory")
_WsdRedundFarmAddr_Type = IpAddress
_WsdRedundFarmAddr_Object = MibTableColumn
wsdRedundFarmAddr = _WsdRedundFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 1),
    _WsdRedundFarmAddr_Type()
)
wsdRedundFarmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsdRedundFarmAddr.setStatus("mandatory")
_WsdRedundMainWsdAddr_Type = IpAddress
_WsdRedundMainWsdAddr_Object = MibTableColumn
wsdRedundMainWsdAddr = _WsdRedundMainWsdAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 2),
    _WsdRedundMainWsdAddr_Type()
)
wsdRedundMainWsdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsdRedundMainWsdAddr.setStatus("mandatory")


class _WsdRedundOperStatus_Type(Integer32):
    """Custom type wsdRedundOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WsdRedundOperStatus_Type.__name__ = "Integer32"
_WsdRedundOperStatus_Object = MibTableColumn
wsdRedundOperStatus = _WsdRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 3),
    _WsdRedundOperStatus_Type()
)
wsdRedundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsdRedundOperStatus.setStatus("mandatory")
_WsdRedundPollInterval_Type = Integer32
_WsdRedundPollInterval_Object = MibTableColumn
wsdRedundPollInterval = _WsdRedundPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 4),
    _WsdRedundPollInterval_Type()
)
wsdRedundPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsdRedundPollInterval.setStatus("mandatory")
_WsdRedundTimeout_Type = Integer32
_WsdRedundTimeout_Object = MibTableColumn
wsdRedundTimeout = _WsdRedundTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 5),
    _WsdRedundTimeout_Type()
)
wsdRedundTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsdRedundTimeout.setStatus("mandatory")


class _WsdRedundStatus_Type(Integer32):
    """Custom type wsdRedundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_WsdRedundStatus_Type.__name__ = "Integer32"
_WsdRedundStatus_Object = MibTableColumn
wsdRedundStatus = _WsdRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 6),
    _WsdRedundStatus_Type()
)
wsdRedundStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsdRedundStatus.setStatus("mandatory")


class _RsWSDNewEntryOnSourcePort_Type(Integer32):
    """Custom type rsWSDNewEntryOnSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDNewEntryOnSourcePort_Type.__name__ = "Integer32"
_RsWSDNewEntryOnSourcePort_Object = MibScalar
rsWSDNewEntryOnSourcePort = _RsWSDNewEntryOnSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 19),
    _RsWSDNewEntryOnSourcePort_Type()
)
rsWSDNewEntryOnSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNewEntryOnSourcePort.setStatus("mandatory")


class _RsWSDSelectServerOnSourcePort_Type(Integer32):
    """Custom type rsWSDSelectServerOnSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSelectServerOnSourcePort_Type.__name__ = "Integer32"
_RsWSDSelectServerOnSourcePort_Object = MibScalar
rsWSDSelectServerOnSourcePort = _RsWSDSelectServerOnSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 20),
    _RsWSDSelectServerOnSourcePort_Type()
)
rsWSDSelectServerOnSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSelectServerOnSourcePort.setStatus("mandatory")


class _RsWSDRedundancyMode_Type(Integer32):
    """Custom type rsWSDRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDRedundancyMode_Type.__name__ = "Integer32"
_RsWSDRedundancyMode_Object = MibScalar
rsWSDRedundancyMode = _RsWSDRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 21),
    _RsWSDRedundancyMode_Type()
)
rsWSDRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDRedundancyMode.setStatus("mandatory")


class _RsNsdMode_Type(Integer32):
    """Custom type rsNsdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slowMode", 1),
          ("fastMode", 2))
    )


_RsNsdMode_Type.__name__ = "Integer32"
_RsNsdMode_Object = MibScalar
rsNsdMode = _RsNsdMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 22),
    _RsNsdMode_Type()
)
rsNsdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsNsdMode.setStatus("mandatory")
_RsNsdWINSAddr_Type = IpAddress
_RsNsdWINSAddr_Object = MibScalar
rsNsdWINSAddr = _RsNsdWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 23),
    _RsNsdWINSAddr_Type()
)
rsNsdWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsNsdWINSAddr.setStatus("mandatory")


class _RsWSDSyslogStatus_Type(Integer32):
    """Custom type rsWSDSyslogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSyslogStatus_Type.__name__ = "Integer32"
_RsWSDSyslogStatus_Object = MibScalar
rsWSDSyslogStatus = _RsWSDSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 26),
    _RsWSDSyslogStatus_Type()
)
rsWSDSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogStatus.setStatus("mandatory")
_RsWSDSyslogAddress_Type = IpAddress
_RsWSDSyslogAddress_Object = MibScalar
rsWSDSyslogAddress = _RsWSDSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 27),
    _RsWSDSyslogAddress_Type()
)
rsWSDSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogAddress.setStatus("mandatory")
_RsWSDNTCheckTable_Object = MibTable
rsWSDNTCheckTable = _RsWSDNTCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28)
)
if mibBuilder.loadTexts:
    rsWSDNTCheckTable.setStatus("mandatory")
_RsWSDNTCheckEntry_Object = MibTableRow
rsWSDNTCheckEntry = _RsWSDNTCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1)
)
rsWSDNTCheckEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDNTSerialNum"),
)
if mibBuilder.loadTexts:
    rsWSDNTCheckEntry.setStatus("mandatory")
_RsWSDNTSerialNum_Type = Integer32
_RsWSDNTSerialNum_Object = MibTableColumn
rsWSDNTSerialNum = _RsWSDNTSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 1),
    _RsWSDNTSerialNum_Type()
)
rsWSDNTSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNTSerialNum.setStatus("mandatory")
_RsWSDNTFrequentCheckPeriod_Type = Integer32
_RsWSDNTFrequentCheckPeriod_Object = MibTableColumn
rsWSDNTFrequentCheckPeriod = _RsWSDNTFrequentCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 2),
    _RsWSDNTFrequentCheckPeriod_Type()
)
rsWSDNTFrequentCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTFrequentCheckPeriod.setStatus("mandatory")
_RsWSDNTOpenSessionsWeight_Type = Integer32
_RsWSDNTOpenSessionsWeight_Object = MibTableColumn
rsWSDNTOpenSessionsWeight = _RsWSDNTOpenSessionsWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 3),
    _RsWSDNTOpenSessionsWeight_Type()
)
rsWSDNTOpenSessionsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTOpenSessionsWeight.setStatus("mandatory")
_RsWSDNTIncomingTrafficWeight_Type = Integer32
_RsWSDNTIncomingTrafficWeight_Object = MibTableColumn
rsWSDNTIncomingTrafficWeight = _RsWSDNTIncomingTrafficWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 4),
    _RsWSDNTIncomingTrafficWeight_Type()
)
rsWSDNTIncomingTrafficWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTIncomingTrafficWeight.setStatus("mandatory")
_RsWSDNTOutgoingTrafficWeight_Type = Integer32
_RsWSDNTOutgoingTrafficWeight_Object = MibTableColumn
rsWSDNTOutgoingTrafficWeight = _RsWSDNTOutgoingTrafficWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 5),
    _RsWSDNTOutgoingTrafficWeight_Type()
)
rsWSDNTOutgoingTrafficWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTOutgoingTrafficWeight.setStatus("mandatory")
_RsWSDNTRegularCheckPeriod_Type = Integer32
_RsWSDNTRegularCheckPeriod_Object = MibTableColumn
rsWSDNTRegularCheckPeriod = _RsWSDNTRegularCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 6),
    _RsWSDNTRegularCheckPeriod_Type()
)
rsWSDNTRegularCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTRegularCheckPeriod.setStatus("mandatory")
_RsWSDNTAvResponseWeight_Type = Integer32
_RsWSDNTAvResponseWeight_Object = MibTableColumn
rsWSDNTAvResponseWeight = _RsWSDNTAvResponseWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 7),
    _RsWSDNTAvResponseWeight_Type()
)
rsWSDNTAvResponseWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTAvResponseWeight.setStatus("mandatory")
_RsWSDNTUsersLimitWeight_Type = Integer32
_RsWSDNTUsersLimitWeight_Object = MibTableColumn
rsWSDNTUsersLimitWeight = _RsWSDNTUsersLimitWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 8),
    _RsWSDNTUsersLimitWeight_Type()
)
rsWSDNTUsersLimitWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTUsersLimitWeight.setStatus("mandatory")
_RsWSDNTTCPLimitWeight_Type = Integer32
_RsWSDNTTCPLimitWeight_Object = MibTableColumn
rsWSDNTTCPLimitWeight = _RsWSDNTTCPLimitWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 9),
    _RsWSDNTTCPLimitWeight_Type()
)
rsWSDNTTCPLimitWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTTCPLimitWeight.setStatus("mandatory")
_RsWSDNTRetries_Type = Integer32
_RsWSDNTRetries_Object = MibTableColumn
rsWSDNTRetries = _RsWSDNTRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 10),
    _RsWSDNTRetries_Type()
)
rsWSDNTRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTRetries.setStatus("mandatory")


class _RsWSDNTCommunity_Type(DisplayString):
    """Custom type rsWSDNTCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsWSDNTCommunity_Type.__name__ = "DisplayString"
_RsWSDNTCommunity_Object = MibTableColumn
rsWSDNTCommunity = _RsWSDNTCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 11),
    _RsWSDNTCommunity_Type()
)
rsWSDNTCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTCommunity.setStatus("mandatory")
_RsWSDPrivateCheckTable_Object = MibTable
rsWSDPrivateCheckTable = _RsWSDPrivateCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29)
)
if mibBuilder.loadTexts:
    rsWSDPrivateCheckTable.setStatus("mandatory")
_RsWSDPrivateCheckEntry_Object = MibTableRow
rsWSDPrivateCheckEntry = _RsWSDPrivateCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1)
)
rsWSDPrivateCheckEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDPrivateSerialNum"),
)
if mibBuilder.loadTexts:
    rsWSDPrivateCheckEntry.setStatus("mandatory")
_RsWSDPrivateSerialNum_Type = Integer32
_RsWSDPrivateSerialNum_Object = MibTableColumn
rsWSDPrivateSerialNum = _RsWSDPrivateSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 1),
    _RsWSDPrivateSerialNum_Type()
)
rsWSDPrivateSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPrivateSerialNum.setStatus("mandatory")
_RsWSDPrivateSpecialCheckPeriod_Type = Integer32
_RsWSDPrivateSpecialCheckPeriod_Object = MibTableColumn
rsWSDPrivateSpecialCheckPeriod = _RsWSDPrivateSpecialCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 2),
    _RsWSDPrivateSpecialCheckPeriod_Type()
)
rsWSDPrivateSpecialCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateSpecialCheckPeriod.setStatus("mandatory")
_RsWSDPrivateExtraVar1ID_Type = ObjectIdentifier
_RsWSDPrivateExtraVar1ID_Object = MibTableColumn
rsWSDPrivateExtraVar1ID = _RsWSDPrivateExtraVar1ID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 3),
    _RsWSDPrivateExtraVar1ID_Type()
)
rsWSDPrivateExtraVar1ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar1ID.setStatus("mandatory")
_RsWSDPrivateExtraVar1Weight_Type = Integer32
_RsWSDPrivateExtraVar1Weight_Object = MibTableColumn
rsWSDPrivateExtraVar1Weight = _RsWSDPrivateExtraVar1Weight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 4),
    _RsWSDPrivateExtraVar1Weight_Type()
)
rsWSDPrivateExtraVar1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar1Weight.setStatus("mandatory")
_RsWSDPrivateExtraVar2ID_Type = ObjectIdentifier
_RsWSDPrivateExtraVar2ID_Object = MibTableColumn
rsWSDPrivateExtraVar2ID = _RsWSDPrivateExtraVar2ID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 5),
    _RsWSDPrivateExtraVar2ID_Type()
)
rsWSDPrivateExtraVar2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar2ID.setStatus("mandatory")
_RsWSDPrivateExtraVar2Weight_Type = Integer32
_RsWSDPrivateExtraVar2Weight_Object = MibTableColumn
rsWSDPrivateExtraVar2Weight = _RsWSDPrivateExtraVar2Weight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 6),
    _RsWSDPrivateExtraVar2Weight_Type()
)
rsWSDPrivateExtraVar2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar2Weight.setStatus("mandatory")
_RsWSDPrivateRetries_Type = Integer32
_RsWSDPrivateRetries_Object = MibTableColumn
rsWSDPrivateRetries = _RsWSDPrivateRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 7),
    _RsWSDPrivateRetries_Type()
)
rsWSDPrivateRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateRetries.setStatus("mandatory")


class _RsWSDPrivateCommunity_Type(DisplayString):
    """Custom type rsWSDPrivateCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsWSDPrivateCommunity_Type.__name__ = "DisplayString"
_RsWSDPrivateCommunity_Object = MibTableColumn
rsWSDPrivateCommunity = _RsWSDPrivateCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 8),
    _RsWSDPrivateCommunity_Type()
)
rsWSDPrivateCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateCommunity.setStatus("mandatory")


class _RsWSDPrivateExtraVar1Mode_Type(Integer32):
    """Custom type rsWSDPrivateExtraVar1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_RsWSDPrivateExtraVar1Mode_Type.__name__ = "Integer32"
_RsWSDPrivateExtraVar1Mode_Object = MibTableColumn
rsWSDPrivateExtraVar1Mode = _RsWSDPrivateExtraVar1Mode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 9),
    _RsWSDPrivateExtraVar1Mode_Type()
)
rsWSDPrivateExtraVar1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar1Mode.setStatus("mandatory")


class _RsWSDPrivateExtraVar2Mode_Type(Integer32):
    """Custom type rsWSDPrivateExtraVar2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_RsWSDPrivateExtraVar2Mode_Type.__name__ = "Integer32"
_RsWSDPrivateExtraVar2Mode_Object = MibTableColumn
rsWSDPrivateExtraVar2Mode = _RsWSDPrivateExtraVar2Mode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 10),
    _RsWSDPrivateExtraVar2Mode_Type()
)
rsWSDPrivateExtraVar2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar2Mode.setStatus("mandatory")


class _RsWSDDNSResolution_Type(Integer32):
    """Custom type rsWSDDNSResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("proximity", 3))
    )


_RsWSDDNSResolution_Type.__name__ = "Integer32"
_RsWSDDNSResolution_Object = MibScalar
rsWSDDNSResolution = _RsWSDDNSResolution_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 31),
    _RsWSDDNSResolution_Type()
)
rsWSDDNSResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDNSResolution.setStatus("mandatory")


class _RsIGTransitTimeout_Type(Integer32):
    """Custom type rsIGTransitTimeout based on Integer32"""
    defaultValue = 4


_RsIGTransitTimeout_Type.__name__ = "Integer32"
_RsIGTransitTimeout_Object = MibScalar
rsIGTransitTimeout = _RsIGTransitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32),
    _RsIGTransitTimeout_Type()
)
rsIGTransitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIGTransitTimeout.setStatus("mandatory")


class _RsWSDUserPassword_Type(DisplayString):
    """Custom type rsWSDUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RsWSDUserPassword_Type.__name__ = "DisplayString"
_RsWSDUserPassword_Object = MibScalar
rsWSDUserPassword = _RsWSDUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 33),
    _RsWSDUserPassword_Type()
)
rsWSDUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUserPassword.setStatus("mandatory")


class _RsWSDUserVersion_Type(DisplayString):
    """Custom type rsWSDUserVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RsWSDUserVersion_Type.__name__ = "DisplayString"
_RsWSDUserVersion_Object = MibScalar
rsWSDUserVersion = _RsWSDUserVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 34),
    _RsWSDUserVersion_Type()
)
rsWSDUserVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUserVersion.setStatus("mandatory")


class _RsWSDNatStatus_Type(Integer32):
    """Custom type rsWSDNatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDNatStatus_Type.__name__ = "Integer32"
_RsWSDNatStatus_Object = MibScalar
rsWSDNatStatus = _RsWSDNatStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 35),
    _RsWSDNatStatus_Type()
)
rsWSDNatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNatStatus.setStatus("mandatory")


class _RsWSDRedundancyTakeback_Type(Integer32):
    """Custom type rsWSDRedundancyTakeback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_RsWSDRedundancyTakeback_Type.__name__ = "Integer32"
_RsWSDRedundancyTakeback_Object = MibScalar
rsWSDRedundancyTakeback = _RsWSDRedundancyTakeback_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 37),
    _RsWSDRedundancyTakeback_Type()
)
rsWSDRedundancyTakeback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDRedundancyTakeback.setStatus("mandatory")
_RsMLB_ObjectIdentity = ObjectIdentity
rsMLB = _RsMLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38)
)
_RsCSD_ObjectIdentity = ObjectIdentity
rsCSD = _RsCSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 39)
)
_RsNWSD_ObjectIdentity = ObjectIdentity
rsNWSD = _RsNWSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40)
)
_RsWSDIfTable_Object = MibTable
rsWSDIfTable = _RsWSDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41)
)
if mibBuilder.loadTexts:
    rsWSDIfTable.setStatus("mandatory")
_RsWSDIfEntry_Object = MibTableRow
rsWSDIfEntry = _RsWSDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1)
)
rsWSDIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDIfIndex"),
)
if mibBuilder.loadTexts:
    rsWSDIfEntry.setStatus("mandatory")
_RsWSDIfIndex_Type = Integer32
_RsWSDIfIndex_Object = MibTableColumn
rsWSDIfIndex = _RsWSDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 1),
    _RsWSDIfIndex_Type()
)
rsWSDIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfIndex.setStatus("mandatory")
_RsWSDIfBoardNum_Type = Integer32
_RsWSDIfBoardNum_Object = MibTableColumn
rsWSDIfBoardNum = _RsWSDIfBoardNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 2),
    _RsWSDIfBoardNum_Type()
)
rsWSDIfBoardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfBoardNum.setStatus("mandatory")
_RsWSDIfNetAddress_Type = IpAddress
_RsWSDIfNetAddress_Object = MibTableColumn
rsWSDIfNetAddress = _RsWSDIfNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 3),
    _RsWSDIfNetAddress_Type()
)
rsWSDIfNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfNetAddress.setStatus("mandatory")


class _RsWSDIfStatus_Type(Integer32):
    """Custom type rsWSDIfStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("okSingleBrg", 2),
          ("okMultiBrg", 3),
          ("connctFault", 4),
          ("rxFault", 5),
          ("txFault", 6),
          ("channelLoopback", 7),
          ("rxClockFault", 8),
          ("t1Alarm", 9))
    )


_RsWSDIfStatus_Type.__name__ = "Integer32"
_RsWSDIfStatus_Object = MibTableColumn
rsWSDIfStatus = _RsWSDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 4),
    _RsWSDIfStatus_Type()
)
rsWSDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfStatus.setStatus("mandatory")


class _RsWSDIfClockType_Type(Integer32):
    """Custom type rsWSDIfClockType based on Integer32"""
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
        *(("external", 1),
          ("internal", 2),
          ("t1", 3),
          ("g703", 4))
    )


_RsWSDIfClockType_Type.__name__ = "Integer32"
_RsWSDIfClockType_Object = MibTableColumn
rsWSDIfClockType = _RsWSDIfClockType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 5),
    _RsWSDIfClockType_Type()
)
rsWSDIfClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfClockType.setStatus("mandatory")
_RsWSDIfBaudRate_Type = Integer32
_RsWSDIfBaudRate_Object = MibTableColumn
rsWSDIfBaudRate = _RsWSDIfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 6),
    _RsWSDIfBaudRate_Type()
)
rsWSDIfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfBaudRate.setStatus("mandatory")
_RsWSDIfCost_Type = Integer32
_RsWSDIfCost_Object = MibTableColumn
rsWSDIfCost = _RsWSDIfCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 7),
    _RsWSDIfCost_Type()
)
rsWSDIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfCost.setStatus("mandatory")


class _RsWSDIfCompression_Type(Integer32):
    """Custom type rsWSDIfCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDIfCompression_Type.__name__ = "Integer32"
_RsWSDIfCompression_Object = MibTableColumn
rsWSDIfCompression = _RsWSDIfCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 8),
    _RsWSDIfCompression_Type()
)
rsWSDIfCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfCompression.setStatus("mandatory")


class _RsWSDIfCompressionStatus_Type(Integer32):
    """Custom type rsWSDIfCompressionStatus based on Integer32"""
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
        *(("not-inserted", 1),
          ("active", 2),
          ("not-active", 3),
          ("disable", 4))
    )


_RsWSDIfCompressionStatus_Type.__name__ = "Integer32"
_RsWSDIfCompressionStatus_Object = MibTableColumn
rsWSDIfCompressionStatus = _RsWSDIfCompressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 9),
    _RsWSDIfCompressionStatus_Type()
)
rsWSDIfCompressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfCompressionStatus.setStatus("mandatory")
_RsWSDIfCompressionRate_Type = Integer32
_RsWSDIfCompressionRate_Object = MibTableColumn
rsWSDIfCompressionRate = _RsWSDIfCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 10),
    _RsWSDIfCompressionRate_Type()
)
rsWSDIfCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfCompressionRate.setStatus("mandatory")


class _RsWSDIfLATCompression_Type(Integer32):
    """Custom type rsWSDIfLATCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDIfLATCompression_Type.__name__ = "Integer32"
_RsWSDIfLATCompression_Object = MibTableColumn
rsWSDIfLATCompression = _RsWSDIfLATCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 11),
    _RsWSDIfLATCompression_Type()
)
rsWSDIfLATCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfLATCompression.setStatus("mandatory")


class _RsWSDIfCompressionType_Type(Integer32):
    """Custom type rsWSDIfCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lowSpeed", 2),
          ("highSpeed", 3))
    )


_RsWSDIfCompressionType_Type.__name__ = "Integer32"
_RsWSDIfCompressionType_Object = MibTableColumn
rsWSDIfCompressionType = _RsWSDIfCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 12),
    _RsWSDIfCompressionType_Type()
)
rsWSDIfCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfCompressionType.setStatus("mandatory")


class _RsWSDIfFilterMode_Type(Integer32):
    """Custom type rsWSDIfFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destinationOnly", 1),
          ("sourceAndDestination", 2),
          ("none", 3))
    )


_RsWSDIfFilterMode_Type.__name__ = "Integer32"
_RsWSDIfFilterMode_Object = MibTableColumn
rsWSDIfFilterMode = _RsWSDIfFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 13),
    _RsWSDIfFilterMode_Type()
)
rsWSDIfFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfFilterMode.setStatus("mandatory")


class _RsWSDIfChannelType_Type(Integer32):
    """Custom type rsWSDIfChannelType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wanChannel", 1),
          ("ogRanPort", 2),
          ("routerToBridge", 3),
          ("spsFramRelay", 4),
          ("dialBackup", 5),
          ("snar", 6),
          ("lan", 7),
          ("spsX25", 8),
          ("frameRelay1490", 9),
          ("frameRelay1490CAR", 10),
          ("frameRelayCAR", 11),
          ("ppp", 12))
    )


_RsWSDIfChannelType_Type.__name__ = "Integer32"
_RsWSDIfChannelType_Object = MibTableColumn
rsWSDIfChannelType = _RsWSDIfChannelType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 14),
    _RsWSDIfChannelType_Type()
)
rsWSDIfChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfChannelType.setStatus("mandatory")


class _RsWSDIfBridge_Type(Integer32):
    """Custom type rsWSDIfBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDIfBridge_Type.__name__ = "Integer32"
_RsWSDIfBridge_Object = MibTableColumn
rsWSDIfBridge = _RsWSDIfBridge_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 15),
    _RsWSDIfBridge_Type()
)
rsWSDIfBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfBridge.setStatus("mandatory")


class _RsWSDHighPriorityIf_Type(Integer32):
    """Custom type rsWSDHighPriorityIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDHighPriorityIf_Type.__name__ = "Integer32"
_RsWSDHighPriorityIf_Object = MibTableColumn
rsWSDHighPriorityIf = _RsWSDHighPriorityIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 16),
    _RsWSDHighPriorityIf_Type()
)
rsWSDHighPriorityIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHighPriorityIf.setStatus("mandatory")


class _RsWSDWanHeader_Type(Integer32):
    """Custom type rsWSDWanHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("short", 2))
    )


_RsWSDWanHeader_Type.__name__ = "Integer32"
_RsWSDWanHeader_Object = MibTableColumn
rsWSDWanHeader = _RsWSDWanHeader_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 17),
    _RsWSDWanHeader_Type()
)
rsWSDWanHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWanHeader.setStatus("mandatory")


class _RsWSDDuplexMode_Type(Integer32):
    """Custom type rsWSDDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2),
          ("auto", 3))
    )


_RsWSDDuplexMode_Type.__name__ = "Integer32"
_RsWSDDuplexMode_Object = MibTableColumn
rsWSDDuplexMode = _RsWSDDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 18),
    _RsWSDDuplexMode_Type()
)
rsWSDDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDuplexMode.setStatus("mandatory")


class _RsWSDClientMirrorPercentage_Type(Integer32):
    """Custom type rsWSDClientMirrorPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDClientMirrorPercentage_Type.__name__ = "Integer32"
_RsWSDClientMirrorPercentage_Object = MibScalar
rsWSDClientMirrorPercentage = _RsWSDClientMirrorPercentage_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 42),
    _RsWSDClientMirrorPercentage_Type()
)
rsWSDClientMirrorPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientMirrorPercentage.setStatus("mandatory")


class _RsWSDMirrorStatus_Type(Integer32):
    """Custom type rsWSDMirrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDMirrorStatus_Type.__name__ = "Integer32"
_RsWSDMirrorStatus_Object = MibScalar
rsWSDMirrorStatus = _RsWSDMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 43),
    _RsWSDMirrorStatus_Type()
)
rsWSDMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMirrorStatus.setStatus("mandatory")


class _RsWSDMirrorProtocolMode_Type(Integer32):
    """Custom type rsWSDMirrorProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDMirrorProtocolMode_Type.__name__ = "Integer32"
_RsWSDMirrorProtocolMode_Object = MibScalar
rsWSDMirrorProtocolMode = _RsWSDMirrorProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 44),
    _RsWSDMirrorProtocolMode_Type()
)
rsWSDMirrorProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMirrorProtocolMode.setStatus("mandatory")
_RsWSDApplicationMirrorTable_Object = MibTable
rsWSDApplicationMirrorTable = _RsWSDApplicationMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45)
)
if mibBuilder.loadTexts:
    rsWSDApplicationMirrorTable.setStatus("mandatory")
_RsWSDApplicationMirrorEntry_Object = MibTableRow
rsWSDApplicationMirrorEntry = _RsWSDApplicationMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 1)
)
rsWSDApplicationMirrorEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDMirrorActiveAddress"),
)
if mibBuilder.loadTexts:
    rsWSDApplicationMirrorEntry.setStatus("mandatory")
_RsWSDMirrorActiveAddress_Type = IpAddress
_RsWSDMirrorActiveAddress_Object = MibTableColumn
rsWSDMirrorActiveAddress = _RsWSDMirrorActiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 1, 1),
    _RsWSDMirrorActiveAddress_Type()
)
rsWSDMirrorActiveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMirrorActiveAddress.setStatus("mandatory")


class _RsWSDMirrorActiveStatus_Type(Integer32):
    """Custom type rsWSDMirrorActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_RsWSDMirrorActiveStatus_Type.__name__ = "Integer32"
_RsWSDMirrorActiveStatus_Object = MibTableColumn
rsWSDMirrorActiveStatus = _RsWSDMirrorActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 1, 2),
    _RsWSDMirrorActiveStatus_Type()
)
rsWSDMirrorActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMirrorActiveStatus.setStatus("mandatory")
_RsWSDClientMirrorPollingTime_Type = Integer32
_RsWSDClientMirrorPollingTime_Object = MibScalar
rsWSDClientMirrorPollingTime = _RsWSDClientMirrorPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 46),
    _RsWSDClientMirrorPollingTime_Type()
)
rsWSDClientMirrorPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientMirrorPollingTime.setStatus("mandatory")


class _RsPlatformIdentifier_Type(Integer32):
    """Custom type rsPlatformIdentifier based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("vgate", 1),
          ("vgfe", 2),
          ("onecpu", 3),
          ("onecpuh", 4),
          ("boomer", 5),
          ("cougar", 6),
          ("argo", 7),
          ("kitty", 8),
          ("voyager", 9),
          ("galaxy", 10),
          ("ninia", 11),
          ("mecong", 12),
          ("congo", 13),
          ("ods1", 14),
          ("ods2", 15),
          ("ods3", 16),
          ("ods3S1", 17),
          ("ods3S2", 18),
          ("vl", 19),
          ("ods-ht", 20))
    )


_RsPlatformIdentifier_Type.__name__ = "Integer32"
_RsPlatformIdentifier_Object = MibScalar
rsPlatformIdentifier = _RsPlatformIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 47),
    _RsPlatformIdentifier_Type()
)
rsPlatformIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPlatformIdentifier.setStatus("mandatory")


class _RsConfigurationIdentifier_Type(Integer32):
    """Custom type rsConfigurationIdentifier based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("twoPorts", 1),
          ("fourPorts", 2),
          ("fixed-2", 3),
          ("fixed-8", 4),
          ("fixed-8-2", 5),
          ("fixed-16-5", 6),
          ("chassis", 7),
          ("fixed-7", 8),
          ("fixed-16-7-1", 9),
          ("fixed-9-1", 10),
          ("fixed-8cg-9fg-2fxg", 11),
          ("fixed-12cg-8fg", 12),
          ("fixed-3cg", 13),
          ("fixed-4-2", 14),
          ("fixed-12-4-2", 15),
          ("fixed-2-8-9", 16),
          ("fixed-4-4-8-2", 17),
          ("fixed-4-8-2", 18),
          ("fixed-6", 19),
          ("fixed-6-2", 20),
          ("fixed-4-20-2", 21))
    )


_RsConfigurationIdentifier_Type.__name__ = "Integer32"
_RsConfigurationIdentifier_Object = MibScalar
rsConfigurationIdentifier = _RsConfigurationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 48),
    _RsConfigurationIdentifier_Type()
)
rsConfigurationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsConfigurationIdentifier.setStatus("mandatory")


class _RsSWPasswordStatus_Type(Integer32):
    """Custom type rsSWPasswordStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("statusUnset", 1),
          ("passwordOK", 2),
          ("wrongPassword", 3))
    )


_RsSWPasswordStatus_Type.__name__ = "Integer32"
_RsSWPasswordStatus_Object = MibScalar
rsSWPasswordStatus = _RsSWPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 49),
    _RsSWPasswordStatus_Type()
)
rsSWPasswordStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSWPasswordStatus.setStatus("mandatory")
_RsWSDFlashSize_Type = Integer32
_RsWSDFlashSize_Object = MibScalar
rsWSDFlashSize = _RsWSDFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 50),
    _RsWSDFlashSize_Type()
)
rsWSDFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDFlashSize.setStatus("mandatory")
_RsWSDDRAMSize_Type = Integer32
_RsWSDDRAMSize_Object = MibScalar
rsWSDDRAMSize = _RsWSDDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 51),
    _RsWSDDRAMSize_Type()
)
rsWSDDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDDRAMSize.setStatus("mandatory")


class _RsWSDVLANRedundOperStatus_Type(Integer32):
    """Custom type rsWSDVLANRedundOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockBroadcast", 1),
          ("forwardTraffic", 2),
          ("blockAll", 3))
    )


_RsWSDVLANRedundOperStatus_Type.__name__ = "Integer32"
_RsWSDVLANRedundOperStatus_Object = MibScalar
rsWSDVLANRedundOperStatus = _RsWSDVLANRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 52),
    _RsWSDVLANRedundOperStatus_Type()
)
rsWSDVLANRedundOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVLANRedundOperStatus.setStatus("mandatory")


class _RsWSDResourceUtilization_Type(Integer32):
    """Custom type rsWSDResourceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDResourceUtilization_Type.__name__ = "Integer32"
_RsWSDResourceUtilization_Object = MibScalar
rsWSDResourceUtilization = _RsWSDResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 53),
    _RsWSDResourceUtilization_Type()
)
rsWSDResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDResourceUtilization.setStatus("mandatory")


class _RsWSDRSResourceUtilization_Type(Integer32):
    """Custom type rsWSDRSResourceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDRSResourceUtilization_Type.__name__ = "Integer32"
_RsWSDRSResourceUtilization_Object = MibScalar
rsWSDRSResourceUtilization = _RsWSDRSResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 54),
    _RsWSDRSResourceUtilization_Type()
)
rsWSDRSResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDRSResourceUtilization.setStatus("mandatory")


class _RsWSDREResourceUtilization_Type(Integer32):
    """Custom type rsWSDREResourceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDREResourceUtilization_Type.__name__ = "Integer32"
_RsWSDREResourceUtilization_Object = MibScalar
rsWSDREResourceUtilization = _RsWSDREResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 55),
    _RsWSDREResourceUtilization_Type()
)
rsWSDREResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDREResourceUtilization.setStatus("mandatory")
_RsWSDBuildNumber_Type = DisplayString
_RsWSDBuildNumber_Object = MibScalar
rsWSDBuildNumber = _RsWSDBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 56),
    _RsWSDBuildNumber_Type()
)
rsWSDBuildNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDBuildNumber.setStatus("mandatory")


class _RsWSDUseOneTrap_Type(Integer32):
    """Custom type rsWSDUseOneTrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDUseOneTrap_Type.__name__ = "Integer32"
_RsWSDUseOneTrap_Object = MibScalar
rsWSDUseOneTrap = _RsWSDUseOneTrap_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 57),
    _RsWSDUseOneTrap_Type()
)
rsWSDUseOneTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUseOneTrap.setStatus("mandatory")
_RsWSDSecuredComm_ObjectIdentity = ObjectIdentity
rsWSDSecuredComm = _RsWSDSecuredComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58)
)
_RsWSDSCProtcolsTable_Object = MibTable
rsWSDSCProtcolsTable = _RsWSDSCProtcolsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1)
)
if mibBuilder.loadTexts:
    rsWSDSCProtcolsTable.setStatus("mandatory")
_RsWSDSCProtcolsEntry_Object = MibTableRow
rsWSDSCProtcolsEntry = _RsWSDSCProtcolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1, 1)
)
rsWSDSCProtcolsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDSCProtocol"),
)
if mibBuilder.loadTexts:
    rsWSDSCProtcolsEntry.setStatus("mandatory")


class _RsWSDSCProtocol_Type(Integer32):
    """Custom type rsWSDSCProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("tftp", 2),
          ("lrp", 3),
          ("prp", 4),
          ("srp", 5),
          ("mirror", 6))
    )


_RsWSDSCProtocol_Type.__name__ = "Integer32"
_RsWSDSCProtocol_Object = MibTableColumn
rsWSDSCProtocol = _RsWSDSCProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1, 1, 1),
    _RsWSDSCProtocol_Type()
)
rsWSDSCProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSCProtocol.setStatus("mandatory")


class _RsWSDSCProtocolStatus_Type(Integer32):
    """Custom type rsWSDSCProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 1),
          ("notEncrypted", 2))
    )


_RsWSDSCProtocolStatus_Type.__name__ = "Integer32"
_RsWSDSCProtocolStatus_Object = MibTableColumn
rsWSDSCProtocolStatus = _RsWSDSCProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1, 1, 2),
    _RsWSDSCProtocolStatus_Type()
)
rsWSDSCProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSCProtocolStatus.setStatus("mandatory")
_RsWSDSNMPPortsTable_Object = MibTable
rsWSDSNMPPortsTable = _RsWSDSNMPPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59)
)
if mibBuilder.loadTexts:
    rsWSDSNMPPortsTable.setStatus("mandatory")
_RsWSDSNMPPortsEntry_Object = MibTableRow
rsWSDSNMPPortsEntry = _RsWSDSNMPPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1)
)
rsWSDSNMPPortsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDSNMPPhysicalPortNumber"),
)
if mibBuilder.loadTexts:
    rsWSDSNMPPortsEntry.setStatus("mandatory")
_RsWSDSNMPPhysicalPortNumber_Type = Integer32
_RsWSDSNMPPhysicalPortNumber_Object = MibTableColumn
rsWSDSNMPPhysicalPortNumber = _RsWSDSNMPPhysicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 1),
    _RsWSDSNMPPhysicalPortNumber_Type()
)
rsWSDSNMPPhysicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortNumber.setStatus("mandatory")


class _RsWSDSNMPPhysicalPortState_Type(Integer32):
    """Custom type rsWSDSNMPPhysicalPortState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSNMPPhysicalPortState_Type.__name__ = "Integer32"
_RsWSDSNMPPhysicalPortState_Object = MibTableColumn
rsWSDSNMPPhysicalPortState = _RsWSDSNMPPhysicalPortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 2),
    _RsWSDSNMPPhysicalPortState_Type()
)
rsWSDSNMPPhysicalPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortState.setStatus("mandatory")


class _RsWSDSNMPPhysicalPortTelnetState_Type(Integer32):
    """Custom type rsWSDSNMPPhysicalPortTelnetState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSNMPPhysicalPortTelnetState_Type.__name__ = "Integer32"
_RsWSDSNMPPhysicalPortTelnetState_Object = MibTableColumn
rsWSDSNMPPhysicalPortTelnetState = _RsWSDSNMPPhysicalPortTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 3),
    _RsWSDSNMPPhysicalPortTelnetState_Type()
)
rsWSDSNMPPhysicalPortTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortTelnetState.setStatus("mandatory")


class _RsWSDSNMPPhysicalPortSSHState_Type(Integer32):
    """Custom type rsWSDSNMPPhysicalPortSSHState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSNMPPhysicalPortSSHState_Type.__name__ = "Integer32"
_RsWSDSNMPPhysicalPortSSHState_Object = MibTableColumn
rsWSDSNMPPhysicalPortSSHState = _RsWSDSNMPPhysicalPortSSHState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 4),
    _RsWSDSNMPPhysicalPortSSHState_Type()
)
rsWSDSNMPPhysicalPortSSHState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortSSHState.setStatus("mandatory")


class _RsWSDSNMPPhysicalPortWebState_Type(Integer32):
    """Custom type rsWSDSNMPPhysicalPortWebState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSNMPPhysicalPortWebState_Type.__name__ = "Integer32"
_RsWSDSNMPPhysicalPortWebState_Object = MibTableColumn
rsWSDSNMPPhysicalPortWebState = _RsWSDSNMPPhysicalPortWebState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 5),
    _RsWSDSNMPPhysicalPortWebState_Type()
)
rsWSDSNMPPhysicalPortWebState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortWebState.setStatus("mandatory")


class _RsWSDSNMPPhysicalPortSSLState_Type(Integer32):
    """Custom type rsWSDSNMPPhysicalPortSSLState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSNMPPhysicalPortSSLState_Type.__name__ = "Integer32"
_RsWSDSNMPPhysicalPortSSLState_Object = MibTableColumn
rsWSDSNMPPhysicalPortSSLState = _RsWSDSNMPPhysicalPortSSLState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 6),
    _RsWSDSNMPPhysicalPortSSLState_Type()
)
rsWSDSNMPPhysicalPortSSLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortSSLState.setStatus("mandatory")
_RsBWM_ObjectIdentity = ObjectIdentity
rsBWM = _RsBWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60)
)
_RsWSDTelnetUserTable_Object = MibTable
rsWSDTelnetUserTable = _RsWSDTelnetUserTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61)
)
if mibBuilder.loadTexts:
    rsWSDTelnetUserTable.setStatus("mandatory")
_RsWSDTelnetUserEntry_Object = MibTableRow
rsWSDTelnetUserEntry = _RsWSDTelnetUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1)
)
rsWSDTelnetUserEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDTelnetUserName"),
)
if mibBuilder.loadTexts:
    rsWSDTelnetUserEntry.setStatus("mandatory")


class _RsWSDTelnetUserName_Type(DisplayString):
    """Custom type rsWSDTelnetUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsWSDTelnetUserName_Type.__name__ = "DisplayString"
_RsWSDTelnetUserName_Object = MibTableColumn
rsWSDTelnetUserName = _RsWSDTelnetUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 1),
    _RsWSDTelnetUserName_Type()
)
rsWSDTelnetUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserName.setStatus("mandatory")


class _RsWSDTelnetUserPassword_Type(DisplayString):
    """Custom type rsWSDTelnetUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsWSDTelnetUserPassword_Type.__name__ = "DisplayString"
_RsWSDTelnetUserPassword_Object = MibTableColumn
rsWSDTelnetUserPassword = _RsWSDTelnetUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 2),
    _RsWSDTelnetUserPassword_Type()
)
rsWSDTelnetUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserPassword.setStatus("mandatory")


class _RsWSDTelnetUserEAddr_Type(DisplayString):
    """Custom type rsWSDTelnetUserEAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsWSDTelnetUserEAddr_Type.__name__ = "DisplayString"
_RsWSDTelnetUserEAddr_Object = MibTableColumn
rsWSDTelnetUserEAddr = _RsWSDTelnetUserEAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 3),
    _RsWSDTelnetUserEAddr_Type()
)
rsWSDTelnetUserEAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserEAddr.setStatus("mandatory")


class _RsWSDTelnetUserSeverity_Type(Integer32):
    """Custom type rsWSDTelnetUserSeverity based on Integer32"""
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
        *(("none", 1),
          ("info", 2),
          ("warning", 3),
          ("error", 4),
          ("fatal", 5))
    )


_RsWSDTelnetUserSeverity_Type.__name__ = "Integer32"
_RsWSDTelnetUserSeverity_Object = MibTableColumn
rsWSDTelnetUserSeverity = _RsWSDTelnetUserSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 4),
    _RsWSDTelnetUserSeverity_Type()
)
rsWSDTelnetUserSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserSeverity.setStatus("mandatory")
_RsWSDTelnetUserStatus_Type = RowStatus
_RsWSDTelnetUserStatus_Object = MibTableColumn
rsWSDTelnetUserStatus = _RsWSDTelnetUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 5),
    _RsWSDTelnetUserStatus_Type()
)
rsWSDTelnetUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserStatus.setStatus("mandatory")


class _RsWSDTelnetUserGroup_Type(DisplayString):
    """Custom type rsWSDTelnetUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsWSDTelnetUserGroup_Type.__name__ = "DisplayString"
_RsWSDTelnetUserGroup_Object = MibTableColumn
rsWSDTelnetUserGroup = _RsWSDTelnetUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 6),
    _RsWSDTelnetUserGroup_Type()
)
rsWSDTelnetUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserGroup.setStatus("mandatory")


class _RsWSDTelnetUserConfigurationTraceStatus_Type(Integer32):
    """Custom type rsWSDTelnetUserConfigurationTraceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDTelnetUserConfigurationTraceStatus_Type.__name__ = "Integer32"
_RsWSDTelnetUserConfigurationTraceStatus_Object = MibTableColumn
rsWSDTelnetUserConfigurationTraceStatus = _RsWSDTelnetUserConfigurationTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 7),
    _RsWSDTelnetUserConfigurationTraceStatus_Type()
)
rsWSDTelnetUserConfigurationTraceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserConfigurationTraceStatus.setStatus("mandatory")


class _RsWSDTelnetUserConfigurationTraceInf_Type(Integer32):
    """Custom type rsWSDTelnetUserConfigurationTraceInf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("webBased", 2),
          ("terminal", 3),
          ("snmp", 4),
          ("telnetSSH", 5),
          ("ftp", 6),
          ("ftpSSH", 7))
    )


_RsWSDTelnetUserConfigurationTraceInf_Type.__name__ = "Integer32"
_RsWSDTelnetUserConfigurationTraceInf_Object = MibTableColumn
rsWSDTelnetUserConfigurationTraceInf = _RsWSDTelnetUserConfigurationTraceInf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 8),
    _RsWSDTelnetUserConfigurationTraceInf_Type()
)
rsWSDTelnetUserConfigurationTraceInf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserConfigurationTraceInf.setStatus("mandatory")


class _RsWSDTelnetUserWebAccessLevel_Type(Integer32):
    """Custom type rsWSDTelnetUserWebAccessLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readwrite", 1),
          ("readonly", 2),
          ("none", 3))
    )


_RsWSDTelnetUserWebAccessLevel_Type.__name__ = "Integer32"
_RsWSDTelnetUserWebAccessLevel_Object = MibTableColumn
rsWSDTelnetUserWebAccessLevel = _RsWSDTelnetUserWebAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 9),
    _RsWSDTelnetUserWebAccessLevel_Type()
)
rsWSDTelnetUserWebAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserWebAccessLevel.setStatus("mandatory")


class _RsWSDTelnetUserSshPublicKeyName_Type(DisplayString):
    """Custom type rsWSDTelnetUserSshPublicKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsWSDTelnetUserSshPublicKeyName_Type.__name__ = "DisplayString"
_RsWSDTelnetUserSshPublicKeyName_Object = MibTableColumn
rsWSDTelnetUserSshPublicKeyName = _RsWSDTelnetUserSshPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 10),
    _RsWSDTelnetUserSshPublicKeyName_Type()
)
rsWSDTelnetUserSshPublicKeyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserSshPublicKeyName.setStatus("mandatory")
_RsWSDTelnetParams_ObjectIdentity = ObjectIdentity
rsWSDTelnetParams = _RsWSDTelnetParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62)
)
_RsWSDTelnetPort_Type = Integer32
_RsWSDTelnetPort_Object = MibScalar
rsWSDTelnetPort = _RsWSDTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62, 1),
    _RsWSDTelnetPort_Type()
)
rsWSDTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetPort.setStatus("mandatory")


class _RsWSDTelnetStatus_Type(Integer32):
    """Custom type rsWSDTelnetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDTelnetStatus_Type.__name__ = "Integer32"
_RsWSDTelnetStatus_Object = MibScalar
rsWSDTelnetStatus = _RsWSDTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62, 2),
    _RsWSDTelnetStatus_Type()
)
rsWSDTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetStatus.setStatus("mandatory")
_RsSSD_ObjectIdentity = ObjectIdentity
rsSSD = _RsSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63)
)
_RsSSDvirtualLan_ObjectIdentity = ObjectIdentity
rsSSDvirtualLan = _RsSSDvirtualLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1)
)
_RsSSDvirtualLanTable_Object = MibTable
rsSSDvirtualLanTable = _RsSSDvirtualLanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1)
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanTable.setStatus("mandatory")
_RsSSDvirtualLanEntry_Object = MibTableRow
rsSSDvirtualLanEntry = _RsSSDvirtualLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1)
)
rsSSDvirtualLanEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsSSDvlIfIndex"),
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanEntry.setStatus("mandatory")
_RsSSDvlIfIndex_Type = Integer32
_RsSSDvlIfIndex_Object = MibTableColumn
rsSSDvlIfIndex = _RsSSDvlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 1),
    _RsSSDvlIfIndex_Type()
)
rsSSDvlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlIfIndex.setStatus("mandatory")


class _RsSSDvlProto_Type(Integer32):
    """Custom type rsSSDvlProto based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ip", 2),
          ("ipmulticast", 3),
          ("ipxRaw", 4),
          ("ipxET", 5),
          ("ipxLLC", 6),
          ("ipxSNAP", 7),
          ("decNET", 8),
          ("decLAT", 9),
          ("netBios", 10),
          ("appleTalk", 11),
          ("xns", 12),
          ("sna", 13),
          ("userDefined", 14),
          ("swVlan", 15))
    )


_RsSSDvlProto_Type.__name__ = "Integer32"
_RsSSDvlProto_Object = MibTableColumn
rsSSDvlProto = _RsSSDvlProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 2),
    _RsSSDvlProto_Type()
)
rsSSDvlProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlProto.setStatus("mandatory")
_RsSSDvlAutoConfigEnable_Type = TruthValue
_RsSSDvlAutoConfigEnable_Object = MibTableColumn
rsSSDvlAutoConfigEnable = _RsSSDvlAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 3),
    _RsSSDvlAutoConfigEnable_Type()
)
rsSSDvlAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlAutoConfigEnable.setStatus("mandatory")
_RsSSDvlStatus_Type = RowStatus
_RsSSDvlStatus_Object = MibTableColumn
rsSSDvlStatus = _RsSSDvlStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 4),
    _RsSSDvlStatus_Type()
)
rsSSDvlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlStatus.setStatus("mandatory")


class _RsSSDvlType_Type(Integer32):
    """Custom type rsSSDvlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("specBroadcast", 2),
          ("specArpReq", 3),
          ("specBroadcastAndUnicast", 4),
          ("specArpReqAndUnicast", 5),
          ("specSwitch", 6))
    )


_RsSSDvlType_Type.__name__ = "Integer32"
_RsSSDvlType_Object = MibTableColumn
rsSSDvlType = _RsSSDvlType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 5),
    _RsSSDvlType_Type()
)
rsSSDvlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlType.setStatus("mandatory")


class _RsSSDvlTag_Type(Integer32):
    """Custom type rsSSDvlTag based on Integer32"""
    defaultValue = 0


_RsSSDvlTag_Type.__name__ = "Integer32"
_RsSSDvlTag_Object = MibTableColumn
rsSSDvlTag = _RsSSDvlTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 6),
    _RsSSDvlTag_Type()
)
rsSSDvlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlTag.setStatus("mandatory")


class _RsSSDvlPriority_Type(Integer32):
    """Custom type rsSSDvlPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_RsSSDvlPriority_Type.__name__ = "Integer32"
_RsSSDvlPriority_Object = MibTableColumn
rsSSDvlPriority = _RsSSDvlPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 7),
    _RsSSDvlPriority_Type()
)
rsSSDvlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlPriority.setStatus("mandatory")


class _RsSSDvlUpCriterion_Type(Integer32):
    """Custom type rsSSDvlUpCriterion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaultByType", 1),
          ("onePort", 2),
          ("allPorts", 3))
    )


_RsSSDvlUpCriterion_Type.__name__ = "Integer32"
_RsSSDvlUpCriterion_Object = MibTableColumn
rsSSDvlUpCriterion = _RsSSDvlUpCriterion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 8),
    _RsSSDvlUpCriterion_Type()
)
rsSSDvlUpCriterion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlUpCriterion.setStatus("mandatory")


class _RsSSDvlDownCriterion_Type(Integer32):
    """Custom type rsSSDvlDownCriterion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaultByType", 1),
          ("onePort", 2),
          ("allPorts", 3))
    )


_RsSSDvlDownCriterion_Type.__name__ = "Integer32"
_RsSSDvlDownCriterion_Object = MibTableColumn
rsSSDvlDownCriterion = _RsSSDvlDownCriterion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 9),
    _RsSSDvlDownCriterion_Type()
)
rsSSDvlDownCriterion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlDownCriterion.setStatus("mandatory")
_RsSSDvirtualLanPortsTable_Object = MibTable
rsSSDvirtualLanPortsTable = _RsSSDvirtualLanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2)
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanPortsTable.setStatus("mandatory")
_RsSSDvirtualLanPortEntry_Object = MibTableRow
rsSSDvirtualLanPortEntry = _RsSSDvirtualLanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1)
)
rsSSDvirtualLanPortEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsSSDvLIfIndex"),
    (0, "RADWARE-MIB", "rsSSDvLPortIfIndex"),
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanPortEntry.setStatus("mandatory")
_RsSSDvLIfIndex_Type = Integer32
_RsSSDvLIfIndex_Object = MibTableColumn
rsSSDvLIfIndex = _RsSSDvLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 1),
    _RsSSDvLIfIndex_Type()
)
rsSSDvLIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLIfIndex.setStatus("mandatory")
_RsSSDvLPortIfIndex_Type = Integer32
_RsSSDvLPortIfIndex_Object = MibTableColumn
rsSSDvLPortIfIndex = _RsSSDvLPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 2),
    _RsSSDvLPortIfIndex_Type()
)
rsSSDvLPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortIfIndex.setStatus("mandatory")


class _RsSSDvLPortType_Type(Integer32):
    """Custom type rsSSDvLPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_RsSSDvLPortType_Type.__name__ = "Integer32"
_RsSSDvLPortType_Object = MibTableColumn
rsSSDvLPortType = _RsSSDvLPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 3),
    _RsSSDvLPortType_Type()
)
rsSSDvLPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSSDvLPortType.setStatus("mandatory")
_RsSSDvLPortStatus_Type = RowStatus
_RsSSDvLPortStatus_Object = MibTableColumn
rsSSDvLPortStatus = _RsSSDvLPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 4),
    _RsSSDvLPortStatus_Type()
)
rsSSDvLPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortStatus.setStatus("mandatory")


class _RsSSDvLPortTag_Type(Integer32):
    """Custom type rsSSDvLPortTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("tag", 2))
    )


_RsSSDvLPortTag_Type.__name__ = "Integer32"
_RsSSDvLPortTag_Object = MibTableColumn
rsSSDvLPortTag = _RsSSDvLPortTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 5),
    _RsSSDvLPortTag_Type()
)
rsSSDvLPortTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortTag.setStatus("mandatory")


class _RsSSDvLPortInterfaceGroupingState_Type(Integer32):
    """Custom type rsSSDvLPortInterfaceGroupingState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_RsSSDvLPortInterfaceGroupingState_Type.__name__ = "Integer32"
_RsSSDvLPortInterfaceGroupingState_Object = MibTableColumn
rsSSDvLPortInterfaceGroupingState = _RsSSDvLPortInterfaceGroupingState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 6),
    _RsSSDvLPortInterfaceGroupingState_Type()
)
rsSSDvLPortInterfaceGroupingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortInterfaceGroupingState.setStatus("mandatory")
_RsWSDThresholdWarnings_ObjectIdentity = ObjectIdentity
rsWSDThresholdWarnings = _RsWSDThresholdWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64)
)


class _RsWSDThreshTrapFloodDelay_Type(Integer32):
    """Custom type rsWSDThreshTrapFloodDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RsWSDThreshTrapFloodDelay_Type.__name__ = "Integer32"
_RsWSDThreshTrapFloodDelay_Object = MibScalar
rsWSDThreshTrapFloodDelay = _RsWSDThreshTrapFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 1),
    _RsWSDThreshTrapFloodDelay_Type()
)
rsWSDThreshTrapFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDThreshTrapFloodDelay.setStatus("mandatory")


class _RsWSDCriticalTrapFloodDelay_Type(Integer32):
    """Custom type rsWSDCriticalTrapFloodDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsWSDCriticalTrapFloodDelay_Type.__name__ = "Integer32"
_RsWSDCriticalTrapFloodDelay_Object = MibScalar
rsWSDCriticalTrapFloodDelay = _RsWSDCriticalTrapFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 2),
    _RsWSDCriticalTrapFloodDelay_Type()
)
rsWSDCriticalTrapFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCriticalTrapFloodDelay.setStatus("mandatory")
_RsIDS_ObjectIdentity = ObjectIdentity
rsIDS = _RsIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65)
)


class _RsWSDLicense_Type(DisplayString):
    """Custom type rsWSDLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDLicense_Type.__name__ = "DisplayString"
_RsWSDLicense_Object = MibScalar
rsWSDLicense = _RsWSDLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 66),
    _RsWSDLicense_Type()
)
rsWSDLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDLicense.setStatus("mandatory")
_RsErrMailParams_ObjectIdentity = ObjectIdentity
rsErrMailParams = _RsErrMailParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67)
)


class _RsErrMailEnable_Type(Integer32):
    """Custom type rsErrMailEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsErrMailEnable_Type.__name__ = "Integer32"
_RsErrMailEnable_Object = MibScalar
rsErrMailEnable = _RsErrMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 1),
    _RsErrMailEnable_Type()
)
rsErrMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailEnable.setStatus("mandatory")
_RsErrMailGateway_Type = IpAddress
_RsErrMailGateway_Object = MibScalar
rsErrMailGateway = _RsErrMailGateway_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 2),
    _RsErrMailGateway_Type()
)
rsErrMailGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailGateway.setStatus("mandatory")


class _RsErrMailSrcAddress_Type(DisplayString):
    """Custom type rsErrMailSrcAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RsErrMailSrcAddress_Type.__name__ = "DisplayString"
_RsErrMailSrcAddress_Object = MibScalar
rsErrMailSrcAddress = _RsErrMailSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 3),
    _RsErrMailSrcAddress_Type()
)
rsErrMailSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailSrcAddress.setStatus("mandatory")


class _RsErrMailToFieldText_Type(DisplayString):
    """Custom type rsErrMailToFieldText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsErrMailToFieldText_Type.__name__ = "DisplayString"
_RsErrMailToFieldText_Object = MibScalar
rsErrMailToFieldText = _RsErrMailToFieldText_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 4),
    _RsErrMailToFieldText_Type()
)
rsErrMailToFieldText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailToFieldText.setStatus("mandatory")
_RsWSDWebParams_ObjectIdentity = ObjectIdentity
rsWSDWebParams = _RsWSDWebParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68)
)
_RsWSDWebPort_Type = Integer32
_RsWSDWebPort_Object = MibScalar
rsWSDWebPort = _RsWSDWebPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 1),
    _RsWSDWebPort_Type()
)
rsWSDWebPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebPort.setStatus("mandatory")


class _RsWSDWebStatus_Type(Integer32):
    """Custom type rsWSDWebStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDWebStatus_Type.__name__ = "Integer32"
_RsWSDWebStatus_Object = MibScalar
rsWSDWebStatus = _RsWSDWebStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 2),
    _RsWSDWebStatus_Type()
)
rsWSDWebStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebStatus.setStatus("mandatory")


class _RsWSDWebHelpLocation_Type(DisplayString):
    """Custom type rsWSDWebHelpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDWebHelpLocation_Type.__name__ = "DisplayString"
_RsWSDWebHelpLocation_Object = MibScalar
rsWSDWebHelpLocation = _RsWSDWebHelpLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 3),
    _RsWSDWebHelpLocation_Type()
)
rsWSDWebHelpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebHelpLocation.setStatus("mandatory")


class _RsWSDWebSSLPort_Type(Integer32):
    """Custom type rsWSDWebSSLPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsWSDWebSSLPort_Type.__name__ = "Integer32"
_RsWSDWebSSLPort_Object = MibScalar
rsWSDWebSSLPort = _RsWSDWebSSLPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 4),
    _RsWSDWebSSLPort_Type()
)
rsWSDWebSSLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLPort.setStatus("mandatory")


class _RsWSDWebSSLStatus_Type(Integer32):
    """Custom type rsWSDWebSSLStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDWebSSLStatus_Type.__name__ = "Integer32"
_RsWSDWebSSLStatus_Object = MibScalar
rsWSDWebSSLStatus = _RsWSDWebSSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 5),
    _RsWSDWebSSLStatus_Type()
)
rsWSDWebSSLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLStatus.setStatus("mandatory")


class _RsWSDWebSSLPrivateKeyFile_Type(DisplayString):
    """Custom type rsWSDWebSSLPrivateKeyFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDWebSSLPrivateKeyFile_Type.__name__ = "DisplayString"
_RsWSDWebSSLPrivateKeyFile_Object = MibScalar
rsWSDWebSSLPrivateKeyFile = _RsWSDWebSSLPrivateKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 6),
    _RsWSDWebSSLPrivateKeyFile_Type()
)
rsWSDWebSSLPrivateKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLPrivateKeyFile.setStatus("mandatory")


class _RsWSDWebSSLCertificateFile_Type(DisplayString):
    """Custom type rsWSDWebSSLCertificateFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDWebSSLCertificateFile_Type.__name__ = "DisplayString"
_RsWSDWebSSLCertificateFile_Object = MibScalar
rsWSDWebSSLCertificateFile = _RsWSDWebSSLCertificateFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 7),
    _RsWSDWebSSLCertificateFile_Type()
)
rsWSDWebSSLCertificateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLCertificateFile.setStatus("mandatory")


class _RsWSDWebSSLCaFile_Type(DisplayString):
    """Custom type rsWSDWebSSLCaFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDWebSSLCaFile_Type.__name__ = "DisplayString"
_RsWSDWebSSLCaFile_Object = MibScalar
rsWSDWebSSLCaFile = _RsWSDWebSSLCaFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 8),
    _RsWSDWebSSLCaFile_Type()
)
rsWSDWebSSLCaFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLCaFile.setStatus("mandatory")


class _RsWSDWebSSLCaPath_Type(DisplayString):
    """Custom type rsWSDWebSSLCaPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDWebSSLCaPath_Type.__name__ = "DisplayString"
_RsWSDWebSSLCaPath_Object = MibScalar
rsWSDWebSSLCaPath = _RsWSDWebSSLCaPath_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 9),
    _RsWSDWebSSLCaPath_Type()
)
rsWSDWebSSLCaPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLCaPath.setStatus("mandatory")


class _RsWSDWebSSLClientAuthentication_Type(Integer32):
    """Custom type rsWSDWebSSLClientAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("password", 1),
          ("certificate", 2))
    )


_RsWSDWebSSLClientAuthentication_Type.__name__ = "Integer32"
_RsWSDWebSSLClientAuthentication_Object = MibScalar
rsWSDWebSSLClientAuthentication = _RsWSDWebSSLClientAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 10),
    _RsWSDWebSSLClientAuthentication_Type()
)
rsWSDWebSSLClientAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLClientAuthentication.setStatus("mandatory")


class _RsWSDWebAccessLevel_Type(Integer32):
    """Custom type rsWSDWebAccessLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_RsWSDWebAccessLevel_Type.__name__ = "Integer32"
_RsWSDWebAccessLevel_Object = MibScalar
rsWSDWebAccessLevel = _RsWSDWebAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 11),
    _RsWSDWebAccessLevel_Type()
)
rsWSDWebAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebAccessLevel.setStatus("mandatory")


class _RsWSDWebSoapSupportStatus_Type(Integer32):
    """Custom type rsWSDWebSoapSupportStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDWebSoapSupportStatus_Type.__name__ = "Integer32"
_RsWSDWebSoapSupportStatus_Object = MibScalar
rsWSDWebSoapSupportStatus = _RsWSDWebSoapSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 12),
    _RsWSDWebSoapSupportStatus_Type()
)
rsWSDWebSoapSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSoapSupportStatus.setStatus("mandatory")


class _RsWSDWebSSLWeakCiphersSupportStatus_Type(Integer32):
    """Custom type rsWSDWebSSLWeakCiphersSupportStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDWebSSLWeakCiphersSupportStatus_Type.__name__ = "Integer32"
_RsWSDWebSSLWeakCiphersSupportStatus_Object = MibScalar
rsWSDWebSSLWeakCiphersSupportStatus = _RsWSDWebSSLWeakCiphersSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 13),
    _RsWSDWebSSLWeakCiphersSupportStatus_Type()
)
rsWSDWebSSLWeakCiphersSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebSSLWeakCiphersSupportStatus.setStatus("mandatory")
_RsWSDSysParams_ObjectIdentity = ObjectIdentity
rsWSDSysParams = _RsWSDSysParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69)
)
_RsWSDSysFlashSize_Type = Integer32
_RsWSDSysFlashSize_Object = MibScalar
rsWSDSysFlashSize = _RsWSDSysFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 1),
    _RsWSDSysFlashSize_Type()
)
rsWSDSysFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSysFlashSize.setStatus("mandatory")
_RsWSDSysUpTime_Type = DisplayString
_RsWSDSysUpTime_Object = MibScalar
rsWSDSysUpTime = _RsWSDSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 2),
    _RsWSDSysUpTime_Type()
)
rsWSDSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSysUpTime.setStatus("mandatory")


class _RsWSDSysManagedTime_Type(DisplayString):
    """Custom type rsWSDSysManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDSysManagedTime_Type.__name__ = "DisplayString"
_RsWSDSysManagedTime_Object = MibScalar
rsWSDSysManagedTime = _RsWSDSysManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 3),
    _RsWSDSysManagedTime_Type()
)
rsWSDSysManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSysManagedTime.setStatus("mandatory")


class _RsWSDSysManagedDate_Type(DisplayString):
    """Custom type rsWSDSysManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDSysManagedDate_Type.__name__ = "DisplayString"
_RsWSDSysManagedDate_Object = MibScalar
rsWSDSysManagedDate = _RsWSDSysManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 4),
    _RsWSDSysManagedDate_Type()
)
rsWSDSysManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSysManagedDate.setStatus("mandatory")


class _RsWSDSysBaseMACAddress_Type(DisplayString):
    """Custom type rsWSDSysBaseMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RsWSDSysBaseMACAddress_Type.__name__ = "DisplayString"
_RsWSDSysBaseMACAddress_Object = MibScalar
rsWSDSysBaseMACAddress = _RsWSDSysBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 5),
    _RsWSDSysBaseMACAddress_Type()
)
rsWSDSysBaseMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSysBaseMACAddress.setStatus("mandatory")
_RdwrDualPowerSupplyParams_ObjectIdentity = ObjectIdentity
rdwrDualPowerSupplyParams = _RdwrDualPowerSupplyParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 6)
)


class _RdwrPowerSupply1Status_Type(Integer32):
    """Custom type rdwrPowerSupply1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("invalid", 3))
    )


_RdwrPowerSupply1Status_Type.__name__ = "Integer32"
_RdwrPowerSupply1Status_Object = MibScalar
rdwrPowerSupply1Status = _RdwrPowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 6, 1),
    _RdwrPowerSupply1Status_Type()
)
rdwrPowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrPowerSupply1Status.setStatus("mandatory")


class _RdwrPowerSupply2Status_Type(Integer32):
    """Custom type rdwrPowerSupply2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("invalid", 3))
    )


_RdwrPowerSupply2Status_Type.__name__ = "Integer32"
_RdwrPowerSupply2Status_Object = MibScalar
rdwrPowerSupply2Status = _RdwrPowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 6, 2),
    _RdwrPowerSupply2Status_Type()
)
rdwrPowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrPowerSupply2Status.setStatus("mandatory")
_RdwrPowerSupplyTrapStatus_Type = FeatureStatus
_RdwrPowerSupplyTrapStatus_Object = MibScalar
rdwrPowerSupplyTrapStatus = _RdwrPowerSupplyTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 6, 3),
    _RdwrPowerSupplyTrapStatus_Type()
)
rdwrPowerSupplyTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrPowerSupplyTrapStatus.setStatus("mandatory")


class _RdwrPowerSupplyStatus_Type(Integer32):
    """Custom type rdwrPowerSupplyStatus based on Integer32"""
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
        *(("singlePowerSupplyOk", 1),
          ("firstPowerSupplyFailed", 2),
          ("secondPowerSupplyFailed", 3),
          ("doublePowerSupplyOk", 4),
          ("unknownPowerSupplyFailed", 5))
    )


_RdwrPowerSupplyStatus_Type.__name__ = "Integer32"
_RdwrPowerSupplyStatus_Object = MibScalar
rdwrPowerSupplyStatus = _RdwrPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 6, 4),
    _RdwrPowerSupplyStatus_Type()
)
rdwrPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrPowerSupplyStatus.setStatus("mandatory")


class _RsWSDLicenseID_Type(DisplayString):
    """Custom type rsWSDLicenseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDLicenseID_Type.__name__ = "DisplayString"
_RsWSDLicenseID_Object = MibScalar
rsWSDLicenseID = _RsWSDLicenseID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 70),
    _RsWSDLicenseID_Type()
)
rsWSDLicenseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDLicenseID.setStatus("mandatory")


class _RsWSDSendFakeArp_Type(Integer32):
    """Custom type rsWSDSendFakeArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSendFakeArp_Type.__name__ = "Integer32"
_RsWSDSendFakeArp_Object = MibScalar
rsWSDSendFakeArp = _RsWSDSendFakeArp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 71),
    _RsWSDSendFakeArp_Type()
)
rsWSDSendFakeArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSendFakeArp.setStatus("mandatory")
_RsWSDNTP_ObjectIdentity = ObjectIdentity
rsWSDNTP = _RsWSDNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72)
)
_RsWSDNTPServerAddr_Type = IpAddress
_RsWSDNTPServerAddr_Object = MibScalar
rsWSDNTPServerAddr = _RsWSDNTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 1),
    _RsWSDNTPServerAddr_Type()
)
rsWSDNTPServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPServerAddr.setStatus("mandatory")
_RsWSDNTPInterval_Type = Integer32
_RsWSDNTPInterval_Object = MibScalar
rsWSDNTPInterval = _RsWSDNTPInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 2),
    _RsWSDNTPInterval_Type()
)
rsWSDNTPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPInterval.setStatus("mandatory")


class _RsWSDNTPStatus_Type(Integer32):
    """Custom type rsWSDNTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDNTPStatus_Type.__name__ = "Integer32"
_RsWSDNTPStatus_Object = MibScalar
rsWSDNTPStatus = _RsWSDNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 3),
    _RsWSDNTPStatus_Type()
)
rsWSDNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPStatus.setStatus("mandatory")


class _RsWSDNTPTimeZone_Type(DisplayString):
    """Custom type rsWSDNTPTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RsWSDNTPTimeZone_Type.__name__ = "DisplayString"
_RsWSDNTPTimeZone_Object = MibScalar
rsWSDNTPTimeZone = _RsWSDNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 4),
    _RsWSDNTPTimeZone_Type()
)
rsWSDNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPTimeZone.setStatus("mandatory")
_RsWSDNTPPort_Type = Integer32
_RsWSDNTPPort_Object = MibScalar
rsWSDNTPPort = _RsWSDNTPPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 5),
    _RsWSDNTPPort_Type()
)
rsWSDNTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPPort.setStatus("mandatory")


class _RsWSDNTPServerUrl_Type(DisplayString):
    """Custom type rsWSDNTPServerUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsWSDNTPServerUrl_Type.__name__ = "DisplayString"
_RsWSDNTPServerUrl_Object = MibScalar
rsWSDNTPServerUrl = _RsWSDNTPServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 6),
    _RsWSDNTPServerUrl_Type()
)
rsWSDNTPServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPServerUrl.setStatus("mandatory")
_RsStatistics_ObjectIdentity = ObjectIdentity
rsStatistics = _RsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 73)
)
_RsPhysPortMirrorTable_Object = MibTable
rsPhysPortMirrorTable = _RsPhysPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74)
)
if mibBuilder.loadTexts:
    rsPhysPortMirrorTable.setStatus("mandatory")
_RsPhysPortMirrorEntry_Object = MibTableRow
rsPhysPortMirrorEntry = _RsPhysPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1)
)
rsPhysPortMirrorEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsPhysPortMirrorSrcInf"),
    (0, "RADWARE-MIB", "rsPhysPortMirrorDstPort"),
)
if mibBuilder.loadTexts:
    rsPhysPortMirrorEntry.setStatus("mandatory")
_RsPhysPortMirrorSrcInf_Type = Integer32
_RsPhysPortMirrorSrcInf_Object = MibTableColumn
rsPhysPortMirrorSrcInf = _RsPhysPortMirrorSrcInf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 1),
    _RsPhysPortMirrorSrcInf_Type()
)
rsPhysPortMirrorSrcInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorSrcInf.setStatus("mandatory")
_RsPhysPortMirrorDstPort_Type = Integer32
_RsPhysPortMirrorDstPort_Object = MibTableColumn
rsPhysPortMirrorDstPort = _RsPhysPortMirrorDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 2),
    _RsPhysPortMirrorDstPort_Type()
)
rsPhysPortMirrorDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorDstPort.setStatus("mandatory")


class _RsPhysPortMirrorRxTx_Type(Integer32):
    """Custom type rsPhysPortMirrorRxTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyRxTx", 1),
          ("copyRxOnly", 2),
          ("copyTxOnly", 3))
    )


_RsPhysPortMirrorRxTx_Type.__name__ = "Integer32"
_RsPhysPortMirrorRxTx_Object = MibTableColumn
rsPhysPortMirrorRxTx = _RsPhysPortMirrorRxTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 3),
    _RsPhysPortMirrorRxTx_Type()
)
rsPhysPortMirrorRxTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorRxTx.setStatus("mandatory")


class _RsPhysPortMirrorRxBroadCast_Type(Integer32):
    """Custom type rsPhysPortMirrorRxBroadCast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsPhysPortMirrorRxBroadCast_Type.__name__ = "Integer32"
_RsPhysPortMirrorRxBroadCast_Object = MibTableColumn
rsPhysPortMirrorRxBroadCast = _RsPhysPortMirrorRxBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 4),
    _RsPhysPortMirrorRxBroadCast_Type()
)
rsPhysPortMirrorRxBroadCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorRxBroadCast.setStatus("mandatory")
_RsPhysPortMirrorStatus_Type = RowStatus
_RsPhysPortMirrorStatus_Object = MibTableColumn
rsPhysPortMirrorStatus = _RsPhysPortMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 5),
    _RsPhysPortMirrorStatus_Type()
)
rsPhysPortMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorStatus.setStatus("mandatory")
_RsPhysPortMirrorBackupDstPort_Type = Integer32
_RsPhysPortMirrorBackupDstPort_Object = MibTableColumn
rsPhysPortMirrorBackupDstPort = _RsPhysPortMirrorBackupDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 6),
    _RsPhysPortMirrorBackupDstPort_Type()
)
rsPhysPortMirrorBackupDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorBackupDstPort.setStatus("mandatory")


class _RsPhysPortMirrorDstStatus_Type(Integer32):
    """Custom type rsPhysPortMirrorDstStatus based on Integer32"""
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
        *(("active", 1),
          ("portDown", 2),
          ("checkIDSFail", 3),
          ("checkIDSFailAndPortDown", 4))
    )


_RsPhysPortMirrorDstStatus_Type.__name__ = "Integer32"
_RsPhysPortMirrorDstStatus_Object = MibTableColumn
rsPhysPortMirrorDstStatus = _RsPhysPortMirrorDstStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 7),
    _RsPhysPortMirrorDstStatus_Type()
)
rsPhysPortMirrorDstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorDstStatus.setStatus("mandatory")


class _RsPhysPortMirrorBackupStatus_Type(Integer32):
    """Custom type rsPhysPortMirrorBackupStatus based on Integer32"""
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
        *(("active", 1),
          ("portDown", 2),
          ("checkIDSFail", 3),
          ("checkIDSFailAndPortDown", 4),
          ("none", 5))
    )


_RsPhysPortMirrorBackupStatus_Type.__name__ = "Integer32"
_RsPhysPortMirrorBackupStatus_Object = MibTableColumn
rsPhysPortMirrorBackupStatus = _RsPhysPortMirrorBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 8),
    _RsPhysPortMirrorBackupStatus_Type()
)
rsPhysPortMirrorBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorBackupStatus.setStatus("mandatory")


class _RsPhysPortMirrorActiveDstPort_Type(Integer32):
    """Custom type rsPhysPortMirrorActiveDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dstPort", 1),
          ("backupPort", 2),
          ("none", 3))
    )


_RsPhysPortMirrorActiveDstPort_Type.__name__ = "Integer32"
_RsPhysPortMirrorActiveDstPort_Object = MibTableColumn
rsPhysPortMirrorActiveDstPort = _RsPhysPortMirrorActiveDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 9),
    _RsPhysPortMirrorActiveDstPort_Type()
)
rsPhysPortMirrorActiveDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorActiveDstPort.setStatus("mandatory")


class _RsPhysPortMirrorMode_Type(Integer32):
    """Custom type rsPhysPortMirrorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("traffic-rate", 2))
    )


_RsPhysPortMirrorMode_Type.__name__ = "Integer32"
_RsPhysPortMirrorMode_Object = MibTableColumn
rsPhysPortMirrorMode = _RsPhysPortMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 10),
    _RsPhysPortMirrorMode_Type()
)
rsPhysPortMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorMode.setStatus("mandatory")


class _RsPhysPortMirrorThreshold_Type(Integer32):
    """Custom type rsPhysPortMirrorThreshold based on Integer32"""
    defaultValue = 0


_RsPhysPortMirrorThreshold_Type.__name__ = "Integer32"
_RsPhysPortMirrorThreshold_Object = MibTableColumn
rsPhysPortMirrorThreshold = _RsPhysPortMirrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 11),
    _RsPhysPortMirrorThreshold_Type()
)
rsPhysPortMirrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorThreshold.setStatus("mandatory")


class _RsPhysPortMirrorThresholdStatus_Type(Integer32):
    """Custom type rsPhysPortMirrorThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("waiting", 1),
          ("active", 2),
          ("elapsed", 3))
    )


_RsPhysPortMirrorThresholdStatus_Type.__name__ = "Integer32"
_RsPhysPortMirrorThresholdStatus_Object = MibTableColumn
rsPhysPortMirrorThresholdStatus = _RsPhysPortMirrorThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 12),
    _RsPhysPortMirrorThresholdStatus_Type()
)
rsPhysPortMirrorThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorThresholdStatus.setStatus("mandatory")
_RsCP_ObjectIdentity = ObjectIdentity
rsCP = _RsCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 75)
)
_RsVWSD_ObjectIdentity = ObjectIdentity
rsVWSD = _RsVWSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76)
)
_RsVWSDDataPermissionsTable_Object = MibTable
rsVWSDDataPermissionsTable = _RsVWSDDataPermissionsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1)
)
if mibBuilder.loadTexts:
    rsVWSDDataPermissionsTable.setStatus("mandatory")
_RsVWSDDataPermissionsTableEntry_Object = MibTableRow
rsVWSDDataPermissionsTableEntry = _RsVWSDDataPermissionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1)
)
rsVWSDDataPermissionsTableEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsVWSDUserGroup"),
    (0, "RADWARE-MIB", "rsVWSDDataType"),
    (0, "RADWARE-MIB", "rsVWSDDataItems"),
)
if mibBuilder.loadTexts:
    rsVWSDDataPermissionsTableEntry.setStatus("mandatory")


class _RsVWSDUserGroup_Type(DisplayString):
    """Custom type rsVWSDUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsVWSDUserGroup_Type.__name__ = "DisplayString"
_RsVWSDUserGroup_Object = MibTableColumn
rsVWSDUserGroup = _RsVWSDUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 1),
    _RsVWSDUserGroup_Type()
)
rsVWSDUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVWSDUserGroup.setStatus("mandatory")


class _RsVWSDDataType_Type(OctetString):
    """Custom type rsVWSDDataType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsVWSDDataType_Type.__name__ = "OctetString"
_RsVWSDDataType_Object = MibTableColumn
rsVWSDDataType = _RsVWSDDataType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 2),
    _RsVWSDDataType_Type()
)
rsVWSDDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVWSDDataType.setStatus("mandatory")


class _RsVWSDDataItems_Type(OctetString):
    """Custom type rsVWSDDataItems based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsVWSDDataItems_Type.__name__ = "OctetString"
_RsVWSDDataItems_Object = MibTableColumn
rsVWSDDataItems = _RsVWSDDataItems_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 3),
    _RsVWSDDataItems_Type()
)
rsVWSDDataItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVWSDDataItems.setStatus("mandatory")
_RsVWSDDataStatus_Type = RowStatus
_RsVWSDDataStatus_Object = MibTableColumn
rsVWSDDataStatus = _RsVWSDDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 4),
    _RsVWSDDataStatus_Type()
)
rsVWSDDataStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsVWSDDataStatus.setStatus("mandatory")


class _RsWSDManagementPorts_Type(Integer32):
    """Custom type rsWSDManagementPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("outOfPath", 1),
          ("switch", 2),
          ("promiscuous", 3))
    )


_RsWSDManagementPorts_Type.__name__ = "Integer32"
_RsWSDManagementPorts_Object = MibScalar
rsWSDManagementPorts = _RsWSDManagementPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 77),
    _RsWSDManagementPorts_Type()
)
rsWSDManagementPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDManagementPorts.setStatus("mandatory")
_RsWSDManagementPortsTable_Object = MibTable
rsWSDManagementPortsTable = _RsWSDManagementPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78)
)
if mibBuilder.loadTexts:
    rsWSDManagementPortsTable.setStatus("mandatory")
_RsWSDManagementPortsEntry_Object = MibTableRow
rsWSDManagementPortsEntry = _RsWSDManagementPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78, 1)
)
rsWSDManagementPortsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDPortIndex"),
)
if mibBuilder.loadTexts:
    rsWSDManagementPortsEntry.setStatus("mandatory")
_RsWSDPortIndex_Type = Integer32
_RsWSDPortIndex_Object = MibTableColumn
rsWSDPortIndex = _RsWSDPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78, 1, 1),
    _RsWSDPortIndex_Type()
)
rsWSDPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPortIndex.setStatus("mandatory")


class _RsWSDPortOperation_Type(Integer32):
    """Custom type rsWSDPortOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management", 1),
          ("sniffer", 2))
    )


_RsWSDPortOperation_Type.__name__ = "Integer32"
_RsWSDPortOperation_Object = MibTableColumn
rsWSDPortOperation = _RsWSDPortOperation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78, 1, 2),
    _RsWSDPortOperation_Type()
)
rsWSDPortOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPortOperation.setStatus("mandatory")
_RsCCK_ObjectIdentity = ObjectIdentity
rsCCK = _RsCCK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79)
)
_RsWSDSshParams_ObjectIdentity = ObjectIdentity
rsWSDSshParams = _RsWSDSshParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80)
)
_RsWSDSshPort_Type = Integer32
_RsWSDSshPort_Object = MibScalar
rsWSDSshPort = _RsWSDSshPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 1),
    _RsWSDSshPort_Type()
)
rsWSDSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshPort.setStatus("mandatory")


class _RsWSDSshStatus_Type(Integer32):
    """Custom type rsWSDSshStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSshStatus_Type.__name__ = "Integer32"
_RsWSDSshStatus_Object = MibScalar
rsWSDSshStatus = _RsWSDSshStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 2),
    _RsWSDSshStatus_Type()
)
rsWSDSshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshStatus.setStatus("mandatory")


class _RsWSDSshAllowPwdAndPubKey_Type(Integer32):
    """Custom type rsWSDSshAllowPwdAndPubKey based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSshAllowPwdAndPubKey_Type.__name__ = "Integer32"
_RsWSDSshAllowPwdAndPubKey_Object = MibScalar
rsWSDSshAllowPwdAndPubKey = _RsWSDSshAllowPwdAndPubKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 3),
    _RsWSDSshAllowPwdAndPubKey_Type()
)
rsWSDSshAllowPwdAndPubKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshAllowPwdAndPubKey.setStatus("mandatory")
_RsWSDHttpsParams_ObjectIdentity = ObjectIdentity
rsWSDHttpsParams = _RsWSDHttpsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 81)
)
_RsWSDHttpsPort_Type = Integer32
_RsWSDHttpsPort_Object = MibScalar
rsWSDHttpsPort = _RsWSDHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 81, 1),
    _RsWSDHttpsPort_Type()
)
rsWSDHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHttpsPort.setStatus("mandatory")


class _RsWSDHttpsStatus_Type(Integer32):
    """Custom type rsWSDHttpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDHttpsStatus_Type.__name__ = "Integer32"
_RsWSDHttpsStatus_Object = MibScalar
rsWSDHttpsStatus = _RsWSDHttpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 81, 2),
    _RsWSDHttpsStatus_Type()
)
rsWSDHttpsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHttpsStatus.setStatus("mandatory")
_RsWSDStaticForwardingTable_Object = MibTable
rsWSDStaticForwardingTable = _RsWSDStaticForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82)
)
if mibBuilder.loadTexts:
    rsWSDStaticForwardingTable.setStatus("mandatory")
_RsWSDStaticForwardingEntry_Object = MibTableRow
rsWSDStaticForwardingEntry = _RsWSDStaticForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1)
)
rsWSDStaticForwardingEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDStaticSourcePort"),
)
if mibBuilder.loadTexts:
    rsWSDStaticForwardingEntry.setStatus("mandatory")
_RsWSDStaticSourcePort_Type = Integer32
_RsWSDStaticSourcePort_Object = MibTableColumn
rsWSDStaticSourcePort = _RsWSDStaticSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 1),
    _RsWSDStaticSourcePort_Type()
)
rsWSDStaticSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDStaticSourcePort.setStatus("mandatory")
_RsWSDStaticDestinationPort_Type = Integer32
_RsWSDStaticDestinationPort_Object = MibTableColumn
rsWSDStaticDestinationPort = _RsWSDStaticDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 2),
    _RsWSDStaticDestinationPort_Type()
)
rsWSDStaticDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticDestinationPort.setStatus("mandatory")


class _RsWSDStaticPortOperation_Type(Integer32):
    """Custom type rsWSDStaticPortOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("process", 1),
          ("forward", 2))
    )


_RsWSDStaticPortOperation_Type.__name__ = "Integer32"
_RsWSDStaticPortOperation_Object = MibTableColumn
rsWSDStaticPortOperation = _RsWSDStaticPortOperation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 3),
    _RsWSDStaticPortOperation_Type()
)
rsWSDStaticPortOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticPortOperation.setStatus("mandatory")
_RsWSDStaticStatus_Type = RowStatus
_RsWSDStaticStatus_Object = MibTableColumn
rsWSDStaticStatus = _RsWSDStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 4),
    _RsWSDStaticStatus_Type()
)
rsWSDStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticStatus.setStatus("mandatory")


class _RsWSDStaticFailureMode_Type(Integer32):
    """Custom type rsWSDStaticFailureMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail-close", 1),
          ("fail-open", 2))
    )


_RsWSDStaticFailureMode_Type.__name__ = "Integer32"
_RsWSDStaticFailureMode_Object = MibTableColumn
rsWSDStaticFailureMode = _RsWSDStaticFailureMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 5),
    _RsWSDStaticFailureMode_Type()
)
rsWSDStaticFailureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticFailureMode.setStatus("mandatory")


class _RsWSDStaticInPort_Type(Integer32):
    """Custom type rsWSDStaticInPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2))
    )


_RsWSDStaticInPort_Type.__name__ = "Integer32"
_RsWSDStaticInPort_Object = MibTableColumn
rsWSDStaticInPort = _RsWSDStaticInPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 6),
    _RsWSDStaticInPort_Type()
)
rsWSDStaticInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticInPort.setStatus("mandatory")
_RsRadiusServer_ObjectIdentity = ObjectIdentity
rsRadiusServer = _RsRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83)
)
_RsRadiusMainServerAddr_Type = IpAddress
_RsRadiusMainServerAddr_Object = MibScalar
rsRadiusMainServerAddr = _RsRadiusMainServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 1),
    _RsRadiusMainServerAddr_Type()
)
rsRadiusMainServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerAddr.setStatus("mandatory")
_RsRadiusMainServerPort_Type = Integer32
_RsRadiusMainServerPort_Object = MibScalar
rsRadiusMainServerPort = _RsRadiusMainServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 2),
    _RsRadiusMainServerPort_Type()
)
rsRadiusMainServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerPort.setStatus("mandatory")


class _RsRadiusMainServerSecret_Type(DisplayString):
    """Custom type rsRadiusMainServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RsRadiusMainServerSecret_Type.__name__ = "DisplayString"
_RsRadiusMainServerSecret_Object = MibScalar
rsRadiusMainServerSecret = _RsRadiusMainServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 3),
    _RsRadiusMainServerSecret_Type()
)
rsRadiusMainServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerSecret.setStatus("mandatory")
_RsRadiusBackupServerAddr_Type = IpAddress
_RsRadiusBackupServerAddr_Object = MibScalar
rsRadiusBackupServerAddr = _RsRadiusBackupServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 4),
    _RsRadiusBackupServerAddr_Type()
)
rsRadiusBackupServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerAddr.setStatus("mandatory")
_RsRadiusBackupServerPort_Type = Integer32
_RsRadiusBackupServerPort_Object = MibScalar
rsRadiusBackupServerPort = _RsRadiusBackupServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 5),
    _RsRadiusBackupServerPort_Type()
)
rsRadiusBackupServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerPort.setStatus("mandatory")


class _RsRadiusBackupServerSecret_Type(DisplayString):
    """Custom type rsRadiusBackupServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RsRadiusBackupServerSecret_Type.__name__ = "DisplayString"
_RsRadiusBackupServerSecret_Object = MibScalar
rsRadiusBackupServerSecret = _RsRadiusBackupServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 6),
    _RsRadiusBackupServerSecret_Type()
)
rsRadiusBackupServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerSecret.setStatus("mandatory")


class _RsAuthenticationMethod_Type(Integer32):
    """Custom type rsAuthenticationMethod based on Integer32"""
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
        *(("userTable", 1),
          ("radius", 2),
          ("radiusAndUserTable", 3),
          ("tacacsAndUserTable", 4))
    )


_RsAuthenticationMethod_Type.__name__ = "Integer32"
_RsAuthenticationMethod_Object = MibScalar
rsAuthenticationMethod = _RsAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 7),
    _RsAuthenticationMethod_Type()
)
rsAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAuthenticationMethod.setStatus("mandatory")


class _RsRadiusServerTimeout_Type(Integer32):
    """Custom type rsRadiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsRadiusServerTimeout_Type.__name__ = "Integer32"
_RsRadiusServerTimeout_Object = MibScalar
rsRadiusServerTimeout = _RsRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 8),
    _RsRadiusServerTimeout_Type()
)
rsRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusServerTimeout.setStatus("mandatory")


class _RsRadiusServerRetries_Type(Integer32):
    """Custom type rsRadiusServerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RsRadiusServerRetries_Type.__name__ = "Integer32"
_RsRadiusServerRetries_Object = MibScalar
rsRadiusServerRetries = _RsRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 9),
    _RsRadiusServerRetries_Type()
)
rsRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusServerRetries.setStatus("mandatory")


class _RsLockUserAfterLoginFailure_Type(Integer32):
    """Custom type rsLockUserAfterLoginFailure based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsLockUserAfterLoginFailure_Type.__name__ = "Integer32"
_RsLockUserAfterLoginFailure_Object = MibScalar
rsLockUserAfterLoginFailure = _RsLockUserAfterLoginFailure_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 10),
    _RsLockUserAfterLoginFailure_Type()
)
rsLockUserAfterLoginFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLockUserAfterLoginFailure.setStatus("mandatory")


class _RsRadiusClientLifeTime_Type(Integer32):
    """Custom type rsRadiusClientLifeTime based on Integer32"""
    defaultValue = 0


_RsRadiusClientLifeTime_Type.__name__ = "Integer32"
_RsRadiusClientLifeTime_Object = MibScalar
rsRadiusClientLifeTime = _RsRadiusClientLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 11),
    _RsRadiusClientLifeTime_Type()
)
rsRadiusClientLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusClientLifeTime.setStatus("mandatory")


class _RsRadiusMainServerUrl_Type(DisplayString):
    """Custom type rsRadiusMainServerUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsRadiusMainServerUrl_Type.__name__ = "DisplayString"
_RsRadiusMainServerUrl_Object = MibScalar
rsRadiusMainServerUrl = _RsRadiusMainServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 12),
    _RsRadiusMainServerUrl_Type()
)
rsRadiusMainServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerUrl.setStatus("mandatory")


class _RsRadiusBackupServerUrl_Type(DisplayString):
    """Custom type rsRadiusBackupServerUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsRadiusBackupServerUrl_Type.__name__ = "DisplayString"
_RsRadiusBackupServerUrl_Object = MibScalar
rsRadiusBackupServerUrl = _RsRadiusBackupServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 13),
    _RsRadiusBackupServerUrl_Type()
)
rsRadiusBackupServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerUrl.setStatus("mandatory")
_RspRadiusParameters_ObjectIdentity = ObjectIdentity
rspRadiusParameters = _RspRadiusParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14)
)


class _RspRadiusPrimaryAddr_Type(DisplayString):
    """Custom type rspRadiusPrimaryAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RspRadiusPrimaryAddr_Type.__name__ = "DisplayString"
_RspRadiusPrimaryAddr_Object = MibScalar
rspRadiusPrimaryAddr = _RspRadiusPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 1),
    _RspRadiusPrimaryAddr_Type()
)
rspRadiusPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusPrimaryAddr.setStatus("mandatory")
_RspRadiusPrimaryAuthPort_Type = Integer32
_RspRadiusPrimaryAuthPort_Object = MibScalar
rspRadiusPrimaryAuthPort = _RspRadiusPrimaryAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 2),
    _RspRadiusPrimaryAuthPort_Type()
)
rspRadiusPrimaryAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusPrimaryAuthPort.setStatus("mandatory")
_RspRadiusPrimaryAccPort_Type = Integer32
_RspRadiusPrimaryAccPort_Object = MibScalar
rspRadiusPrimaryAccPort = _RspRadiusPrimaryAccPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 3),
    _RspRadiusPrimaryAccPort_Type()
)
rspRadiusPrimaryAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusPrimaryAccPort.setStatus("mandatory")


class _RspRadiusPrimarySecret_Type(DisplayString):
    """Custom type rspRadiusPrimarySecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RspRadiusPrimarySecret_Type.__name__ = "DisplayString"
_RspRadiusPrimarySecret_Object = MibScalar
rspRadiusPrimarySecret = _RspRadiusPrimarySecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 4),
    _RspRadiusPrimarySecret_Type()
)
rspRadiusPrimarySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusPrimarySecret.setStatus("mandatory")


class _RspRadiusAltAddr_Type(DisplayString):
    """Custom type rspRadiusAltAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RspRadiusAltAddr_Type.__name__ = "DisplayString"
_RspRadiusAltAddr_Object = MibScalar
rspRadiusAltAddr = _RspRadiusAltAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 5),
    _RspRadiusAltAddr_Type()
)
rspRadiusAltAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusAltAddr.setStatus("mandatory")
_RspRadiusAltAuthPort_Type = Integer32
_RspRadiusAltAuthPort_Object = MibScalar
rspRadiusAltAuthPort = _RspRadiusAltAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 6),
    _RspRadiusAltAuthPort_Type()
)
rspRadiusAltAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusAltAuthPort.setStatus("mandatory")
_RspRadiusAltAccPort_Type = Integer32
_RspRadiusAltAccPort_Object = MibScalar
rspRadiusAltAccPort = _RspRadiusAltAccPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 7),
    _RspRadiusAltAccPort_Type()
)
rspRadiusAltAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusAltAccPort.setStatus("mandatory")


class _RspRadiusAltSecret_Type(DisplayString):
    """Custom type rspRadiusAltSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RspRadiusAltSecret_Type.__name__ = "DisplayString"
_RspRadiusAltSecret_Object = MibScalar
rspRadiusAltSecret = _RspRadiusAltSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 8),
    _RspRadiusAltSecret_Type()
)
rspRadiusAltSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusAltSecret.setStatus("mandatory")
_RspRadiusOwnAuthPort_Type = Integer32
_RspRadiusOwnAuthPort_Object = MibScalar
rspRadiusOwnAuthPort = _RspRadiusOwnAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 9),
    _RspRadiusOwnAuthPort_Type()
)
rspRadiusOwnAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusOwnAuthPort.setStatus("mandatory")
_RspRadiusOwnAccPort_Type = Integer32
_RspRadiusOwnAccPort_Object = MibScalar
rspRadiusOwnAccPort = _RspRadiusOwnAccPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 10),
    _RspRadiusOwnAccPort_Type()
)
rspRadiusOwnAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusOwnAccPort.setStatus("mandatory")


class _RspRadiusEnable_Type(Integer32):
    """Custom type rspRadiusEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RspRadiusEnable_Type.__name__ = "Integer32"
_RspRadiusEnable_Object = MibScalar
rspRadiusEnable = _RspRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 11),
    _RspRadiusEnable_Type()
)
rspRadiusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusEnable.setStatus("mandatory")


class _RspRadiusTransparentEnable_Type(Integer32):
    """Custom type rspRadiusTransparentEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RspRadiusTransparentEnable_Type.__name__ = "Integer32"
_RspRadiusTransparentEnable_Object = MibScalar
rspRadiusTransparentEnable = _RspRadiusTransparentEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 12),
    _RspRadiusTransparentEnable_Type()
)
rspRadiusTransparentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusTransparentEnable.setStatus("mandatory")
_RspRadiusRuleTable_Object = MibTable
rspRadiusRuleTable = _RspRadiusRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 13)
)
if mibBuilder.loadTexts:
    rspRadiusRuleTable.setStatus("mandatory")
_RspRadiusRuleEntry_Object = MibTableRow
rspRadiusRuleEntry = _RspRadiusRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 13, 1)
)
rspRadiusRuleEntry.setIndexNames(
    (0, "RADWARE-MIB", "rspRadiusattId"),
    (0, "RADWARE-MIB", "rspRadiusattValue"),
    (0, "RADWARE-MIB", "rspRadiusNetworkName"),
)
if mibBuilder.loadTexts:
    rspRadiusRuleEntry.setStatus("mandatory")
_RspRadiusattId_Type = Integer32
_RspRadiusattId_Object = MibTableColumn
rspRadiusattId = _RspRadiusattId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 13, 1, 1),
    _RspRadiusattId_Type()
)
rspRadiusattId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rspRadiusattId.setStatus("mandatory")


class _RspRadiusattValue_Type(DisplayString):
    """Custom type rspRadiusattValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RspRadiusattValue_Type.__name__ = "DisplayString"
_RspRadiusattValue_Object = MibTableColumn
rspRadiusattValue = _RspRadiusattValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 13, 1, 2),
    _RspRadiusattValue_Type()
)
rspRadiusattValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rspRadiusattValue.setStatus("mandatory")


class _RspRadiusNetworkName_Type(DisplayString):
    """Custom type rspRadiusNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RspRadiusNetworkName_Type.__name__ = "DisplayString"
_RspRadiusNetworkName_Object = MibTableColumn
rspRadiusNetworkName = _RspRadiusNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 13, 1, 3),
    _RspRadiusNetworkName_Type()
)
rspRadiusNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rspRadiusNetworkName.setStatus("mandatory")
_RspRadiusrowStatus_Type = RowStatus
_RspRadiusrowStatus_Object = MibTableColumn
rspRadiusrowStatus = _RspRadiusrowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 13, 1, 4),
    _RspRadiusrowStatus_Type()
)
rspRadiusrowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusrowStatus.setStatus("mandatory")
_RspRadiusNasTable_Object = MibTable
rspRadiusNasTable = _RspRadiusNasTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 14)
)
if mibBuilder.loadTexts:
    rspRadiusNasTable.setStatus("mandatory")
_RspRadiusNasEntry_Object = MibTableRow
rspRadiusNasEntry = _RspRadiusNasEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 14, 1)
)
rspRadiusNasEntry.setIndexNames(
    (0, "RADWARE-MIB", "rspRadiusNasIp"),
)
if mibBuilder.loadTexts:
    rspRadiusNasEntry.setStatus("mandatory")
_RspRadiusNasIp_Type = IpAddress
_RspRadiusNasIp_Object = MibTableColumn
rspRadiusNasIp = _RspRadiusNasIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 14, 1, 1),
    _RspRadiusNasIp_Type()
)
rspRadiusNasIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rspRadiusNasIp.setStatus("mandatory")


class _RspRadiusNasSecret_Type(DisplayString):
    """Custom type rspRadiusNasSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RspRadiusNasSecret_Type.__name__ = "DisplayString"
_RspRadiusNasSecret_Object = MibTableColumn
rspRadiusNasSecret = _RspRadiusNasSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 14, 1, 2),
    _RspRadiusNasSecret_Type()
)
rspRadiusNasSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusNasSecret.setStatus("mandatory")
_RspRadiusNasrowStatus_Type = RowStatus
_RspRadiusNasrowStatus_Object = MibTableColumn
rspRadiusNasrowStatus = _RspRadiusNasrowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 14, 1, 3),
    _RspRadiusNasrowStatus_Type()
)
rspRadiusNasrowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusNasrowStatus.setStatus("mandatory")


class _RspRadiusUserMirrorProtocolMode_Type(Integer32):
    """Custom type rspRadiusUserMirrorProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RspRadiusUserMirrorProtocolMode_Type.__name__ = "Integer32"
_RspRadiusUserMirrorProtocolMode_Object = MibScalar
rspRadiusUserMirrorProtocolMode = _RspRadiusUserMirrorProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 15),
    _RspRadiusUserMirrorProtocolMode_Type()
)
rspRadiusUserMirrorProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusUserMirrorProtocolMode.setStatus("mandatory")


class _RspRadiusUserMirrorPollingTime_Type(Integer32):
    """Custom type rspRadiusUserMirrorPollingTime based on Integer32"""
    defaultValue = 10


_RspRadiusUserMirrorPollingTime_Type.__name__ = "Integer32"
_RspRadiusUserMirrorPollingTime_Object = MibScalar
rspRadiusUserMirrorPollingTime = _RspRadiusUserMirrorPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 16),
    _RspRadiusUserMirrorPollingTime_Type()
)
rspRadiusUserMirrorPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusUserMirrorPollingTime.setStatus("mandatory")


class _RspRadiusNetworkUpdatePolicy_Type(Integer32):
    """Custom type rspRadiusNetworkUpdatePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 1),
          ("add", 2))
    )


_RspRadiusNetworkUpdatePolicy_Type.__name__ = "Integer32"
_RspRadiusNetworkUpdatePolicy_Object = MibScalar
rspRadiusNetworkUpdatePolicy = _RspRadiusNetworkUpdatePolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 14, 17),
    _RspRadiusNetworkUpdatePolicy_Type()
)
rspRadiusNetworkUpdatePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rspRadiusNetworkUpdatePolicy.setStatus("mandatory")
_RsIfTable_Object = MibTable
rsIfTable = _RsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84)
)
if mibBuilder.loadTexts:
    rsIfTable.setStatus("mandatory")
_RsIfEntry_Object = MibTableRow
rsIfEntry = _RsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1)
)
rsIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIfIndex"),
)
if mibBuilder.loadTexts:
    rsIfEntry.setStatus("mandatory")
_RsIfIndex_Type = Integer32
_RsIfIndex_Object = MibTableColumn
rsIfIndex = _RsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 1),
    _RsIfIndex_Type()
)
rsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfIndex.setStatus("mandatory")


class _RsIfSpeed_Type(Integer32):
    """Custom type rsIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("eth10", 1),
          ("fe100", 2),
          ("ge1000", 3),
          ("xg10000", 4),
          ("qxg10000", 5))
    )


_RsIfSpeed_Type.__name__ = "Integer32"
_RsIfSpeed_Object = MibTableColumn
rsIfSpeed = _RsIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 2),
    _RsIfSpeed_Type()
)
rsIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfSpeed.setStatus("mandatory")


class _RsIfDuplex_Type(Integer32):
    """Custom type rsIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_RsIfDuplex_Type.__name__ = "Integer32"
_RsIfDuplex_Object = MibTableColumn
rsIfDuplex = _RsIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 3),
    _RsIfDuplex_Type()
)
rsIfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfDuplex.setStatus("mandatory")


class _RsIfAutoNegotiate_Type(Integer32):
    """Custom type rsIfAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("on", 1),
          ("off", 2))
    )


_RsIfAutoNegotiate_Type.__name__ = "Integer32"
_RsIfAutoNegotiate_Object = MibTableColumn
rsIfAutoNegotiate = _RsIfAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 4),
    _RsIfAutoNegotiate_Type()
)
rsIfAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfAutoNegotiate.setStatus("mandatory")


class _RsIfAutoNegotiateCfg_Type(Integer32):
    """Custom type rsIfAutoNegotiateCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("on", 1),
          ("off", 2))
    )


_RsIfAutoNegotiateCfg_Type.__name__ = "Integer32"
_RsIfAutoNegotiateCfg_Object = MibTableColumn
rsIfAutoNegotiateCfg = _RsIfAutoNegotiateCfg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 5),
    _RsIfAutoNegotiateCfg_Type()
)
rsIfAutoNegotiateCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfAutoNegotiateCfg.setStatus("mandatory")


class _RsWSDDeviceOperationMode_Type(Integer32):
    """Custom type rsWSDDeviceOperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trafficRedirection", 1),
          ("staticForwarding", 2),
          ("transparentForwarding", 3))
    )


_RsWSDDeviceOperationMode_Type.__name__ = "Integer32"
_RsWSDDeviceOperationMode_Object = MibScalar
rsWSDDeviceOperationMode = _RsWSDDeviceOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 85),
    _RsWSDDeviceOperationMode_Type()
)
rsWSDDeviceOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDeviceOperationMode.setStatus("mandatory")


class _RsWSDVersionStatus_Type(Integer32):
    """Custom type rsWSDVersionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("final", 2))
    )


_RsWSDVersionStatus_Type.__name__ = "Integer32"
_RsWSDVersionStatus_Object = MibScalar
rsWSDVersionStatus = _RsWSDVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 86),
    _RsWSDVersionStatus_Type()
)
rsWSDVersionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDVersionStatus.setStatus("mandatory")


class _RsWSDSyslogFacility_Type(Integer32):
    """Custom type rsWSDSyslogFacility based on Integer32"""
    defaultValue = 22

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
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernelMsg", 0),
          ("userLevelMsg", 1),
          ("mailSystem", 2),
          ("systemDaemons", 3),
          ("authorization", 4),
          ("syslogdMessages", 5),
          ("linePrinter", 6),
          ("networkNews", 7),
          ("uucp", 8),
          ("clockDaemon1", 9),
          ("security", 10),
          ("ftpDaemon", 11),
          ("ntpSubsystem", 12),
          ("logAudit", 13),
          ("logAlert", 14),
          ("clockDaemon2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )


_RsWSDSyslogFacility_Type.__name__ = "Integer32"
_RsWSDSyslogFacility_Object = MibScalar
rsWSDSyslogFacility = _RsWSDSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 87),
    _RsWSDSyslogFacility_Type()
)
rsWSDSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogFacility.setStatus("mandatory")
_RsACC_ObjectIdentity = ObjectIdentity
rsACC = _RsACC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88)
)
_RsWSDPingPortsTable_Object = MibTable
rsWSDPingPortsTable = _RsWSDPingPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 89)
)
if mibBuilder.loadTexts:
    rsWSDPingPortsTable.setStatus("mandatory")
_RsWSDPingPortsEntry_Object = MibTableRow
rsWSDPingPortsEntry = _RsWSDPingPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 89, 1)
)
rsWSDPingPortsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDPingPhysicalPortNumber"),
)
if mibBuilder.loadTexts:
    rsWSDPingPortsEntry.setStatus("mandatory")
_RsWSDPingPhysicalPortNumber_Type = Integer32
_RsWSDPingPhysicalPortNumber_Object = MibTableColumn
rsWSDPingPhysicalPortNumber = _RsWSDPingPhysicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 89, 1, 1),
    _RsWSDPingPhysicalPortNumber_Type()
)
rsWSDPingPhysicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPingPhysicalPortNumber.setStatus("mandatory")


class _RsWSDPingPhysicalPortState_Type(Integer32):
    """Custom type rsWSDPingPhysicalPortState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDPingPhysicalPortState_Type.__name__ = "Integer32"
_RsWSDPingPhysicalPortState_Object = MibTableColumn
rsWSDPingPhysicalPortState = _RsWSDPingPhysicalPortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 89, 1, 2),
    _RsWSDPingPhysicalPortState_Type()
)
rsWSDPingPhysicalPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPingPhysicalPortState.setStatus("mandatory")


class _RsWSDBackupInterfaceGrouping_Type(Integer32):
    """Custom type rsWSDBackupInterfaceGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDBackupInterfaceGrouping_Type.__name__ = "Integer32"
_RsWSDBackupInterfaceGrouping_Object = MibScalar
rsWSDBackupInterfaceGrouping = _RsWSDBackupInterfaceGrouping_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 90),
    _RsWSDBackupInterfaceGrouping_Type()
)
rsWSDBackupInterfaceGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDBackupInterfaceGrouping.setStatus("mandatory")


class _RsRegistrationStatus_Type(Integer32):
    """Custom type rsRegistrationStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("notRegistered", 2))
    )


_RsRegistrationStatus_Type.__name__ = "Integer32"
_RsRegistrationStatus_Object = MibScalar
rsRegistrationStatus = _RsRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 91),
    _RsRegistrationStatus_Type()
)
rsRegistrationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRegistrationStatus.setStatus("mandatory")
_RsCT100_ObjectIdentity = ObjectIdentity
rsCT100 = _RsCT100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 92)
)


class _RsFloatingPacketOffset_Type(Integer32):
    """Custom type rsFloatingPacketOffset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsFloatingPacketOffset_Type.__name__ = "Integer32"
_RsFloatingPacketOffset_Object = MibScalar
rsFloatingPacketOffset = _RsFloatingPacketOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 93),
    _RsFloatingPacketOffset_Type()
)
rsFloatingPacketOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFloatingPacketOffset.setStatus("mandatory")
_RsDnsParameters_ObjectIdentity = ObjectIdentity
rsDnsParameters = _RsDnsParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94)
)
_RsDnsrParameters_ObjectIdentity = ObjectIdentity
rsDnsrParameters = _RsDnsrParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1)
)
_RsDnsrPrimaryAddr_Type = IpAddress
_RsDnsrPrimaryAddr_Object = MibScalar
rsDnsrPrimaryAddr = _RsDnsrPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 1),
    _RsDnsrPrimaryAddr_Type()
)
rsDnsrPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsrPrimaryAddr.setStatus("mandatory")
_RsDnsrAlternateAddr_Type = IpAddress
_RsDnsrAlternateAddr_Object = MibScalar
rsDnsrAlternateAddr = _RsDnsrAlternateAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 2),
    _RsDnsrAlternateAddr_Type()
)
rsDnsrAlternateAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsrAlternateAddr.setStatus("mandatory")


class _RsDnsrEnable_Type(Integer32):
    """Custom type rsDnsrEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsDnsrEnable_Type.__name__ = "Integer32"
_RsDnsrEnable_Object = MibScalar
rsDnsrEnable = _RsDnsrEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 3),
    _RsDnsrEnable_Type()
)
rsDnsrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsrEnable.setStatus("mandatory")
_RsDnsrStaticResTable_Object = MibTable
rsDnsrStaticResTable = _RsDnsrStaticResTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 4)
)
if mibBuilder.loadTexts:
    rsDnsrStaticResTable.setStatus("mandatory")
_RsDnsrStaticResEntry_Object = MibTableRow
rsDnsrStaticResEntry = _RsDnsrStaticResEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 4, 1)
)
rsDnsrStaticResEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsDnsrSUrl"),
)
if mibBuilder.loadTexts:
    rsDnsrStaticResEntry.setStatus("mandatory")


class _RsDnsrSUrl_Type(DisplayString):
    """Custom type rsDnsrSUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 49),
    )


_RsDnsrSUrl_Type.__name__ = "DisplayString"
_RsDnsrSUrl_Object = MibTableColumn
rsDnsrSUrl = _RsDnsrSUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 4, 1, 1),
    _RsDnsrSUrl_Type()
)
rsDnsrSUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDnsrSUrl.setStatus("mandatory")
_RsDnsrSIp_Type = IpAddress
_RsDnsrSIp_Object = MibTableColumn
rsDnsrSIp = _RsDnsrSIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 4, 1, 2),
    _RsDnsrSIp_Type()
)
rsDnsrSIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsrSIp.setStatus("mandatory")
_RsDnsrSrowStatus_Type = RowStatus
_RsDnsrSrowStatus_Object = MibTableColumn
rsDnsrSrowStatus = _RsDnsrSrowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 1, 4, 1, 3),
    _RsDnsrSrowStatus_Type()
)
rsDnsrSrowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsrSrowStatus.setStatus("mandatory")
_RsDnsServerParameters_ObjectIdentity = ObjectIdentity
rsDnsServerParameters = _RsDnsServerParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2)
)


class _RsDnsServerEnable_Type(Integer32):
    """Custom type rsDnsServerEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsDnsServerEnable_Type.__name__ = "Integer32"
_RsDnsServerEnable_Object = MibScalar
rsDnsServerEnable = _RsDnsServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 1),
    _RsDnsServerEnable_Type()
)
rsDnsServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsServerEnable.setStatus("mandatory")
_RsDnsServerStaticResTable_Object = MibTable
rsDnsServerStaticResTable = _RsDnsServerStaticResTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 2)
)
if mibBuilder.loadTexts:
    rsDnsServerStaticResTable.setStatus("mandatory")
_RsDnsServerStaticResEntry_Object = MibTableRow
rsDnsServerStaticResEntry = _RsDnsServerStaticResEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 2, 1)
)
rsDnsServerStaticResEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsDnsServerSUrl"),
)
if mibBuilder.loadTexts:
    rsDnsServerStaticResEntry.setStatus("mandatory")


class _RsDnsServerSUrl_Type(DisplayString):
    """Custom type rsDnsServerSUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsDnsServerSUrl_Type.__name__ = "DisplayString"
_RsDnsServerSUrl_Object = MibTableColumn
rsDnsServerSUrl = _RsDnsServerSUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 2, 1, 1),
    _RsDnsServerSUrl_Type()
)
rsDnsServerSUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDnsServerSUrl.setStatus("mandatory")
_RsDnsServerSIp_Type = IpAddress
_RsDnsServerSIp_Object = MibTableColumn
rsDnsServerSIp = _RsDnsServerSIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 2, 1, 2),
    _RsDnsServerSIp_Type()
)
rsDnsServerSIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsServerSIp.setStatus("mandatory")


class _RsDnsServerSEnable_Type(Integer32):
    """Custom type rsDnsServerSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsDnsServerSEnable_Type.__name__ = "Integer32"
_RsDnsServerSEnable_Object = MibTableColumn
rsDnsServerSEnable = _RsDnsServerSEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 2, 1, 3),
    _RsDnsServerSEnable_Type()
)
rsDnsServerSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsServerSEnable.setStatus("mandatory")
_RsDnsServerSrowStatus_Type = RowStatus
_RsDnsServerSrowStatus_Object = MibTableColumn
rsDnsServerSrowStatus = _RsDnsServerSrowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 94, 2, 2, 1, 4),
    _RsDnsServerSrowStatus_Type()
)
rsDnsServerSrowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDnsServerSrowStatus.setStatus("mandatory")


class _RsPrivateCheckSNMPPort_Type(Integer32):
    """Custom type rsPrivateCheckSNMPPort based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsPrivateCheckSNMPPort_Type.__name__ = "Integer32"
_RsPrivateCheckSNMPPort_Object = MibScalar
rsPrivateCheckSNMPPort = _RsPrivateCheckSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 95),
    _RsPrivateCheckSNMPPort_Type()
)
rsPrivateCheckSNMPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPrivateCheckSNMPPort.setStatus("mandatory")


class _RsVlanTagHandling_Type(Integer32):
    """Custom type rsVlanTagHandling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("retain", 1),
          ("overwrite", 2))
    )


_RsVlanTagHandling_Type.__name__ = "Integer32"
_RsVlanTagHandling_Object = MibScalar
rsVlanTagHandling = _RsVlanTagHandling_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 96),
    _RsVlanTagHandling_Type()
)
rsVlanTagHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsVlanTagHandling.setStatus("mandatory")
_RsSmtpParameters_ObjectIdentity = ObjectIdentity
rsSmtpParameters = _RsSmtpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 97)
)


class _RsSmtpPrimaryAddr_Type(DisplayString):
    """Custom type rsSmtpPrimaryAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSmtpPrimaryAddr_Type.__name__ = "DisplayString"
_RsSmtpPrimaryAddr_Object = MibScalar
rsSmtpPrimaryAddr = _RsSmtpPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 97, 1),
    _RsSmtpPrimaryAddr_Type()
)
rsSmtpPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSmtpPrimaryAddr.setStatus("mandatory")


class _RsSmtpAlternateAddr_Type(DisplayString):
    """Custom type rsSmtpAlternateAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSmtpAlternateAddr_Type.__name__ = "DisplayString"
_RsSmtpAlternateAddr_Object = MibScalar
rsSmtpAlternateAddr = _RsSmtpAlternateAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 97, 2),
    _RsSmtpAlternateAddr_Type()
)
rsSmtpAlternateAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSmtpAlternateAddr.setStatus("mandatory")


class _RsSmtpEnable_Type(Integer32):
    """Custom type rsSmtpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsSmtpEnable_Type.__name__ = "Integer32"
_RsSmtpEnable_Object = MibScalar
rsSmtpEnable = _RsSmtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 97, 3),
    _RsSmtpEnable_Type()
)
rsSmtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSmtpEnable.setStatus("mandatory")


class _RsSmtpOwnAddr_Type(DisplayString):
    """Custom type rsSmtpOwnAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSmtpOwnAddr_Type.__name__ = "DisplayString"
_RsSmtpOwnAddr_Object = MibScalar
rsSmtpOwnAddr = _RsSmtpOwnAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 97, 4),
    _RsSmtpOwnAddr_Type()
)
rsSmtpOwnAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSmtpOwnAddr.setStatus("mandatory")


class _RsSmtpBackupOwnAddr_Type(DisplayString):
    """Custom type rsSmtpBackupOwnAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSmtpBackupOwnAddr_Type.__name__ = "DisplayString"
_RsSmtpBackupOwnAddr_Object = MibScalar
rsSmtpBackupOwnAddr = _RsSmtpBackupOwnAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 97, 5),
    _RsSmtpBackupOwnAddr_Type()
)
rsSmtpBackupOwnAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSmtpBackupOwnAddr.setStatus("mandatory")


class _RsWSDSyslogUrl_Type(DisplayString):
    """Custom type rsWSDSyslogUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsWSDSyslogUrl_Type.__name__ = "DisplayString"
_RsWSDSyslogUrl_Object = MibScalar
rsWSDSyslogUrl = _RsWSDSyslogUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 98),
    _RsWSDSyslogUrl_Type()
)
rsWSDSyslogUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogUrl.setStatus("mandatory")
_RsFileSystem_ObjectIdentity = ObjectIdentity
rsFileSystem = _RsFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99)
)
_RsFSapplList_Object = MibTable
rsFSapplList = _RsFSapplList_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1)
)
if mibBuilder.loadTexts:
    rsFSapplList.setStatus("mandatory")
_RsFSapplEntry_Object = MibTableRow
rsFSapplEntry = _RsFSapplEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1)
)
rsFSapplEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsFSapplName"),
)
if mibBuilder.loadTexts:
    rsFSapplEntry.setStatus("mandatory")


class _RsFSapplName_Type(DisplayString):
    """Custom type rsFSapplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_RsFSapplName_Type.__name__ = "DisplayString"
_RsFSapplName_Object = MibTableColumn
rsFSapplName = _RsFSapplName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 1),
    _RsFSapplName_Type()
)
rsFSapplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFSapplName.setStatus("mandatory")
_RsFSapplIndex_Type = Integer32
_RsFSapplIndex_Object = MibTableColumn
rsFSapplIndex = _RsFSapplIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 2),
    _RsFSapplIndex_Type()
)
rsFSapplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFSapplIndex.setStatus("mandatory")
_RsFSapplValid_Type = TruthValue
_RsFSapplValid_Object = MibTableColumn
rsFSapplValid = _RsFSapplValid_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 3),
    _RsFSapplValid_Type()
)
rsFSapplValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFSapplValid.setStatus("mandatory")
_RsFSapplActive_Type = TruthValue
_RsFSapplActive_Object = MibTableColumn
rsFSapplActive = _RsFSapplActive_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 4),
    _RsFSapplActive_Type()
)
rsFSapplActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFSapplActive.setStatus("mandatory")


class _RsFSapplVersion_Type(DisplayString):
    """Custom type rsFSapplVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsFSapplVersion_Type.__name__ = "DisplayString"
_RsFSapplVersion_Object = MibTableColumn
rsFSapplVersion = _RsFSapplVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 5),
    _RsFSapplVersion_Type()
)
rsFSapplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFSapplVersion.setStatus("mandatory")
_RsFSapplStartup_Type = TruthValue
_RsFSapplStartup_Object = MibTableColumn
rsFSapplStartup = _RsFSapplStartup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 6),
    _RsFSapplStartup_Type()
)
rsFSapplStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFSapplStartup.setStatus("mandatory")
_RsFSapplStatus_Type = RowStatus
_RsFSapplStatus_Object = MibTableColumn
rsFSapplStatus = _RsFSapplStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 1, 1, 7),
    _RsFSapplStatus_Type()
)
rsFSapplStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFSapplStatus.setStatus("mandatory")


class _RsFSinstallNew_Type(Integer32):
    """Custom type rsFSinstallNew based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsFSinstallNew_Type.__name__ = "Integer32"
_RsFSinstallNew_Object = MibScalar
rsFSinstallNew = _RsFSinstallNew_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 2),
    _RsFSinstallNew_Type()
)
rsFSinstallNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFSinstallNew.setStatus("mandatory")
_RdwrConfigurationFileTable_Object = MibTable
rdwrConfigurationFileTable = _RdwrConfigurationFileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3)
)
if mibBuilder.loadTexts:
    rdwrConfigurationFileTable.setStatus("mandatory")
_RdwrConfigurationFileEntry_Object = MibTableRow
rdwrConfigurationFileEntry = _RdwrConfigurationFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1)
)
rdwrConfigurationFileEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrConfigurationFileApp"),
    (0, "RADWARE-MIB", "rdwrConfigurationFileName"),
)
if mibBuilder.loadTexts:
    rdwrConfigurationFileEntry.setStatus("mandatory")


class _RdwrConfigurationFileApp_Type(DisplayString):
    """Custom type rdwrConfigurationFileApp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RdwrConfigurationFileApp_Type.__name__ = "DisplayString"
_RdwrConfigurationFileApp_Object = MibTableColumn
rdwrConfigurationFileApp = _RdwrConfigurationFileApp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 1),
    _RdwrConfigurationFileApp_Type()
)
rdwrConfigurationFileApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfigurationFileApp.setStatus("mandatory")


class _RdwrConfigurationFileName_Type(DisplayString):
    """Custom type rdwrConfigurationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RdwrConfigurationFileName_Type.__name__ = "DisplayString"
_RdwrConfigurationFileName_Object = MibTableColumn
rdwrConfigurationFileName = _RdwrConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 2),
    _RdwrConfigurationFileName_Type()
)
rdwrConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfigurationFileName.setStatus("mandatory")
_RdwrConfigurationFileRunning_Type = TruthValue
_RdwrConfigurationFileRunning_Object = MibTableColumn
rdwrConfigurationFileRunning = _RdwrConfigurationFileRunning_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 3),
    _RdwrConfigurationFileRunning_Type()
)
rdwrConfigurationFileRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfigurationFileRunning.setStatus("mandatory")
_RdwrConfigurationFileInstalled_Type = TruthValue
_RdwrConfigurationFileInstalled_Object = MibTableColumn
rdwrConfigurationFileInstalled = _RdwrConfigurationFileInstalled_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 4),
    _RdwrConfigurationFileInstalled_Type()
)
rdwrConfigurationFileInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfigurationFileInstalled.setStatus("mandatory")


class _RdwrConfigurationFilePath_Type(DisplayString):
    """Custom type rdwrConfigurationFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RdwrConfigurationFilePath_Type.__name__ = "DisplayString"
_RdwrConfigurationFilePath_Object = MibTableColumn
rdwrConfigurationFilePath = _RdwrConfigurationFilePath_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 5),
    _RdwrConfigurationFilePath_Type()
)
rdwrConfigurationFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfigurationFilePath.setStatus("mandatory")


class _RdwrConfigurationFileAction_Type(Integer32):
    """Custom type rdwrConfigurationFileAction based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("add", 2),
          ("install", 3),
          ("delete", 4))
    )


_RdwrConfigurationFileAction_Type.__name__ = "Integer32"
_RdwrConfigurationFileAction_Object = MibTableColumn
rdwrConfigurationFileAction = _RdwrConfigurationFileAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 6),
    _RdwrConfigurationFileAction_Type()
)
rdwrConfigurationFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfigurationFileAction.setStatus("mandatory")
_RdwrConfigurationFileStatus_Type = RowStatus
_RdwrConfigurationFileStatus_Object = MibTableColumn
rdwrConfigurationFileStatus = _RdwrConfigurationFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 3, 1, 7),
    _RdwrConfigurationFileStatus_Type()
)
rdwrConfigurationFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfigurationFileStatus.setStatus("mandatory")
_RdwrDefCfg_ObjectIdentity = ObjectIdentity
rdwrDefCfg = _RdwrDefCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4)
)
_RdwrDefCfgIpAddress_Type = IpAddress
_RdwrDefCfgIpAddress_Object = MibScalar
rdwrDefCfgIpAddress = _RdwrDefCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 1),
    _RdwrDefCfgIpAddress_Type()
)
rdwrDefCfgIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgIpAddress.setStatus("mandatory")
_RdwrDefCfgIpMask_Type = IpAddress
_RdwrDefCfgIpMask_Object = MibScalar
rdwrDefCfgIpMask = _RdwrDefCfgIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 2),
    _RdwrDefCfgIpMask_Type()
)
rdwrDefCfgIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgIpMask.setStatus("mandatory")
_RdwrDefCfgPort_Type = Integer32
_RdwrDefCfgPort_Object = MibScalar
rdwrDefCfgPort = _RdwrDefCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 3),
    _RdwrDefCfgPort_Type()
)
rdwrDefCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgPort.setStatus("mandatory")
_RdwrDefCfgGateway_Type = IpAddress
_RdwrDefCfgGateway_Object = MibScalar
rdwrDefCfgGateway = _RdwrDefCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 4),
    _RdwrDefCfgGateway_Type()
)
rdwrDefCfgGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgGateway.setStatus("mandatory")


class _RdwrDefCfgUserName_Type(DisplayString):
    """Custom type rdwrDefCfgUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RdwrDefCfgUserName_Type.__name__ = "DisplayString"
_RdwrDefCfgUserName_Object = MibScalar
rdwrDefCfgUserName = _RdwrDefCfgUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 5),
    _RdwrDefCfgUserName_Type()
)
rdwrDefCfgUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgUserName.setStatus("mandatory")


class _RdwrDefCfgUserPassword_Type(DisplayString):
    """Custom type rdwrDefCfgUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RdwrDefCfgUserPassword_Type.__name__ = "DisplayString"
_RdwrDefCfgUserPassword_Object = MibScalar
rdwrDefCfgUserPassword = _RdwrDefCfgUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 6),
    _RdwrDefCfgUserPassword_Type()
)
rdwrDefCfgUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgUserPassword.setStatus("mandatory")


class _RdwrDefCfgCommunity_Type(DisplayString):
    """Custom type rdwrDefCfgCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RdwrDefCfgCommunity_Type.__name__ = "DisplayString"
_RdwrDefCfgCommunity_Object = MibScalar
rdwrDefCfgCommunity = _RdwrDefCfgCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 4, 7),
    _RdwrDefCfgCommunity_Type()
)
rdwrDefCfgCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDefCfgCommunity.setStatus("mandatory")
_RdwrApplicationFileTable_Object = MibTable
rdwrApplicationFileTable = _RdwrApplicationFileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5)
)
if mibBuilder.loadTexts:
    rdwrApplicationFileTable.setStatus("mandatory")
_RdwrApplicationFileEntry_Object = MibTableRow
rdwrApplicationFileEntry = _RdwrApplicationFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1)
)
rdwrApplicationFileEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrApplicationFileName"),
)
if mibBuilder.loadTexts:
    rdwrApplicationFileEntry.setStatus("mandatory")


class _RdwrApplicationFileName_Type(DisplayString):
    """Custom type rdwrApplicationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RdwrApplicationFileName_Type.__name__ = "DisplayString"
_RdwrApplicationFileName_Object = MibTableColumn
rdwrApplicationFileName = _RdwrApplicationFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 1),
    _RdwrApplicationFileName_Type()
)
rdwrApplicationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrApplicationFileName.setStatus("mandatory")
_RdwrApplicationFileRunning_Type = TruthValue
_RdwrApplicationFileRunning_Object = MibTableColumn
rdwrApplicationFileRunning = _RdwrApplicationFileRunning_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 2),
    _RdwrApplicationFileRunning_Type()
)
rdwrApplicationFileRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrApplicationFileRunning.setStatus("mandatory")
_RdwrApplicationFileSelected_Type = TruthValue
_RdwrApplicationFileSelected_Object = MibTableColumn
rdwrApplicationFileSelected = _RdwrApplicationFileSelected_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 3),
    _RdwrApplicationFileSelected_Type()
)
rdwrApplicationFileSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrApplicationFileSelected.setStatus("mandatory")
_RdwrApplicationFileValid_Type = TruthValue
_RdwrApplicationFileValid_Object = MibTableColumn
rdwrApplicationFileValid = _RdwrApplicationFileValid_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 4),
    _RdwrApplicationFileValid_Type()
)
rdwrApplicationFileValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrApplicationFileValid.setStatus("mandatory")
_RdwrApplicationFileStartup_Type = TruthValue
_RdwrApplicationFileStartup_Object = MibTableColumn
rdwrApplicationFileStartup = _RdwrApplicationFileStartup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 5),
    _RdwrApplicationFileStartup_Type()
)
rdwrApplicationFileStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrApplicationFileStartup.setStatus("mandatory")


class _RdwrApplicationFileVersion_Type(DisplayString):
    """Custom type rdwrApplicationFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RdwrApplicationFileVersion_Type.__name__ = "DisplayString"
_RdwrApplicationFileVersion_Object = MibTableColumn
rdwrApplicationFileVersion = _RdwrApplicationFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 6),
    _RdwrApplicationFileVersion_Type()
)
rdwrApplicationFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrApplicationFileVersion.setStatus("mandatory")


class _RdwrApplicationFileAction_Type(Integer32):
    """Custom type rdwrApplicationFileAction based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("add", 2),
          ("select", 3),
          ("delete", 4))
    )


_RdwrApplicationFileAction_Type.__name__ = "Integer32"
_RdwrApplicationFileAction_Object = MibTableColumn
rdwrApplicationFileAction = _RdwrApplicationFileAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 7),
    _RdwrApplicationFileAction_Type()
)
rdwrApplicationFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrApplicationFileAction.setStatus("mandatory")
_RdwrApplicationFileStatus_Type = RowStatus
_RdwrApplicationFileStatus_Object = MibTableColumn
rdwrApplicationFileStatus = _RdwrApplicationFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 99, 5, 1, 8),
    _RdwrApplicationFileStatus_Type()
)
rdwrApplicationFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrApplicationFileStatus.setStatus("mandatory")


class _RsWSDHardwareLicense_Type(DisplayString):
    """Custom type rsWSDHardwareLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDHardwareLicense_Type.__name__ = "DisplayString"
_RsWSDHardwareLicense_Object = MibScalar
rsWSDHardwareLicense = _RsWSDHardwareLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 100),
    _RsWSDHardwareLicense_Type()
)
rsWSDHardwareLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHardwareLicense.setStatus("mandatory")


class _RsWSDHardwareLicenseID_Type(DisplayString):
    """Custom type rsWSDHardwareLicenseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDHardwareLicenseID_Type.__name__ = "DisplayString"
_RsWSDHardwareLicenseID_Object = MibScalar
rsWSDHardwareLicenseID = _RsWSDHardwareLicenseID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 101),
    _RsWSDHardwareLicenseID_Type()
)
rsWSDHardwareLicenseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDHardwareLicenseID.setStatus("mandatory")
_RdwrSnmpParameters_ObjectIdentity = ObjectIdentity
rdwrSnmpParameters = _RdwrSnmpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102)
)
_RdwrSnmpSupportedVersions_Type = Integer32
_RdwrSnmpSupportedVersions_Object = MibScalar
rdwrSnmpSupportedVersions = _RdwrSnmpSupportedVersions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 1),
    _RdwrSnmpSupportedVersions_Type()
)
rdwrSnmpSupportedVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpSupportedVersions.setStatus("mandatory")
_RdwrSnmpSupportedVersionsAfterReset_Type = Integer32
_RdwrSnmpSupportedVersionsAfterReset_Object = MibScalar
rdwrSnmpSupportedVersionsAfterReset = _RdwrSnmpSupportedVersionsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 2),
    _RdwrSnmpSupportedVersionsAfterReset_Type()
)
rdwrSnmpSupportedVersionsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSnmpSupportedVersionsAfterReset.setStatus("mandatory")
_RdwrSnmpPort_Type = Integer32
_RdwrSnmpPort_Object = MibScalar
rdwrSnmpPort = _RdwrSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 3),
    _RdwrSnmpPort_Type()
)
rdwrSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSnmpPort.setStatus("mandatory")


class _RdwrSnmpStatus_Type(Integer32):
    """Custom type rdwrSnmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RdwrSnmpStatus_Type.__name__ = "Integer32"
_RdwrSnmpStatus_Object = MibScalar
rdwrSnmpStatus = _RdwrSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 4),
    _RdwrSnmpStatus_Type()
)
rdwrSnmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSnmpStatus.setStatus("mandatory")


class _RdwrSnmpConfigFileFormat_Type(Integer32):
    """Custom type rdwrSnmpConfigFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("ber", 2),
          ("ascii", 3))
    )


_RdwrSnmpConfigFileFormat_Type.__name__ = "Integer32"
_RdwrSnmpConfigFileFormat_Object = MibScalar
rdwrSnmpConfigFileFormat = _RdwrSnmpConfigFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 5),
    _RdwrSnmpConfigFileFormat_Type()
)
rdwrSnmpConfigFileFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSnmpConfigFileFormat.setStatus("mandatory")
_RdwrSnmpErrorIndex_Type = Integer32
_RdwrSnmpErrorIndex_Object = MibScalar
rdwrSnmpErrorIndex = _RdwrSnmpErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 6),
    _RdwrSnmpErrorIndex_Type()
)
rdwrSnmpErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorIndex.setStatus("mandatory")
_RdwrSnmpErrorStatus_Type = Integer32
_RdwrSnmpErrorStatus_Object = MibScalar
rdwrSnmpErrorStatus = _RdwrSnmpErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 7),
    _RdwrSnmpErrorStatus_Type()
)
rdwrSnmpErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorStatus.setStatus("mandatory")


class _RdwrSnmpErrorDescription_Type(DisplayString):
    """Custom type rdwrSnmpErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrSnmpErrorDescription_Type.__name__ = "DisplayString"
_RdwrSnmpErrorDescription_Object = MibScalar
rdwrSnmpErrorDescription = _RdwrSnmpErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 8),
    _RdwrSnmpErrorDescription_Type()
)
rdwrSnmpErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorDescription.setStatus("mandatory")
_RdwrSnmpErrorRequestId_Type = Integer32
_RdwrSnmpErrorRequestId_Object = MibScalar
rdwrSnmpErrorRequestId = _RdwrSnmpErrorRequestId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 9),
    _RdwrSnmpErrorRequestId_Type()
)
rdwrSnmpErrorRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorRequestId.setStatus("mandatory")
_RdwrSnmpErrorTbTable_Object = MibTable
rdwrSnmpErrorTbTable = _RdwrSnmpErrorTbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10)
)
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbTable.setStatus("mandatory")
_RdwrSnmpErrorTbEntry_Object = MibTableRow
rdwrSnmpErrorTbEntry = _RdwrSnmpErrorTbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1)
)
rdwrSnmpErrorTbEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrSnmpErrorTbRequestId"),
)
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbEntry.setStatus("mandatory")
_RdwrSnmpErrorTbRequestId_Type = Integer32
_RdwrSnmpErrorTbRequestId_Object = MibTableColumn
rdwrSnmpErrorTbRequestId = _RdwrSnmpErrorTbRequestId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 1),
    _RdwrSnmpErrorTbRequestId_Type()
)
rdwrSnmpErrorTbRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbRequestId.setStatus("mandatory")
_RdwrSnmpErrorTbVarId_Type = ObjectIdentifier
_RdwrSnmpErrorTbVarId_Object = MibTableColumn
rdwrSnmpErrorTbVarId = _RdwrSnmpErrorTbVarId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 2),
    _RdwrSnmpErrorTbVarId_Type()
)
rdwrSnmpErrorTbVarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbVarId.setStatus("mandatory")


class _RdwrSnmpErrorTbDescription_Type(DisplayString):
    """Custom type rdwrSnmpErrorTbDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrSnmpErrorTbDescription_Type.__name__ = "DisplayString"
_RdwrSnmpErrorTbDescription_Object = MibTableColumn
rdwrSnmpErrorTbDescription = _RdwrSnmpErrorTbDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 3),
    _RdwrSnmpErrorTbDescription_Type()
)
rdwrSnmpErrorTbDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbDescription.setStatus("mandatory")
_RdwrSnmpErrorTbErrorIndex_Type = Integer32
_RdwrSnmpErrorTbErrorIndex_Object = MibTableColumn
rdwrSnmpErrorTbErrorIndex = _RdwrSnmpErrorTbErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 4),
    _RdwrSnmpErrorTbErrorIndex_Type()
)
rdwrSnmpErrorTbErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbErrorIndex.setStatus("mandatory")


class _RdwrSnmpErrorTbType_Type(Integer32):
    """Custom type rdwrSnmpErrorTbType based on Integer32"""
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
        *(("ok", 0),
          ("application", 1),
          ("internalRange", 2),
          ("internalGeneral", 3))
    )


_RdwrSnmpErrorTbType_Type.__name__ = "Integer32"
_RdwrSnmpErrorTbType_Object = MibTableColumn
rdwrSnmpErrorTbType = _RdwrSnmpErrorTbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 5),
    _RdwrSnmpErrorTbType_Type()
)
rdwrSnmpErrorTbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbType.setStatus("mandatory")


class _RdwrSnmpErrorTbStatus_Type(Integer32):
    """Custom type rdwrSnmpErrorTbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("tooBig", 1),
          ("noSuchName", 2),
          ("badValue", 3),
          ("readOnly", 4),
          ("genErr", 5))
    )


_RdwrSnmpErrorTbStatus_Type.__name__ = "Integer32"
_RdwrSnmpErrorTbStatus_Object = MibTableColumn
rdwrSnmpErrorTbStatus = _RdwrSnmpErrorTbStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 6),
    _RdwrSnmpErrorTbStatus_Type()
)
rdwrSnmpErrorTbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbStatus.setStatus("mandatory")
_RdwrSnmpErrorTbFieldInEntry_Type = Integer32
_RdwrSnmpErrorTbFieldInEntry_Object = MibTableColumn
rdwrSnmpErrorTbFieldInEntry = _RdwrSnmpErrorTbFieldInEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 7),
    _RdwrSnmpErrorTbFieldInEntry_Type()
)
rdwrSnmpErrorTbFieldInEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbFieldInEntry.setStatus("mandatory")


class _RdwrSnmpErrorTbTime_Type(DisplayString):
    """Custom type rdwrSnmpErrorTbTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixed_length = 9


_RdwrSnmpErrorTbTime_Type.__name__ = "DisplayString"
_RdwrSnmpErrorTbTime_Object = MibTableColumn
rdwrSnmpErrorTbTime = _RdwrSnmpErrorTbTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 8),
    _RdwrSnmpErrorTbTime_Type()
)
rdwrSnmpErrorTbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbTime.setStatus("mandatory")


class _RdwrSnmpErrorTbDate_Type(DisplayString):
    """Custom type rdwrSnmpErrorTbDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_RdwrSnmpErrorTbDate_Type.__name__ = "DisplayString"
_RdwrSnmpErrorTbDate_Object = MibTableColumn
rdwrSnmpErrorTbDate = _RdwrSnmpErrorTbDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 10, 1, 9),
    _RdwrSnmpErrorTbDate_Type()
)
rdwrSnmpErrorTbDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbDate.setStatus("mandatory")


class _RdwrSnmpErrorTbTableReset_Type(Integer32):
    """Custom type rdwrSnmpErrorTbTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RdwrSnmpErrorTbTableReset_Type.__name__ = "Integer32"
_RdwrSnmpErrorTbTableReset_Object = MibScalar
rdwrSnmpErrorTbTableReset = _RdwrSnmpErrorTbTableReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 11),
    _RdwrSnmpErrorTbTableReset_Type()
)
rdwrSnmpErrorTbTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSnmpErrorTbTableReset.setStatus("mandatory")
_RdwrLastConfigurationChangesTable_Object = MibTable
rdwrLastConfigurationChangesTable = _RdwrLastConfigurationChangesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12)
)
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesTable.setStatus("mandatory")
_RdwrLastConfigurationChangesEntry_Object = MibTableRow
rdwrLastConfigurationChangesEntry = _RdwrLastConfigurationChangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12, 1)
)
rdwrLastConfigurationChangesEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrLastConfigurationChangesID"),
)
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesEntry.setStatus("mandatory")
_RdwrLastConfigurationChangesID_Type = Integer32
_RdwrLastConfigurationChangesID_Object = MibTableColumn
rdwrLastConfigurationChangesID = _RdwrLastConfigurationChangesID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12, 1, 1),
    _RdwrLastConfigurationChangesID_Type()
)
rdwrLastConfigurationChangesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesID.setStatus("mandatory")
_RdwrLastConfigurationChangesStatus_Type = RowStatus
_RdwrLastConfigurationChangesStatus_Object = MibTableColumn
rdwrLastConfigurationChangesStatus = _RdwrLastConfigurationChangesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12, 1, 2),
    _RdwrLastConfigurationChangesStatus_Type()
)
rdwrLastConfigurationChangesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesStatus.setStatus("mandatory")
_RdwrLastConfigurationChangesMibOid_Type = ObjectIdentifier
_RdwrLastConfigurationChangesMibOid_Object = MibTableColumn
rdwrLastConfigurationChangesMibOid = _RdwrLastConfigurationChangesMibOid_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12, 1, 3),
    _RdwrLastConfigurationChangesMibOid_Type()
)
rdwrLastConfigurationChangesMibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesMibOid.setStatus("mandatory")


class _RdwrLastConfigurationChangesChangeType_Type(Integer32):
    """Custom type rdwrLastConfigurationChangesChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("modify", 2),
          ("delete", 3),
          ("configurationFileLoaded", 4),
          ("tableNotUpdated", 5),
          ("refreshTable", 6),
          ("updatePolicies", 7))
    )


_RdwrLastConfigurationChangesChangeType_Type.__name__ = "Integer32"
_RdwrLastConfigurationChangesChangeType_Object = MibTableColumn
rdwrLastConfigurationChangesChangeType = _RdwrLastConfigurationChangesChangeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12, 1, 4),
    _RdwrLastConfigurationChangesChangeType_Type()
)
rdwrLastConfigurationChangesChangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesChangeType.setStatus("mandatory")
_RdwrLastConfigurationChangesKeys_Type = DisplayString
_RdwrLastConfigurationChangesKeys_Object = MibTableColumn
rdwrLastConfigurationChangesKeys = _RdwrLastConfigurationChangesKeys_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 12, 1, 5),
    _RdwrLastConfigurationChangesKeys_Type()
)
rdwrLastConfigurationChangesKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesKeys.setStatus("mandatory")


class _RdwrLastConfigurationChangesTableReset_Type(Integer32):
    """Custom type rdwrLastConfigurationChangesTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RdwrLastConfigurationChangesTableReset_Type.__name__ = "Integer32"
_RdwrLastConfigurationChangesTableReset_Object = MibScalar
rdwrLastConfigurationChangesTableReset = _RdwrLastConfigurationChangesTableReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 13),
    _RdwrLastConfigurationChangesTableReset_Type()
)
rdwrLastConfigurationChangesTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesTableReset.setStatus("mandatory")
_RdwrLastConfigurationChangesTimestamp_Type = TimeStamp
_RdwrLastConfigurationChangesTimestamp_Object = MibScalar
rdwrLastConfigurationChangesTimestamp = _RdwrLastConfigurationChangesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 14),
    _RdwrLastConfigurationChangesTimestamp_Type()
)
rdwrLastConfigurationChangesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesTimestamp.setStatus("mandatory")
_RdwrLastConfigurationChangesTime_Type = Integer32
_RdwrLastConfigurationChangesTime_Object = MibScalar
rdwrLastConfigurationChangesTime = _RdwrLastConfigurationChangesTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 102, 15),
    _RdwrLastConfigurationChangesTime_Type()
)
rdwrLastConfigurationChangesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrLastConfigurationChangesTime.setStatus("mandatory")


class _RsWSDSyslogSourcePort_Type(Integer32):
    """Custom type rsWSDSyslogSourcePort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(1024, 65535),
    )


_RsWSDSyslogSourcePort_Type.__name__ = "Integer32"
_RsWSDSyslogSourcePort_Object = MibScalar
rsWSDSyslogSourcePort = _RsWSDSyslogSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 103),
    _RsWSDSyslogSourcePort_Type()
)
rsWSDSyslogSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogSourcePort.setStatus("mandatory")
_RsSESSION_ObjectIdentity = ObjectIdentity
rsSESSION = _RsSESSION_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104)
)
_RsLinkAggregationHash_ObjectIdentity = ObjectIdentity
rsLinkAggregationHash = _RsLinkAggregationHash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 105)
)


class _RsLinkAggregationL2Hash_Type(Integer32):
    """Custom type rsLinkAggregationL2Hash based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("source", 2),
          ("detination", 3),
          ("both", 4))
    )


_RsLinkAggregationL2Hash_Type.__name__ = "Integer32"
_RsLinkAggregationL2Hash_Object = MibScalar
rsLinkAggregationL2Hash = _RsLinkAggregationL2Hash_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 105, 1),
    _RsLinkAggregationL2Hash_Type()
)
rsLinkAggregationL2Hash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLinkAggregationL2Hash.setStatus("mandatory")


class _RsLinkAggregationL3Hash_Type(Integer32):
    """Custom type rsLinkAggregationL3Hash based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("source", 2),
          ("detination", 3),
          ("both", 4))
    )


_RsLinkAggregationL3Hash_Type.__name__ = "Integer32"
_RsLinkAggregationL3Hash_Object = MibScalar
rsLinkAggregationL3Hash = _RsLinkAggregationL3Hash_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 105, 2),
    _RsLinkAggregationL3Hash_Type()
)
rsLinkAggregationL3Hash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLinkAggregationL3Hash.setStatus("mandatory")


class _RsLinkAggregationL4Hash_Type(Integer32):
    """Custom type rsLinkAggregationL4Hash based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("source", 2),
          ("detination", 3),
          ("both", 4))
    )


_RsLinkAggregationL4Hash_Type.__name__ = "Integer32"
_RsLinkAggregationL4Hash_Object = MibScalar
rsLinkAggregationL4Hash = _RsLinkAggregationL4Hash_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 105, 3),
    _RsLinkAggregationL4Hash_Type()
)
rsLinkAggregationL4Hash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLinkAggregationL4Hash.setStatus("mandatory")
_RsScheduleTable_Object = MibTable
rsScheduleTable = _RsScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106)
)
if mibBuilder.loadTexts:
    rsScheduleTable.setStatus("mandatory")
_RsScheduleEntry_Object = MibTableRow
rsScheduleEntry = _RsScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1)
)
rsScheduleEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsScheduleName"),
)
if mibBuilder.loadTexts:
    rsScheduleEntry.setStatus("mandatory")


class _RsScheduleName_Type(DisplayString):
    """Custom type rsScheduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsScheduleName_Type.__name__ = "DisplayString"
_RsScheduleName_Object = MibTableColumn
rsScheduleName = _RsScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1, 1),
    _RsScheduleName_Type()
)
rsScheduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsScheduleName.setStatus("mandatory")


class _RsScheduleFrequency_Type(Integer32):
    """Custom type rsScheduleFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("once", 1),
          ("daily", 2),
          ("weekly", 3))
    )


_RsScheduleFrequency_Type.__name__ = "Integer32"
_RsScheduleFrequency_Object = MibTableColumn
rsScheduleFrequency = _RsScheduleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1, 2),
    _RsScheduleFrequency_Type()
)
rsScheduleFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsScheduleFrequency.setStatus("mandatory")


class _RsScheduleTime_Type(DisplayString):
    """Custom type rsScheduleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RsScheduleTime_Type.__name__ = "DisplayString"
_RsScheduleTime_Object = MibTableColumn
rsScheduleTime = _RsScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1, 3),
    _RsScheduleTime_Type()
)
rsScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsScheduleTime.setStatus("mandatory")


class _RsScheduleDays_Type(DisplayString):
    """Custom type rsScheduleDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_RsScheduleDays_Type.__name__ = "DisplayString"
_RsScheduleDays_Object = MibTableColumn
rsScheduleDays = _RsScheduleDays_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1, 4),
    _RsScheduleDays_Type()
)
rsScheduleDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsScheduleDays.setStatus("mandatory")


class _RsScheduleDate_Type(DisplayString):
    """Custom type rsScheduleDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RsScheduleDate_Type.__name__ = "DisplayString"
_RsScheduleDate_Object = MibTableColumn
rsScheduleDate = _RsScheduleDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1, 5),
    _RsScheduleDate_Type()
)
rsScheduleDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsScheduleDate.setStatus("mandatory")
_RsScheduleStatus_Type = RowStatus
_RsScheduleStatus_Object = MibTableColumn
rsScheduleStatus = _RsScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 106, 1, 6),
    _RsScheduleStatus_Type()
)
rsScheduleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsScheduleStatus.setStatus("mandatory")
_RdwrFtpParameters_ObjectIdentity = ObjectIdentity
rdwrFtpParameters = _RdwrFtpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 107)
)
_RdwrFtpPort_Type = Integer32
_RdwrFtpPort_Object = MibScalar
rdwrFtpPort = _RdwrFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 107, 1),
    _RdwrFtpPort_Type()
)
rdwrFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrFtpPort.setStatus("mandatory")


class _RdwrFtpStatus_Type(Integer32):
    """Custom type rdwrFtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RdwrFtpStatus_Type.__name__ = "Integer32"
_RdwrFtpStatus_Object = MibScalar
rdwrFtpStatus = _RdwrFtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 107, 2),
    _RdwrFtpStatus_Type()
)
rdwrFtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrFtpStatus.setStatus("mandatory")


class _RsFullMacCompareStatus_Type(Integer32):
    """Custom type rsFullMacCompareStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enforce", 1),
          ("share", 2))
    )


_RsFullMacCompareStatus_Type.__name__ = "Integer32"
_RsFullMacCompareStatus_Object = MibScalar
rsFullMacCompareStatus = _RsFullMacCompareStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 108),
    _RsFullMacCompareStatus_Type()
)
rsFullMacCompareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFullMacCompareStatus.setStatus("mandatory")
_RsREStateMonitoring_ObjectIdentity = ObjectIdentity
rsREStateMonitoring = _RsREStateMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109)
)
_RsREACCReasonCounters_ObjectIdentity = ObjectIdentity
rsREACCReasonCounters = _RsREACCReasonCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1)
)
_RsACCReasonUnknownCounter_Type = Counter32
_RsACCReasonUnknownCounter_Object = MibScalar
rsACCReasonUnknownCounter = _RsACCReasonUnknownCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 1),
    _RsACCReasonUnknownCounter_Type()
)
rsACCReasonUnknownCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonUnknownCounter.setStatus("mandatory")
_RsACCReasonETHBroadcastCounter_Type = Counter32
_RsACCReasonETHBroadcastCounter_Object = MibScalar
rsACCReasonETHBroadcastCounter = _RsACCReasonETHBroadcastCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 2),
    _RsACCReasonETHBroadcastCounter_Type()
)
rsACCReasonETHBroadcastCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonETHBroadcastCounter.setStatus("mandatory")
_RsACCReasonProtolcolTypeCounter_Type = Counter32
_RsACCReasonProtolcolTypeCounter_Object = MibScalar
rsACCReasonProtolcolTypeCounter = _RsACCReasonProtolcolTypeCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 3),
    _RsACCReasonProtolcolTypeCounter_Type()
)
rsACCReasonProtolcolTypeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonProtolcolTypeCounter.setStatus("mandatory")
_RsACCReasonIPVERCounter_Type = Counter32
_RsACCReasonIPVERCounter_Object = MibScalar
rsACCReasonIPVERCounter = _RsACCReasonIPVERCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 4),
    _RsACCReasonIPVERCounter_Type()
)
rsACCReasonIPVERCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonIPVERCounter.setStatus("mandatory")
_RsACCReasonIPHeaderLenCounter_Type = Counter32
_RsACCReasonIPHeaderLenCounter_Object = MibScalar
rsACCReasonIPHeaderLenCounter = _RsACCReasonIPHeaderLenCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 5),
    _RsACCReasonIPHeaderLenCounter_Type()
)
rsACCReasonIPHeaderLenCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonIPHeaderLenCounter.setStatus("mandatory")
_RsACCReasonIPFragmentedCounter_Type = Counter32
_RsACCReasonIPFragmentedCounter_Object = MibScalar
rsACCReasonIPFragmentedCounter = _RsACCReasonIPFragmentedCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 6),
    _RsACCReasonIPFragmentedCounter_Type()
)
rsACCReasonIPFragmentedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonIPFragmentedCounter.setStatus("mandatory")
_RsACCReasonTTLCounter_Type = Counter32
_RsACCReasonTTLCounter_Object = MibScalar
rsACCReasonTTLCounter = _RsACCReasonTTLCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 7),
    _RsACCReasonTTLCounter_Type()
)
rsACCReasonTTLCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonTTLCounter.setStatus("mandatory")
_RsACCReasonNoFlowCounter_Type = Counter32
_RsACCReasonNoFlowCounter_Object = MibScalar
rsACCReasonNoFlowCounter = _RsACCReasonNoFlowCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 8),
    _RsACCReasonNoFlowCounter_Type()
)
rsACCReasonNoFlowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonNoFlowCounter.setStatus("mandatory")
_RsACCReasonMACCFGCounter_Type = Counter32
_RsACCReasonMACCFGCounter_Object = MibScalar
rsACCReasonMACCFGCounter = _RsACCReasonMACCFGCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 9),
    _RsACCReasonMACCFGCounter_Type()
)
rsACCReasonMACCFGCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonMACCFGCounter.setStatus("mandatory")
_RsACCReasonSYNcookieOKCounter_Type = Counter32
_RsACCReasonSYNcookieOKCounter_Object = MibScalar
rsACCReasonSYNcookieOKCounter = _RsACCReasonSYNcookieOKCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 10),
    _RsACCReasonSYNcookieOKCounter_Type()
)
rsACCReasonSYNcookieOKCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonSYNcookieOKCounter.setStatus("mandatory")
_RsACCReasonSYNcookieInvalidCounter_Type = Counter32
_RsACCReasonSYNcookieInvalidCounter_Object = MibScalar
rsACCReasonSYNcookieInvalidCounter = _RsACCReasonSYNcookieInvalidCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 11),
    _RsACCReasonSYNcookieInvalidCounter_Type()
)
rsACCReasonSYNcookieInvalidCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonSYNcookieInvalidCounter.setStatus("mandatory")
_RsACCReasonInconsistentPktLenCounter_Type = Counter32
_RsACCReasonInconsistentPktLenCounter_Object = MibScalar
rsACCReasonInconsistentPktLenCounter = _RsACCReasonInconsistentPktLenCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 12),
    _RsACCReasonInconsistentPktLenCounter_Type()
)
rsACCReasonInconsistentPktLenCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonInconsistentPktLenCounter.setStatus("mandatory")
_RsACCReasonNoReasonCounter_Type = Counter32
_RsACCReasonNoReasonCounter_Object = MibScalar
rsACCReasonNoReasonCounter = _RsACCReasonNoReasonCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 13),
    _RsACCReasonNoReasonCounter_Type()
)
rsACCReasonNoReasonCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonNoReasonCounter.setStatus("mandatory")
_RsACCReasonFTPportCounter_Type = Counter32
_RsACCReasonFTPportCounter_Object = MibScalar
rsACCReasonFTPportCounter = _RsACCReasonFTPportCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 14),
    _RsACCReasonFTPportCounter_Type()
)
rsACCReasonFTPportCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonFTPportCounter.setStatus("mandatory")
_RsACCReasonFTP227Counter_Type = Counter32
_RsACCReasonFTP227Counter_Object = MibScalar
rsACCReasonFTP227Counter = _RsACCReasonFTP227Counter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 15),
    _RsACCReasonFTP227Counter_Type()
)
rsACCReasonFTP227Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonFTP227Counter.setStatus("mandatory")
_RsACCReasonIPLenghtCounter_Type = Counter32
_RsACCReasonIPLenghtCounter_Object = MibScalar
rsACCReasonIPLenghtCounter = _RsACCReasonIPLenghtCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 16),
    _RsACCReasonIPLenghtCounter_Type()
)
rsACCReasonIPLenghtCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonIPLenghtCounter.setStatus("mandatory")
_RsACCReasonFINorRSTCounter_Type = Counter32
_RsACCReasonFINorRSTCounter_Object = MibScalar
rsACCReasonFINorRSTCounter = _RsACCReasonFINorRSTCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 17),
    _RsACCReasonFINorRSTCounter_Type()
)
rsACCReasonFINorRSTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonFINorRSTCounter.setStatus("mandatory")
_RsACCReasonClassifyCounter_Type = Counter32
_RsACCReasonClassifyCounter_Object = MibScalar
rsACCReasonClassifyCounter = _RsACCReasonClassifyCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 18),
    _RsACCReasonClassifyCounter_Type()
)
rsACCReasonClassifyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonClassifyCounter.setStatus("mandatory")
_RsACCReasonVlanReplyCounter_Type = Counter32
_RsACCReasonVlanReplyCounter_Object = MibScalar
rsACCReasonVlanReplyCounter = _RsACCReasonVlanReplyCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 19),
    _RsACCReasonVlanReplyCounter_Type()
)
rsACCReasonVlanReplyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonVlanReplyCounter.setStatus("mandatory")
_RsACCReasonDBindNewSYNCounter_Type = Counter32
_RsACCReasonDBindNewSYNCounter_Object = MibScalar
rsACCReasonDBindNewSYNCounter = _RsACCReasonDBindNewSYNCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 20),
    _RsACCReasonDBindNewSYNCounter_Type()
)
rsACCReasonDBindNewSYNCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonDBindNewSYNCounter.setStatus("mandatory")
_RsACCReasonAllToMasterCounter_Type = Counter32
_RsACCReasonAllToMasterCounter_Object = MibScalar
rsACCReasonAllToMasterCounter = _RsACCReasonAllToMasterCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 1, 21),
    _RsACCReasonAllToMasterCounter_Type()
)
rsACCReasonAllToMasterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCReasonAllToMasterCounter.setStatus("mandatory")
_RsREStateCounters_ObjectIdentity = ObjectIdentity
rsREStateCounters = _RsREStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 2)
)
_RsREStateRXReplyCounter_Type = Counter32
_RsREStateRXReplyCounter_Object = MibScalar
rsREStateRXReplyCounter = _RsREStateRXReplyCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 2, 1),
    _RsREStateRXReplyCounter_Type()
)
rsREStateRXReplyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsREStateRXReplyCounter.setStatus("mandatory")
_RsREStateRXRequestCounter_Type = Counter32
_RsREStateRXRequestCounter_Object = MibScalar
rsREStateRXRequestCounter = _RsREStateRXRequestCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 2, 2),
    _RsREStateRXRequestCounter_Type()
)
rsREStateRXRequestCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsREStateRXRequestCounter.setStatus("mandatory")
_RsREStateIPDAinFFTCounter_Type = Counter32
_RsREStateIPDAinFFTCounter_Object = MibScalar
rsREStateIPDAinFFTCounter = _RsREStateIPDAinFFTCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 2, 3),
    _RsREStateIPDAinFFTCounter_Type()
)
rsREStateIPDAinFFTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsREStateIPDAinFFTCounter.setStatus("mandatory")
_RsREStateIPDAnotFFTCounter_Type = Counter32
_RsREStateIPDAnotFFTCounter_Object = MibScalar
rsREStateIPDAnotFFTCounter = _RsREStateIPDAnotFFTCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 2, 4),
    _RsREStateIPDAnotFFTCounter_Type()
)
rsREStateIPDAnotFFTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsREStateIPDAnotFFTCounter.setStatus("mandatory")
_RsREStateBridgeCounter_Type = Counter32
_RsREStateBridgeCounter_Object = MibScalar
rsREStateBridgeCounter = _RsREStateBridgeCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 2, 5),
    _RsREStateBridgeCounter_Type()
)
rsREStateBridgeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsREStateBridgeCounter.setStatus("mandatory")


class _RsREStateResetCounter_Type(Integer32):
    """Custom type rsREStateResetCounter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RsREStateResetCounter_Type.__name__ = "Integer32"
_RsREStateResetCounter_Object = MibScalar
rsREStateResetCounter = _RsREStateResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 109, 3),
    _RsREStateResetCounter_Type()
)
rsREStateResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsREStateResetCounter.setStatus("mandatory")
_RdwrTerminalParams_ObjectIdentity = ObjectIdentity
rdwrTerminalParams = _RdwrTerminalParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110)
)
_RdwrTerminalAliasTable_Object = MibTable
rdwrTerminalAliasTable = _RdwrTerminalAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 1)
)
if mibBuilder.loadTexts:
    rdwrTerminalAliasTable.setStatus("mandatory")
_RdwrTerminalAliasEntry_Object = MibTableRow
rdwrTerminalAliasEntry = _RdwrTerminalAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 1, 1)
)
rdwrTerminalAliasEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrTerminalAliasName"),
    (0, "RADWARE-MIB", "rdwrTerminalUserName"),
)
if mibBuilder.loadTexts:
    rdwrTerminalAliasEntry.setStatus("mandatory")


class _RdwrTerminalAliasName_Type(DisplayString):
    """Custom type rdwrTerminalAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RdwrTerminalAliasName_Type.__name__ = "DisplayString"
_RdwrTerminalAliasName_Object = MibTableColumn
rdwrTerminalAliasName = _RdwrTerminalAliasName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 1, 1, 1),
    _RdwrTerminalAliasName_Type()
)
rdwrTerminalAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrTerminalAliasName.setStatus("mandatory")


class _RdwrTerminalUserName_Type(DisplayString):
    """Custom type rdwrTerminalUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RdwrTerminalUserName_Type.__name__ = "DisplayString"
_RdwrTerminalUserName_Object = MibTableColumn
rdwrTerminalUserName = _RdwrTerminalUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 1, 1, 2),
    _RdwrTerminalUserName_Type()
)
rdwrTerminalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrTerminalUserName.setStatus("mandatory")


class _RdwrTerminalAliasCommand_Type(DisplayString):
    """Custom type rdwrTerminalAliasCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RdwrTerminalAliasCommand_Type.__name__ = "DisplayString"
_RdwrTerminalAliasCommand_Object = MibTableColumn
rdwrTerminalAliasCommand = _RdwrTerminalAliasCommand_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 1, 1, 3),
    _RdwrTerminalAliasCommand_Type()
)
rdwrTerminalAliasCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrTerminalAliasCommand.setStatus("mandatory")
_RdwrTerminalAliasStatus_Type = RowStatus
_RdwrTerminalAliasStatus_Object = MibTableColumn
rdwrTerminalAliasStatus = _RdwrTerminalAliasStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 1, 1, 4),
    _RdwrTerminalAliasStatus_Type()
)
rdwrTerminalAliasStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrTerminalAliasStatus.setStatus("mandatory")


class _RdwrTerminalPrompt_Type(DisplayString):
    """Custom type rdwrTerminalPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RdwrTerminalPrompt_Type.__name__ = "DisplayString"
_RdwrTerminalPrompt_Object = MibScalar
rdwrTerminalPrompt = _RdwrTerminalPrompt_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 110, 2),
    _RdwrTerminalPrompt_Type()
)
rdwrTerminalPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrTerminalPrompt.setStatus("mandatory")
_RdwrMasterInterfaceGroupingPortsTable_Object = MibTable
rdwrMasterInterfaceGroupingPortsTable = _RdwrMasterInterfaceGroupingPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 111)
)
if mibBuilder.loadTexts:
    rdwrMasterInterfaceGroupingPortsTable.setStatus("mandatory")
_RdwrMasterInterfaceGroupingPortsEntry_Object = MibTableRow
rdwrMasterInterfaceGroupingPortsEntry = _RdwrMasterInterfaceGroupingPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 111, 1)
)
rdwrMasterInterfaceGroupingPortsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrMasterInterfaceGroupingPortNumber"),
)
if mibBuilder.loadTexts:
    rdwrMasterInterfaceGroupingPortsEntry.setStatus("mandatory")
_RdwrMasterInterfaceGroupingPortNumber_Type = Integer32
_RdwrMasterInterfaceGroupingPortNumber_Object = MibTableColumn
rdwrMasterInterfaceGroupingPortNumber = _RdwrMasterInterfaceGroupingPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 111, 1, 1),
    _RdwrMasterInterfaceGroupingPortNumber_Type()
)
rdwrMasterInterfaceGroupingPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrMasterInterfaceGroupingPortNumber.setStatus("mandatory")


class _RdwrMasterInterfaceGroupingPortState_Type(Integer32):
    """Custom type rdwrMasterInterfaceGroupingPortState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_RdwrMasterInterfaceGroupingPortState_Type.__name__ = "Integer32"
_RdwrMasterInterfaceGroupingPortState_Object = MibTableColumn
rdwrMasterInterfaceGroupingPortState = _RdwrMasterInterfaceGroupingPortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 111, 1, 2),
    _RdwrMasterInterfaceGroupingPortState_Type()
)
rdwrMasterInterfaceGroupingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMasterInterfaceGroupingPortState.setStatus("mandatory")


class _Rdwr5SecAvgResourceUtilization_Type(Integer32):
    """Custom type rdwr5SecAvgResourceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Rdwr5SecAvgResourceUtilization_Type.__name__ = "Integer32"
_Rdwr5SecAvgResourceUtilization_Object = MibScalar
rdwr5SecAvgResourceUtilization = _Rdwr5SecAvgResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 112),
    _Rdwr5SecAvgResourceUtilization_Type()
)
rdwr5SecAvgResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwr5SecAvgResourceUtilization.setStatus("mandatory")


class _Rdwr60SecAvgResourceUtilization_Type(Integer32):
    """Custom type rdwr60SecAvgResourceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Rdwr60SecAvgResourceUtilization_Type.__name__ = "Integer32"
_Rdwr60SecAvgResourceUtilization_Object = MibScalar
rdwr60SecAvgResourceUtilization = _Rdwr60SecAvgResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 113),
    _Rdwr60SecAvgResourceUtilization_Type()
)
rdwr60SecAvgResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwr60SecAvgResourceUtilization.setStatus("mandatory")


class _RdwrArpWithInterfaceGroup_Type(Integer32):
    """Custom type rdwrArpWithInterfaceGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("avoid", 2))
    )


_RdwrArpWithInterfaceGroup_Type.__name__ = "Integer32"
_RdwrArpWithInterfaceGroup_Object = MibScalar
rdwrArpWithInterfaceGroup = _RdwrArpWithInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 114),
    _RdwrArpWithInterfaceGroup_Type()
)
rdwrArpWithInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrArpWithInterfaceGroup.setStatus("mandatory")
_RdwrDBind_ObjectIdentity = ObjectIdentity
rdwrDBind = _RdwrDBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 115)
)
_RdwrDP_ObjectIdentity = ObjectIdentity
rdwrDP = _RdwrDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 116)
)
_RsDOS_ObjectIdentity = ObjectIdentity
rsDOS = _RsDOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 117)
)
_RsSTATEFUL_ObjectIdentity = ObjectIdentity
rsSTATEFUL = _RsSTATEFUL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118)
)
_RsAPM_ObjectIdentity = ObjectIdentity
rsAPM = _RsAPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 119)
)
_RdwrIpsec_ObjectIdentity = ObjectIdentity
rdwrIpsec = _RdwrIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120)
)
_RdwrIpsecIke_ObjectIdentity = ObjectIdentity
rdwrIpsecIke = _RdwrIpsecIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1)
)
_RdwrIkeTable_Object = MibTable
rdwrIkeTable = _RdwrIkeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1)
)
if mibBuilder.loadTexts:
    rdwrIkeTable.setStatus("mandatory")
_RdwrIkeEntry_Object = MibTableRow
rdwrIkeEntry = _RdwrIkeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1)
)
rdwrIkeEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrIkeName"),
)
if mibBuilder.loadTexts:
    rdwrIkeEntry.setStatus("mandatory")


class _RdwrIkeName_Type(DisplayString):
    """Custom type rdwrIkeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RdwrIkeName_Type.__name__ = "DisplayString"
_RdwrIkeName_Object = MibTableColumn
rdwrIkeName = _RdwrIkeName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 1),
    _RdwrIkeName_Type()
)
rdwrIkeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrIkeName.setStatus("mandatory")


class _RdwrIkePhase1EncryptionAlg_Type(Integer32):
    """Custom type rdwrIkePhase1EncryptionAlg based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("idea", 2),
          ("blowfish", 3),
          ("rc5", 4),
          ("des3", 5),
          ("cast", 6),
          ("aes", 7))
    )


_RdwrIkePhase1EncryptionAlg_Type.__name__ = "Integer32"
_RdwrIkePhase1EncryptionAlg_Object = MibTableColumn
rdwrIkePhase1EncryptionAlg = _RdwrIkePhase1EncryptionAlg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 2),
    _RdwrIkePhase1EncryptionAlg_Type()
)
rdwrIkePhase1EncryptionAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase1EncryptionAlg.setStatus("mandatory")


class _RdwrIkePhase1HashAlg_Type(Integer32):
    """Custom type rdwrIkePhase1HashAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_RdwrIkePhase1HashAlg_Type.__name__ = "Integer32"
_RdwrIkePhase1HashAlg_Object = MibTableColumn
rdwrIkePhase1HashAlg = _RdwrIkePhase1HashAlg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 3),
    _RdwrIkePhase1HashAlg_Type()
)
rdwrIkePhase1HashAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase1HashAlg.setStatus("mandatory")


class _RdwrIkePhase1DhKeyGroup_Type(Integer32):
    """Custom type rdwrIkePhase1DhKeyGroup based on Integer32"""
    defaultValue = 1

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
        *(("modp768", 1),
          ("modp1024", 2),
          ("ec2n155", 3),
          ("ec2n185", 4),
          ("modp1536", 5))
    )


_RdwrIkePhase1DhKeyGroup_Type.__name__ = "Integer32"
_RdwrIkePhase1DhKeyGroup_Object = MibTableColumn
rdwrIkePhase1DhKeyGroup = _RdwrIkePhase1DhKeyGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 4),
    _RdwrIkePhase1DhKeyGroup_Type()
)
rdwrIkePhase1DhKeyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase1DhKeyGroup.setStatus("mandatory")


class _RdwrIkePhase1LifeTime_Type(Integer32):
    """Custom type rdwrIkePhase1LifeTime based on Integer32"""
    defaultValue = 28800


_RdwrIkePhase1LifeTime_Type.__name__ = "Integer32"
_RdwrIkePhase1LifeTime_Object = MibTableColumn
rdwrIkePhase1LifeTime = _RdwrIkePhase1LifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 5),
    _RdwrIkePhase1LifeTime_Type()
)
rdwrIkePhase1LifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase1LifeTime.setStatus("mandatory")


class _RdwrIkePhase1Psk_Type(DisplayString):
    """Custom type rdwrIkePhase1Psk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RdwrIkePhase1Psk_Type.__name__ = "DisplayString"
_RdwrIkePhase1Psk_Object = MibTableColumn
rdwrIkePhase1Psk = _RdwrIkePhase1Psk_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 6),
    _RdwrIkePhase1Psk_Type()
)
rdwrIkePhase1Psk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase1Psk.setStatus("mandatory")


class _RdwrIkePhase2Protocol_Type(Integer32):
    """Custom type rdwrIkePhase2Protocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ah", 2),
          ("esp", 3))
    )


_RdwrIkePhase2Protocol_Type.__name__ = "Integer32"
_RdwrIkePhase2Protocol_Object = MibTableColumn
rdwrIkePhase2Protocol = _RdwrIkePhase2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 7),
    _RdwrIkePhase2Protocol_Type()
)
rdwrIkePhase2Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase2Protocol.setStatus("mandatory")


class _RdwrIkePhase2EncryptionAlg_Type(Integer32):
    """Custom type rdwrIkePhase2EncryptionAlg based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("idea", 2),
          ("blowfish", 3),
          ("rc5", 4),
          ("des3", 5),
          ("cast", 6),
          ("aes", 7))
    )


_RdwrIkePhase2EncryptionAlg_Type.__name__ = "Integer32"
_RdwrIkePhase2EncryptionAlg_Object = MibTableColumn
rdwrIkePhase2EncryptionAlg = _RdwrIkePhase2EncryptionAlg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 8),
    _RdwrIkePhase2EncryptionAlg_Type()
)
rdwrIkePhase2EncryptionAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase2EncryptionAlg.setStatus("mandatory")


class _RdwrIkePhase2HashAlg_Type(Integer32):
    """Custom type rdwrIkePhase2HashAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2),
          ("null", 3))
    )


_RdwrIkePhase2HashAlg_Type.__name__ = "Integer32"
_RdwrIkePhase2HashAlg_Object = MibTableColumn
rdwrIkePhase2HashAlg = _RdwrIkePhase2HashAlg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 9),
    _RdwrIkePhase2HashAlg_Type()
)
rdwrIkePhase2HashAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePhase2HashAlg.setStatus("mandatory")


class _RdwrIkePfsKeyGroup_Type(Integer32):
    """Custom type rdwrIkePfsKeyGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("modp768", 1),
          ("modp1024", 2),
          ("ec2n155", 3),
          ("ec2n185", 4),
          ("modp1536", 5),
          ("off", 65535))
    )


_RdwrIkePfsKeyGroup_Type.__name__ = "Integer32"
_RdwrIkePfsKeyGroup_Object = MibTableColumn
rdwrIkePfsKeyGroup = _RdwrIkePfsKeyGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 10),
    _RdwrIkePfsKeyGroup_Type()
)
rdwrIkePfsKeyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkePfsKeyGroup.setStatus("mandatory")


class _RdwrIkeSaLifeTime_Type(Integer32):
    """Custom type rdwrIkeSaLifeTime based on Integer32"""
    defaultValue = 28800


_RdwrIkeSaLifeTime_Type.__name__ = "Integer32"
_RdwrIkeSaLifeTime_Object = MibTableColumn
rdwrIkeSaLifeTime = _RdwrIkeSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 11),
    _RdwrIkeSaLifeTime_Type()
)
rdwrIkeSaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeSaLifeTime.setStatus("mandatory")


class _RdwrIkeIpCompression_Type(Integer32):
    """Custom type rdwrIkeIpCompression based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RdwrIkeIpCompression_Type.__name__ = "Integer32"
_RdwrIkeIpCompression_Object = MibTableColumn
rdwrIkeIpCompression = _RdwrIkeIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 12),
    _RdwrIkeIpCompression_Type()
)
rdwrIkeIpCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeIpCompression.setStatus("mandatory")


class _RdwrIkeManualKeyMode_Type(Integer32):
    """Custom type rdwrIkeManualKeyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2))
    )


_RdwrIkeManualKeyMode_Type.__name__ = "Integer32"
_RdwrIkeManualKeyMode_Object = MibTableColumn
rdwrIkeManualKeyMode = _RdwrIkeManualKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 13),
    _RdwrIkeManualKeyMode_Type()
)
rdwrIkeManualKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeManualKeyMode.setStatus("mandatory")


class _RdwrIkeEncrypKey_Type(DisplayString):
    """Custom type rdwrIkeEncrypKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RdwrIkeEncrypKey_Type.__name__ = "DisplayString"
_RdwrIkeEncrypKey_Object = MibTableColumn
rdwrIkeEncrypKey = _RdwrIkeEncrypKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 14),
    _RdwrIkeEncrypKey_Type()
)
rdwrIkeEncrypKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeEncrypKey.setStatus("mandatory")


class _RdwrIkeAuthntKey_Type(DisplayString):
    """Custom type rdwrIkeAuthntKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RdwrIkeAuthntKey_Type.__name__ = "DisplayString"
_RdwrIkeAuthntKey_Object = MibTableColumn
rdwrIkeAuthntKey = _RdwrIkeAuthntKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 15),
    _RdwrIkeAuthntKey_Type()
)
rdwrIkeAuthntKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeAuthntKey.setStatus("mandatory")
_RdwrIkeInSpi_Type = Integer32
_RdwrIkeInSpi_Object = MibTableColumn
rdwrIkeInSpi = _RdwrIkeInSpi_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 16),
    _RdwrIkeInSpi_Type()
)
rdwrIkeInSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeInSpi.setStatus("mandatory")
_RdwrIkeOutSpi_Type = Integer32
_RdwrIkeOutSpi_Object = MibTableColumn
rdwrIkeOutSpi = _RdwrIkeOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 17),
    _RdwrIkeOutSpi_Type()
)
rdwrIkeOutSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeOutSpi.setStatus("mandatory")
_RdwrIkeDPDCheckInterval_Type = Integer32
_RdwrIkeDPDCheckInterval_Object = MibTableColumn
rdwrIkeDPDCheckInterval = _RdwrIkeDPDCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 18),
    _RdwrIkeDPDCheckInterval_Type()
)
rdwrIkeDPDCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeDPDCheckInterval.setStatus("mandatory")
_RdwrIkeStatus_Type = RowStatus
_RdwrIkeStatus_Object = MibTableColumn
rdwrIkeStatus = _RdwrIkeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 120, 1, 1, 1, 19),
    _RdwrIkeStatus_Type()
)
rdwrIkeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrIkeStatus.setStatus("mandatory")


class _RdwrDedicatedManagementPort_Type(Integer32):
    """Custom type rdwrDedicatedManagementPort based on Integer32"""
    defaultValue = 0


_RdwrDedicatedManagementPort_Type.__name__ = "Integer32"
_RdwrDedicatedManagementPort_Object = MibScalar
rdwrDedicatedManagementPort = _RdwrDedicatedManagementPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 121),
    _RdwrDedicatedManagementPort_Type()
)
rdwrDedicatedManagementPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDedicatedManagementPort.setStatus("mandatory")
_RsGeneric_ObjectIdentity = ObjectIdentity
rsGeneric = _RsGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122)
)
_RdwrClientsTableStatistics_ObjectIdentity = ObjectIdentity
rdwrClientsTableStatistics = _RdwrClientsTableStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 123)
)
_RdwrClientsTableNumEntries_Type = Integer32
_RdwrClientsTableNumEntries_Object = MibScalar
rdwrClientsTableNumEntries = _RdwrClientsTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 123, 1),
    _RdwrClientsTableNumEntries_Type()
)
rdwrClientsTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsTableNumEntries.setStatus("mandatory")
_RdwrClientsTableNumEntries5SecAvg_Type = Integer32
_RdwrClientsTableNumEntries5SecAvg_Object = MibScalar
rdwrClientsTableNumEntries5SecAvg = _RdwrClientsTableNumEntries5SecAvg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 123, 2),
    _RdwrClientsTableNumEntries5SecAvg_Type()
)
rdwrClientsTableNumEntries5SecAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsTableNumEntries5SecAvg.setStatus("mandatory")
_RdwrClientsTableNumEntries60SecAvg_Type = Integer32
_RdwrClientsTableNumEntries60SecAvg_Object = MibScalar
rdwrClientsTableNumEntries60SecAvg = _RdwrClientsTableNumEntries60SecAvg_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 123, 3),
    _RdwrClientsTableNumEntries60SecAvg_Type()
)
rdwrClientsTableNumEntries60SecAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsTableNumEntries60SecAvg.setStatus("mandatory")


class _RsWSDSyslogDestinationPort_Type(Integer32):
    """Custom type rsWSDSyslogDestinationPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(1024, 65535),
    )


_RsWSDSyslogDestinationPort_Type.__name__ = "Integer32"
_RsWSDSyslogDestinationPort_Object = MibScalar
rsWSDSyslogDestinationPort = _RsWSDSyslogDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 124),
    _RsWSDSyslogDestinationPort_Type()
)
rsWSDSyslogDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogDestinationPort.setStatus("mandatory")
_RdwrPortsTagTable_Object = MibTable
rdwrPortsTagTable = _RdwrPortsTagTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 125)
)
if mibBuilder.loadTexts:
    rdwrPortsTagTable.setStatus("mandatory")
_RdwrPortsTagEntry_Object = MibTableRow
rdwrPortsTagEntry = _RdwrPortsTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 125, 1)
)
rdwrPortsTagEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrPortsTagPortNumber"),
)
if mibBuilder.loadTexts:
    rdwrPortsTagEntry.setStatus("mandatory")
_RdwrPortsTagPortNumber_Type = Integer32
_RdwrPortsTagPortNumber_Object = MibTableColumn
rdwrPortsTagPortNumber = _RdwrPortsTagPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 125, 1, 1),
    _RdwrPortsTagPortNumber_Type()
)
rdwrPortsTagPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrPortsTagPortNumber.setStatus("mandatory")
_RdwrPortsTagPortInTag_Type = Integer32
_RdwrPortsTagPortInTag_Object = MibTableColumn
rdwrPortsTagPortInTag = _RdwrPortsTagPortInTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 125, 1, 2),
    _RdwrPortsTagPortInTag_Type()
)
rdwrPortsTagPortInTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrPortsTagPortInTag.setStatus("mandatory")
_RdwrPortsTagPortOutTag_Type = Integer32
_RdwrPortsTagPortOutTag_Object = MibTableColumn
rdwrPortsTagPortOutTag = _RdwrPortsTagPortOutTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 125, 1, 3),
    _RdwrPortsTagPortOutTag_Type()
)
rdwrPortsTagPortOutTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrPortsTagPortOutTag.setStatus("mandatory")


class _RsPhysPortMirrorThresholdUnits_Type(Integer32):
    """Custom type rsPhysPortMirrorThresholdUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("kbps", 2))
    )


_RsPhysPortMirrorThresholdUnits_Type.__name__ = "Integer32"
_RsPhysPortMirrorThresholdUnits_Object = MibScalar
rsPhysPortMirrorThresholdUnits = _RsPhysPortMirrorThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 126),
    _RsPhysPortMirrorThresholdUnits_Type()
)
rsPhysPortMirrorThresholdUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorThresholdUnits.setStatus("mandatory")
_RsPhysPortMirrorThresholdInterval_Type = Integer32
_RsPhysPortMirrorThresholdInterval_Object = MibScalar
rsPhysPortMirrorThresholdInterval = _RsPhysPortMirrorThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 127),
    _RsPhysPortMirrorThresholdInterval_Type()
)
rsPhysPortMirrorThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorThresholdInterval.setStatus("mandatory")


class _RsPhysPortMirrorThresholdReset_Type(Integer32):
    """Custom type rsPhysPortMirrorThresholdReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("no-reset", 2))
    )


_RsPhysPortMirrorThresholdReset_Type.__name__ = "Integer32"
_RsPhysPortMirrorThresholdReset_Object = MibScalar
rsPhysPortMirrorThresholdReset = _RsPhysPortMirrorThresholdReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 128),
    _RsPhysPortMirrorThresholdReset_Type()
)
rsPhysPortMirrorThresholdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorThresholdReset.setStatus("mandatory")
_RdwrDayLightSaving_ObjectIdentity = ObjectIdentity
rdwrDayLightSaving = _RdwrDayLightSaving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129)
)


class _RdwrDayLightSavingBegins_Type(DisplayString):
    """Custom type rdwrDayLightSavingBegins based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDayLightSavingBegins_Type.__name__ = "DisplayString"
_RdwrDayLightSavingBegins_Object = MibScalar
rdwrDayLightSavingBegins = _RdwrDayLightSavingBegins_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 1),
    _RdwrDayLightSavingBegins_Type()
)
rdwrDayLightSavingBegins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDayLightSavingBegins.setStatus("mandatory")


class _RdwrDayLightSavingEnds_Type(DisplayString):
    """Custom type rdwrDayLightSavingEnds based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDayLightSavingEnds_Type.__name__ = "DisplayString"
_RdwrDayLightSavingEnds_Object = MibScalar
rdwrDayLightSavingEnds = _RdwrDayLightSavingEnds_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 2),
    _RdwrDayLightSavingEnds_Type()
)
rdwrDayLightSavingEnds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDayLightSavingEnds.setStatus("mandatory")


class _RdwrDayLightSavingTimeDesignations_Type(Integer32):
    """Custom type rdwrDayLightSavingTimeDesignations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standardTime", 1),
          ("summerTime", 2))
    )


_RdwrDayLightSavingTimeDesignations_Type.__name__ = "Integer32"
_RdwrDayLightSavingTimeDesignations_Object = MibScalar
rdwrDayLightSavingTimeDesignations = _RdwrDayLightSavingTimeDesignations_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 3),
    _RdwrDayLightSavingTimeDesignations_Type()
)
rdwrDayLightSavingTimeDesignations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDayLightSavingTimeDesignations.setStatus("mandatory")


class _RdwrDayLightSavingAdminStatus_Type(Integer32):
    """Custom type rdwrDayLightSavingAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RdwrDayLightSavingAdminStatus_Type.__name__ = "Integer32"
_RdwrDayLightSavingAdminStatus_Object = MibScalar
rdwrDayLightSavingAdminStatus = _RdwrDayLightSavingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 4),
    _RdwrDayLightSavingAdminStatus_Type()
)
rdwrDayLightSavingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDayLightSavingAdminStatus.setStatus("mandatory")


class _RdwrDayLightSavingBeginDate_Type(DisplayString):
    """Custom type rdwrDayLightSavingBeginDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDayLightSavingBeginDate_Type.__name__ = "DisplayString"
_RdwrDayLightSavingBeginDate_Object = MibScalar
rdwrDayLightSavingBeginDate = _RdwrDayLightSavingBeginDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 5),
    _RdwrDayLightSavingBeginDate_Type()
)
rdwrDayLightSavingBeginDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDayLightSavingBeginDate.setStatus("mandatory")


class _RdwrDayLightSavingEndDate_Type(DisplayString):
    """Custom type rdwrDayLightSavingEndDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RdwrDayLightSavingEndDate_Type.__name__ = "DisplayString"
_RdwrDayLightSavingEndDate_Object = MibScalar
rdwrDayLightSavingEndDate = _RdwrDayLightSavingEndDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 6),
    _RdwrDayLightSavingEndDate_Type()
)
rdwrDayLightSavingEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDayLightSavingEndDate.setStatus("mandatory")
_RdwrDayLightSavingDelta_Type = Integer32
_RdwrDayLightSavingDelta_Object = MibScalar
rdwrDayLightSavingDelta = _RdwrDayLightSavingDelta_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 129, 7),
    _RdwrDayLightSavingDelta_Type()
)
rdwrDayLightSavingDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrDayLightSavingDelta.setStatus("mandatory")
_RdwrCommonClientTable_ObjectIdentity = ObjectIdentity
rdwrCommonClientTable = _RdwrCommonClientTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130)
)
_RdwrClientsViewTable_Object = MibTable
rdwrClientsViewTable = _RdwrClientsViewTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1)
)
if mibBuilder.loadTexts:
    rdwrClientsViewTable.setStatus("mandatory")
_RdwrClientsViewEntry_Object = MibTableRow
rdwrClientsViewEntry = _RdwrClientsViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1)
)
rdwrClientsViewEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrClientsViewIndex"),
)
if mibBuilder.loadTexts:
    rdwrClientsViewEntry.setStatus("mandatory")
_RdwrClientsViewIndex_Type = Integer32
_RdwrClientsViewIndex_Object = MibTableColumn
rdwrClientsViewIndex = _RdwrClientsViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 1),
    _RdwrClientsViewIndex_Type()
)
rdwrClientsViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsViewIndex.setStatus("mandatory")
_RdwrClientsViewSrcAddrFrom_Type = IpAddress
_RdwrClientsViewSrcAddrFrom_Object = MibTableColumn
rdwrClientsViewSrcAddrFrom = _RdwrClientsViewSrcAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 2),
    _RdwrClientsViewSrcAddrFrom_Type()
)
rdwrClientsViewSrcAddrFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewSrcAddrFrom.setStatus("mandatory")
_RdwrClientsViewSrcAddrTo_Type = IpAddress
_RdwrClientsViewSrcAddrTo_Object = MibTableColumn
rdwrClientsViewSrcAddrTo = _RdwrClientsViewSrcAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 3),
    _RdwrClientsViewSrcAddrTo_Type()
)
rdwrClientsViewSrcAddrTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewSrcAddrTo.setStatus("mandatory")
_RdwrClientsViewDstAddrFrom_Type = IpAddress
_RdwrClientsViewDstAddrFrom_Object = MibTableColumn
rdwrClientsViewDstAddrFrom = _RdwrClientsViewDstAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 4),
    _RdwrClientsViewDstAddrFrom_Type()
)
rdwrClientsViewDstAddrFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewDstAddrFrom.setStatus("mandatory")
_RdwrClientsViewDstAddrTo_Type = IpAddress
_RdwrClientsViewDstAddrTo_Object = MibTableColumn
rdwrClientsViewDstAddrTo = _RdwrClientsViewDstAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 5),
    _RdwrClientsViewDstAddrTo_Type()
)
rdwrClientsViewDstAddrTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewDstAddrTo.setStatus("mandatory")


class _RdwrClientsViewSrcPortFrom_Type(Integer32):
    """Custom type rdwrClientsViewSrcPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdwrClientsViewSrcPortFrom_Type.__name__ = "Integer32"
_RdwrClientsViewSrcPortFrom_Object = MibTableColumn
rdwrClientsViewSrcPortFrom = _RdwrClientsViewSrcPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 6),
    _RdwrClientsViewSrcPortFrom_Type()
)
rdwrClientsViewSrcPortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewSrcPortFrom.setStatus("mandatory")


class _RdwrClientsViewSrcPortTo_Type(Integer32):
    """Custom type rdwrClientsViewSrcPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdwrClientsViewSrcPortTo_Type.__name__ = "Integer32"
_RdwrClientsViewSrcPortTo_Object = MibTableColumn
rdwrClientsViewSrcPortTo = _RdwrClientsViewSrcPortTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 7),
    _RdwrClientsViewSrcPortTo_Type()
)
rdwrClientsViewSrcPortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewSrcPortTo.setStatus("mandatory")


class _RdwrClientsViewDstPortFrom_Type(Integer32):
    """Custom type rdwrClientsViewDstPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdwrClientsViewDstPortFrom_Type.__name__ = "Integer32"
_RdwrClientsViewDstPortFrom_Object = MibTableColumn
rdwrClientsViewDstPortFrom = _RdwrClientsViewDstPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 8),
    _RdwrClientsViewDstPortFrom_Type()
)
rdwrClientsViewDstPortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewDstPortFrom.setStatus("mandatory")


class _RdwrClientsViewDstPortTo_Type(Integer32):
    """Custom type rdwrClientsViewDstPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdwrClientsViewDstPortTo_Type.__name__ = "Integer32"
_RdwrClientsViewDstPortTo_Object = MibTableColumn
rdwrClientsViewDstPortTo = _RdwrClientsViewDstPortTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 9),
    _RdwrClientsViewDstPortTo_Type()
)
rdwrClientsViewDstPortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewDstPortTo.setStatus("mandatory")
_RdwrClientsViewFarmAddr_Type = IpAddress
_RdwrClientsViewFarmAddr_Object = MibTableColumn
rdwrClientsViewFarmAddr = _RdwrClientsViewFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 10),
    _RdwrClientsViewFarmAddr_Type()
)
rdwrClientsViewFarmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewFarmAddr.setStatus("mandatory")
_RdwrClientsViewServerAddr_Type = IpAddress
_RdwrClientsViewServerAddr_Object = MibTableColumn
rdwrClientsViewServerAddr = _RdwrClientsViewServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 11),
    _RdwrClientsViewServerAddr_Type()
)
rdwrClientsViewServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewServerAddr.setStatus("mandatory")


class _RdwrClientsViewClientType_Type(DisplayString):
    """Custom type rdwrClientsViewClientType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RdwrClientsViewClientType_Type.__name__ = "DisplayString"
_RdwrClientsViewClientType_Object = MibTableColumn
rdwrClientsViewClientType = _RdwrClientsViewClientType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 12),
    _RdwrClientsViewClientType_Type()
)
rdwrClientsViewClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewClientType.setStatus("mandatory")


class _RdwrClientsViewAdminStatus_Type(Integer32):
    """Custom type rdwrClientsViewAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RdwrClientsViewAdminStatus_Type.__name__ = "Integer32"
_RdwrClientsViewAdminStatus_Object = MibTableColumn
rdwrClientsViewAdminStatus = _RdwrClientsViewAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 13),
    _RdwrClientsViewAdminStatus_Type()
)
rdwrClientsViewAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewAdminStatus.setStatus("mandatory")
_RdwrClientsViewStatus_Type = RowStatus
_RdwrClientsViewStatus_Object = MibTableColumn
rdwrClientsViewStatus = _RdwrClientsViewStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 14),
    _RdwrClientsViewStatus_Type()
)
rdwrClientsViewStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewStatus.setStatus("mandatory")


class _RdwrClientsViewAction_Type(Integer32):
    """Custom type rdwrClientsViewAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("deleteMatching", 2),
          ("countMatching", 3))
    )


_RdwrClientsViewAction_Type.__name__ = "Integer32"
_RdwrClientsViewAction_Object = MibTableColumn
rdwrClientsViewAction = _RdwrClientsViewAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 15),
    _RdwrClientsViewAction_Type()
)
rdwrClientsViewAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewAction.setStatus("mandatory")


class _RdwrClientsViewActionFeedback_Type(DisplayString):
    """Custom type rdwrClientsViewActionFeedback based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_RdwrClientsViewActionFeedback_Type.__name__ = "DisplayString"
_RdwrClientsViewActionFeedback_Object = MibTableColumn
rdwrClientsViewActionFeedback = _RdwrClientsViewActionFeedback_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 16),
    _RdwrClientsViewActionFeedback_Type()
)
rdwrClientsViewActionFeedback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsViewActionFeedback.setStatus("mandatory")


class _RdwrClientsViewVlanTag_Type(Integer32):
    """Custom type rdwrClientsViewVlanTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RdwrClientsViewVlanTag_Type.__name__ = "Integer32"
_RdwrClientsViewVlanTag_Object = MibTableColumn
rdwrClientsViewVlanTag = _RdwrClientsViewVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 17),
    _RdwrClientsViewVlanTag_Type()
)
rdwrClientsViewVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewVlanTag.setStatus("mandatory")


class _RdwrClientsViewFarmName_Type(DisplayString):
    """Custom type rdwrClientsViewFarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RdwrClientsViewFarmName_Type.__name__ = "DisplayString"
_RdwrClientsViewFarmName_Object = MibTableColumn
rdwrClientsViewFarmName = _RdwrClientsViewFarmName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 1, 1, 18),
    _RdwrClientsViewFarmName_Type()
)
rdwrClientsViewFarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsViewFarmName.setStatus("mandatory")
_RdwrClientsTable_Object = MibTable
rdwrClientsTable = _RdwrClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2)
)
if mibBuilder.loadTexts:
    rdwrClientsTable.setStatus("mandatory")
_RdwrClientsEntry_Object = MibTableRow
rdwrClientsEntry = _RdwrClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1)
)
rdwrClientsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrClientsIndex"),
)
if mibBuilder.loadTexts:
    rdwrClientsEntry.setStatus("mandatory")
_RdwrClientsIndex_Type = Integer32
_RdwrClientsIndex_Object = MibTableColumn
rdwrClientsIndex = _RdwrClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 1),
    _RdwrClientsIndex_Type()
)
rdwrClientsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsIndex.setStatus("mandatory")
_RdwrClientsSourceAddr_Type = IpAddress
_RdwrClientsSourceAddr_Object = MibTableColumn
rdwrClientsSourceAddr = _RdwrClientsSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 2),
    _RdwrClientsSourceAddr_Type()
)
rdwrClientsSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsSourceAddr.setStatus("mandatory")
_RdwrClientsSourcePort_Type = Integer32
_RdwrClientsSourcePort_Object = MibTableColumn
rdwrClientsSourcePort = _RdwrClientsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 3),
    _RdwrClientsSourcePort_Type()
)
rdwrClientsSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsSourcePort.setStatus("mandatory")
_RdwrClientsRequestedAddr_Type = IpAddress
_RdwrClientsRequestedAddr_Object = MibTableColumn
rdwrClientsRequestedAddr = _RdwrClientsRequestedAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 4),
    _RdwrClientsRequestedAddr_Type()
)
rdwrClientsRequestedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsRequestedAddr.setStatus("mandatory")
_RdwrClientsRequestedPort_Type = Integer32
_RdwrClientsRequestedPort_Object = MibTableColumn
rdwrClientsRequestedPort = _RdwrClientsRequestedPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 5),
    _RdwrClientsRequestedPort_Type()
)
rdwrClientsRequestedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsRequestedPort.setStatus("mandatory")
_RdwrClientsFarmAddr_Type = IpAddress
_RdwrClientsFarmAddr_Object = MibTableColumn
rdwrClientsFarmAddr = _RdwrClientsFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 6),
    _RdwrClientsFarmAddr_Type()
)
rdwrClientsFarmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsFarmAddr.setStatus("mandatory")
_RdwrClientsServerAddr_Type = IpAddress
_RdwrClientsServerAddr_Object = MibTableColumn
rdwrClientsServerAddr = _RdwrClientsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 7),
    _RdwrClientsServerAddr_Type()
)
rdwrClientsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsServerAddr.setStatus("mandatory")
_RdwrClientsServerPort_Type = Integer32
_RdwrClientsServerPort_Object = MibTableColumn
rdwrClientsServerPort = _RdwrClientsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 8),
    _RdwrClientsServerPort_Type()
)
rdwrClientsServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsServerPort.setStatus("mandatory")
_RdwrClientsAttachedTime_Type = Integer32
_RdwrClientsAttachedTime_Object = MibTableColumn
rdwrClientsAttachedTime = _RdwrClientsAttachedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 9),
    _RdwrClientsAttachedTime_Type()
)
rdwrClientsAttachedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsAttachedTime.setStatus("mandatory")
_RdwrClientsNATaddr_Type = IpAddress
_RdwrClientsNATaddr_Object = MibTableColumn
rdwrClientsNATaddr = _RdwrClientsNATaddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 10),
    _RdwrClientsNATaddr_Type()
)
rdwrClientsNATaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsNATaddr.setStatus("mandatory")
_RdwrClientsNATPort_Type = Integer32
_RdwrClientsNATPort_Object = MibTableColumn
rdwrClientsNATPort = _RdwrClientsNATPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 11),
    _RdwrClientsNATPort_Type()
)
rdwrClientsNATPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsNATPort.setStatus("mandatory")
_RdwrClientsTimeToLive_Type = Integer32
_RdwrClientsTimeToLive_Object = MibTableColumn
rdwrClientsTimeToLive = _RdwrClientsTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 12),
    _RdwrClientsTimeToLive_Type()
)
rdwrClientsTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsTimeToLive.setStatus("mandatory")


class _RdwrClientsClientType_Type(DisplayString):
    """Custom type rdwrClientsClientType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RdwrClientsClientType_Type.__name__ = "DisplayString"
_RdwrClientsClientType_Object = MibTableColumn
rdwrClientsClientType = _RdwrClientsClientType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 13),
    _RdwrClientsClientType_Type()
)
rdwrClientsClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsClientType.setStatus("mandatory")


class _RdwrClientsClientMode_Type(DisplayString):
    """Custom type rdwrClientsClientMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RdwrClientsClientMode_Type.__name__ = "DisplayString"
_RdwrClientsClientMode_Object = MibTableColumn
rdwrClientsClientMode = _RdwrClientsClientMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 14),
    _RdwrClientsClientMode_Type()
)
rdwrClientsClientMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsClientMode.setStatus("mandatory")


class _RdwrClientsUserData1_Type(DisplayString):
    """Custom type rdwrClientsUserData1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_RdwrClientsUserData1_Type.__name__ = "DisplayString"
_RdwrClientsUserData1_Object = MibTableColumn
rdwrClientsUserData1 = _RdwrClientsUserData1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 15),
    _RdwrClientsUserData1_Type()
)
rdwrClientsUserData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsUserData1.setStatus("mandatory")


class _RdwrClientsUserData2_Type(DisplayString):
    """Custom type rdwrClientsUserData2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_RdwrClientsUserData2_Type.__name__ = "DisplayString"
_RdwrClientsUserData2_Object = MibTableColumn
rdwrClientsUserData2 = _RdwrClientsUserData2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 16),
    _RdwrClientsUserData2_Type()
)
rdwrClientsUserData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsUserData2.setStatus("mandatory")
_RdwrClientsStatus_Type = RowStatus
_RdwrClientsStatus_Object = MibTableColumn
rdwrClientsStatus = _RdwrClientsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 2, 1, 17),
    _RdwrClientsStatus_Type()
)
rdwrClientsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrClientsStatus.setStatus("mandatory")
_RdwrClientsTypeTable_Object = MibTable
rdwrClientsTypeTable = _RdwrClientsTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 3)
)
if mibBuilder.loadTexts:
    rdwrClientsTypeTable.setStatus("mandatory")
_RdwrClientsTypeEntry_Object = MibTableRow
rdwrClientsTypeEntry = _RdwrClientsTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 3, 1)
)
rdwrClientsTypeEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrClientsType"),
)
if mibBuilder.loadTexts:
    rdwrClientsTypeEntry.setStatus("mandatory")


class _RdwrClientsType_Type(DisplayString):
    """Custom type rdwrClientsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RdwrClientsType_Type.__name__ = "DisplayString"
_RdwrClientsType_Object = MibTableColumn
rdwrClientsType = _RdwrClientsType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 130, 3, 1, 1),
    _RdwrClientsType_Type()
)
rdwrClientsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrClientsType.setStatus("mandatory")
_RdwrVersionIdentifierTable_Object = MibTable
rdwrVersionIdentifierTable = _RdwrVersionIdentifierTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 131)
)
if mibBuilder.loadTexts:
    rdwrVersionIdentifierTable.setStatus("mandatory")
_RdwrVersionIdentifierEntry_Object = MibTableRow
rdwrVersionIdentifierEntry = _RdwrVersionIdentifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 131, 1)
)
rdwrVersionIdentifierEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrVersionIdentifierIdx"),
)
if mibBuilder.loadTexts:
    rdwrVersionIdentifierEntry.setStatus("mandatory")
_RdwrVersionIdentifierIdx_Type = Integer32
_RdwrVersionIdentifierIdx_Object = MibTableColumn
rdwrVersionIdentifierIdx = _RdwrVersionIdentifierIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 131, 1, 1),
    _RdwrVersionIdentifierIdx_Type()
)
rdwrVersionIdentifierIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrVersionIdentifierIdx.setStatus("mandatory")
_RdwrVersionIdentifierBase_Type = Integer32
_RdwrVersionIdentifierBase_Object = MibTableColumn
rdwrVersionIdentifierBase = _RdwrVersionIdentifierBase_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 131, 1, 2),
    _RdwrVersionIdentifierBase_Type()
)
rdwrVersionIdentifierBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrVersionIdentifierBase.setStatus("mandatory")


class _RdwrVersionIdentifierVal_Type(DisplayString):
    """Custom type rdwrVersionIdentifierVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RdwrVersionIdentifierVal_Type.__name__ = "DisplayString"
_RdwrVersionIdentifierVal_Object = MibTableColumn
rdwrVersionIdentifierVal = _RdwrVersionIdentifierVal_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 131, 1, 3),
    _RdwrVersionIdentifierVal_Type()
)
rdwrVersionIdentifierVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrVersionIdentifierVal.setStatus("mandatory")
_RdwrVrrp_ObjectIdentity = ObjectIdentity
rdwrVrrp = _RdwrVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132)
)


class _RdwrVrrpAdmin_Type(Integer32):
    """Custom type rdwrVrrpAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allDown", 1),
          ("allUp", 2),
          ("noChange", 3))
    )


_RdwrVrrpAdmin_Type.__name__ = "Integer32"
_RdwrVrrpAdmin_Object = MibScalar
rdwrVrrpAdmin = _RdwrVrrpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 1),
    _RdwrVrrpAdmin_Type()
)
rdwrVrrpAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrVrrpAdmin.setStatus("mandatory")


class _RdwrVrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type rdwrVrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 0


_RdwrVrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_RdwrVrrpOperAdvertisementInterval_Object = MibScalar
rdwrVrrpOperAdvertisementInterval = _RdwrVrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 2),
    _RdwrVrrpOperAdvertisementInterval_Type()
)
rdwrVrrpOperAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrVrrpOperAdvertisementInterval.setStatus("mandatory")
_RdwrVrrpAssoIpV6AddrTable_Object = MibTable
rdwrVrrpAssoIpV6AddrTable = _RdwrVrrpAssoIpV6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 3)
)
if mibBuilder.loadTexts:
    rdwrVrrpAssoIpV6AddrTable.setStatus("mandatory")
_RdwrVrrpAssoIpV6AddrEntry_Object = MibTableRow
rdwrVrrpAssoIpV6AddrEntry = _RdwrVrrpAssoIpV6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 3, 1)
)
rdwrVrrpAssoIpV6AddrEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrVrrpAssoIpV6IfIndex"),
    (0, "RADWARE-MIB", "rdwrVrrpAssoIpV6VrId"),
    (0, "RADWARE-MIB", "rdwrVrrpAssoIpV6Addr"),
)
if mibBuilder.loadTexts:
    rdwrVrrpAssoIpV6AddrEntry.setStatus("mandatory")
_RdwrVrrpAssoIpV6IfIndex_Type = Integer32
_RdwrVrrpAssoIpV6IfIndex_Object = MibTableColumn
rdwrVrrpAssoIpV6IfIndex = _RdwrVrrpAssoIpV6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 3, 1, 1),
    _RdwrVrrpAssoIpV6IfIndex_Type()
)
rdwrVrrpAssoIpV6IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrVrrpAssoIpV6IfIndex.setStatus("mandatory")
_RdwrVrrpAssoIpV6VrId_Type = VrId
_RdwrVrrpAssoIpV6VrId_Object = MibTableColumn
rdwrVrrpAssoIpV6VrId = _RdwrVrrpAssoIpV6VrId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 3, 1, 2),
    _RdwrVrrpAssoIpV6VrId_Type()
)
rdwrVrrpAssoIpV6VrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrVrrpAssoIpV6VrId.setStatus("mandatory")
_RdwrVrrpAssoIpV6Addr_Type = Ipv6Address
_RdwrVrrpAssoIpV6Addr_Object = MibTableColumn
rdwrVrrpAssoIpV6Addr = _RdwrVrrpAssoIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 3, 1, 3),
    _RdwrVrrpAssoIpV6Addr_Type()
)
rdwrVrrpAssoIpV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrVrrpAssoIpV6Addr.setStatus("mandatory")
_RdwrVrrpAssoIpV6AddrRowStatus_Type = RowStatus
_RdwrVrrpAssoIpV6AddrRowStatus_Object = MibTableColumn
rdwrVrrpAssoIpV6AddrRowStatus = _RdwrVrrpAssoIpV6AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 3, 1, 4),
    _RdwrVrrpAssoIpV6AddrRowStatus_Type()
)
rdwrVrrpAssoIpV6AddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrVrrpAssoIpV6AddrRowStatus.setStatus("mandatory")


class _RdwrVrrpPriorityTracking_Type(Integer32):
    """Custom type rdwrVrrpPriorityTracking based on Integer32"""
    defaultValue = 0


_RdwrVrrpPriorityTracking_Type.__name__ = "Integer32"
_RdwrVrrpPriorityTracking_Object = MibScalar
rdwrVrrpPriorityTracking = _RdwrVrrpPriorityTracking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 132, 4),
    _RdwrVrrpPriorityTracking_Type()
)
rdwrVrrpPriorityTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrVrrpPriorityTracking.setStatus("mandatory")
_RdwrWSDCommon_ObjectIdentity = ObjectIdentity
rdwrWSDCommon = _RdwrWSDCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 134)
)
_RdwrCdbParameters_ObjectIdentity = ObjectIdentity
rdwrCdbParameters = _RdwrCdbParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 139)
)
_RdwrCdbTimeStamp_Type = Integer32
_RdwrCdbTimeStamp_Object = MibScalar
rdwrCdbTimeStamp = _RdwrCdbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 139, 1),
    _RdwrCdbTimeStamp_Type()
)
rdwrCdbTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrCdbTimeStamp.setStatus("mandatory")
_RdwrMirroring_ObjectIdentity = ObjectIdentity
rdwrMirroring = _RdwrMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140)
)
_RdwrMirroringActiveThreshold_Type = Integer32
_RdwrMirroringActiveThreshold_Object = MibScalar
rdwrMirroringActiveThreshold = _RdwrMirroringActiveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140, 1),
    _RdwrMirroringActiveThreshold_Type()
)
rdwrMirroringActiveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMirroringActiveThreshold.setStatus("mandatory")
_RdwrMirroringActiveSleep_Type = Integer32
_RdwrMirroringActiveSleep_Object = MibScalar
rdwrMirroringActiveSleep = _RdwrMirroringActiveSleep_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140, 2),
    _RdwrMirroringActiveSleep_Type()
)
rdwrMirroringActiveSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMirroringActiveSleep.setStatus("mandatory")
_RdwrMirroringActiveBackupThreshold_Type = Integer32
_RdwrMirroringActiveBackupThreshold_Object = MibScalar
rdwrMirroringActiveBackupThreshold = _RdwrMirroringActiveBackupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140, 3),
    _RdwrMirroringActiveBackupThreshold_Type()
)
rdwrMirroringActiveBackupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMirroringActiveBackupThreshold.setStatus("mandatory")
_RdwrMirroringActiveBackupSleep_Type = Integer32
_RdwrMirroringActiveBackupSleep_Object = MibScalar
rdwrMirroringActiveBackupSleep = _RdwrMirroringActiveBackupSleep_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140, 4),
    _RdwrMirroringActiveBackupSleep_Type()
)
rdwrMirroringActiveBackupSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMirroringActiveBackupSleep.setStatus("mandatory")
_RdwrMirroringActiveBackupHoldtime_Type = Integer32
_RdwrMirroringActiveBackupHoldtime_Object = MibScalar
rdwrMirroringActiveBackupHoldtime = _RdwrMirroringActiveBackupHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140, 5),
    _RdwrMirroringActiveBackupHoldtime_Type()
)
rdwrMirroringActiveBackupHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMirroringActiveBackupHoldtime.setStatus("mandatory")


class _RdwrMirroringActiveBackupUpdate_Type(Integer32):
    """Custom type rdwrMirroringActiveBackupUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RdwrMirroringActiveBackupUpdate_Type.__name__ = "Integer32"
_RdwrMirroringActiveBackupUpdate_Object = MibScalar
rdwrMirroringActiveBackupUpdate = _RdwrMirroringActiveBackupUpdate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 140, 6),
    _RdwrMirroringActiveBackupUpdate_Type()
)
rdwrMirroringActiveBackupUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrMirroringActiveBackupUpdate.setStatus("mandatory")


class _RsWSDThroughputLicense_Type(DisplayString):
    """Custom type rsWSDThroughputLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDThroughputLicense_Type.__name__ = "DisplayString"
_RsWSDThroughputLicense_Object = MibScalar
rsWSDThroughputLicense = _RsWSDThroughputLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 141),
    _RsWSDThroughputLicense_Type()
)
rsWSDThroughputLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDThroughputLicense.setStatus("mandatory")


class _RsWSDThroughputLicenseID_Type(DisplayString):
    """Custom type rsWSDThroughputLicenseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDThroughputLicenseID_Type.__name__ = "DisplayString"
_RsWSDThroughputLicenseID_Object = MibScalar
rsWSDThroughputLicenseID = _RsWSDThroughputLicenseID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 142),
    _RsWSDThroughputLicenseID_Type()
)
rsWSDThroughputLicenseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDThroughputLicenseID.setStatus("mandatory")
_RsSSLCertificate_ObjectIdentity = ObjectIdentity
rsSSLCertificate = _RsSSLCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148)
)
_RsSSLCertificateDefaultValues_ObjectIdentity = ObjectIdentity
rsSSLCertificateDefaultValues = _RsSSLCertificateDefaultValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1)
)


class _RsSSLCertificateDefaultCommon_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultCommon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RsSSLCertificateDefaultCommon_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultCommon_Object = MibScalar
rsSSLCertificateDefaultCommon = _RsSSLCertificateDefaultCommon_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 1),
    _RsSSLCertificateDefaultCommon_Type()
)
rsSSLCertificateDefaultCommon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultCommon.setStatus("mandatory")


class _RsSSLCertificateDefaultLocality_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultLocality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSSLCertificateDefaultLocality_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultLocality_Object = MibScalar
rsSSLCertificateDefaultLocality = _RsSSLCertificateDefaultLocality_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 2),
    _RsSSLCertificateDefaultLocality_Type()
)
rsSSLCertificateDefaultLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultLocality.setStatus("mandatory")


class _RsSSLCertificateDefaultStateOrProvince_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultStateOrProvince based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSSLCertificateDefaultStateOrProvince_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultStateOrProvince_Object = MibScalar
rsSSLCertificateDefaultStateOrProvince = _RsSSLCertificateDefaultStateOrProvince_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 3),
    _RsSSLCertificateDefaultStateOrProvince_Type()
)
rsSSLCertificateDefaultStateOrProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultStateOrProvince.setStatus("mandatory")


class _RsSSLCertificateDefaultOrganization_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateDefaultOrganization_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultOrganization_Object = MibScalar
rsSSLCertificateDefaultOrganization = _RsSSLCertificateDefaultOrganization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 4),
    _RsSSLCertificateDefaultOrganization_Type()
)
rsSSLCertificateDefaultOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultOrganization.setStatus("mandatory")


class _RsSSLCertificateDefaultOrganizationUnit_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultOrganizationUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateDefaultOrganizationUnit_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultOrganizationUnit_Object = MibScalar
rsSSLCertificateDefaultOrganizationUnit = _RsSSLCertificateDefaultOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 5),
    _RsSSLCertificateDefaultOrganizationUnit_Type()
)
rsSSLCertificateDefaultOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultOrganizationUnit.setStatus("mandatory")


class _RsSSLCertificateDefaultCountryName_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_RsSSLCertificateDefaultCountryName_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultCountryName_Object = MibScalar
rsSSLCertificateDefaultCountryName = _RsSSLCertificateDefaultCountryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 6),
    _RsSSLCertificateDefaultCountryName_Type()
)
rsSSLCertificateDefaultCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultCountryName.setStatus("mandatory")


class _RsSSLCertificateDefaultEMail_Type(DisplayString):
    """Custom type rsSSLCertificateDefaultEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSSLCertificateDefaultEMail_Type.__name__ = "DisplayString"
_RsSSLCertificateDefaultEMail_Object = MibScalar
rsSSLCertificateDefaultEMail = _RsSSLCertificateDefaultEMail_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 1, 7),
    _RsSSLCertificateDefaultEMail_Type()
)
rsSSLCertificateDefaultEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateDefaultEMail.setStatus("mandatory")
_RsSSLCertificateTable_Object = MibTable
rsSSLCertificateTable = _RsSSLCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2)
)
if mibBuilder.loadTexts:
    rsSSLCertificateTable.setStatus("mandatory")
_RsSSLCertificateEntry_Object = MibTableRow
rsSSLCertificateEntry = _RsSSLCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1)
)
rsSSLCertificateEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsSSLCertificateName"),
)
if mibBuilder.loadTexts:
    rsSSLCertificateEntry.setStatus("mandatory")


class _RsSSLCertificateName_Type(DisplayString):
    """Custom type rsSSLCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_RsSSLCertificateName_Type.__name__ = "DisplayString"
_RsSSLCertificateName_Object = MibTableColumn
rsSSLCertificateName = _RsSSLCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 1),
    _RsSSLCertificateName_Type()
)
rsSSLCertificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSSLCertificateName.setStatus("mandatory")


class _RsSSLCertificateEntryType_Type(Integer32):
    """Custom type rsSSLCertificateEntryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("key", 1),
          ("certificateSigningRequest", 2),
          ("certificate", 3),
          ("certificateChain", 4),
          ("clientCAcertificate", 5),
          ("rootTSLcertificate", 6),
          ("sshPublicKey", 7))
    )


_RsSSLCertificateEntryType_Type.__name__ = "Integer32"
_RsSSLCertificateEntryType_Object = MibTableColumn
rsSSLCertificateEntryType = _RsSSLCertificateEntryType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 2),
    _RsSSLCertificateEntryType_Type()
)
rsSSLCertificateEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateEntryType.setStatus("mandatory")


class _RsSSLCertificateKeySize_Type(Integer32):
    """Custom type rsSSLCertificateKeySize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("size512", 512),
          ("size1024", 1024),
          ("size2048", 2048))
    )


_RsSSLCertificateKeySize_Type.__name__ = "Integer32"
_RsSSLCertificateKeySize_Object = MibTableColumn
rsSSLCertificateKeySize = _RsSSLCertificateKeySize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 3),
    _RsSSLCertificateKeySize_Type()
)
rsSSLCertificateKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateKeySize.setStatus("mandatory")


class _RsSSLCertificateKeyPassphrase_Type(DisplayString):
    """Custom type rsSSLCertificateKeyPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateKeyPassphrase_Type.__name__ = "DisplayString"
_RsSSLCertificateKeyPassphrase_Object = MibTableColumn
rsSSLCertificateKeyPassphrase = _RsSSLCertificateKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 4),
    _RsSSLCertificateKeyPassphrase_Type()
)
rsSSLCertificateKeyPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateKeyPassphrase.setStatus("mandatory")


class _RsSSLCertificateCommon_Type(DisplayString):
    """Custom type rsSSLCertificateCommon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateCommon_Type.__name__ = "DisplayString"
_RsSSLCertificateCommon_Object = MibTableColumn
rsSSLCertificateCommon = _RsSSLCertificateCommon_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 5),
    _RsSSLCertificateCommon_Type()
)
rsSSLCertificateCommon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateCommon.setStatus("mandatory")


class _RsSSLCertificateLocality_Type(DisplayString):
    """Custom type rsSSLCertificateLocality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSSLCertificateLocality_Type.__name__ = "DisplayString"
_RsSSLCertificateLocality_Object = MibTableColumn
rsSSLCertificateLocality = _RsSSLCertificateLocality_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 6),
    _RsSSLCertificateLocality_Type()
)
rsSSLCertificateLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateLocality.setStatus("mandatory")


class _RsSSLCertificateStateOrProvince_Type(DisplayString):
    """Custom type rsSSLCertificateStateOrProvince based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSSLCertificateStateOrProvince_Type.__name__ = "DisplayString"
_RsSSLCertificateStateOrProvince_Object = MibTableColumn
rsSSLCertificateStateOrProvince = _RsSSLCertificateStateOrProvince_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 7),
    _RsSSLCertificateStateOrProvince_Type()
)
rsSSLCertificateStateOrProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateStateOrProvince.setStatus("mandatory")


class _RsSSLCertificateOrganization_Type(DisplayString):
    """Custom type rsSSLCertificateOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateOrganization_Type.__name__ = "DisplayString"
_RsSSLCertificateOrganization_Object = MibTableColumn
rsSSLCertificateOrganization = _RsSSLCertificateOrganization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 8),
    _RsSSLCertificateOrganization_Type()
)
rsSSLCertificateOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateOrganization.setStatus("mandatory")


class _RsSSLCertificateOrganizationUnit_Type(DisplayString):
    """Custom type rsSSLCertificateOrganizationUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateOrganizationUnit_Type.__name__ = "DisplayString"
_RsSSLCertificateOrganizationUnit_Object = MibTableColumn
rsSSLCertificateOrganizationUnit = _RsSSLCertificateOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 9),
    _RsSSLCertificateOrganizationUnit_Type()
)
rsSSLCertificateOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateOrganizationUnit.setStatus("mandatory")


class _RsSSLCertificateCountryName_Type(DisplayString):
    """Custom type rsSSLCertificateCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_RsSSLCertificateCountryName_Type.__name__ = "DisplayString"
_RsSSLCertificateCountryName_Object = MibTableColumn
rsSSLCertificateCountryName = _RsSSLCertificateCountryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 10),
    _RsSSLCertificateCountryName_Type()
)
rsSSLCertificateCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateCountryName.setStatus("mandatory")


class _RsSSLCertificateEMail_Type(DisplayString):
    """Custom type rsSSLCertificateEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSSLCertificateEMail_Type.__name__ = "DisplayString"
_RsSSLCertificateEMail_Object = MibTableColumn
rsSSLCertificateEMail = _RsSSLCertificateEMail_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 11),
    _RsSSLCertificateEMail_Type()
)
rsSSLCertificateEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateEMail.setStatus("mandatory")
_RsSSLCertificateExpiry_Type = DisplayString
_RsSSLCertificateExpiry_Object = MibTableColumn
rsSSLCertificateExpiry = _RsSSLCertificateExpiry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 12),
    _RsSSLCertificateExpiry_Type()
)
rsSSLCertificateExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSSLCertificateExpiry.setStatus("mandatory")
_RsSSLCertificateOCSPUrl_Type = DisplayString
_RsSSLCertificateOCSPUrl_Object = MibTableColumn
rsSSLCertificateOCSPUrl = _RsSSLCertificateOCSPUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 13),
    _RsSSLCertificateOCSPUrl_Type()
)
rsSSLCertificateOCSPUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateOCSPUrl.setStatus("mandatory")
_RsSSLCertificateStatus_Type = RowStatus
_RsSSLCertificateStatus_Object = MibTableColumn
rsSSLCertificateStatus = _RsSSLCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 14),
    _RsSSLCertificateStatus_Type()
)
rsSSLCertificateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateStatus.setStatus("mandatory")
_RsSSLCertificateRequestedValidityPeriod_Type = Integer32
_RsSSLCertificateRequestedValidityPeriod_Object = MibTableColumn
rsSSLCertificateRequestedValidityPeriod = _RsSSLCertificateRequestedValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 2, 1, 15),
    _RsSSLCertificateRequestedValidityPeriod_Type()
)
rsSSLCertificateRequestedValidityPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateRequestedValidityPeriod.setStatus("mandatory")
_RsSSLCertificateImportExport_ObjectIdentity = ObjectIdentity
rsSSLCertificateImportExport = _RsSSLCertificateImportExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 3)
)


class _RsSSLCertificateImportExportEntryName_Type(DisplayString):
    """Custom type rsSSLCertificateImportExportEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RsSSLCertificateImportExportEntryName_Type.__name__ = "DisplayString"
_RsSSLCertificateImportExportEntryName_Object = MibScalar
rsSSLCertificateImportExportEntryName = _RsSSLCertificateImportExportEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 3, 1),
    _RsSSLCertificateImportExportEntryName_Type()
)
rsSSLCertificateImportExportEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateImportExportEntryName.setStatus("mandatory")
_RsSSLCertificateImportExportFileName_Type = DisplayString
_RsSSLCertificateImportExportFileName_Object = MibScalar
rsSSLCertificateImportExportFileName = _RsSSLCertificateImportExportFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 3, 2),
    _RsSSLCertificateImportExportFileName_Type()
)
rsSSLCertificateImportExportFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateImportExportFileName.setStatus("mandatory")


class _RsSSLCertificateImportExportPassphrase_Type(DisplayString):
    """Custom type rsSSLCertificateImportExportPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsSSLCertificateImportExportPassphrase_Type.__name__ = "DisplayString"
_RsSSLCertificateImportExportPassphrase_Object = MibScalar
rsSSLCertificateImportExportPassphrase = _RsSSLCertificateImportExportPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 3, 3),
    _RsSSLCertificateImportExportPassphrase_Type()
)
rsSSLCertificateImportExportPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateImportExportPassphrase.setStatus("mandatory")


class _RsSSLCertificateImportExportAction_Type(Integer32):
    """Custom type rsSSLCertificateImportExportAction based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("importKey", 1),
          ("exportKey", 2),
          ("importCertificate", 3),
          ("exportCertificate", 4),
          ("exportSigningRequest", 5),
          ("importCertChain", 6),
          ("exportCertChain", 7),
          ("importCertClientCA", 8),
          ("exportCertClientCA", 9))
    )


_RsSSLCertificateImportExportAction_Type.__name__ = "Integer32"
_RsSSLCertificateImportExportAction_Object = MibScalar
rsSSLCertificateImportExportAction = _RsSSLCertificateImportExportAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 148, 3, 4),
    _RsSSLCertificateImportExportAction_Type()
)
rsSSLCertificateImportExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSLCertificateImportExportAction.setStatus("mandatory")
_RdwrTemperatureCPU1Get_Type = Integer32
_RdwrTemperatureCPU1Get_Object = MibScalar
rdwrTemperatureCPU1Get = _RdwrTemperatureCPU1Get_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 150),
    _RdwrTemperatureCPU1Get_Type()
)
rdwrTemperatureCPU1Get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTemperatureCPU1Get.setStatus("mandatory")
_RdwrTemperatureCPU2Get_Type = Integer32
_RdwrTemperatureCPU2Get_Object = MibScalar
rdwrTemperatureCPU2Get = _RdwrTemperatureCPU2Get_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 151),
    _RdwrTemperatureCPU2Get_Type()
)
rdwrTemperatureCPU2Get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTemperatureCPU2Get.setStatus("mandatory")
_RdwrTemperatureWarningThresholdGet_Type = Integer32
_RdwrTemperatureWarningThresholdGet_Object = MibScalar
rdwrTemperatureWarningThresholdGet = _RdwrTemperatureWarningThresholdGet_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 152),
    _RdwrTemperatureWarningThresholdGet_Type()
)
rdwrTemperatureWarningThresholdGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTemperatureWarningThresholdGet.setStatus("mandatory")
_RdwrTemperatureShutdownThresholdGet_Type = Integer32
_RdwrTemperatureShutdownThresholdGet_Object = MibScalar
rdwrTemperatureShutdownThresholdGet = _RdwrTemperatureShutdownThresholdGet_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 153),
    _RdwrTemperatureShutdownThresholdGet_Type()
)
rdwrTemperatureShutdownThresholdGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTemperatureShutdownThresholdGet.setStatus("mandatory")


class _RdwrTemperatureThresholdStatusCPU1Get_Type(Integer32):
    """Custom type rdwrTemperatureThresholdStatusCPU1Get based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_RdwrTemperatureThresholdStatusCPU1Get_Type.__name__ = "Integer32"
_RdwrTemperatureThresholdStatusCPU1Get_Object = MibScalar
rdwrTemperatureThresholdStatusCPU1Get = _RdwrTemperatureThresholdStatusCPU1Get_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 154),
    _RdwrTemperatureThresholdStatusCPU1Get_Type()
)
rdwrTemperatureThresholdStatusCPU1Get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTemperatureThresholdStatusCPU1Get.setStatus("mandatory")


class _RdwrTemperatureThresholdStatusCPU2Get_Type(Integer32):
    """Custom type rdwrTemperatureThresholdStatusCPU2Get based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_RdwrTemperatureThresholdStatusCPU2Get_Type.__name__ = "Integer32"
_RdwrTemperatureThresholdStatusCPU2Get_Object = MibScalar
rdwrTemperatureThresholdStatusCPU2Get = _RdwrTemperatureThresholdStatusCPU2Get_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 155),
    _RdwrTemperatureThresholdStatusCPU2Get_Type()
)
rdwrTemperatureThresholdStatusCPU2Get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTemperatureThresholdStatusCPU2Get.setStatus("mandatory")
_RndNumberOfHD_Type = Integer32
_RndNumberOfHD_Object = MibScalar
rndNumberOfHD = _RndNumberOfHD_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 156),
    _RndNumberOfHD_Type()
)
rndNumberOfHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndNumberOfHD.setStatus("mandatory")


class _RndSSLCardName_Type(DisplayString):
    """Custom type rndSSLCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RndSSLCardName_Type.__name__ = "DisplayString"
_RndSSLCardName_Object = MibScalar
rndSSLCardName = _RndSSLCardName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 157),
    _RndSSLCardName_Type()
)
rndSSLCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndSSLCardName.setStatus("mandatory")


class _RndCompCardName_Type(DisplayString):
    """Custom type rndCompCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RndCompCardName_Type.__name__ = "DisplayString"
_RndCompCardName_Object = MibScalar
rndCompCardName = _RndCompCardName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 158),
    _RndCompCardName_Type()
)
rndCompCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndCompCardName.setStatus("mandatory")
_RdwrHardDisk_ObjectIdentity = ObjectIdentity
rdwrHardDisk = _RdwrHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 159)
)
_RdwrHardDiskLogging_ObjectIdentity = ObjectIdentity
rdwrHardDiskLogging = _RdwrHardDiskLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 160)
)
_RdwrConfigurationSync_ObjectIdentity = ObjectIdentity
rdwrConfigurationSync = _RdwrConfigurationSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161)
)
_RsSystemFansTable_Object = MibTable
rsSystemFansTable = _RsSystemFansTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 162)
)
if mibBuilder.loadTexts:
    rsSystemFansTable.setStatus("mandatory")
_RsSystemFansEntry_Object = MibTableRow
rsSystemFansEntry = _RsSystemFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 162, 1)
)
rsSystemFansEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsSystemFanIndex"),
)
if mibBuilder.loadTexts:
    rsSystemFansEntry.setStatus("mandatory")
_RsSystemFanIndex_Type = Integer32
_RsSystemFanIndex_Object = MibTableColumn
rsSystemFanIndex = _RsSystemFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 162, 1, 1),
    _RsSystemFanIndex_Type()
)
rsSystemFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemFanIndex.setStatus("mandatory")
_RsSystemFansStatus_Type = DisplayString
_RsSystemFansStatus_Object = MibTableColumn
rsSystemFansStatus = _RsSystemFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 162, 1, 2),
    _RsSystemFansStatus_Type()
)
rsSystemFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemFansStatus.setStatus("mandatory")


class _RdwrDualPsuStatus_Type(Integer32):
    """Custom type rdwrDualPsuStatus based on Integer32"""
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
        *(("singlePwrSupplyOk", 0),
          ("firstPwrSupplyFailed", 1),
          ("secondPwrSupplyFailed", 2),
          ("doublePwrSupplyOk", 3),
          ("unknownPwrSupplyFailed", 4))
    )


_RdwrDualPsuStatus_Type.__name__ = "Integer32"
_RdwrDualPsuStatus_Object = MibScalar
rdwrDualPsuStatus = _RdwrDualPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 163),
    _RdwrDualPsuStatus_Type()
)
rdwrDualPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrDualPsuStatus.setStatus("mandatory")
_RsNetPortUtilizationTable_Object = MibTable
rsNetPortUtilizationTable = _RsNetPortUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 164)
)
if mibBuilder.loadTexts:
    rsNetPortUtilizationTable.setStatus("mandatory")
_RsNetPortUtilizationEntry_Object = MibTableRow
rsNetPortUtilizationEntry = _RsNetPortUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 164, 1)
)
rsNetPortUtilizationEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsNetPortUtilizationIndex"),
)
if mibBuilder.loadTexts:
    rsNetPortUtilizationEntry.setStatus("mandatory")
_RsNetPortUtilizationIndex_Type = Integer32
_RsNetPortUtilizationIndex_Object = MibTableColumn
rsNetPortUtilizationIndex = _RsNetPortUtilizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 164, 1, 1),
    _RsNetPortUtilizationIndex_Type()
)
rsNetPortUtilizationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNetPortUtilizationIndex.setStatus("mandatory")
_RsNetPortUtilizationEntryInUtil_Type = Integer32
_RsNetPortUtilizationEntryInUtil_Object = MibTableColumn
rsNetPortUtilizationEntryInUtil = _RsNetPortUtilizationEntryInUtil_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 164, 1, 2),
    _RsNetPortUtilizationEntryInUtil_Type()
)
rsNetPortUtilizationEntryInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNetPortUtilizationEntryInUtil.setStatus("mandatory")
_RsNetPortUtilizationEntryOutUtil_Type = Integer32
_RsNetPortUtilizationEntryOutUtil_Object = MibTableColumn
rsNetPortUtilizationEntryOutUtil = _RsNetPortUtilizationEntryOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 164, 1, 3),
    _RsNetPortUtilizationEntryOutUtil_Type()
)
rsNetPortUtilizationEntryOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNetPortUtilizationEntryOutUtil.setStatus("mandatory")
_RsHWCPUTemperatureTable_Object = MibTable
rsHWCPUTemperatureTable = _RsHWCPUTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 165)
)
if mibBuilder.loadTexts:
    rsHWCPUTemperatureTable.setStatus("mandatory")
_RsHWCPUTemperatureEntry_Object = MibTableRow
rsHWCPUTemperatureEntry = _RsHWCPUTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 165, 1)
)
rsHWCPUTemperatureEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsHWCPUTemperatureIndex"),
)
if mibBuilder.loadTexts:
    rsHWCPUTemperatureEntry.setStatus("mandatory")
_RsHWCPUTemperatureIndex_Type = Integer32
_RsHWCPUTemperatureIndex_Object = MibTableColumn
rsHWCPUTemperatureIndex = _RsHWCPUTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 165, 1, 1),
    _RsHWCPUTemperatureIndex_Type()
)
rsHWCPUTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHWCPUTemperatureIndex.setStatus("mandatory")
_RsHWCPUTemperatureValue_Type = Integer32
_RsHWCPUTemperatureValue_Object = MibTableColumn
rsHWCPUTemperatureValue = _RsHWCPUTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 165, 1, 2),
    _RsHWCPUTemperatureValue_Type()
)
rsHWCPUTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHWCPUTemperatureValue.setStatus("mandatory")
_RdwrTotalIncomingTrafficPeak_Type = Integer32
_RdwrTotalIncomingTrafficPeak_Object = MibScalar
rdwrTotalIncomingTrafficPeak = _RdwrTotalIncomingTrafficPeak_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 166),
    _RdwrTotalIncomingTrafficPeak_Type()
)
rdwrTotalIncomingTrafficPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrTotalIncomingTrafficPeak.setStatus("mandatory")
_RsHWCoreUtilizationTable_Object = MibTable
rsHWCoreUtilizationTable = _RsHWCoreUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 167)
)
if mibBuilder.loadTexts:
    rsHWCoreUtilizationTable.setStatus("mandatory")
_RsHWCoreUtilizationEntry_Object = MibTableRow
rsHWCoreUtilizationEntry = _RsHWCoreUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 167, 1)
)
rsHWCoreUtilizationEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsHWCoreUtilizationIndex"),
)
if mibBuilder.loadTexts:
    rsHWCoreUtilizationEntry.setStatus("mandatory")
_RsHWCoreUtilizationIndex_Type = Integer32
_RsHWCoreUtilizationIndex_Object = MibTableColumn
rsHWCoreUtilizationIndex = _RsHWCoreUtilizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 167, 1, 1),
    _RsHWCoreUtilizationIndex_Type()
)
rsHWCoreUtilizationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHWCoreUtilizationIndex.setStatus("mandatory")
_RsHWCoreUtilizationValue_Type = Integer32
_RsHWCoreUtilizationValue_Object = MibTableColumn
rsHWCoreUtilizationValue = _RsHWCoreUtilizationValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 167, 1, 2),
    _RsHWCoreUtilizationValue_Type()
)
rsHWCoreUtilizationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHWCoreUtilizationValue.setStatus("mandatory")
_RsManagePro_ObjectIdentity = ObjectIdentity
rsManagePro = _RsManagePro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 170)
)


class _RsUserLockoutInterval_Type(Integer32):
    """Custom type rsUserLockoutInterval based on Integer32"""
    defaultValue = 10


_RsUserLockoutInterval_Type.__name__ = "Integer32"
_RsUserLockoutInterval_Object = MibScalar
rsUserLockoutInterval = _RsUserLockoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 171),
    _RsUserLockoutInterval_Type()
)
rsUserLockoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsUserLockoutInterval.setStatus("mandatory")


class _RdwrManagmentPortsStatus_Type(FeatureStatus):
    """Custom type rdwrManagmentPortsStatus based on FeatureStatus"""
    defaultValue = 2


_RdwrManagmentPortsStatus_Type.__name__ = "FeatureStatus"
_RdwrManagmentPortsStatus_Object = MibScalar
rdwrManagmentPortsStatus = _RdwrManagmentPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 172),
    _RdwrManagmentPortsStatus_Type()
)
rdwrManagmentPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrManagmentPortsStatus.setStatus("mandatory")
_RdwrSyslogServerTable_Object = MibTable
rdwrSyslogServerTable = _RdwrSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173)
)
if mibBuilder.loadTexts:
    rdwrSyslogServerTable.setStatus("mandatory")
_RdwrSyslogServerEntry_Object = MibTableRow
rdwrSyslogServerEntry = _RdwrSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1)
)
rdwrSyslogServerEntry.setIndexNames(
    (0, "RADWARE-MIB", "rdwrSyslogServerAddress"),
)
if mibBuilder.loadTexts:
    rdwrSyslogServerEntry.setStatus("mandatory")
_RdwrSyslogServerAddress_Type = DisplayString
_RdwrSyslogServerAddress_Object = MibTableColumn
rdwrSyslogServerAddress = _RdwrSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 1),
    _RdwrSyslogServerAddress_Type()
)
rdwrSyslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerAddress.setStatus("mandatory")


class _RdwrSyslogServerStatus_Type(FeatureStatus):
    """Custom type rdwrSyslogServerStatus based on FeatureStatus"""
    defaultValue = 1


_RdwrSyslogServerStatus_Type.__name__ = "FeatureStatus"
_RdwrSyslogServerStatus_Object = MibTableColumn
rdwrSyslogServerStatus = _RdwrSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 2),
    _RdwrSyslogServerStatus_Type()
)
rdwrSyslogServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerStatus.setStatus("mandatory")


class _RdwrSyslogServerSrcPort_Type(Integer32):
    """Custom type rdwrSyslogServerSrcPort based on Integer32"""
    defaultValue = 514


_RdwrSyslogServerSrcPort_Type.__name__ = "Integer32"
_RdwrSyslogServerSrcPort_Object = MibTableColumn
rdwrSyslogServerSrcPort = _RdwrSyslogServerSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 3),
    _RdwrSyslogServerSrcPort_Type()
)
rdwrSyslogServerSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerSrcPort.setStatus("mandatory")


class _RdwrSyslogServerDstPort_Type(Integer32):
    """Custom type rdwrSyslogServerDstPort based on Integer32"""
    defaultValue = 514


_RdwrSyslogServerDstPort_Type.__name__ = "Integer32"
_RdwrSyslogServerDstPort_Object = MibTableColumn
rdwrSyslogServerDstPort = _RdwrSyslogServerDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 4),
    _RdwrSyslogServerDstPort_Type()
)
rdwrSyslogServerDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerDstPort.setStatus("mandatory")


class _RdwrSyslogServerFacility_Type(Integer32):
    """Custom type rdwrSyslogServerFacility based on Integer32"""
    defaultValue = 22

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
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernelMsg", 0),
          ("userLevelMsg", 1),
          ("mailSystem", 2),
          ("systemDaemons", 3),
          ("authorization", 4),
          ("syslogdMessages", 5),
          ("linePrinter", 6),
          ("networkNews", 7),
          ("uucp", 8),
          ("clockDaemon1", 9),
          ("security", 10),
          ("ftpDaemon", 11),
          ("ntpSubsystem", 12),
          ("logAudit", 13),
          ("logAlert", 14),
          ("clockDaemon2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )


_RdwrSyslogServerFacility_Type.__name__ = "Integer32"
_RdwrSyslogServerFacility_Object = MibTableColumn
rdwrSyslogServerFacility = _RdwrSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 5),
    _RdwrSyslogServerFacility_Type()
)
rdwrSyslogServerFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerFacility.setStatus("mandatory")


class _RdwrSyslogServerProtocol_Type(Integer32):
    """Custom type rdwrSyslogServerProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("udpProtocol", 1),
          ("tcpProtocol", 2),
          ("tlsProtocol", 3))
    )


_RdwrSyslogServerProtocol_Type.__name__ = "Integer32"
_RdwrSyslogServerProtocol_Object = MibTableColumn
rdwrSyslogServerProtocol = _RdwrSyslogServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 6),
    _RdwrSyslogServerProtocol_Type()
)
rdwrSyslogServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerProtocol.setStatus("mandatory")
_RdwrSyslogCACertificate_Type = DisplayString
_RdwrSyslogCACertificate_Object = MibTableColumn
rdwrSyslogCACertificate = _RdwrSyslogCACertificate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 7),
    _RdwrSyslogCACertificate_Type()
)
rdwrSyslogCACertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogCACertificate.setStatus("mandatory")
_RdwrSyslogServerRowStatus_Type = RowStatus
_RdwrSyslogServerRowStatus_Object = MibTableColumn
rdwrSyslogServerRowStatus = _RdwrSyslogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 8),
    _RdwrSyslogServerRowStatus_Type()
)
rdwrSyslogServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerRowStatus.setStatus("mandatory")


class _RdwrSyslogServerConnectionStatus_Type(Integer32):
    """Custom type rdwrSyslogServerConnectionStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nr", 1),
          ("reachable", 2),
          ("unreachable", 3))
    )


_RdwrSyslogServerConnectionStatus_Type.__name__ = "Integer32"
_RdwrSyslogServerConnectionStatus_Object = MibTableColumn
rdwrSyslogServerConnectionStatus = _RdwrSyslogServerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 9),
    _RdwrSyslogServerConnectionStatus_Type()
)
rdwrSyslogServerConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerConnectionStatus.setStatus("mandatory")


class _RdwrSyslogServerNumberOfLogsInBackLog_Type(Integer32):
    """Custom type rdwrSyslogServerNumberOfLogsInBackLog based on Integer32"""
    defaultValue = 0


_RdwrSyslogServerNumberOfLogsInBackLog_Type.__name__ = "Integer32"
_RdwrSyslogServerNumberOfLogsInBackLog_Object = MibTableColumn
rdwrSyslogServerNumberOfLogsInBackLog = _RdwrSyslogServerNumberOfLogsInBackLog_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 10),
    _RdwrSyslogServerNumberOfLogsInBackLog_Type()
)
rdwrSyslogServerNumberOfLogsInBackLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogServerNumberOfLogsInBackLog.setStatus("mandatory")


class _RdwrSyslogSecuritySending_Type(FeatureStatus):
    """Custom type rdwrSyslogSecuritySending based on FeatureStatus"""
    defaultValue = 1


_RdwrSyslogSecuritySending_Type.__name__ = "FeatureStatus"
_RdwrSyslogSecuritySending_Object = MibTableColumn
rdwrSyslogSecuritySending = _RdwrSyslogSecuritySending_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 11),
    _RdwrSyslogSecuritySending_Type()
)
rdwrSyslogSecuritySending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogSecuritySending.setStatus("mandatory")


class _RdwrSyslogHealthSending_Type(FeatureStatus):
    """Custom type rdwrSyslogHealthSending based on FeatureStatus"""
    defaultValue = 1


_RdwrSyslogHealthSending_Type.__name__ = "FeatureStatus"
_RdwrSyslogHealthSending_Object = MibTableColumn
rdwrSyslogHealthSending = _RdwrSyslogHealthSending_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 12),
    _RdwrSyslogHealthSending_Type()
)
rdwrSyslogHealthSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogHealthSending.setStatus("mandatory")


class _RdwrSyslogUserAuditSending_Type(FeatureStatus):
    """Custom type rdwrSyslogUserAuditSending based on FeatureStatus"""
    defaultValue = 1


_RdwrSyslogUserAuditSending_Type.__name__ = "FeatureStatus"
_RdwrSyslogUserAuditSending_Object = MibTableColumn
rdwrSyslogUserAuditSending = _RdwrSyslogUserAuditSending_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 173, 1, 13),
    _RdwrSyslogUserAuditSending_Type()
)
rdwrSyslogUserAuditSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrSyslogUserAuditSending.setStatus("mandatory")


class _RsWSDSyslogGlobalStatus_Type(Integer32):
    """Custom type rsWSDSyslogGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsWSDSyslogGlobalStatus_Type.__name__ = "Integer32"
_RsWSDSyslogGlobalStatus_Object = MibScalar
rsWSDSyslogGlobalStatus = _RsWSDSyslogGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 174),
    _RsWSDSyslogGlobalStatus_Type()
)
rsWSDSyslogGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogGlobalStatus.setStatus("mandatory")


class _RsSendPortUnreachableStatus_Type(Integer32):
    """Custom type rsSendPortUnreachableStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsSendPortUnreachableStatus_Type.__name__ = "Integer32"
_RsSendPortUnreachableStatus_Object = MibScalar
rsSendPortUnreachableStatus = _RsSendPortUnreachableStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 175),
    _RsSendPortUnreachableStatus_Type()
)
rsSendPortUnreachableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSendPortUnreachableStatus.setStatus("mandatory")
_RsTacacsServer_ObjectIdentity = ObjectIdentity
rsTacacsServer = _RsTacacsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180)
)
_RsTacacsPrimaryServerAddr_Type = IpAddress
_RsTacacsPrimaryServerAddr_Object = MibScalar
rsTacacsPrimaryServerAddr = _RsTacacsPrimaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 1),
    _RsTacacsPrimaryServerAddr_Type()
)
rsTacacsPrimaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsPrimaryServerAddr.setStatus("mandatory")


class _RsTacacsPrimaryServerSecret_Type(DisplayString):
    """Custom type rsTacacsPrimaryServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RsTacacsPrimaryServerSecret_Type.__name__ = "DisplayString"
_RsTacacsPrimaryServerSecret_Object = MibScalar
rsTacacsPrimaryServerSecret = _RsTacacsPrimaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 2),
    _RsTacacsPrimaryServerSecret_Type()
)
rsTacacsPrimaryServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsPrimaryServerSecret.setStatus("mandatory")


class _RsTacacsPrimaryServerPort_Type(Integer32):
    """Custom type rsTacacsPrimaryServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_RsTacacsPrimaryServerPort_Type.__name__ = "Integer32"
_RsTacacsPrimaryServerPort_Object = MibScalar
rsTacacsPrimaryServerPort = _RsTacacsPrimaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 3),
    _RsTacacsPrimaryServerPort_Type()
)
rsTacacsPrimaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsPrimaryServerPort.setStatus("mandatory")
_RsTacacsSecondaryServerAddr_Type = IpAddress
_RsTacacsSecondaryServerAddr_Object = MibScalar
rsTacacsSecondaryServerAddr = _RsTacacsSecondaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 4),
    _RsTacacsSecondaryServerAddr_Type()
)
rsTacacsSecondaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsSecondaryServerAddr.setStatus("mandatory")


class _RsTacacsSecondaryServerSecret_Type(DisplayString):
    """Custom type rsTacacsSecondaryServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RsTacacsSecondaryServerSecret_Type.__name__ = "DisplayString"
_RsTacacsSecondaryServerSecret_Object = MibScalar
rsTacacsSecondaryServerSecret = _RsTacacsSecondaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 5),
    _RsTacacsSecondaryServerSecret_Type()
)
rsTacacsSecondaryServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsSecondaryServerSecret.setStatus("mandatory")


class _RsTacacsSecondaryServerPort_Type(Integer32):
    """Custom type rsTacacsSecondaryServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_RsTacacsSecondaryServerPort_Type.__name__ = "Integer32"
_RsTacacsSecondaryServerPort_Object = MibScalar
rsTacacsSecondaryServerPort = _RsTacacsSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 6),
    _RsTacacsSecondaryServerPort_Type()
)
rsTacacsSecondaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsSecondaryServerPort.setStatus("mandatory")


class _RsTacacsServerRetries_Type(Integer32):
    """Custom type rsTacacsServerRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsTacacsServerRetries_Type.__name__ = "Integer32"
_RsTacacsServerRetries_Object = MibScalar
rsTacacsServerRetries = _RsTacacsServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 7),
    _RsTacacsServerRetries_Type()
)
rsTacacsServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsServerRetries.setStatus("mandatory")


class _RsTacacsServerTimeout_Type(Integer32):
    """Custom type rsTacacsServerTimeout based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RsTacacsServerTimeout_Type.__name__ = "Integer32"
_RsTacacsServerTimeout_Object = MibScalar
rsTacacsServerTimeout = _RsTacacsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 8),
    _RsTacacsServerTimeout_Type()
)
rsTacacsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsServerTimeout.setStatus("mandatory")


class _RsTacacsCommandLoggingStatus_Type(FeatureStatus):
    """Custom type rsTacacsCommandLoggingStatus based on FeatureStatus"""
    defaultValue = 2


_RsTacacsCommandLoggingStatus_Type.__name__ = "FeatureStatus"
_RsTacacsCommandLoggingStatus_Object = MibScalar
rsTacacsCommandLoggingStatus = _RsTacacsCommandLoggingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 9),
    _RsTacacsCommandLoggingStatus_Type()
)
rsTacacsCommandLoggingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsCommandLoggingStatus.setStatus("mandatory")


class _RsTacacsCommandAuthorizationStatus_Type(FeatureStatus):
    """Custom type rsTacacsCommandAuthorizationStatus based on FeatureStatus"""
    defaultValue = 2


_RsTacacsCommandAuthorizationStatus_Type.__name__ = "FeatureStatus"
_RsTacacsCommandAuthorizationStatus_Object = MibScalar
rsTacacsCommandAuthorizationStatus = _RsTacacsCommandAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 10),
    _RsTacacsCommandAuthorizationStatus_Type()
)
rsTacacsCommandAuthorizationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsCommandAuthorizationStatus.setStatus("mandatory")


class _RsTacacsClientAging_Type(Integer32):
    """Custom type rsTacacsClientAging based on Integer32"""
    defaultValue = 0


_RsTacacsClientAging_Type.__name__ = "Integer32"
_RsTacacsClientAging_Object = MibScalar
rsTacacsClientAging = _RsTacacsClientAging_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 180, 11),
    _RsTacacsClientAging_Type()
)
rsTacacsClientAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTacacsClientAging.setStatus("mandatory")


class _RsWSDResourceUtilizationInstance1_Type(Integer32):
    """Custom type rsWSDResourceUtilizationInstance1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDResourceUtilizationInstance1_Type.__name__ = "Integer32"
_RsWSDResourceUtilizationInstance1_Object = MibScalar
rsWSDResourceUtilizationInstance1 = _RsWSDResourceUtilizationInstance1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 181),
    _RsWSDResourceUtilizationInstance1_Type()
)
rsWSDResourceUtilizationInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDResourceUtilizationInstance1.setStatus("mandatory")


class _RsWSDREResourceUtilizationInstance1_Type(Integer32):
    """Custom type rsWSDREResourceUtilizationInstance1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDREResourceUtilizationInstance1_Type.__name__ = "Integer32"
_RsWSDREResourceUtilizationInstance1_Object = MibScalar
rsWSDREResourceUtilizationInstance1 = _RsWSDREResourceUtilizationInstance1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 182),
    _RsWSDREResourceUtilizationInstance1_Type()
)
rsWSDREResourceUtilizationInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDREResourceUtilizationInstance1.setStatus("mandatory")


class _RsWSDRSResourceUtilizationInstance1_Type(Integer32):
    """Custom type rsWSDRSResourceUtilizationInstance1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDRSResourceUtilizationInstance1_Type.__name__ = "Integer32"
_RsWSDRSResourceUtilizationInstance1_Object = MibScalar
rsWSDRSResourceUtilizationInstance1 = _RsWSDRSResourceUtilizationInstance1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 183),
    _RsWSDRSResourceUtilizationInstance1_Type()
)
rsWSDRSResourceUtilizationInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDRSResourceUtilizationInstance1.setStatus("mandatory")


class _Rdwr5SecAvgResourceUtilizationInstance1_Type(Integer32):
    """Custom type rdwr5SecAvgResourceUtilizationInstance1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Rdwr5SecAvgResourceUtilizationInstance1_Type.__name__ = "Integer32"
_Rdwr5SecAvgResourceUtilizationInstance1_Object = MibScalar
rdwr5SecAvgResourceUtilizationInstance1 = _Rdwr5SecAvgResourceUtilizationInstance1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 184),
    _Rdwr5SecAvgResourceUtilizationInstance1_Type()
)
rdwr5SecAvgResourceUtilizationInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwr5SecAvgResourceUtilizationInstance1.setStatus("mandatory")


class _Rdwr60SecAvgResourceUtilizationInstance1_Type(Integer32):
    """Custom type rdwr60SecAvgResourceUtilizationInstance1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Rdwr60SecAvgResourceUtilizationInstance1_Type.__name__ = "Integer32"
_Rdwr60SecAvgResourceUtilizationInstance1_Object = MibScalar
rdwr60SecAvgResourceUtilizationInstance1 = _Rdwr60SecAvgResourceUtilizationInstance1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 185),
    _Rdwr60SecAvgResourceUtilizationInstance1_Type()
)
rdwr60SecAvgResourceUtilizationInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwr60SecAvgResourceUtilizationInstance1.setStatus("mandatory")
_RndMidLevelManagement_ObjectIdentity = ObjectIdentity
rndMidLevelManagement = _RndMidLevelManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 2)
)
_RndAlarmOptions_ObjectIdentity = ObjectIdentity
rndAlarmOptions = _RndAlarmOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 2)
)


class _RndAlarmEnabling_Type(Integer32):
    """Custom type rndAlarmEnabling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RndAlarmEnabling_Type.__name__ = "Integer32"
_RndAlarmEnabling_Object = MibScalar
rndAlarmEnabling = _RndAlarmEnabling_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 2, 1),
    _RndAlarmEnabling_Type()
)
rndAlarmEnabling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmEnabling.setStatus("mandatory")
_RndAlarmInterval_Type = Integer32
_RndAlarmInterval_Object = MibScalar
rndAlarmInterval = _RndAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 2, 2),
    _RndAlarmInterval_Type()
)
rndAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmInterval.setStatus("mandatory")
_RndMonitoredElementsTable_Object = MibTable
rndMonitoredElementsTable = _RndMonitoredElementsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3)
)
if mibBuilder.loadTexts:
    rndMonitoredElementsTable.setStatus("mandatory")
_RndMonitoredElementEntry_Object = MibTableRow
rndMonitoredElementEntry = _RndMonitoredElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1)
)
rndMonitoredElementEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndMonitoredElementAddress"),
)
if mibBuilder.loadTexts:
    rndMonitoredElementEntry.setStatus("mandatory")
_RndMonitoredElementAddress_Type = IpAddress
_RndMonitoredElementAddress_Object = MibTableColumn
rndMonitoredElementAddress = _RndMonitoredElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 1),
    _RndMonitoredElementAddress_Type()
)
rndMonitoredElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredElementAddress.setStatus("mandatory")


class _RndMonitoredElementCommunity_Type(DisplayString):
    """Custom type rndMonitoredElementCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElementCommunity_Type.__name__ = "DisplayString"
_RndMonitoredElementCommunity_Object = MibTableColumn
rndMonitoredElementCommunity = _RndMonitoredElementCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 2),
    _RndMonitoredElementCommunity_Type()
)
rndMonitoredElementCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementCommunity.setStatus("mandatory")


class _RndMonitoredElementLabel_Type(DisplayString):
    """Custom type rndMonitoredElementLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElementLabel_Type.__name__ = "DisplayString"
_RndMonitoredElementLabel_Object = MibTableColumn
rndMonitoredElementLabel = _RndMonitoredElementLabel_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 3),
    _RndMonitoredElementLabel_Type()
)
rndMonitoredElementLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementLabel.setStatus("mandatory")
_RndDefaultPollingInterval_Type = Integer32
_RndDefaultPollingInterval_Object = MibTableColumn
rndDefaultPollingInterval = _RndDefaultPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 4),
    _RndDefaultPollingInterval_Type()
)
rndDefaultPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDefaultPollingInterval.setStatus("mandatory")
_RndDefaultLogFile_Type = DisplayString
_RndDefaultLogFile_Object = MibTableColumn
rndDefaultLogFile = _RndDefaultLogFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 5),
    _RndDefaultLogFile_Type()
)
rndDefaultLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDefaultLogFile.setStatus("mandatory")
_RndMonitoredElementStatus_Type = RowStatus
_RndMonitoredElementStatus_Object = MibTableColumn
rndMonitoredElementStatus = _RndMonitoredElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 6),
    _RndMonitoredElementStatus_Type()
)
rndMonitoredElementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementStatus.setStatus("mandatory")
_RndMonitoringTable_Object = MibTable
rndMonitoringTable = _RndMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4)
)
if mibBuilder.loadTexts:
    rndMonitoringTable.setStatus("mandatory")
_RndMonitoringEntry_Object = MibTableRow
rndMonitoringEntry = _RndMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1)
)
rndMonitoringEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndMonitoredElement"),
    (0, "RADWARE-MIB", "rndMonitoredObjectInstanceLabel"),
)
if mibBuilder.loadTexts:
    rndMonitoringEntry.setStatus("mandatory")


class _RndMonitoredElement_Type(DisplayString):
    """Custom type rndMonitoredElement based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElement_Type.__name__ = "DisplayString"
_RndMonitoredElement_Object = MibTableColumn
rndMonitoredElement = _RndMonitoredElement_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 1),
    _RndMonitoredElement_Type()
)
rndMonitoredElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredElement.setStatus("mandatory")


class _RndMonitoredObjectInstanceLabel_Type(DisplayString):
    """Custom type rndMonitoredObjectInstanceLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredObjectInstanceLabel_Type.__name__ = "DisplayString"
_RndMonitoredObjectInstanceLabel_Object = MibTableColumn
rndMonitoredObjectInstanceLabel = _RndMonitoredObjectInstanceLabel_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 2),
    _RndMonitoredObjectInstanceLabel_Type()
)
rndMonitoredObjectInstanceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredObjectInstanceLabel.setStatus("mandatory")


class _RndMonitoredObjectName_Type(DisplayString):
    """Custom type rndMonitoredObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RndMonitoredObjectName_Type.__name__ = "DisplayString"
_RndMonitoredObjectName_Object = MibTableColumn
rndMonitoredObjectName = _RndMonitoredObjectName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 3),
    _RndMonitoredObjectName_Type()
)
rndMonitoredObjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectName.setStatus("mandatory")
_RndMonitoredObjectIdentifier_Type = ObjectIdentifier
_RndMonitoredObjectIdentifier_Object = MibTableColumn
rndMonitoredObjectIdentifier = _RndMonitoredObjectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 4),
    _RndMonitoredObjectIdentifier_Type()
)
rndMonitoredObjectIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectIdentifier.setStatus("mandatory")
_RndMonitoredObjectInstance_Type = ObjectIdentifier
_RndMonitoredObjectInstance_Object = MibTableColumn
rndMonitoredObjectInstance = _RndMonitoredObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 5),
    _RndMonitoredObjectInstance_Type()
)
rndMonitoredObjectInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectInstance.setStatus("mandatory")


class _RndMonitoredObjectSyntax_Type(Integer32):
    """Custom type rndMonitoredObjectSyntax based on Integer32"""
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
        *(("integer", 1),
          ("octet-string", 2),
          ("ip-address", 3),
          ("object-identifier", 4))
    )


_RndMonitoredObjectSyntax_Type.__name__ = "Integer32"
_RndMonitoredObjectSyntax_Object = MibTableColumn
rndMonitoredObjectSyntax = _RndMonitoredObjectSyntax_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 6),
    _RndMonitoredObjectSyntax_Type()
)
rndMonitoredObjectSyntax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectSyntax.setStatus("mandatory")
_RndMonitoringInterval_Type = Integer32
_RndMonitoringInterval_Object = MibTableColumn
rndMonitoringInterval = _RndMonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 7),
    _RndMonitoringInterval_Type()
)
rndMonitoringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringInterval.setStatus("mandatory")
_RndAlarmMaxTreshold_Type = Integer32
_RndAlarmMaxTreshold_Object = MibTableColumn
rndAlarmMaxTreshold = _RndAlarmMaxTreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 8),
    _RndAlarmMaxTreshold_Type()
)
rndAlarmMaxTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmMaxTreshold.setStatus("mandatory")
_RndAlarmMinTreshold_Type = Integer32
_RndAlarmMinTreshold_Object = MibTableColumn
rndAlarmMinTreshold = _RndAlarmMinTreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 9),
    _RndAlarmMinTreshold_Type()
)
rndAlarmMinTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmMinTreshold.setStatus("mandatory")
_RndMonitoringLogfile_Type = DisplayString
_RndMonitoringLogfile_Object = MibTableColumn
rndMonitoringLogfile = _RndMonitoringLogfile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 10),
    _RndMonitoringLogfile_Type()
)
rndMonitoringLogfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringLogfile.setStatus("mandatory")
_RndMonitoringEntryStatus_Type = RowStatus
_RndMonitoringEntryStatus_Object = MibTableColumn
rndMonitoringEntryStatus = _RndMonitoringEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 11),
    _RndMonitoringEntryStatus_Type()
)
rndMonitoringEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringEntryStatus.setStatus("mandatory")
_RndMibFilesTable_Object = MibTable
rndMibFilesTable = _RndMibFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5)
)
if mibBuilder.loadTexts:
    rndMibFilesTable.setStatus("mandatory")
_RndMibFileEntry_Object = MibTableRow
rndMibFileEntry = _RndMibFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1)
)
rndMibFileEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndMibFileIndex"),
)
if mibBuilder.loadTexts:
    rndMibFileEntry.setStatus("mandatory")
_RndMibFileIndex_Type = Integer32
_RndMibFileIndex_Object = MibTableColumn
rndMibFileIndex = _RndMibFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 1),
    _RndMibFileIndex_Type()
)
rndMibFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMibFileIndex.setStatus("mandatory")
_RndMibFilePath_Type = DisplayString
_RndMibFilePath_Object = MibTableColumn
rndMibFilePath = _RndMibFilePath_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 2),
    _RndMibFilePath_Type()
)
rndMibFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFilePath.setStatus("mandatory")


class _RndMibFileRefresh_Type(Integer32):
    """Custom type rndMibFileRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RndMibFileRefresh_Type.__name__ = "Integer32"
_RndMibFileRefresh_Object = MibTableColumn
rndMibFileRefresh = _RndMibFileRefresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 3),
    _RndMibFileRefresh_Type()
)
rndMibFileRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFileRefresh.setStatus("mandatory")
_RndMibFileEntryStatus_Type = RowStatus
_RndMibFileEntryStatus_Object = MibTableColumn
rndMibFileEntryStatus = _RndMibFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 4),
    _RndMibFileEntryStatus_Type()
)
rndMibFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFileEntryStatus.setStatus("mandatory")
_RndHardwareConfiguration_Type = TruthValue
_RndHardwareConfiguration_Object = MibScalar
rndHardwareConfiguration = _RndHardwareConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 6),
    _RndHardwareConfiguration_Type()
)
rndHardwareConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndHardwareConfiguration.setStatus("mandatory")


class _RndEraseSimulatedConfiguration_Type(Integer32):
    """Custom type rndEraseSimulatedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eraseSimulatedConfiguration", 1),
          ("simulatedConfigurationPresent", 2),
          ("simulatedConfigurationErased", 3))
    )


_RndEraseSimulatedConfiguration_Type.__name__ = "Integer32"
_RndEraseSimulatedConfiguration_Object = MibScalar
rndEraseSimulatedConfiguration = _RndEraseSimulatedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 7),
    _RndEraseSimulatedConfiguration_Type()
)
rndEraseSimulatedConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndEraseSimulatedConfiguration.setStatus("mandatory")
_RndDeleteValuesTable_Object = MibTable
rndDeleteValuesTable = _RndDeleteValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8)
)
if mibBuilder.loadTexts:
    rndDeleteValuesTable.setStatus("mandatory")
_RndDeleteValuesEntry_Object = MibTableRow
rndDeleteValuesEntry = _RndDeleteValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1)
)
rndDeleteValuesEntry.setIndexNames(
    (1, "RADWARE-MIB", "rndRowStatusVariableName"),
)
if mibBuilder.loadTexts:
    rndDeleteValuesEntry.setStatus("mandatory")


class _RndRowStatusVariableName_Type(DisplayString):
    """Custom type rndRowStatusVariableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RndRowStatusVariableName_Type.__name__ = "DisplayString"
_RndRowStatusVariableName_Object = MibTableColumn
rndRowStatusVariableName = _RndRowStatusVariableName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 1),
    _RndRowStatusVariableName_Type()
)
rndRowStatusVariableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowStatusVariableName.setStatus("mandatory")
_RndRowStatusObjectId_Type = ObjectIdentifier
_RndRowStatusObjectId_Object = MibTableColumn
rndRowStatusObjectId = _RndRowStatusObjectId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 2),
    _RndRowStatusObjectId_Type()
)
rndRowStatusObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowStatusObjectId.setStatus("mandatory")
_RndRowDeleteValue_Type = Integer32
_RndRowDeleteValue_Object = MibTableColumn
rndRowDeleteValue = _RndRowDeleteValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 3),
    _RndRowDeleteValue_Type()
)
rndRowDeleteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowDeleteValue.setStatus("mandatory")
_RndDeleteValueEntryStatus_Type = RowStatus
_RndDeleteValueEntryStatus_Object = MibTableColumn
rndDeleteValueEntryStatus = _RndDeleteValueEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 4),
    _RndDeleteValueEntryStatus_Type()
)
rndDeleteValueEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDeleteValueEntryStatus.setStatus("mandatory")
_RndVisionDriver_ObjectIdentity = ObjectIdentity
rndVisionDriver = _RndVisionDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9)
)


class _RndVisionDriverActiveName_Type(DisplayString):
    """Custom type rndVisionDriverActiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_RndVisionDriverActiveName_Type.__name__ = "DisplayString"
_RndVisionDriverActiveName_Object = MibScalar
rndVisionDriverActiveName = _RndVisionDriverActiveName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 1),
    _RndVisionDriverActiveName_Type()
)
rndVisionDriverActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndVisionDriverActiveName.setStatus("mandatory")


class _RndVisionDriverRestoreFromBackup_Type(Integer32):
    """Custom type rndVisionDriverRestoreFromBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_RndVisionDriverRestoreFromBackup_Type.__name__ = "Integer32"
_RndVisionDriverRestoreFromBackup_Object = MibScalar
rndVisionDriverRestoreFromBackup = _RndVisionDriverRestoreFromBackup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 2),
    _RndVisionDriverRestoreFromBackup_Type()
)
rndVisionDriverRestoreFromBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndVisionDriverRestoreFromBackup.setStatus("mandatory")
_RndSmartFan_ObjectIdentity = ObjectIdentity
rndSmartFan = _RndSmartFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 10)
)


class _RndSmartFanStatus_Type(Integer32):
    """Custom type rndSmartFanStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RndSmartFanStatus_Type.__name__ = "Integer32"
_RndSmartFanStatus_Object = MibScalar
rndSmartFanStatus = _RndSmartFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 10, 1),
    _RndSmartFanStatus_Type()
)
rndSmartFanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSmartFanStatus.setStatus("mandatory")
_RsIpZeroHopRouting_ObjectIdentity = ObjectIdentity
rsIpZeroHopRouting = _RsIpZeroHopRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 3)
)


class _RsIpZhrGeneralStatus_Type(Integer32):
    """Custom type rsIpZhrGeneralStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsIpZhrGeneralStatus_Type.__name__ = "Integer32"
_RsIpZhrGeneralStatus_Object = MibScalar
rsIpZhrGeneralStatus = _RsIpZhrGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 1),
    _RsIpZhrGeneralStatus_Type()
)
rsIpZhrGeneralStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrGeneralStatus.setStatus("mandatory")


class _RsIpZhrAgingTimeout_Type(Integer32):
    """Custom type rsIpZhrAgingTimeout based on Integer32"""
    defaultValue = 600


_RsIpZhrAgingTimeout_Type.__name__ = "Integer32"
_RsIpZhrAgingTimeout_Object = MibScalar
rsIpZhrAgingTimeout = _RsIpZhrAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 2),
    _RsIpZhrAgingTimeout_Type()
)
rsIpZhrAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrAgingTimeout.setStatus("mandatory")
_RsIpZhrStatusTable_Object = MibTable
rsIpZhrStatusTable = _RsIpZhrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3)
)
if mibBuilder.loadTexts:
    rsIpZhrStatusTable.setStatus("mandatory")
_RsIpZhrStatusEntry_Object = MibTableRow
rsIpZhrStatusEntry = _RsIpZhrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3, 1)
)
rsIpZhrStatusEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpZhrStatusIpIntf"),
)
if mibBuilder.loadTexts:
    rsIpZhrStatusEntry.setStatus("mandatory")
_RsIpZhrStatusIpIntf_Type = IpAddress
_RsIpZhrStatusIpIntf_Object = MibTableColumn
rsIpZhrStatusIpIntf = _RsIpZhrStatusIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3, 1, 1),
    _RsIpZhrStatusIpIntf_Type()
)
rsIpZhrStatusIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrStatusIpIntf.setStatus("mandatory")


class _RsIpZhrAdminStatus_Type(Integer32):
    """Custom type rsIpZhrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsIpZhrAdminStatus_Type.__name__ = "Integer32"
_RsIpZhrAdminStatus_Object = MibTableColumn
rsIpZhrAdminStatus = _RsIpZhrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3, 1, 2),
    _RsIpZhrAdminStatus_Type()
)
rsIpZhrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrAdminStatus.setStatus("mandatory")
_RsIpZhrVirtAddressTable_Object = MibTable
rsIpZhrVirtAddressTable = _RsIpZhrVirtAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4)
)
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressTable.setStatus("mandatory")
_RsIpZhrVirtAddressEntry_Object = MibTableRow
rsIpZhrVirtAddressEntry = _RsIpZhrVirtAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1)
)
rsIpZhrVirtAddressEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpZhrVirtAddressIpIntf"),
    (0, "RADWARE-MIB", "rsIpZhrVirtAddressTo"),
)
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressEntry.setStatus("mandatory")
_RsIpZhrVirtAddressIpIntf_Type = IpAddress
_RsIpZhrVirtAddressIpIntf_Object = MibTableColumn
rsIpZhrVirtAddressIpIntf = _RsIpZhrVirtAddressIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 1),
    _RsIpZhrVirtAddressIpIntf_Type()
)
rsIpZhrVirtAddressIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressIpIntf.setStatus("mandatory")
_RsIpZhrVirtAddressTo_Type = IpAddress
_RsIpZhrVirtAddressTo_Object = MibTableColumn
rsIpZhrVirtAddressTo = _RsIpZhrVirtAddressTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 2),
    _RsIpZhrVirtAddressTo_Type()
)
rsIpZhrVirtAddressTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressTo.setStatus("mandatory")
_RsIpZhrVirtAddressFrom_Type = IpAddress
_RsIpZhrVirtAddressFrom_Object = MibTableColumn
rsIpZhrVirtAddressFrom = _RsIpZhrVirtAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 3),
    _RsIpZhrVirtAddressFrom_Type()
)
rsIpZhrVirtAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressFrom.setStatus("mandatory")
_RsIpZhrVirtAddressStatus_Type = RowStatus
_RsIpZhrVirtAddressStatus_Object = MibTableColumn
rsIpZhrVirtAddressStatus = _RsIpZhrVirtAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 4),
    _RsIpZhrVirtAddressStatus_Type()
)
rsIpZhrVirtAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressStatus.setStatus("mandatory")
_RsIpZhrConnectionsTable_Object = MibTable
rsIpZhrConnectionsTable = _RsIpZhrConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5)
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTable.setStatus("mandatory")
_RsIpZhrConnectionEntry_Object = MibTableRow
rsIpZhrConnectionEntry = _RsIpZhrConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1)
)
rsIpZhrConnectionEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpZhrConnectionIpIntf"),
    (0, "RADWARE-MIB", "rsIpZhrConnectionSrcIp"),
    (0, "RADWARE-MIB", "rsIpZhrConnectionDestIp"),
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionEntry.setStatus("mandatory")
_RsIpZhrConnectionIpIntf_Type = IpAddress
_RsIpZhrConnectionIpIntf_Object = MibTableColumn
rsIpZhrConnectionIpIntf = _RsIpZhrConnectionIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 1),
    _RsIpZhrConnectionIpIntf_Type()
)
rsIpZhrConnectionIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionIpIntf.setStatus("mandatory")
_RsIpZhrConnectionSrcIp_Type = IpAddress
_RsIpZhrConnectionSrcIp_Object = MibTableColumn
rsIpZhrConnectionSrcIp = _RsIpZhrConnectionSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 2),
    _RsIpZhrConnectionSrcIp_Type()
)
rsIpZhrConnectionSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionSrcIp.setStatus("mandatory")
_RsIpZhrConnectionDestIp_Type = IpAddress
_RsIpZhrConnectionDestIp_Object = MibTableColumn
rsIpZhrConnectionDestIp = _RsIpZhrConnectionDestIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 3),
    _RsIpZhrConnectionDestIp_Type()
)
rsIpZhrConnectionDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionDestIp.setStatus("mandatory")
_RsIpZhrConnectionVirtualIp_Type = IpAddress
_RsIpZhrConnectionVirtualIp_Object = MibTableColumn
rsIpZhrConnectionVirtualIp = _RsIpZhrConnectionVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 4),
    _RsIpZhrConnectionVirtualIp_Type()
)
rsIpZhrConnectionVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionVirtualIp.setStatus("mandatory")


class _RsIpZhrConnectionType_Type(Integer32):
    """Custom type rsIpZhrConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("disabled", 3))
    )


_RsIpZhrConnectionType_Type.__name__ = "Integer32"
_RsIpZhrConnectionType_Object = MibTableColumn
rsIpZhrConnectionType = _RsIpZhrConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 5),
    _RsIpZhrConnectionType_Type()
)
rsIpZhrConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionType.setStatus("mandatory")
_RsIpZhrConnectionAge_Type = Integer32
_RsIpZhrConnectionAge_Object = MibTableColumn
rsIpZhrConnectionAge = _RsIpZhrConnectionAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 6),
    _RsIpZhrConnectionAge_Type()
)
rsIpZhrConnectionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionAge.setStatus("mandatory")
_RsIpZhrConnectionStatus_Type = RowStatus
_RsIpZhrConnectionStatus_Object = MibTableColumn
rsIpZhrConnectionStatus = _RsIpZhrConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 7),
    _RsIpZhrConnectionStatus_Type()
)
rsIpZhrConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrConnectionStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

routeTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 5)
)
routeTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    routeTableOverflow.setStatus(
        ""
    )

fanNotWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 7)
)
fanNotWorking.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    fanNotWorking.setStatus(
        ""
    )

resetRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 10)
)
resetRequired.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    resetRequired.setStatus(
        ""
    )

endTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 12)
)
endTftp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    endTftp.setStatus(
        ""
    )

abortTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 13)
)
abortTftp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    abortTftp.setStatus(
        ""
    )

startTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 14)
)
startTftp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    startTftp.setStatus(
        ""
    )

deviceTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 15)
)
deviceTemperatureNormal.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    deviceTemperatureNormal.setStatus(
        ""
    )

deviceTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 16)
)
deviceTemperatureHigh.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    deviceTemperatureHigh.setStatus(
        ""
    )

deviceTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 17)
)
deviceTemperatureCritical.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    deviceTemperatureCritical.setStatus(
        ""
    )

rsARPTableIpConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 21)
)
rsARPTableIpConflict.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsARPTableIpConflict.setStatus(
        ""
    )

ipxRipTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 36)
)
ipxRipTblOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxRipTblOverflow.setStatus(
        ""
    )

ipxSapTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 37)
)
ipxSapTblOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxSapTblOverflow.setStatus(
        ""
    )

facsAccessVoilation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 49)
)
facsAccessVoilation.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    facsAccessVoilation.setStatus(
        ""
    )

autoConfigurationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 50)
)
autoConfigurationCompleted.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    autoConfigurationCompleted.setStatus(
        ""
    )

forwardingTabOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 51)
)
forwardingTabOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    forwardingTabOverflow.setStatus(
        ""
    )

errorsDuringInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 61)
)
errorsDuringInit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    errorsDuringInit.setStatus(
        ""
    )

vlanDynPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 66)
)
vlanDynPortAdded.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortAdded.setStatus(
        ""
    )

vlanDynPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 67)
)
vlanDynPortRemoved.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortRemoved.setStatus(
        ""
    )

rsSDclientsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 68)
)
rsSDclientsTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDclientsTableOverflow.setStatus(
        ""
    )

rsSDinactiveServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 69)
)
rsSDinactiveServer.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDinactiveServer.setStatus(
        ""
    )

rsIpZhrConnectionsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 70)
)
rsIpZhrConnectionsTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTableOverflow.setStatus(
        ""
    )

rsIpZhrReqStaticConnNotAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 71)
)
rsIpZhrReqStaticConnNotAccepted.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrReqStaticConnNotAccepted.setStatus(
        ""
    )

rsIpZhrVirtualIpAsSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 72)
)
rsIpZhrVirtualIpAsSource.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrVirtualIpAsSource.setStatus(
        ""
    )

rsIpZhrNotAllocVirtualIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 73)
)
rsIpZhrNotAllocVirtualIp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrNotAllocVirtualIp.setStatus(
        ""
    )

rsSnmpSetRequestInSpecialCfgState = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 74)
)
rsSnmpSetRequestInSpecialCfgState.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSnmpSetRequestInSpecialCfgState.setStatus(
        ""
    )

rsConfigurationAuditEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 75)
)
rsConfigurationAuditEvent.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsConfigurationAuditEvent.setStatus(
        ""
    )

rdwrFanNotWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 76)
)
rdwrFanNotWorking.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrFanNotWorking.setStatus(
        ""
    )

rdwrFanInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 77)
)
rdwrFanInfo.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrFanInfo.setStatus(
        ""
    )

rdwrCertExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 78)
)
rdwrCertExpiration.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrCertExpiration.setStatus(
        ""
    )

cdeResyncronizing = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 79)
)
cdeResyncronizing.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeResyncronizing.setStatus(
        ""
    )

cdeCannotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 80)
)
cdeCannotSync.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeCannotSync.setStatus(
        ""
    )

cdeConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 81)
)
cdeConnected.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeConnected.setStatus(
        ""
    )

cdeConfigUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 82)
)
cdeConfigUpdateFailed.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeConfigUpdateFailed.setStatus(
        ""
    )

cdeSlaveReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 83)
)
cdeSlaveReboot.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeSlaveReboot.setStatus(
        ""
    )

cdeSlaveRebootFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 84)
)
cdeSlaveRebootFailed.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeSlaveRebootFailed.setStatus(
        ""
    )

cdeEnterOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 85)
)
cdeEnterOutOfSync.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeEnterOutOfSync.setStatus(
        ""
    )

cdeSlaveRebootPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 86)
)
cdeSlaveRebootPending.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeSlaveRebootPending.setStatus(
        ""
    )

cdeDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 87)
)
cdeDisconnected.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeDisconnected.setStatus(
        ""
    )

cdeInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 88)
)
cdeInSync.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeInSync.setStatus(
        ""
    )

cdeIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 89)
)
cdeIncompatible.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeIncompatible.setStatus(
        ""
    )

cdeNoMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 90)
)
cdeNoMaster.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeNoMaster.setStatus(
        ""
    )

cdeMasterConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 91)
)
cdeMasterConnected.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    cdeMasterConnected.setStatus(
        ""
    )

rsWSDRedundancySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 141)
)
rsWSDRedundancySwitch.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRedundancySwitch.setStatus(
        ""
    )

rsStpPortStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 30, 0, 1)
)
rsStpPortStateTrap.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsStpPortStateTrap.setStatus(
        ""
    )

rsWSDConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 1)
)
rsWSDConnectionLimitReached.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDConnectionLimitReached.setStatus(
        ""
    )

rsWSDReadyForShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 2)
)
rsWSDReadyForShutDown.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDReadyForShutDown.setStatus(
        ""
    )

rsWSDIllegalReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 3)
)
rsWSDIllegalReport.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDIllegalReport.setStatus(
        ""
    )

rsWSDRemoteWSDUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 4)
)
rsWSDRemoteWSDUnavailable.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRemoteWSDUnavailable.setStatus(
        ""
    )

rsWSDCapacityLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 5)
)
rsWSDCapacityLimitReached.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDCapacityLimitReached.setStatus(
        ""
    )

rsWSDStatusMonitoring = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 6)
)
rsWSDStatusMonitoring.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDStatusMonitoring.setStatus(
        ""
    )

rsWSDWrongPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 7)
)
rsWSDWrongPassword.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDWrongPassword.setStatus(
        ""
    )

rsWSDInternalTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 8)
)
rsWSDInternalTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDInternalTableOverflow.setStatus(
        ""
    )

rsWSDServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 9)
)
rsWSDServerUp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDServerUp.setStatus(
        ""
    )

rsWSDPoliciesUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 10)
)
rsWSDPoliciesUpdated.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDPoliciesUpdated.setStatus(
        ""
    )

rsWSDIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 11)
)
rsWSDIntrusionDetected.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDIntrusionDetected.setStatus(
        ""
    )

rsWSDUserLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 12)
)
rsWSDUserLocked.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDUserLocked.setStatus(
        ""
    )

rsWSDAuthenticationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 13)
)
rsWSDAuthenticationSuccess.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDAuthenticationSuccess.setStatus(
        ""
    )

rsRadwareNTPUpdateProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 14)
)
rsRadwareNTPUpdateProblem.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsRadwareNTPUpdateProblem.setStatus(
        ""
    )

rsRadwareVrrpErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 15)
)
rsRadwareVrrpErrors.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsRadwareVrrpErrors.setStatus(
        ""
    )

rdwrDualPowerSupplyProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 16)
)
rdwrDualPowerSupplyProblem.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrDualPowerSupplyProblem.setStatus(
        ""
    )

rdwrDualPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 17)
)
rdwrDualPowerSupplyUp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrDualPowerSupplyUp.setStatus(
        ""
    )

rdwrMngmntPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 18)
)
rdwrMngmntPortDisabled.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrMngmntPortDisabled.setStatus(
        ""
    )

rdwrUnauthorizedSourceIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 19)
)
rdwrUnauthorizedSourceIP.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rdwrUnauthorizedSourceIP.setStatus(
        ""
    )

rsSSLCertificateSyncProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 20)
)
rsSSLCertificateSyncProblem.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSSLCertificateSyncProblem.setStatus(
        ""
    )

rsWSDAuthenticationServerSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 22)
)
rsWSDAuthenticationServerSuccess.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDAuthenticationServerSuccess.setStatus(
        ""
    )

rsWSDAuthenticationServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 23)
)
rsWSDAuthenticationServerFail.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDAuthenticationServerFail.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADWARE-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "FeatureStatus": FeatureStatus,
       "NetNumber": NetNumber,
       "BitFlag": BitFlag,
       "VrId": VrId,
       "RouteTag": RouteTag,
       "RsIfType": RsIfType,
       "rnd": rnd,
       "routeTableOverflow": routeTableOverflow,
       "fanNotWorking": fanNotWorking,
       "resetRequired": resetRequired,
       "endTftp": endTftp,
       "abortTftp": abortTftp,
       "startTftp": startTftp,
       "deviceTemperatureNormal": deviceTemperatureNormal,
       "deviceTemperatureHigh": deviceTemperatureHigh,
       "deviceTemperatureCritical": deviceTemperatureCritical,
       "rsARPTableIpConflict": rsARPTableIpConflict,
       "ipxRipTblOverflow": ipxRipTblOverflow,
       "ipxSapTblOverflow": ipxSapTblOverflow,
       "facsAccessVoilation": facsAccessVoilation,
       "autoConfigurationCompleted": autoConfigurationCompleted,
       "forwardingTabOverflow": forwardingTabOverflow,
       "errorsDuringInit": errorsDuringInit,
       "vlanDynPortAdded": vlanDynPortAdded,
       "vlanDynPortRemoved": vlanDynPortRemoved,
       "rsSDclientsTableOverflow": rsSDclientsTableOverflow,
       "rsSDinactiveServer": rsSDinactiveServer,
       "rsIpZhrConnectionsTableOverflow": rsIpZhrConnectionsTableOverflow,
       "rsIpZhrReqStaticConnNotAccepted": rsIpZhrReqStaticConnNotAccepted,
       "rsIpZhrVirtualIpAsSource": rsIpZhrVirtualIpAsSource,
       "rsIpZhrNotAllocVirtualIp": rsIpZhrNotAllocVirtualIp,
       "rsSnmpSetRequestInSpecialCfgState": rsSnmpSetRequestInSpecialCfgState,
       "rsConfigurationAuditEvent": rsConfigurationAuditEvent,
       "rdwrFanNotWorking": rdwrFanNotWorking,
       "rdwrFanInfo": rdwrFanInfo,
       "rdwrCertExpiration": rdwrCertExpiration,
       "cdeResyncronizing": cdeResyncronizing,
       "cdeCannotSync": cdeCannotSync,
       "cdeConnected": cdeConnected,
       "cdeConfigUpdateFailed": cdeConfigUpdateFailed,
       "cdeSlaveReboot": cdeSlaveReboot,
       "cdeSlaveRebootFailed": cdeSlaveRebootFailed,
       "cdeEnterOutOfSync": cdeEnterOutOfSync,
       "cdeSlaveRebootPending": cdeSlaveRebootPending,
       "cdeDisconnected": cdeDisconnected,
       "cdeInSync": cdeInSync,
       "cdeIncompatible": cdeIncompatible,
       "cdeNoMaster": cdeNoMaster,
       "cdeMasterConnected": cdeMasterConnected,
       "rsWSDRedundancySwitch": rsWSDRedundancySwitch,
       "rndMng": rndMng,
       "rndSysId": rndSysId,
       "rndAction": rndAction,
       "rndFileName": rndFileName,
       "removeViewTablePermissionReductionCheck": removeViewTablePermissionReductionCheck,
       "rsConfigurationAuditStatus": rsConfigurationAuditStatus,
       "rdwrPrintToLogAndCli": rdwrPrintToLogAndCli,
       "rdwrClearTheLogFile": rdwrClearTheLogFile,
       "rdwrAutoRowGenerationStatus": rdwrAutoRowGenerationStatus,
       "rsConfigurationAuditingType": rsConfigurationAuditingType,
       "rndDeviceParams": rndDeviceParams,
       "rndBridgeType": rndBridgeType,
       "rndInactiveArpTimeOut": rndInactiveArpTimeOut,
       "rndBridgeAlarm": rndBridgeAlarm,
       "rndErrorDesc": rndErrorDesc,
       "rndErrorSeverity": rndErrorSeverity,
       "rndBrgVersion": rndBrgVersion,
       "rndBrgFeatures": rndBrgFeatures,
       "rndBrgLicense": rndBrgLicense,
       "rndIpHost": rndIpHost,
       "rndICMPTransmitionEnable": rndICMPTransmitionEnable,
       "rndCommunityTable": rndCommunityTable,
       "rndCommunityEntry": rndCommunityEntry,
       "rndCommunityMngStationAddr": rndCommunityMngStationAddr,
       "rndCommunityString": rndCommunityString,
       "rndCommunityAccess": rndCommunityAccess,
       "rndCommunityTrapsEnable": rndCommunityTrapsEnable,
       "rndCommunityStatus": rndCommunityStatus,
       "rndManagedTime": rndManagedTime,
       "rndManagedDate": rndManagedDate,
       "genGroup": genGroup,
       "genGroupHWVersion": genGroupHWVersion,
       "genGroupConfigurationSymbol": genGroupConfigurationSymbol,
       "genGroupHWStatus": genGroupHWStatus,
       "rndSerialNumber": rndSerialNumber,
       "rndApsoluteOSVersion": rndApsoluteOSVersion,
       "rdwrDeviceType": rdwrDeviceType,
       "rdwrDeviceNumberOfPorts": rdwrDeviceNumberOfPorts,
       "rdwrDevicePortsConfig": rdwrDevicePortsConfig,
       "rdwrDeviceThroughput": rdwrDeviceThroughput,
       "rdwrDeviceNetworkDriver": rdwrDeviceNetworkDriver,
       "rdwrDeviceCPUsNumber": rdwrDeviceCPUsNumber,
       "rdwrDeviceActiveBoot": rdwrDeviceActiveBoot,
       "rdwrDeviceSecondaryBoot": rdwrDeviceSecondaryBoot,
       "rndInterface": rndInterface,
       "rndIfTable": rndIfTable,
       "rndIfEntry": rndIfEntry,
       "rndIfIndex": rndIfIndex,
       "rndIfBoardNum": rndIfBoardNum,
       "rndIfNetAddress": rndIfNetAddress,
       "rndIfStatus": rndIfStatus,
       "rndIfClockType": rndIfClockType,
       "rndIfBaudRate": rndIfBaudRate,
       "rndIfCost": rndIfCost,
       "rndIfCompression": rndIfCompression,
       "rndIfCompressionStatus": rndIfCompressionStatus,
       "rndIfCompressionRate": rndIfCompressionRate,
       "rndIfLATCompression": rndIfLATCompression,
       "rndIfCompressionType": rndIfCompressionType,
       "rndIfFilterMode": rndIfFilterMode,
       "rndIfChannelType": rndIfChannelType,
       "rndIfBridge": rndIfBridge,
       "rndHighPriorityIf": rndHighPriorityIf,
       "rndWanHeader": rndWanHeader,
       "rndDuplexMode": rndDuplexMode,
       "rndIPX": rndIPX,
       "rndFACS": rndFACS,
       "rndFACSDefaultAction": rndFACSDefaultAction,
       "rndFACSActTable": rndFACSActTable,
       "rndFACSActEntry": rndFACSActEntry,
       "rndFACSActType": rndFACSActType,
       "rndFACSActIfIndex": rndFACSActIfIndex,
       "rndFACSAction": rndFACSAction,
       "rndFACSTable": rndFACSTable,
       "rndFACSEntry": rndFACSEntry,
       "rndFACSIfIndex": rndFACSIfIndex,
       "rndFACSProtocolType": rndFACSProtocolType,
       "rndFACSType": rndFACSType,
       "rndFACSIndex": rndFACSIndex,
       "rndFACSSrcAdd": rndFACSSrcAdd,
       "rndFACSSrcAddMask": rndFACSSrcAddMask,
       "rndFACSDesAdd": rndFACSDesAdd,
       "rndFACSDesAddMask": rndFACSDesAddMask,
       "rndFACSOperation": rndFACSOperation,
       "rndFACSNetFiltering": rndFACSNetFiltering,
       "rndFACSSoketNum": rndFACSSoketNum,
       "rndFACSMask1Id": rndFACSMask1Id,
       "rndFACSMask2Id": rndFACSMask2Id,
       "rndFACSStatus": rndFACSStatus,
       "rndBootP": rndBootP,
       "rndBootPServerAddress": rndBootPServerAddress,
       "rndBootPRelaySecThreshold": rndBootPRelaySecThreshold,
       "ipSpec": ipSpec,
       "rsIpAddrTable": rsIpAddrTable,
       "rsIpAddrEntry": rsIpAddrEntry,
       "rsIpAdEntAddr": rsIpAdEntAddr,
       "rsIpAdEntIfIndex": rsIpAdEntIfIndex,
       "rsIpAdEntNetMask": rsIpAdEntNetMask,
       "rsIpAdEntForwardIpBroadcast": rsIpAdEntForwardIpBroadcast,
       "rsIpAdEntReasmMaxSize": rsIpAdEntReasmMaxSize,
       "rsIpAdEntStatus": rsIpAdEntStatus,
       "rsIpAdEntBcastAddr": rsIpAdEntBcastAddr,
       "rsIpAdEntVlanTag": rsIpAdEntVlanTag,
       "rsIpAdEntOneIpMode": rsIpAdEntOneIpMode,
       "rsIpAdEntType": rsIpAdEntType,
       "rsIpAdEntPeerAddr": rsIpAdEntPeerAddr,
       "rsIpAdEntPeerAddrStatus": rsIpAdEntPeerAddrStatus,
       "icmpSpec": icmpSpec,
       "rsIcmpGenErrMsgEnable": rsIcmpGenErrMsgEnable,
       "rsIcmpRdTable": rsIcmpRdTable,
       "rsIcmpRdEntry": rsIcmpRdEntry,
       "rsIcmpRdIpAddr": rsIcmpRdIpAddr,
       "rsIcmpRdIpAdvertAddr": rsIcmpRdIpAdvertAddr,
       "rsIcmpRdMaxAdvertInterval": rsIcmpRdMaxAdvertInterval,
       "rsIcmpRdMinAdvertInterval": rsIcmpRdMinAdvertInterval,
       "rsIcmpRdAdvertLifetime": rsIcmpRdAdvertLifetime,
       "rsIcmpRdAdvertise": rsIcmpRdAdvertise,
       "rsIcmpRdPreferenceLevel": rsIcmpRdPreferenceLevel,
       "rsIcmpRdEntStatus": rsIcmpRdEntStatus,
       "rip2Spec": rip2Spec,
       "rsRip2IfConfTable": rsRip2IfConfTable,
       "rsRip2IfConfEntry": rsRip2IfConfEntry,
       "rsRip2IfConfAddress": rsRip2IfConfAddress,
       "rsRip2IfConfVirtualDis": rsRip2IfConfVirtualDis,
       "rsRip2IfConfAutoSend": rsRip2IfConfAutoSend,
       "rdwrRip2IfConfTable": rdwrRip2IfConfTable,
       "rdwrRip2IfConfEntry": rdwrRip2IfConfEntry,
       "rdwrRip2IfConfAddress": rdwrRip2IfConfAddress,
       "rdwrRip2IfConfDomain": rdwrRip2IfConfDomain,
       "rdwrRip2IfConfAuthType": rdwrRip2IfConfAuthType,
       "rdwrRip2IfConfAuthKey": rdwrRip2IfConfAuthKey,
       "rdwrRip2IfConfSend": rdwrRip2IfConfSend,
       "rdwrRip2IfConfReceive": rdwrRip2IfConfReceive,
       "rdwrRip2IfConfDefaultMetric": rdwrRip2IfConfDefaultMetric,
       "rdwrRip2IfConfStatus": rdwrRip2IfConfStatus,
       "rdwrRip2IfConfSrcAddress": rdwrRip2IfConfSrcAddress,
       "rdwrRip2IfConfVirtualDis": rdwrRip2IfConfVirtualDis,
       "rdwrRip2IfConfAutoSend": rdwrRip2IfConfAutoSend,
       "arpSpec": arpSpec,
       "rsArpDeleteTable": rsArpDeleteTable,
       "rsArpInactiveTimeOut": rsArpInactiveTimeOut,
       "rsArpProxy": rsArpProxy,
       "tftp": tftp,
       "rsTftpRetryTimeOut": rsTftpRetryTimeOut,
       "rsTftpTotalTimeOut": rsTftpTotalTimeOut,
       "rsSendConfigFile": rsSendConfigFile,
       "rsGetConfigFile": rsGetConfigFile,
       "rsLoadSoftware": rsLoadSoftware,
       "rsFileServerAddress": rsFileServerAddress,
       "rsGetConfigFileAppend": rsGetConfigFileAppend,
       "rsGetConfigFileAppendReboot": rsGetConfigFileAppendReboot,
       "rsGetConfigErrorLog": rsGetConfigErrorLog,
       "rsSendConfigFileBer": rsSendConfigFileBer,
       "rsIncludePrivateKeys": rsIncludePrivateKeys,
       "rsGetConfigFileType": rsGetConfigFileType,
       "ipRedundancy": ipRedundancy,
       "ipRedundAdminStatus": ipRedundAdminStatus,
       "ipRedundOperStatus": ipRedundOperStatus,
       "ipRedundRoutersTable": ipRedundRoutersTable,
       "ipRedundRoutersEntry": ipRedundRoutersEntry,
       "ipRedundRoutersIfAddr": ipRedundRoutersIfAddr,
       "ipRedundRoutersMainRouterAddr": ipRedundRoutersMainRouterAddr,
       "ipRedundRoutersOperStatus": ipRedundRoutersOperStatus,
       "ipRedundRoutersPollInterval": ipRedundRoutersPollInterval,
       "ipRedundRoutersTimeout": ipRedundRoutersTimeout,
       "ipRedundRoutersStatus": ipRedundRoutersStatus,
       "rdwrRedunForceDownPorts": rdwrRedunForceDownPorts,
       "rdwrRedundancyInfoTable": rdwrRedundancyInfoTable,
       "rdwrRedundancyInfoEntry": rdwrRedundancyInfoEntry,
       "rdwrRedundancyInfoIdx": rdwrRedundancyInfoIdx,
       "rdwrRedundancyInfoInterface": rdwrRedundancyInfoInterface,
       "rdwrRedundancyInfoVRID": rdwrRedundancyInfoVRID,
       "rdwrRedundancyInfoMode": rdwrRedundancyInfoMode,
       "rdwrRedundancyInfoMyAddress": rdwrRedundancyInfoMyAddress,
       "rdwrRedundancyInfoNeighborAddress": rdwrRedundancyInfoNeighborAddress,
       "rdwrRedundancyInfoStatus": rdwrRedundancyInfoStatus,
       "ipRouteLeaking": ipRouteLeaking,
       "ipLeakStaticToRip": ipLeakStaticToRip,
       "ipLeakStaticToOspf": ipLeakStaticToOspf,
       "ipLeakOspfToRip": ipLeakOspfToRip,
       "ipLeakRipToOspf": ipLeakRipToOspf,
       "ipLeakExtDirectToOspf": ipLeakExtDirectToOspf,
       "ipLeakOverrideOSPFLeakonFailure": ipLeakOverrideOSPFLeakonFailure,
       "ipLeakAdvertiseOSPFAccordingtoPortRules": ipLeakAdvertiseOSPFAccordingtoPortRules,
       "ipRipFilter": ipRipFilter,
       "rsIpRipFilterGlbTable": rsIpRipFilterGlbTable,
       "rsIpRipFilterGlbEntry": rsIpRipFilterGlbEntry,
       "rsIpRipFilterGlbType": rsIpRipFilterGlbType,
       "rsIpRipFilterGlbNumber": rsIpRipFilterGlbNumber,
       "rsIpRipFilterGlbStatus": rsIpRipFilterGlbStatus,
       "rsIpRipFilterGlbIpAddr": rsIpRipFilterGlbIpAddr,
       "rsIpRipFilterGlbNetworkMaskBits": rsIpRipFilterGlbNetworkMaskBits,
       "rsIpRipFilterGlbMatchBits": rsIpRipFilterGlbMatchBits,
       "rsIpRipFilterGlbAction": rsIpRipFilterGlbAction,
       "rsIpRipFilterLclTable": rsIpRipFilterLclTable,
       "rsIpRipFilterLclEntry": rsIpRipFilterLclEntry,
       "rsIpRipFilterLclIpIntf": rsIpRipFilterLclIpIntf,
       "rsIpRipFilterLclType": rsIpRipFilterLclType,
       "rsIpRipFilterLclNumber": rsIpRipFilterLclNumber,
       "rsIpRipFilterLclStatus": rsIpRipFilterLclStatus,
       "rsIpRipFilterLclIpAddr": rsIpRipFilterLclIpAddr,
       "rsIpRipFilterLclNetworkMaskBits": rsIpRipFilterLclNetworkMaskBits,
       "rsIpRipFilterLclMatchBits": rsIpRipFilterLclMatchBits,
       "rsIpRipFilterLclAction": rsIpRipFilterLclAction,
       "rsRipEnable": rsRipEnable,
       "lreBoxAgentIP": lreBoxAgentIP,
       "ipIfTable": ipIfTable,
       "ipIfEntry": ipIfEntry,
       "ipIfAddr": ipIfAddr,
       "ipIfPrefix": ipIfPrefix,
       "ipIfIndex": ipIfIndex,
       "ipIfFwdBroadcast": ipIfFwdBroadcast,
       "ipIfBcastAddr": ipIfBcastAddr,
       "ipIfVlanTag": ipIfVlanTag,
       "ipIfLabel": ipIfLabel,
       "ipIfEntryStatus": ipIfEntryStatus,
       "ipIfBackupAddr": ipIfBackupAddr,
       "ipSpecRouteTable": ipSpecRouteTable,
       "ipSpecRouteEntry": ipSpecRouteEntry,
       "ipSpecRouteDest": ipSpecRouteDest,
       "ipSpecRoutePfxLen": ipSpecRoutePfxLen,
       "ipSpecRouteNextHop": ipSpecRouteNextHop,
       "ipSpecRouteMetric": ipSpecRouteMetric,
       "ipSpecRoutePort": ipSpecRoutePort,
       "ipSpecRouteLabel": ipSpecRouteLabel,
       "ipSpecRouteStatus": ipSpecRouteStatus,
       "ip6NetToMediaTable": ip6NetToMediaTable,
       "ip6NetToMediaEntry": ip6NetToMediaEntry,
       "ip6NetToMediaIfIndex": ip6NetToMediaIfIndex,
       "ip6NetToMediaPhysAddress": ip6NetToMediaPhysAddress,
       "ip6NetToMediaNetAddress": ip6NetToMediaNetAddress,
       "ip6NetToMediaType": ip6NetToMediaType,
       "ndSpec": ndSpec,
       "rsNetNdInactiveTimeOut": rsNetNdInactiveTimeOut,
       "virtualLan": virtualLan,
       "virtualLanTable": virtualLanTable,
       "virtualLanEntry": virtualLanEntry,
       "vlIfIndex": vlIfIndex,
       "vlProto": vlProto,
       "vlAutoConfigEnable": vlAutoConfigEnable,
       "vlStatus": vlStatus,
       "vlType": vlType,
       "virtualLanPortsTable": virtualLanPortsTable,
       "virtualLanPortEntry": virtualLanPortEntry,
       "vLIfIndex": vLIfIndex,
       "vLPortIfIndex": vLPortIfIndex,
       "vLPortType": vLPortType,
       "vLPortStatus": vLPortStatus,
       "virtualLanAutoConfTable": virtualLanAutoConfTable,
       "virtualLanAutoConfEntry": virtualLanAutoConfEntry,
       "vlAutoConfPortIfIndex": vlAutoConfPortIfIndex,
       "vlAutoConfProto": vlAutoConfProto,
       "vlAutoConfStatus": vlAutoConfStatus,
       "virtualLanAutoConfAgingTimeout": virtualLanAutoConfAgingTimeout,
       "virtualLanProtocolVlan": virtualLanProtocolVlan,
       "virtualLanUserEtherType": virtualLanUserEtherType,
       "virtualLanUserMask": virtualLanUserMask,
       "rsConf": rsConf,
       "rsIfConfTable": rsIfConfTable,
       "rsIfConfEntry": rsIfConfEntry,
       "rsIfConfIndex": rsIfConfIndex,
       "rsIfConfType": rsIfConfType,
       "rsIfConfName": rsIfConfName,
       "rsIfConfStatus": rsIfConfStatus,
       "rsTunning": rsTunning,
       "rsHighPriority": rsHighPriority,
       "rsLowPriority": rsLowPriority,
       "rsDbgLevel": rsDbgLevel,
       "rsDiagnostic": rsDiagnostic,
       "rsConfirmMessagTab": rsConfirmMessagTab,
       "eventMessageTable": eventMessageTable,
       "eventMessageEntry": eventMessageEntry,
       "eventNum": eventNum,
       "eventDesc": eventDesc,
       "reaTunning": reaTunning,
       "reaIpRemoteAgingTime": reaIpRemoteAgingTime,
       "reaFftHashMaxChain": reaFftHashMaxChain,
       "reaMltcstBitOn": reaMltcstBitOn,
       "reaIpForwardEnable": reaIpForwardEnable,
       "reaIpxForwardEnable": reaIpxForwardEnable,
       "reaBridgeEnable": reaBridgeEnable,
       "reaFacsEnable": reaFacsEnable,
       "reaIpForwardDatagrams": reaIpForwardDatagrams,
       "reaIpInDiscards": reaIpInDiscards,
       "reaIpxForwardDatagrams": reaIpxForwardDatagrams,
       "reaIpxInDiscards": reaIpxInDiscards,
       "reaBridgeFftTable": reaBridgeFftTable,
       "reaBridgeFftEntry": reaBridgeFftEntry,
       "reaBrgFftEntryNum": reaBrgFftEntryNum,
       "reaBrgFftMacAddr": reaBrgFftMacAddr,
       "reaBrgFftReNum": reaBrgFftReNum,
       "reaBrgFftPortNum": reaBrgFftPortNum,
       "reaBrgFftFacsSrcIndex": reaBrgFftFacsSrcIndex,
       "reaBrgFftFacsDstIndex": reaBrgFftFacsDstIndex,
       "reaBrgDiscards": reaBrgDiscards,
       "reaBrgForwards": reaBrgForwards,
       "reaIpFftTable": reaIpFftTable,
       "reaIpFftEntry": reaIpFftEntry,
       "reaIpFftEntryNum": reaIpFftEntryNum,
       "reaIpFftDstIpAddr": reaIpFftDstIpAddr,
       "reaIpFftDstIpMask": reaIpFftDstIpMask,
       "reaIpFftRangeType": reaIpFftRangeType,
       "reaIpFftSrcMacAddr": reaIpFftSrcMacAddr,
       "reaIpFftDstMacAddr": reaIpFftDstMacAddr,
       "reaIpFftReNum": reaIpFftReNum,
       "reaIpFftPortNum": reaIpFftPortNum,
       "reaIpFftFacsSrcIndex": reaIpFftFacsSrcIndex,
       "reaIpFftFacsDstIndex": reaIpFftFacsDstIndex,
       "reaIpFftApplFlags": reaIpFftApplFlags,
       "reaIpxFftTable": reaIpxFftTable,
       "reaIpxFftEntry": reaIpxFftEntry,
       "reaIpxFftEntryNum": reaIpxFftEntryNum,
       "reaIpxFftDstNetid": reaIpxFftDstNetid,
       "reaIpxFftRangeType": reaIpxFftRangeType,
       "reaIpxFftSrcMacAddr": reaIpxFftSrcMacAddr,
       "reaIpxFftDstMacAddr": reaIpxFftDstMacAddr,
       "reaIpxFftReNum": reaIpxFftReNum,
       "reaIpxFftPortNum": reaIpxFftPortNum,
       "reaIpxFftFacsSrcIndex": reaIpxFftFacsSrcIndex,
       "reaIpxFftFacsDstIndex": reaIpxFftFacsDstIndex,
       "lreVnResposibilityTable": lreVnResposibilityTable,
       "lreVnResposibilityEntry": lreVnResposibilityEntry,
       "lreVnRespVn": lreVnRespVn,
       "lreVnRespStatus": lreVnRespStatus,
       "reaSrcViolationEnable": reaSrcViolationEnable,
       "reaSrcViolationTrapEnable": reaSrcViolationTrapEnable,
       "reaSrcAddrValidationEnable": reaSrcAddrValidationEnable,
       "reaRsQueueDiscards": reaRsQueueDiscards,
       "reaBufFree": reaBufFree,
       "lreResetDstMacBit46": lreResetDstMacBit46,
       "lreQueSourceSelect": lreQueSourceSelect,
       "lreResetDstMacBit47": lreResetDstMacBit47,
       "rsMaxEntriesTuning": rsMaxEntriesTuning,
       "rsMaxBridgeForwardingEntriesTuning": rsMaxBridgeForwardingEntriesTuning,
       "rsMaxBrgFrwEntries": rsMaxBrgFrwEntries,
       "rsMaxBrgFrwEntriesAfterReset": rsMaxBrgFrwEntriesAfterReset,
       "rsMaxIpForwardingEntriesTuning": rsMaxIpForwardingEntriesTuning,
       "rsMaxIpFrwEntries": rsMaxIpFrwEntries,
       "rsMaxIpFrwEntriesAfterReset": rsMaxIpFrwEntriesAfterReset,
       "rsMaxArpEntriesTuning": rsMaxArpEntriesTuning,
       "rsMaxArpEntries": rsMaxArpEntries,
       "rsMaxArpEntriesAfterReset": rsMaxArpEntriesAfterReset,
       "rsMaxIpxForwardingEntriesTuning": rsMaxIpxForwardingEntriesTuning,
       "rsMaxIpxFrwEntries": rsMaxIpxFrwEntries,
       "rsMaxIpxFrwEntriesAfterReset": rsMaxIpxFrwEntriesAfterReset,
       "rsMaxIpxSapEntriesTuning": rsMaxIpxSapEntriesTuning,
       "rsMaxIpxSapEntries": rsMaxIpxSapEntries,
       "rsMaxIpxSapEntriesAfterReset": rsMaxIpxSapEntriesAfterReset,
       "rsMaxDspClntEntriesTuning": rsMaxDspClntEntriesTuning,
       "rsMaxDspClntEntries": rsMaxDspClntEntries,
       "rsMaxDspClntEntriesAfterReset": rsMaxDspClntEntriesAfterReset,
       "rsMaxZeroHopRoutEntriesTuning": rsMaxZeroHopRoutEntriesTuning,
       "rsMaxZhrConns": rsMaxZhrConns,
       "rsMaxZhrConnsAfterReset": rsMaxZhrConnsAfterReset,
       "rsMaxDspFrmEntriesTuning": rsMaxDspFrmEntriesTuning,
       "rsMaxDspFrmEntries": rsMaxDspFrmEntries,
       "rsMaxDspFrmEntriesAfterReset": rsMaxDspFrmEntriesAfterReset,
       "rsMaxRoutingEntriesTuning": rsMaxRoutingEntriesTuning,
       "rsMaxRoutingEntries": rsMaxRoutingEntries,
       "rsMaxRoutingEntriesAfterReset": rsMaxRoutingEntriesAfterReset,
       "rsMaxRadiusEntriesTuning": rsMaxRadiusEntriesTuning,
       "rsMaxRadiusUsersEntries": rsMaxRadiusUsersEntries,
       "rsMaxRadiusUsersEntriesAfterReset": rsMaxRadiusUsersEntriesAfterReset,
       "rsMaxRadiusNasAuthEntries": rsMaxRadiusNasAuthEntries,
       "rsMaxRadiusNasAuthEntriesAfterReset": rsMaxRadiusNasAuthEntriesAfterReset,
       "rsTuneCheckMemory": rsTuneCheckMemory,
       "rsTuneLastCheckResult": rsTuneLastCheckResult,
       "stpSpec": stpSpec,
       "rsStpPortStateTrap": rsStpPortStateTrap,
       "rsStpMode": rsStpMode,
       "rsStpDefaultBridgePriority": rsStpDefaultBridgePriority,
       "rsStpDefaultHelloTime": rsStpDefaultHelloTime,
       "rsStpDefaultMaxAgingTime": rsStpDefaultMaxAgingTime,
       "rsStpDefaultForwardDelayTime": rsStpDefaultForwardDelayTime,
       "rsStpDefaultPortPriority": rsStpDefaultPortPriority,
       "rsStpInstancesTable": rsStpInstancesTable,
       "rsStpInstanceEntry": rsStpInstanceEntry,
       "rsStpInstanceVlanId": rsStpInstanceVlanId,
       "rsStpInstanceBridgePriority": rsStpInstanceBridgePriority,
       "rsStpInstanceHelloTime": rsStpInstanceHelloTime,
       "rsStpInstanceMaxAgingTime": rsStpInstanceMaxAgingTime,
       "rsStpInstanceForwardDelayTime": rsStpInstanceForwardDelayTime,
       "rsStpInstanceEnabled": rsStpInstanceEnabled,
       "rsStpInstanceRootId": rsStpInstanceRootId,
       "rsStpInstanceRootPathCost": rsStpInstanceRootPathCost,
       "rsStpInstanceDesignatedBridgeId": rsStpInstanceDesignatedBridgeId,
       "rsStpInstanceDesignatedPortId": rsStpInstanceDesignatedPortId,
       "rsStpPortTable": rsStpPortTable,
       "rsStpPortEntry": rsStpPortEntry,
       "rsStpPortId": rsStpPortId,
       "rsStpPortVlanId": rsStpPortVlanId,
       "rsStpPortPriority": rsStpPortPriority,
       "rsStpPortPathCost": rsStpPortPathCost,
       "rsStpPortModeFast": rsStpPortModeFast,
       "rsStpPortEnabled": rsStpPortEnabled,
       "rsStpPortState": rsStpPortState,
       "rsStpPortRole": rsStpPortRole,
       "rndApplications": rndApplications,
       "rsServerDispatcher": rsServerDispatcher,
       "rsWSDConnectionLimitReached": rsWSDConnectionLimitReached,
       "rsWSDReadyForShutDown": rsWSDReadyForShutDown,
       "rsWSDIllegalReport": rsWSDIllegalReport,
       "rsWSDRemoteWSDUnavailable": rsWSDRemoteWSDUnavailable,
       "rsWSDCapacityLimitReached": rsWSDCapacityLimitReached,
       "rsWSDStatusMonitoring": rsWSDStatusMonitoring,
       "rsWSDWrongPassword": rsWSDWrongPassword,
       "rsWSDInternalTableOverflow": rsWSDInternalTableOverflow,
       "rsWSDServerUp": rsWSDServerUp,
       "rsWSDPoliciesUpdated": rsWSDPoliciesUpdated,
       "rsWSDIntrusionDetected": rsWSDIntrusionDetected,
       "rsWSDUserLocked": rsWSDUserLocked,
       "rsWSDAuthenticationSuccess": rsWSDAuthenticationSuccess,
       "rsRadwareNTPUpdateProblem": rsRadwareNTPUpdateProblem,
       "rsRadwareVrrpErrors": rsRadwareVrrpErrors,
       "rdwrDualPowerSupplyProblem": rdwrDualPowerSupplyProblem,
       "rdwrDualPowerSupplyUp": rdwrDualPowerSupplyUp,
       "rdwrMngmntPortDisabled": rdwrMngmntPortDisabled,
       "rdwrUnauthorizedSourceIP": rdwrUnauthorizedSourceIP,
       "rsSSLCertificateSyncProblem": rsSSLCertificateSyncProblem,
       "rsWSDAuthenticationServerSuccess": rsWSDAuthenticationServerSuccess,
       "rsWSDAuthenticationServerFail": rsWSDAuthenticationServerFail,
       "rsWSDServerStatTable": rsWSDServerStatTable,
       "rsWSDServerStatEntry": rsWSDServerStatEntry,
       "rsWSDSerStatName": rsWSDSerStatName,
       "rsWSDSerStatAttUsersNum": rsWSDSerStatAttUsersNum,
       "rsWSDSerStatPeakLoad": rsWSDSerStatPeakLoad,
       "rsWSDSerStatFramesRate": rsWSDSerStatFramesRate,
       "rsWSDSerStatFramesLoad": rsWSDSerStatFramesLoad,
       "rsWSDSerStatRecoveryTime": rsWSDSerStatRecoveryTime,
       "rsWSDSerStatWarmUpTime": rsWSDSerStatWarmUpTime,
       "rsWSDSerStatConnectionLimit": rsWSDSerStatConnectionLimit,
       "rsWSDSerStatAdminStatus": rsWSDSerStatAdminStatus,
       "rsWSDSerStatConnectionLimitReached": rsWSDSerStatConnectionLimitReached,
       "wsdRedundTable": wsdRedundTable,
       "wsdRedundEntry": wsdRedundEntry,
       "wsdRedundFarmAddr": wsdRedundFarmAddr,
       "wsdRedundMainWsdAddr": wsdRedundMainWsdAddr,
       "wsdRedundOperStatus": wsdRedundOperStatus,
       "wsdRedundPollInterval": wsdRedundPollInterval,
       "wsdRedundTimeout": wsdRedundTimeout,
       "wsdRedundStatus": wsdRedundStatus,
       "rsWSDNewEntryOnSourcePort": rsWSDNewEntryOnSourcePort,
       "rsWSDSelectServerOnSourcePort": rsWSDSelectServerOnSourcePort,
       "rsWSDRedundancyMode": rsWSDRedundancyMode,
       "rsNsdMode": rsNsdMode,
       "rsNsdWINSAddr": rsNsdWINSAddr,
       "rsWSDSyslogStatus": rsWSDSyslogStatus,
       "rsWSDSyslogAddress": rsWSDSyslogAddress,
       "rsWSDNTCheckTable": rsWSDNTCheckTable,
       "rsWSDNTCheckEntry": rsWSDNTCheckEntry,
       "rsWSDNTSerialNum": rsWSDNTSerialNum,
       "rsWSDNTFrequentCheckPeriod": rsWSDNTFrequentCheckPeriod,
       "rsWSDNTOpenSessionsWeight": rsWSDNTOpenSessionsWeight,
       "rsWSDNTIncomingTrafficWeight": rsWSDNTIncomingTrafficWeight,
       "rsWSDNTOutgoingTrafficWeight": rsWSDNTOutgoingTrafficWeight,
       "rsWSDNTRegularCheckPeriod": rsWSDNTRegularCheckPeriod,
       "rsWSDNTAvResponseWeight": rsWSDNTAvResponseWeight,
       "rsWSDNTUsersLimitWeight": rsWSDNTUsersLimitWeight,
       "rsWSDNTTCPLimitWeight": rsWSDNTTCPLimitWeight,
       "rsWSDNTRetries": rsWSDNTRetries,
       "rsWSDNTCommunity": rsWSDNTCommunity,
       "rsWSDPrivateCheckTable": rsWSDPrivateCheckTable,
       "rsWSDPrivateCheckEntry": rsWSDPrivateCheckEntry,
       "rsWSDPrivateSerialNum": rsWSDPrivateSerialNum,
       "rsWSDPrivateSpecialCheckPeriod": rsWSDPrivateSpecialCheckPeriod,
       "rsWSDPrivateExtraVar1ID": rsWSDPrivateExtraVar1ID,
       "rsWSDPrivateExtraVar1Weight": rsWSDPrivateExtraVar1Weight,
       "rsWSDPrivateExtraVar2ID": rsWSDPrivateExtraVar2ID,
       "rsWSDPrivateExtraVar2Weight": rsWSDPrivateExtraVar2Weight,
       "rsWSDPrivateRetries": rsWSDPrivateRetries,
       "rsWSDPrivateCommunity": rsWSDPrivateCommunity,
       "rsWSDPrivateExtraVar1Mode": rsWSDPrivateExtraVar1Mode,
       "rsWSDPrivateExtraVar2Mode": rsWSDPrivateExtraVar2Mode,
       "rsWSDDNSResolution": rsWSDDNSResolution,
       "rsIGTransitTimeout": rsIGTransitTimeout,
       "rsWSDUserPassword": rsWSDUserPassword,
       "rsWSDUserVersion": rsWSDUserVersion,
       "rsWSDNatStatus": rsWSDNatStatus,
       "rsWSDRedundancyTakeback": rsWSDRedundancyTakeback,
       "rsMLB": rsMLB,
       "rsCSD": rsCSD,
       "rsNWSD": rsNWSD,
       "rsWSDIfTable": rsWSDIfTable,
       "rsWSDIfEntry": rsWSDIfEntry,
       "rsWSDIfIndex": rsWSDIfIndex,
       "rsWSDIfBoardNum": rsWSDIfBoardNum,
       "rsWSDIfNetAddress": rsWSDIfNetAddress,
       "rsWSDIfStatus": rsWSDIfStatus,
       "rsWSDIfClockType": rsWSDIfClockType,
       "rsWSDIfBaudRate": rsWSDIfBaudRate,
       "rsWSDIfCost": rsWSDIfCost,
       "rsWSDIfCompression": rsWSDIfCompression,
       "rsWSDIfCompressionStatus": rsWSDIfCompressionStatus,
       "rsWSDIfCompressionRate": rsWSDIfCompressionRate,
       "rsWSDIfLATCompression": rsWSDIfLATCompression,
       "rsWSDIfCompressionType": rsWSDIfCompressionType,
       "rsWSDIfFilterMode": rsWSDIfFilterMode,
       "rsWSDIfChannelType": rsWSDIfChannelType,
       "rsWSDIfBridge": rsWSDIfBridge,
       "rsWSDHighPriorityIf": rsWSDHighPriorityIf,
       "rsWSDWanHeader": rsWSDWanHeader,
       "rsWSDDuplexMode": rsWSDDuplexMode,
       "rsWSDClientMirrorPercentage": rsWSDClientMirrorPercentage,
       "rsWSDMirrorStatus": rsWSDMirrorStatus,
       "rsWSDMirrorProtocolMode": rsWSDMirrorProtocolMode,
       "rsWSDApplicationMirrorTable": rsWSDApplicationMirrorTable,
       "rsWSDApplicationMirrorEntry": rsWSDApplicationMirrorEntry,
       "rsWSDMirrorActiveAddress": rsWSDMirrorActiveAddress,
       "rsWSDMirrorActiveStatus": rsWSDMirrorActiveStatus,
       "rsWSDClientMirrorPollingTime": rsWSDClientMirrorPollingTime,
       "rsPlatformIdentifier": rsPlatformIdentifier,
       "rsConfigurationIdentifier": rsConfigurationIdentifier,
       "rsSWPasswordStatus": rsSWPasswordStatus,
       "rsWSDFlashSize": rsWSDFlashSize,
       "rsWSDDRAMSize": rsWSDDRAMSize,
       "rsWSDVLANRedundOperStatus": rsWSDVLANRedundOperStatus,
       "rsWSDResourceUtilization": rsWSDResourceUtilization,
       "rsWSDRSResourceUtilization": rsWSDRSResourceUtilization,
       "rsWSDREResourceUtilization": rsWSDREResourceUtilization,
       "rsWSDBuildNumber": rsWSDBuildNumber,
       "rsWSDUseOneTrap": rsWSDUseOneTrap,
       "rsWSDSecuredComm": rsWSDSecuredComm,
       "rsWSDSCProtcolsTable": rsWSDSCProtcolsTable,
       "rsWSDSCProtcolsEntry": rsWSDSCProtcolsEntry,
       "rsWSDSCProtocol": rsWSDSCProtocol,
       "rsWSDSCProtocolStatus": rsWSDSCProtocolStatus,
       "rsWSDSNMPPortsTable": rsWSDSNMPPortsTable,
       "rsWSDSNMPPortsEntry": rsWSDSNMPPortsEntry,
       "rsWSDSNMPPhysicalPortNumber": rsWSDSNMPPhysicalPortNumber,
       "rsWSDSNMPPhysicalPortState": rsWSDSNMPPhysicalPortState,
       "rsWSDSNMPPhysicalPortTelnetState": rsWSDSNMPPhysicalPortTelnetState,
       "rsWSDSNMPPhysicalPortSSHState": rsWSDSNMPPhysicalPortSSHState,
       "rsWSDSNMPPhysicalPortWebState": rsWSDSNMPPhysicalPortWebState,
       "rsWSDSNMPPhysicalPortSSLState": rsWSDSNMPPhysicalPortSSLState,
       "rsBWM": rsBWM,
       "rsWSDTelnetUserTable": rsWSDTelnetUserTable,
       "rsWSDTelnetUserEntry": rsWSDTelnetUserEntry,
       "rsWSDTelnetUserName": rsWSDTelnetUserName,
       "rsWSDTelnetUserPassword": rsWSDTelnetUserPassword,
       "rsWSDTelnetUserEAddr": rsWSDTelnetUserEAddr,
       "rsWSDTelnetUserSeverity": rsWSDTelnetUserSeverity,
       "rsWSDTelnetUserStatus": rsWSDTelnetUserStatus,
       "rsWSDTelnetUserGroup": rsWSDTelnetUserGroup,
       "rsWSDTelnetUserConfigurationTraceStatus": rsWSDTelnetUserConfigurationTraceStatus,
       "rsWSDTelnetUserConfigurationTraceInf": rsWSDTelnetUserConfigurationTraceInf,
       "rsWSDTelnetUserWebAccessLevel": rsWSDTelnetUserWebAccessLevel,
       "rsWSDTelnetUserSshPublicKeyName": rsWSDTelnetUserSshPublicKeyName,
       "rsWSDTelnetParams": rsWSDTelnetParams,
       "rsWSDTelnetPort": rsWSDTelnetPort,
       "rsWSDTelnetStatus": rsWSDTelnetStatus,
       "rsSSD": rsSSD,
       "rsSSDvirtualLan": rsSSDvirtualLan,
       "rsSSDvirtualLanTable": rsSSDvirtualLanTable,
       "rsSSDvirtualLanEntry": rsSSDvirtualLanEntry,
       "rsSSDvlIfIndex": rsSSDvlIfIndex,
       "rsSSDvlProto": rsSSDvlProto,
       "rsSSDvlAutoConfigEnable": rsSSDvlAutoConfigEnable,
       "rsSSDvlStatus": rsSSDvlStatus,
       "rsSSDvlType": rsSSDvlType,
       "rsSSDvlTag": rsSSDvlTag,
       "rsSSDvlPriority": rsSSDvlPriority,
       "rsSSDvlUpCriterion": rsSSDvlUpCriterion,
       "rsSSDvlDownCriterion": rsSSDvlDownCriterion,
       "rsSSDvirtualLanPortsTable": rsSSDvirtualLanPortsTable,
       "rsSSDvirtualLanPortEntry": rsSSDvirtualLanPortEntry,
       "rsSSDvLIfIndex": rsSSDvLIfIndex,
       "rsSSDvLPortIfIndex": rsSSDvLPortIfIndex,
       "rsSSDvLPortType": rsSSDvLPortType,
       "rsSSDvLPortStatus": rsSSDvLPortStatus,
       "rsSSDvLPortTag": rsSSDvLPortTag,
       "rsSSDvLPortInterfaceGroupingState": rsSSDvLPortInterfaceGroupingState,
       "rsWSDThresholdWarnings": rsWSDThresholdWarnings,
       "rsWSDThreshTrapFloodDelay": rsWSDThreshTrapFloodDelay,
       "rsWSDCriticalTrapFloodDelay": rsWSDCriticalTrapFloodDelay,
       "rsIDS": rsIDS,
       "rsWSDLicense": rsWSDLicense,
       "rsErrMailParams": rsErrMailParams,
       "rsErrMailEnable": rsErrMailEnable,
       "rsErrMailGateway": rsErrMailGateway,
       "rsErrMailSrcAddress": rsErrMailSrcAddress,
       "rsErrMailToFieldText": rsErrMailToFieldText,
       "rsWSDWebParams": rsWSDWebParams,
       "rsWSDWebPort": rsWSDWebPort,
       "rsWSDWebStatus": rsWSDWebStatus,
       "rsWSDWebHelpLocation": rsWSDWebHelpLocation,
       "rsWSDWebSSLPort": rsWSDWebSSLPort,
       "rsWSDWebSSLStatus": rsWSDWebSSLStatus,
       "rsWSDWebSSLPrivateKeyFile": rsWSDWebSSLPrivateKeyFile,
       "rsWSDWebSSLCertificateFile": rsWSDWebSSLCertificateFile,
       "rsWSDWebSSLCaFile": rsWSDWebSSLCaFile,
       "rsWSDWebSSLCaPath": rsWSDWebSSLCaPath,
       "rsWSDWebSSLClientAuthentication": rsWSDWebSSLClientAuthentication,
       "rsWSDWebAccessLevel": rsWSDWebAccessLevel,
       "rsWSDWebSoapSupportStatus": rsWSDWebSoapSupportStatus,
       "rsWSDWebSSLWeakCiphersSupportStatus": rsWSDWebSSLWeakCiphersSupportStatus,
       "rsWSDSysParams": rsWSDSysParams,
       "rsWSDSysFlashSize": rsWSDSysFlashSize,
       "rsWSDSysUpTime": rsWSDSysUpTime,
       "rsWSDSysManagedTime": rsWSDSysManagedTime,
       "rsWSDSysManagedDate": rsWSDSysManagedDate,
       "rsWSDSysBaseMACAddress": rsWSDSysBaseMACAddress,
       "rdwrDualPowerSupplyParams": rdwrDualPowerSupplyParams,
       "rdwrPowerSupply1Status": rdwrPowerSupply1Status,
       "rdwrPowerSupply2Status": rdwrPowerSupply2Status,
       "rdwrPowerSupplyTrapStatus": rdwrPowerSupplyTrapStatus,
       "rdwrPowerSupplyStatus": rdwrPowerSupplyStatus,
       "rsWSDLicenseID": rsWSDLicenseID,
       "rsWSDSendFakeArp": rsWSDSendFakeArp,
       "rsWSDNTP": rsWSDNTP,
       "rsWSDNTPServerAddr": rsWSDNTPServerAddr,
       "rsWSDNTPInterval": rsWSDNTPInterval,
       "rsWSDNTPStatus": rsWSDNTPStatus,
       "rsWSDNTPTimeZone": rsWSDNTPTimeZone,
       "rsWSDNTPPort": rsWSDNTPPort,
       "rsWSDNTPServerUrl": rsWSDNTPServerUrl,
       "rsStatistics": rsStatistics,
       "rsPhysPortMirrorTable": rsPhysPortMirrorTable,
       "rsPhysPortMirrorEntry": rsPhysPortMirrorEntry,
       "rsPhysPortMirrorSrcInf": rsPhysPortMirrorSrcInf,
       "rsPhysPortMirrorDstPort": rsPhysPortMirrorDstPort,
       "rsPhysPortMirrorRxTx": rsPhysPortMirrorRxTx,
       "rsPhysPortMirrorRxBroadCast": rsPhysPortMirrorRxBroadCast,
       "rsPhysPortMirrorStatus": rsPhysPortMirrorStatus,
       "rsPhysPortMirrorBackupDstPort": rsPhysPortMirrorBackupDstPort,
       "rsPhysPortMirrorDstStatus": rsPhysPortMirrorDstStatus,
       "rsPhysPortMirrorBackupStatus": rsPhysPortMirrorBackupStatus,
       "rsPhysPortMirrorActiveDstPort": rsPhysPortMirrorActiveDstPort,
       "rsPhysPortMirrorMode": rsPhysPortMirrorMode,
       "rsPhysPortMirrorThreshold": rsPhysPortMirrorThreshold,
       "rsPhysPortMirrorThresholdStatus": rsPhysPortMirrorThresholdStatus,
       "rsCP": rsCP,
       "rsVWSD": rsVWSD,
       "rsVWSDDataPermissionsTable": rsVWSDDataPermissionsTable,
       "rsVWSDDataPermissionsTableEntry": rsVWSDDataPermissionsTableEntry,
       "rsVWSDUserGroup": rsVWSDUserGroup,
       "rsVWSDDataType": rsVWSDDataType,
       "rsVWSDDataItems": rsVWSDDataItems,
       "rsVWSDDataStatus": rsVWSDDataStatus,
       "rsWSDManagementPorts": rsWSDManagementPorts,
       "rsWSDManagementPortsTable": rsWSDManagementPortsTable,
       "rsWSDManagementPortsEntry": rsWSDManagementPortsEntry,
       "rsWSDPortIndex": rsWSDPortIndex,
       "rsWSDPortOperation": rsWSDPortOperation,
       "rsCCK": rsCCK,
       "rsWSDSshParams": rsWSDSshParams,
       "rsWSDSshPort": rsWSDSshPort,
       "rsWSDSshStatus": rsWSDSshStatus,
       "rsWSDSshAllowPwdAndPubKey": rsWSDSshAllowPwdAndPubKey,
       "rsWSDHttpsParams": rsWSDHttpsParams,
       "rsWSDHttpsPort": rsWSDHttpsPort,
       "rsWSDHttpsStatus": rsWSDHttpsStatus,
       "rsWSDStaticForwardingTable": rsWSDStaticForwardingTable,
       "rsWSDStaticForwardingEntry": rsWSDStaticForwardingEntry,
       "rsWSDStaticSourcePort": rsWSDStaticSourcePort,
       "rsWSDStaticDestinationPort": rsWSDStaticDestinationPort,
       "rsWSDStaticPortOperation": rsWSDStaticPortOperation,
       "rsWSDStaticStatus": rsWSDStaticStatus,
       "rsWSDStaticFailureMode": rsWSDStaticFailureMode,
       "rsWSDStaticInPort": rsWSDStaticInPort,
       "rsRadiusServer": rsRadiusServer,
       "rsRadiusMainServerAddr": rsRadiusMainServerAddr,
       "rsRadiusMainServerPort": rsRadiusMainServerPort,
       "rsRadiusMainServerSecret": rsRadiusMainServerSecret,
       "rsRadiusBackupServerAddr": rsRadiusBackupServerAddr,
       "rsRadiusBackupServerPort": rsRadiusBackupServerPort,
       "rsRadiusBackupServerSecret": rsRadiusBackupServerSecret,
       "rsAuthenticationMethod": rsAuthenticationMethod,
       "rsRadiusServerTimeout": rsRadiusServerTimeout,
       "rsRadiusServerRetries": rsRadiusServerRetries,
       "rsLockUserAfterLoginFailure": rsLockUserAfterLoginFailure,
       "rsRadiusClientLifeTime": rsRadiusClientLifeTime,
       "rsRadiusMainServerUrl": rsRadiusMainServerUrl,
       "rsRadiusBackupServerUrl": rsRadiusBackupServerUrl,
       "rspRadiusParameters": rspRadiusParameters,
       "rspRadiusPrimaryAddr": rspRadiusPrimaryAddr,
       "rspRadiusPrimaryAuthPort": rspRadiusPrimaryAuthPort,
       "rspRadiusPrimaryAccPort": rspRadiusPrimaryAccPort,
       "rspRadiusPrimarySecret": rspRadiusPrimarySecret,
       "rspRadiusAltAddr": rspRadiusAltAddr,
       "rspRadiusAltAuthPort": rspRadiusAltAuthPort,
       "rspRadiusAltAccPort": rspRadiusAltAccPort,
       "rspRadiusAltSecret": rspRadiusAltSecret,
       "rspRadiusOwnAuthPort": rspRadiusOwnAuthPort,
       "rspRadiusOwnAccPort": rspRadiusOwnAccPort,
       "rspRadiusEnable": rspRadiusEnable,
       "rspRadiusTransparentEnable": rspRadiusTransparentEnable,
       "rspRadiusRuleTable": rspRadiusRuleTable,
       "rspRadiusRuleEntry": rspRadiusRuleEntry,
       "rspRadiusattId": rspRadiusattId,
       "rspRadiusattValue": rspRadiusattValue,
       "rspRadiusNetworkName": rspRadiusNetworkName,
       "rspRadiusrowStatus": rspRadiusrowStatus,
       "rspRadiusNasTable": rspRadiusNasTable,
       "rspRadiusNasEntry": rspRadiusNasEntry,
       "rspRadiusNasIp": rspRadiusNasIp,
       "rspRadiusNasSecret": rspRadiusNasSecret,
       "rspRadiusNasrowStatus": rspRadiusNasrowStatus,
       "rspRadiusUserMirrorProtocolMode": rspRadiusUserMirrorProtocolMode,
       "rspRadiusUserMirrorPollingTime": rspRadiusUserMirrorPollingTime,
       "rspRadiusNetworkUpdatePolicy": rspRadiusNetworkUpdatePolicy,
       "rsIfTable": rsIfTable,
       "rsIfEntry": rsIfEntry,
       "rsIfIndex": rsIfIndex,
       "rsIfSpeed": rsIfSpeed,
       "rsIfDuplex": rsIfDuplex,
       "rsIfAutoNegotiate": rsIfAutoNegotiate,
       "rsIfAutoNegotiateCfg": rsIfAutoNegotiateCfg,
       "rsWSDDeviceOperationMode": rsWSDDeviceOperationMode,
       "rsWSDVersionStatus": rsWSDVersionStatus,
       "rsWSDSyslogFacility": rsWSDSyslogFacility,
       "rsACC": rsACC,
       "rsWSDPingPortsTable": rsWSDPingPortsTable,
       "rsWSDPingPortsEntry": rsWSDPingPortsEntry,
       "rsWSDPingPhysicalPortNumber": rsWSDPingPhysicalPortNumber,
       "rsWSDPingPhysicalPortState": rsWSDPingPhysicalPortState,
       "rsWSDBackupInterfaceGrouping": rsWSDBackupInterfaceGrouping,
       "rsRegistrationStatus": rsRegistrationStatus,
       "rsCT100": rsCT100,
       "rsFloatingPacketOffset": rsFloatingPacketOffset,
       "rsDnsParameters": rsDnsParameters,
       "rsDnsrParameters": rsDnsrParameters,
       "rsDnsrPrimaryAddr": rsDnsrPrimaryAddr,
       "rsDnsrAlternateAddr": rsDnsrAlternateAddr,
       "rsDnsrEnable": rsDnsrEnable,
       "rsDnsrStaticResTable": rsDnsrStaticResTable,
       "rsDnsrStaticResEntry": rsDnsrStaticResEntry,
       "rsDnsrSUrl": rsDnsrSUrl,
       "rsDnsrSIp": rsDnsrSIp,
       "rsDnsrSrowStatus": rsDnsrSrowStatus,
       "rsDnsServerParameters": rsDnsServerParameters,
       "rsDnsServerEnable": rsDnsServerEnable,
       "rsDnsServerStaticResTable": rsDnsServerStaticResTable,
       "rsDnsServerStaticResEntry": rsDnsServerStaticResEntry,
       "rsDnsServerSUrl": rsDnsServerSUrl,
       "rsDnsServerSIp": rsDnsServerSIp,
       "rsDnsServerSEnable": rsDnsServerSEnable,
       "rsDnsServerSrowStatus": rsDnsServerSrowStatus,
       "rsPrivateCheckSNMPPort": rsPrivateCheckSNMPPort,
       "rsVlanTagHandling": rsVlanTagHandling,
       "rsSmtpParameters": rsSmtpParameters,
       "rsSmtpPrimaryAddr": rsSmtpPrimaryAddr,
       "rsSmtpAlternateAddr": rsSmtpAlternateAddr,
       "rsSmtpEnable": rsSmtpEnable,
       "rsSmtpOwnAddr": rsSmtpOwnAddr,
       "rsSmtpBackupOwnAddr": rsSmtpBackupOwnAddr,
       "rsWSDSyslogUrl": rsWSDSyslogUrl,
       "rsFileSystem": rsFileSystem,
       "rsFSapplList": rsFSapplList,
       "rsFSapplEntry": rsFSapplEntry,
       "rsFSapplName": rsFSapplName,
       "rsFSapplIndex": rsFSapplIndex,
       "rsFSapplValid": rsFSapplValid,
       "rsFSapplActive": rsFSapplActive,
       "rsFSapplVersion": rsFSapplVersion,
       "rsFSapplStartup": rsFSapplStartup,
       "rsFSapplStatus": rsFSapplStatus,
       "rsFSinstallNew": rsFSinstallNew,
       "rdwrConfigurationFileTable": rdwrConfigurationFileTable,
       "rdwrConfigurationFileEntry": rdwrConfigurationFileEntry,
       "rdwrConfigurationFileApp": rdwrConfigurationFileApp,
       "rdwrConfigurationFileName": rdwrConfigurationFileName,
       "rdwrConfigurationFileRunning": rdwrConfigurationFileRunning,
       "rdwrConfigurationFileInstalled": rdwrConfigurationFileInstalled,
       "rdwrConfigurationFilePath": rdwrConfigurationFilePath,
       "rdwrConfigurationFileAction": rdwrConfigurationFileAction,
       "rdwrConfigurationFileStatus": rdwrConfigurationFileStatus,
       "rdwrDefCfg": rdwrDefCfg,
       "rdwrDefCfgIpAddress": rdwrDefCfgIpAddress,
       "rdwrDefCfgIpMask": rdwrDefCfgIpMask,
       "rdwrDefCfgPort": rdwrDefCfgPort,
       "rdwrDefCfgGateway": rdwrDefCfgGateway,
       "rdwrDefCfgUserName": rdwrDefCfgUserName,
       "rdwrDefCfgUserPassword": rdwrDefCfgUserPassword,
       "rdwrDefCfgCommunity": rdwrDefCfgCommunity,
       "rdwrApplicationFileTable": rdwrApplicationFileTable,
       "rdwrApplicationFileEntry": rdwrApplicationFileEntry,
       "rdwrApplicationFileName": rdwrApplicationFileName,
       "rdwrApplicationFileRunning": rdwrApplicationFileRunning,
       "rdwrApplicationFileSelected": rdwrApplicationFileSelected,
       "rdwrApplicationFileValid": rdwrApplicationFileValid,
       "rdwrApplicationFileStartup": rdwrApplicationFileStartup,
       "rdwrApplicationFileVersion": rdwrApplicationFileVersion,
       "rdwrApplicationFileAction": rdwrApplicationFileAction,
       "rdwrApplicationFileStatus": rdwrApplicationFileStatus,
       "rsWSDHardwareLicense": rsWSDHardwareLicense,
       "rsWSDHardwareLicenseID": rsWSDHardwareLicenseID,
       "rdwrSnmpParameters": rdwrSnmpParameters,
       "rdwrSnmpSupportedVersions": rdwrSnmpSupportedVersions,
       "rdwrSnmpSupportedVersionsAfterReset": rdwrSnmpSupportedVersionsAfterReset,
       "rdwrSnmpPort": rdwrSnmpPort,
       "rdwrSnmpStatus": rdwrSnmpStatus,
       "rdwrSnmpConfigFileFormat": rdwrSnmpConfigFileFormat,
       "rdwrSnmpErrorIndex": rdwrSnmpErrorIndex,
       "rdwrSnmpErrorStatus": rdwrSnmpErrorStatus,
       "rdwrSnmpErrorDescription": rdwrSnmpErrorDescription,
       "rdwrSnmpErrorRequestId": rdwrSnmpErrorRequestId,
       "rdwrSnmpErrorTbTable": rdwrSnmpErrorTbTable,
       "rdwrSnmpErrorTbEntry": rdwrSnmpErrorTbEntry,
       "rdwrSnmpErrorTbRequestId": rdwrSnmpErrorTbRequestId,
       "rdwrSnmpErrorTbVarId": rdwrSnmpErrorTbVarId,
       "rdwrSnmpErrorTbDescription": rdwrSnmpErrorTbDescription,
       "rdwrSnmpErrorTbErrorIndex": rdwrSnmpErrorTbErrorIndex,
       "rdwrSnmpErrorTbType": rdwrSnmpErrorTbType,
       "rdwrSnmpErrorTbStatus": rdwrSnmpErrorTbStatus,
       "rdwrSnmpErrorTbFieldInEntry": rdwrSnmpErrorTbFieldInEntry,
       "rdwrSnmpErrorTbTime": rdwrSnmpErrorTbTime,
       "rdwrSnmpErrorTbDate": rdwrSnmpErrorTbDate,
       "rdwrSnmpErrorTbTableReset": rdwrSnmpErrorTbTableReset,
       "rdwrLastConfigurationChangesTable": rdwrLastConfigurationChangesTable,
       "rdwrLastConfigurationChangesEntry": rdwrLastConfigurationChangesEntry,
       "rdwrLastConfigurationChangesID": rdwrLastConfigurationChangesID,
       "rdwrLastConfigurationChangesStatus": rdwrLastConfigurationChangesStatus,
       "rdwrLastConfigurationChangesMibOid": rdwrLastConfigurationChangesMibOid,
       "rdwrLastConfigurationChangesChangeType": rdwrLastConfigurationChangesChangeType,
       "rdwrLastConfigurationChangesKeys": rdwrLastConfigurationChangesKeys,
       "rdwrLastConfigurationChangesTableReset": rdwrLastConfigurationChangesTableReset,
       "rdwrLastConfigurationChangesTimestamp": rdwrLastConfigurationChangesTimestamp,
       "rdwrLastConfigurationChangesTime": rdwrLastConfigurationChangesTime,
       "rsWSDSyslogSourcePort": rsWSDSyslogSourcePort,
       "rsSESSION": rsSESSION,
       "rsLinkAggregationHash": rsLinkAggregationHash,
       "rsLinkAggregationL2Hash": rsLinkAggregationL2Hash,
       "rsLinkAggregationL3Hash": rsLinkAggregationL3Hash,
       "rsLinkAggregationL4Hash": rsLinkAggregationL4Hash,
       "rsScheduleTable": rsScheduleTable,
       "rsScheduleEntry": rsScheduleEntry,
       "rsScheduleName": rsScheduleName,
       "rsScheduleFrequency": rsScheduleFrequency,
       "rsScheduleTime": rsScheduleTime,
       "rsScheduleDays": rsScheduleDays,
       "rsScheduleDate": rsScheduleDate,
       "rsScheduleStatus": rsScheduleStatus,
       "rdwrFtpParameters": rdwrFtpParameters,
       "rdwrFtpPort": rdwrFtpPort,
       "rdwrFtpStatus": rdwrFtpStatus,
       "rsFullMacCompareStatus": rsFullMacCompareStatus,
       "rsREStateMonitoring": rsREStateMonitoring,
       "rsREACCReasonCounters": rsREACCReasonCounters,
       "rsACCReasonUnknownCounter": rsACCReasonUnknownCounter,
       "rsACCReasonETHBroadcastCounter": rsACCReasonETHBroadcastCounter,
       "rsACCReasonProtolcolTypeCounter": rsACCReasonProtolcolTypeCounter,
       "rsACCReasonIPVERCounter": rsACCReasonIPVERCounter,
       "rsACCReasonIPHeaderLenCounter": rsACCReasonIPHeaderLenCounter,
       "rsACCReasonIPFragmentedCounter": rsACCReasonIPFragmentedCounter,
       "rsACCReasonTTLCounter": rsACCReasonTTLCounter,
       "rsACCReasonNoFlowCounter": rsACCReasonNoFlowCounter,
       "rsACCReasonMACCFGCounter": rsACCReasonMACCFGCounter,
       "rsACCReasonSYNcookieOKCounter": rsACCReasonSYNcookieOKCounter,
       "rsACCReasonSYNcookieInvalidCounter": rsACCReasonSYNcookieInvalidCounter,
       "rsACCReasonInconsistentPktLenCounter": rsACCReasonInconsistentPktLenCounter,
       "rsACCReasonNoReasonCounter": rsACCReasonNoReasonCounter,
       "rsACCReasonFTPportCounter": rsACCReasonFTPportCounter,
       "rsACCReasonFTP227Counter": rsACCReasonFTP227Counter,
       "rsACCReasonIPLenghtCounter": rsACCReasonIPLenghtCounter,
       "rsACCReasonFINorRSTCounter": rsACCReasonFINorRSTCounter,
       "rsACCReasonClassifyCounter": rsACCReasonClassifyCounter,
       "rsACCReasonVlanReplyCounter": rsACCReasonVlanReplyCounter,
       "rsACCReasonDBindNewSYNCounter": rsACCReasonDBindNewSYNCounter,
       "rsACCReasonAllToMasterCounter": rsACCReasonAllToMasterCounter,
       "rsREStateCounters": rsREStateCounters,
       "rsREStateRXReplyCounter": rsREStateRXReplyCounter,
       "rsREStateRXRequestCounter": rsREStateRXRequestCounter,
       "rsREStateIPDAinFFTCounter": rsREStateIPDAinFFTCounter,
       "rsREStateIPDAnotFFTCounter": rsREStateIPDAnotFFTCounter,
       "rsREStateBridgeCounter": rsREStateBridgeCounter,
       "rsREStateResetCounter": rsREStateResetCounter,
       "rdwrTerminalParams": rdwrTerminalParams,
       "rdwrTerminalAliasTable": rdwrTerminalAliasTable,
       "rdwrTerminalAliasEntry": rdwrTerminalAliasEntry,
       "rdwrTerminalAliasName": rdwrTerminalAliasName,
       "rdwrTerminalUserName": rdwrTerminalUserName,
       "rdwrTerminalAliasCommand": rdwrTerminalAliasCommand,
       "rdwrTerminalAliasStatus": rdwrTerminalAliasStatus,
       "rdwrTerminalPrompt": rdwrTerminalPrompt,
       "rdwrMasterInterfaceGroupingPortsTable": rdwrMasterInterfaceGroupingPortsTable,
       "rdwrMasterInterfaceGroupingPortsEntry": rdwrMasterInterfaceGroupingPortsEntry,
       "rdwrMasterInterfaceGroupingPortNumber": rdwrMasterInterfaceGroupingPortNumber,
       "rdwrMasterInterfaceGroupingPortState": rdwrMasterInterfaceGroupingPortState,
       "rdwr5SecAvgResourceUtilization": rdwr5SecAvgResourceUtilization,
       "rdwr60SecAvgResourceUtilization": rdwr60SecAvgResourceUtilization,
       "rdwrArpWithInterfaceGroup": rdwrArpWithInterfaceGroup,
       "rdwrDBind": rdwrDBind,
       "rdwrDP": rdwrDP,
       "rsDOS": rsDOS,
       "rsSTATEFUL": rsSTATEFUL,
       "rsAPM": rsAPM,
       "rdwrIpsec": rdwrIpsec,
       "rdwrIpsecIke": rdwrIpsecIke,
       "rdwrIkeTable": rdwrIkeTable,
       "rdwrIkeEntry": rdwrIkeEntry,
       "rdwrIkeName": rdwrIkeName,
       "rdwrIkePhase1EncryptionAlg": rdwrIkePhase1EncryptionAlg,
       "rdwrIkePhase1HashAlg": rdwrIkePhase1HashAlg,
       "rdwrIkePhase1DhKeyGroup": rdwrIkePhase1DhKeyGroup,
       "rdwrIkePhase1LifeTime": rdwrIkePhase1LifeTime,
       "rdwrIkePhase1Psk": rdwrIkePhase1Psk,
       "rdwrIkePhase2Protocol": rdwrIkePhase2Protocol,
       "rdwrIkePhase2EncryptionAlg": rdwrIkePhase2EncryptionAlg,
       "rdwrIkePhase2HashAlg": rdwrIkePhase2HashAlg,
       "rdwrIkePfsKeyGroup": rdwrIkePfsKeyGroup,
       "rdwrIkeSaLifeTime": rdwrIkeSaLifeTime,
       "rdwrIkeIpCompression": rdwrIkeIpCompression,
       "rdwrIkeManualKeyMode": rdwrIkeManualKeyMode,
       "rdwrIkeEncrypKey": rdwrIkeEncrypKey,
       "rdwrIkeAuthntKey": rdwrIkeAuthntKey,
       "rdwrIkeInSpi": rdwrIkeInSpi,
       "rdwrIkeOutSpi": rdwrIkeOutSpi,
       "rdwrIkeDPDCheckInterval": rdwrIkeDPDCheckInterval,
       "rdwrIkeStatus": rdwrIkeStatus,
       "rdwrDedicatedManagementPort": rdwrDedicatedManagementPort,
       "rsGeneric": rsGeneric,
       "rdwrClientsTableStatistics": rdwrClientsTableStatistics,
       "rdwrClientsTableNumEntries": rdwrClientsTableNumEntries,
       "rdwrClientsTableNumEntries5SecAvg": rdwrClientsTableNumEntries5SecAvg,
       "rdwrClientsTableNumEntries60SecAvg": rdwrClientsTableNumEntries60SecAvg,
       "rsWSDSyslogDestinationPort": rsWSDSyslogDestinationPort,
       "rdwrPortsTagTable": rdwrPortsTagTable,
       "rdwrPortsTagEntry": rdwrPortsTagEntry,
       "rdwrPortsTagPortNumber": rdwrPortsTagPortNumber,
       "rdwrPortsTagPortInTag": rdwrPortsTagPortInTag,
       "rdwrPortsTagPortOutTag": rdwrPortsTagPortOutTag,
       "rsPhysPortMirrorThresholdUnits": rsPhysPortMirrorThresholdUnits,
       "rsPhysPortMirrorThresholdInterval": rsPhysPortMirrorThresholdInterval,
       "rsPhysPortMirrorThresholdReset": rsPhysPortMirrorThresholdReset,
       "rdwrDayLightSaving": rdwrDayLightSaving,
       "rdwrDayLightSavingBegins": rdwrDayLightSavingBegins,
       "rdwrDayLightSavingEnds": rdwrDayLightSavingEnds,
       "rdwrDayLightSavingTimeDesignations": rdwrDayLightSavingTimeDesignations,
       "rdwrDayLightSavingAdminStatus": rdwrDayLightSavingAdminStatus,
       "rdwrDayLightSavingBeginDate": rdwrDayLightSavingBeginDate,
       "rdwrDayLightSavingEndDate": rdwrDayLightSavingEndDate,
       "rdwrDayLightSavingDelta": rdwrDayLightSavingDelta,
       "rdwrCommonClientTable": rdwrCommonClientTable,
       "rdwrClientsViewTable": rdwrClientsViewTable,
       "rdwrClientsViewEntry": rdwrClientsViewEntry,
       "rdwrClientsViewIndex": rdwrClientsViewIndex,
       "rdwrClientsViewSrcAddrFrom": rdwrClientsViewSrcAddrFrom,
       "rdwrClientsViewSrcAddrTo": rdwrClientsViewSrcAddrTo,
       "rdwrClientsViewDstAddrFrom": rdwrClientsViewDstAddrFrom,
       "rdwrClientsViewDstAddrTo": rdwrClientsViewDstAddrTo,
       "rdwrClientsViewSrcPortFrom": rdwrClientsViewSrcPortFrom,
       "rdwrClientsViewSrcPortTo": rdwrClientsViewSrcPortTo,
       "rdwrClientsViewDstPortFrom": rdwrClientsViewDstPortFrom,
       "rdwrClientsViewDstPortTo": rdwrClientsViewDstPortTo,
       "rdwrClientsViewFarmAddr": rdwrClientsViewFarmAddr,
       "rdwrClientsViewServerAddr": rdwrClientsViewServerAddr,
       "rdwrClientsViewClientType": rdwrClientsViewClientType,
       "rdwrClientsViewAdminStatus": rdwrClientsViewAdminStatus,
       "rdwrClientsViewStatus": rdwrClientsViewStatus,
       "rdwrClientsViewAction": rdwrClientsViewAction,
       "rdwrClientsViewActionFeedback": rdwrClientsViewActionFeedback,
       "rdwrClientsViewVlanTag": rdwrClientsViewVlanTag,
       "rdwrClientsViewFarmName": rdwrClientsViewFarmName,
       "rdwrClientsTable": rdwrClientsTable,
       "rdwrClientsEntry": rdwrClientsEntry,
       "rdwrClientsIndex": rdwrClientsIndex,
       "rdwrClientsSourceAddr": rdwrClientsSourceAddr,
       "rdwrClientsSourcePort": rdwrClientsSourcePort,
       "rdwrClientsRequestedAddr": rdwrClientsRequestedAddr,
       "rdwrClientsRequestedPort": rdwrClientsRequestedPort,
       "rdwrClientsFarmAddr": rdwrClientsFarmAddr,
       "rdwrClientsServerAddr": rdwrClientsServerAddr,
       "rdwrClientsServerPort": rdwrClientsServerPort,
       "rdwrClientsAttachedTime": rdwrClientsAttachedTime,
       "rdwrClientsNATaddr": rdwrClientsNATaddr,
       "rdwrClientsNATPort": rdwrClientsNATPort,
       "rdwrClientsTimeToLive": rdwrClientsTimeToLive,
       "rdwrClientsClientType": rdwrClientsClientType,
       "rdwrClientsClientMode": rdwrClientsClientMode,
       "rdwrClientsUserData1": rdwrClientsUserData1,
       "rdwrClientsUserData2": rdwrClientsUserData2,
       "rdwrClientsStatus": rdwrClientsStatus,
       "rdwrClientsTypeTable": rdwrClientsTypeTable,
       "rdwrClientsTypeEntry": rdwrClientsTypeEntry,
       "rdwrClientsType": rdwrClientsType,
       "rdwrVersionIdentifierTable": rdwrVersionIdentifierTable,
       "rdwrVersionIdentifierEntry": rdwrVersionIdentifierEntry,
       "rdwrVersionIdentifierIdx": rdwrVersionIdentifierIdx,
       "rdwrVersionIdentifierBase": rdwrVersionIdentifierBase,
       "rdwrVersionIdentifierVal": rdwrVersionIdentifierVal,
       "rdwrVrrp": rdwrVrrp,
       "rdwrVrrpAdmin": rdwrVrrpAdmin,
       "rdwrVrrpOperAdvertisementInterval": rdwrVrrpOperAdvertisementInterval,
       "rdwrVrrpAssoIpV6AddrTable": rdwrVrrpAssoIpV6AddrTable,
       "rdwrVrrpAssoIpV6AddrEntry": rdwrVrrpAssoIpV6AddrEntry,
       "rdwrVrrpAssoIpV6IfIndex": rdwrVrrpAssoIpV6IfIndex,
       "rdwrVrrpAssoIpV6VrId": rdwrVrrpAssoIpV6VrId,
       "rdwrVrrpAssoIpV6Addr": rdwrVrrpAssoIpV6Addr,
       "rdwrVrrpAssoIpV6AddrRowStatus": rdwrVrrpAssoIpV6AddrRowStatus,
       "rdwrVrrpPriorityTracking": rdwrVrrpPriorityTracking,
       "rdwrWSDCommon": rdwrWSDCommon,
       "rdwrCdbParameters": rdwrCdbParameters,
       "rdwrCdbTimeStamp": rdwrCdbTimeStamp,
       "rdwrMirroring": rdwrMirroring,
       "rdwrMirroringActiveThreshold": rdwrMirroringActiveThreshold,
       "rdwrMirroringActiveSleep": rdwrMirroringActiveSleep,
       "rdwrMirroringActiveBackupThreshold": rdwrMirroringActiveBackupThreshold,
       "rdwrMirroringActiveBackupSleep": rdwrMirroringActiveBackupSleep,
       "rdwrMirroringActiveBackupHoldtime": rdwrMirroringActiveBackupHoldtime,
       "rdwrMirroringActiveBackupUpdate": rdwrMirroringActiveBackupUpdate,
       "rsWSDThroughputLicense": rsWSDThroughputLicense,
       "rsWSDThroughputLicenseID": rsWSDThroughputLicenseID,
       "rsSSLCertificate": rsSSLCertificate,
       "rsSSLCertificateDefaultValues": rsSSLCertificateDefaultValues,
       "rsSSLCertificateDefaultCommon": rsSSLCertificateDefaultCommon,
       "rsSSLCertificateDefaultLocality": rsSSLCertificateDefaultLocality,
       "rsSSLCertificateDefaultStateOrProvince": rsSSLCertificateDefaultStateOrProvince,
       "rsSSLCertificateDefaultOrganization": rsSSLCertificateDefaultOrganization,
       "rsSSLCertificateDefaultOrganizationUnit": rsSSLCertificateDefaultOrganizationUnit,
       "rsSSLCertificateDefaultCountryName": rsSSLCertificateDefaultCountryName,
       "rsSSLCertificateDefaultEMail": rsSSLCertificateDefaultEMail,
       "rsSSLCertificateTable": rsSSLCertificateTable,
       "rsSSLCertificateEntry": rsSSLCertificateEntry,
       "rsSSLCertificateName": rsSSLCertificateName,
       "rsSSLCertificateEntryType": rsSSLCertificateEntryType,
       "rsSSLCertificateKeySize": rsSSLCertificateKeySize,
       "rsSSLCertificateKeyPassphrase": rsSSLCertificateKeyPassphrase,
       "rsSSLCertificateCommon": rsSSLCertificateCommon,
       "rsSSLCertificateLocality": rsSSLCertificateLocality,
       "rsSSLCertificateStateOrProvince": rsSSLCertificateStateOrProvince,
       "rsSSLCertificateOrganization": rsSSLCertificateOrganization,
       "rsSSLCertificateOrganizationUnit": rsSSLCertificateOrganizationUnit,
       "rsSSLCertificateCountryName": rsSSLCertificateCountryName,
       "rsSSLCertificateEMail": rsSSLCertificateEMail,
       "rsSSLCertificateExpiry": rsSSLCertificateExpiry,
       "rsSSLCertificateOCSPUrl": rsSSLCertificateOCSPUrl,
       "rsSSLCertificateStatus": rsSSLCertificateStatus,
       "rsSSLCertificateRequestedValidityPeriod": rsSSLCertificateRequestedValidityPeriod,
       "rsSSLCertificateImportExport": rsSSLCertificateImportExport,
       "rsSSLCertificateImportExportEntryName": rsSSLCertificateImportExportEntryName,
       "rsSSLCertificateImportExportFileName": rsSSLCertificateImportExportFileName,
       "rsSSLCertificateImportExportPassphrase": rsSSLCertificateImportExportPassphrase,
       "rsSSLCertificateImportExportAction": rsSSLCertificateImportExportAction,
       "rdwrTemperatureCPU1Get": rdwrTemperatureCPU1Get,
       "rdwrTemperatureCPU2Get": rdwrTemperatureCPU2Get,
       "rdwrTemperatureWarningThresholdGet": rdwrTemperatureWarningThresholdGet,
       "rdwrTemperatureShutdownThresholdGet": rdwrTemperatureShutdownThresholdGet,
       "rdwrTemperatureThresholdStatusCPU1Get": rdwrTemperatureThresholdStatusCPU1Get,
       "rdwrTemperatureThresholdStatusCPU2Get": rdwrTemperatureThresholdStatusCPU2Get,
       "rndNumberOfHD": rndNumberOfHD,
       "rndSSLCardName": rndSSLCardName,
       "rndCompCardName": rndCompCardName,
       "rdwrHardDisk": rdwrHardDisk,
       "rdwrHardDiskLogging": rdwrHardDiskLogging,
       "rdwrConfigurationSync": rdwrConfigurationSync,
       "rsSystemFansTable": rsSystemFansTable,
       "rsSystemFansEntry": rsSystemFansEntry,
       "rsSystemFanIndex": rsSystemFanIndex,
       "rsSystemFansStatus": rsSystemFansStatus,
       "rdwrDualPsuStatus": rdwrDualPsuStatus,
       "rsNetPortUtilizationTable": rsNetPortUtilizationTable,
       "rsNetPortUtilizationEntry": rsNetPortUtilizationEntry,
       "rsNetPortUtilizationIndex": rsNetPortUtilizationIndex,
       "rsNetPortUtilizationEntryInUtil": rsNetPortUtilizationEntryInUtil,
       "rsNetPortUtilizationEntryOutUtil": rsNetPortUtilizationEntryOutUtil,
       "rsHWCPUTemperatureTable": rsHWCPUTemperatureTable,
       "rsHWCPUTemperatureEntry": rsHWCPUTemperatureEntry,
       "rsHWCPUTemperatureIndex": rsHWCPUTemperatureIndex,
       "rsHWCPUTemperatureValue": rsHWCPUTemperatureValue,
       "rdwrTotalIncomingTrafficPeak": rdwrTotalIncomingTrafficPeak,
       "rsHWCoreUtilizationTable": rsHWCoreUtilizationTable,
       "rsHWCoreUtilizationEntry": rsHWCoreUtilizationEntry,
       "rsHWCoreUtilizationIndex": rsHWCoreUtilizationIndex,
       "rsHWCoreUtilizationValue": rsHWCoreUtilizationValue,
       "rsManagePro": rsManagePro,
       "rsUserLockoutInterval": rsUserLockoutInterval,
       "rdwrManagmentPortsStatus": rdwrManagmentPortsStatus,
       "rdwrSyslogServerTable": rdwrSyslogServerTable,
       "rdwrSyslogServerEntry": rdwrSyslogServerEntry,
       "rdwrSyslogServerAddress": rdwrSyslogServerAddress,
       "rdwrSyslogServerStatus": rdwrSyslogServerStatus,
       "rdwrSyslogServerSrcPort": rdwrSyslogServerSrcPort,
       "rdwrSyslogServerDstPort": rdwrSyslogServerDstPort,
       "rdwrSyslogServerFacility": rdwrSyslogServerFacility,
       "rdwrSyslogServerProtocol": rdwrSyslogServerProtocol,
       "rdwrSyslogCACertificate": rdwrSyslogCACertificate,
       "rdwrSyslogServerRowStatus": rdwrSyslogServerRowStatus,
       "rdwrSyslogServerConnectionStatus": rdwrSyslogServerConnectionStatus,
       "rdwrSyslogServerNumberOfLogsInBackLog": rdwrSyslogServerNumberOfLogsInBackLog,
       "rdwrSyslogSecuritySending": rdwrSyslogSecuritySending,
       "rdwrSyslogHealthSending": rdwrSyslogHealthSending,
       "rdwrSyslogUserAuditSending": rdwrSyslogUserAuditSending,
       "rsWSDSyslogGlobalStatus": rsWSDSyslogGlobalStatus,
       "rsSendPortUnreachableStatus": rsSendPortUnreachableStatus,
       "rsTacacsServer": rsTacacsServer,
       "rsTacacsPrimaryServerAddr": rsTacacsPrimaryServerAddr,
       "rsTacacsPrimaryServerSecret": rsTacacsPrimaryServerSecret,
       "rsTacacsPrimaryServerPort": rsTacacsPrimaryServerPort,
       "rsTacacsSecondaryServerAddr": rsTacacsSecondaryServerAddr,
       "rsTacacsSecondaryServerSecret": rsTacacsSecondaryServerSecret,
       "rsTacacsSecondaryServerPort": rsTacacsSecondaryServerPort,
       "rsTacacsServerRetries": rsTacacsServerRetries,
       "rsTacacsServerTimeout": rsTacacsServerTimeout,
       "rsTacacsCommandLoggingStatus": rsTacacsCommandLoggingStatus,
       "rsTacacsCommandAuthorizationStatus": rsTacacsCommandAuthorizationStatus,
       "rsTacacsClientAging": rsTacacsClientAging,
       "rsWSDResourceUtilizationInstance1": rsWSDResourceUtilizationInstance1,
       "rsWSDREResourceUtilizationInstance1": rsWSDREResourceUtilizationInstance1,
       "rsWSDRSResourceUtilizationInstance1": rsWSDRSResourceUtilizationInstance1,
       "rdwr5SecAvgResourceUtilizationInstance1": rdwr5SecAvgResourceUtilizationInstance1,
       "rdwr60SecAvgResourceUtilizationInstance1": rdwr60SecAvgResourceUtilizationInstance1,
       "rndMidLevelManagement": rndMidLevelManagement,
       "rndAlarmOptions": rndAlarmOptions,
       "rndAlarmEnabling": rndAlarmEnabling,
       "rndAlarmInterval": rndAlarmInterval,
       "rndMonitoredElementsTable": rndMonitoredElementsTable,
       "rndMonitoredElementEntry": rndMonitoredElementEntry,
       "rndMonitoredElementAddress": rndMonitoredElementAddress,
       "rndMonitoredElementCommunity": rndMonitoredElementCommunity,
       "rndMonitoredElementLabel": rndMonitoredElementLabel,
       "rndDefaultPollingInterval": rndDefaultPollingInterval,
       "rndDefaultLogFile": rndDefaultLogFile,
       "rndMonitoredElementStatus": rndMonitoredElementStatus,
       "rndMonitoringTable": rndMonitoringTable,
       "rndMonitoringEntry": rndMonitoringEntry,
       "rndMonitoredElement": rndMonitoredElement,
       "rndMonitoredObjectInstanceLabel": rndMonitoredObjectInstanceLabel,
       "rndMonitoredObjectName": rndMonitoredObjectName,
       "rndMonitoredObjectIdentifier": rndMonitoredObjectIdentifier,
       "rndMonitoredObjectInstance": rndMonitoredObjectInstance,
       "rndMonitoredObjectSyntax": rndMonitoredObjectSyntax,
       "rndMonitoringInterval": rndMonitoringInterval,
       "rndAlarmMaxTreshold": rndAlarmMaxTreshold,
       "rndAlarmMinTreshold": rndAlarmMinTreshold,
       "rndMonitoringLogfile": rndMonitoringLogfile,
       "rndMonitoringEntryStatus": rndMonitoringEntryStatus,
       "rndMibFilesTable": rndMibFilesTable,
       "rndMibFileEntry": rndMibFileEntry,
       "rndMibFileIndex": rndMibFileIndex,
       "rndMibFilePath": rndMibFilePath,
       "rndMibFileRefresh": rndMibFileRefresh,
       "rndMibFileEntryStatus": rndMibFileEntryStatus,
       "rndHardwareConfiguration": rndHardwareConfiguration,
       "rndEraseSimulatedConfiguration": rndEraseSimulatedConfiguration,
       "rndDeleteValuesTable": rndDeleteValuesTable,
       "rndDeleteValuesEntry": rndDeleteValuesEntry,
       "rndRowStatusVariableName": rndRowStatusVariableName,
       "rndRowStatusObjectId": rndRowStatusObjectId,
       "rndRowDeleteValue": rndRowDeleteValue,
       "rndDeleteValueEntryStatus": rndDeleteValueEntryStatus,
       "rndVisionDriver": rndVisionDriver,
       "rndVisionDriverActiveName": rndVisionDriverActiveName,
       "rndVisionDriverRestoreFromBackup": rndVisionDriverRestoreFromBackup,
       "rndSmartFan": rndSmartFan,
       "rndSmartFanStatus": rndSmartFanStatus,
       "rsIpZeroHopRouting": rsIpZeroHopRouting,
       "rsIpZhrGeneralStatus": rsIpZhrGeneralStatus,
       "rsIpZhrAgingTimeout": rsIpZhrAgingTimeout,
       "rsIpZhrStatusTable": rsIpZhrStatusTable,
       "rsIpZhrStatusEntry": rsIpZhrStatusEntry,
       "rsIpZhrStatusIpIntf": rsIpZhrStatusIpIntf,
       "rsIpZhrAdminStatus": rsIpZhrAdminStatus,
       "rsIpZhrVirtAddressTable": rsIpZhrVirtAddressTable,
       "rsIpZhrVirtAddressEntry": rsIpZhrVirtAddressEntry,
       "rsIpZhrVirtAddressIpIntf": rsIpZhrVirtAddressIpIntf,
       "rsIpZhrVirtAddressTo": rsIpZhrVirtAddressTo,
       "rsIpZhrVirtAddressFrom": rsIpZhrVirtAddressFrom,
       "rsIpZhrVirtAddressStatus": rsIpZhrVirtAddressStatus,
       "rsIpZhrConnectionsTable": rsIpZhrConnectionsTable,
       "rsIpZhrConnectionEntry": rsIpZhrConnectionEntry,
       "rsIpZhrConnectionIpIntf": rsIpZhrConnectionIpIntf,
       "rsIpZhrConnectionSrcIp": rsIpZhrConnectionSrcIp,
       "rsIpZhrConnectionDestIp": rsIpZhrConnectionDestIp,
       "rsIpZhrConnectionVirtualIp": rsIpZhrConnectionVirtualIp,
       "rsIpZhrConnectionType": rsIpZhrConnectionType,
       "rsIpZhrConnectionAge": rsIpZhrConnectionAge,
       "rsIpZhrConnectionStatus": rsIpZhrConnectionStatus}
)
