# SNMP MIB module (ROSMGMT-OSPFV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-OSPFV2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:07 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(rosMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "rosMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rosMgmtOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47)
)
if mibBuilder.loadTexts:
    rosMgmtOspf.setRevisions(
        ("2020-05-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ProcessID(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-0"


class AreaID(TextualConvention, IpAddress):
    status = "current"
    displayHint = "1d.1d.1d.1d"


class RouterID(TextualConvention, IpAddress):
    status = "current"
    displayHint = "1d.1d.1d.1d"


class Metric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class Status(TextualConvention, Integer32):
    status = "current"
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



class PositiveInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class UpToMaxAge(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class DesignatedRouterPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class OspfAuthenticationType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("simplePassword", 1),
          ("md5", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RosMgmtOspfNotifications_ObjectIdentity = ObjectIdentity
rosMgmtOspfNotifications = _RosMgmtOspfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1)
)
_RosMgmtOspfTraps_ObjectIdentity = ObjectIdentity
rosMgmtOspfTraps = _RosMgmtOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0)
)
_RosMgmtOspfTrapControlTable_Object = MibTable
rosMgmtOspfTrapControlTable = _RosMgmtOspfTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOspfTrapControlTable.setStatus("current")
_RosMgmtOspfTrapControlEntry_Object = MibTableRow
rosMgmtOspfTrapControlEntry = _RosMgmtOspfTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 1, 1)
)
rosMgmtOspfTrapControlEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfTrapControlEntry.setStatus("current")


class _RosMgmtOspfSetTrap_Type(EnableVar):
    """Custom type rosMgmtOspfSetTrap based on EnableVar"""
    defaultValue = 2


_RosMgmtOspfSetTrap_Type.__name__ = "EnableVar"
_RosMgmtOspfSetTrap_Object = MibTableColumn
rosMgmtOspfSetTrap = _RosMgmtOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 1, 1, 1),
    _RosMgmtOspfSetTrap_Type()
)
rosMgmtOspfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOspfSetTrap.setStatus("current")


class _RosMgmtOspfConfigErrorType_Type(Integer32):
    """Custom type rosMgmtOspfConfigErrorType based on Integer32"""
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
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10))
    )


_RosMgmtOspfConfigErrorType_Type.__name__ = "Integer32"
_RosMgmtOspfConfigErrorType_Object = MibTableColumn
rosMgmtOspfConfigErrorType = _RosMgmtOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 1, 1, 2),
    _RosMgmtOspfConfigErrorType_Type()
)
rosMgmtOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfConfigErrorType.setStatus("current")


class _RosMgmtOspfPacketType_Type(Integer32):
    """Custom type rosMgmtOspfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5))
    )


_RosMgmtOspfPacketType_Type.__name__ = "Integer32"
_RosMgmtOspfPacketType_Object = MibTableColumn
rosMgmtOspfPacketType = _RosMgmtOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 1, 1, 3),
    _RosMgmtOspfPacketType_Type()
)
rosMgmtOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfPacketType.setStatus("current")
_RosMgmtOspfPacketSrc_Type = IpAddress
_RosMgmtOspfPacketSrc_Object = MibTableColumn
rosMgmtOspfPacketSrc = _RosMgmtOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 1, 1, 4),
    _RosMgmtOspfPacketSrc_Type()
)
rosMgmtOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfPacketSrc.setStatus("current")
_RosMgmtOspfObjects_ObjectIdentity = ObjectIdentity
rosMgmtOspfObjects = _RosMgmtOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2)
)
_RosMgmtOspfGlobalTable_Object = MibTable
rosMgmtOspfGlobalTable = _RosMgmtOspfGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOspfGlobalTable.setStatus("current")
_RosMgmtOspfGlobalEntry_Object = MibTableRow
rosMgmtOspfGlobalEntry = _RosMgmtOspfGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1)
)
rosMgmtOspfGlobalEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfGlobalEntry.setStatus("current")
_RosMgmtOspfProcessId_Type = ProcessID
_RosMgmtOspfProcessId_Object = MibTableColumn
rosMgmtOspfProcessId = _RosMgmtOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 1),
    _RosMgmtOspfProcessId_Type()
)
rosMgmtOspfProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfProcessId.setStatus("current")
_RosMgmtOspfRouterId_Type = RouterID
_RosMgmtOspfRouterId_Object = MibTableColumn
rosMgmtOspfRouterId = _RosMgmtOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 2),
    _RosMgmtOspfRouterId_Type()
)
rosMgmtOspfRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRouterId.setStatus("current")


class _RosMgmtOspfAdminStat_Type(EnableVar):
    """Custom type rosMgmtOspfAdminStat based on EnableVar"""
    defaultValue = 2


_RosMgmtOspfAdminStat_Type.__name__ = "EnableVar"
_RosMgmtOspfAdminStat_Object = MibTableColumn
rosMgmtOspfAdminStat = _RosMgmtOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 3),
    _RosMgmtOspfAdminStat_Type()
)
rosMgmtOspfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAdminStat.setStatus("current")


class _RosMgmtOspfVersionNumber_Type(Integer32):
    """Custom type rosMgmtOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_RosMgmtOspfVersionNumber_Type.__name__ = "Integer32"
_RosMgmtOspfVersionNumber_Object = MibTableColumn
rosMgmtOspfVersionNumber = _RosMgmtOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 4),
    _RosMgmtOspfVersionNumber_Type()
)
rosMgmtOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVersionNumber.setStatus("current")
_RosMgmtOspfAreaBdrRtrStatus_Type = TruthValue
_RosMgmtOspfAreaBdrRtrStatus_Object = MibTableColumn
rosMgmtOspfAreaBdrRtrStatus = _RosMgmtOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 5),
    _RosMgmtOspfAreaBdrRtrStatus_Type()
)
rosMgmtOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaBdrRtrStatus.setStatus("current")
_RosMgmtOspfASBdrRtrStatus_Type = TruthValue
_RosMgmtOspfASBdrRtrStatus_Object = MibTableColumn
rosMgmtOspfASBdrRtrStatus = _RosMgmtOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 6),
    _RosMgmtOspfASBdrRtrStatus_Type()
)
rosMgmtOspfASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfASBdrRtrStatus.setStatus("current")
_RosMgmtOspfExternLsaCount_Type = Gauge32
_RosMgmtOspfExternLsaCount_Object = MibTableColumn
rosMgmtOspfExternLsaCount = _RosMgmtOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 7),
    _RosMgmtOspfExternLsaCount_Type()
)
rosMgmtOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfExternLsaCount.setStatus("current")
_RosMgmtOspfExternLsaCksumSum_Type = Integer32
_RosMgmtOspfExternLsaCksumSum_Object = MibTableColumn
rosMgmtOspfExternLsaCksumSum = _RosMgmtOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 8),
    _RosMgmtOspfExternLsaCksumSum_Type()
)
rosMgmtOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfExternLsaCksumSum.setStatus("current")
_RosMgmtOspfOriginateNewLsas_Type = Counter32
_RosMgmtOspfOriginateNewLsas_Object = MibTableColumn
rosMgmtOspfOriginateNewLsas = _RosMgmtOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 9),
    _RosMgmtOspfOriginateNewLsas_Type()
)
rosMgmtOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfOriginateNewLsas.setStatus("current")
_RosMgmtOspfRxNewLsas_Type = Counter32
_RosMgmtOspfRxNewLsas_Object = MibTableColumn
rosMgmtOspfRxNewLsas = _RosMgmtOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 10),
    _RosMgmtOspfRxNewLsas_Type()
)
rosMgmtOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRxNewLsas.setStatus("current")


class _RosMgmtOspfExtLsdbLimit_Type(Integer32):
    """Custom type rosMgmtOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RosMgmtOspfExtLsdbLimit_Type.__name__ = "Integer32"
_RosMgmtOspfExtLsdbLimit_Object = MibTableColumn
rosMgmtOspfExtLsdbLimit = _RosMgmtOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 11),
    _RosMgmtOspfExtLsdbLimit_Type()
)
rosMgmtOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfExtLsdbLimit.setStatus("current")


class _RosMgmtOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type rosMgmtOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_RosMgmtOspfExitOverflowInterval_Type.__name__ = "PositiveInteger"
_RosMgmtOspfExitOverflowInterval_Object = MibTableColumn
rosMgmtOspfExitOverflowInterval = _RosMgmtOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 12),
    _RosMgmtOspfExitOverflowInterval_Type()
)
rosMgmtOspfExitOverflowInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfExitOverflowInterval.setStatus("current")


class _RosMgmtOspfReferenceBandwidth_Type(Unsigned32):
    """Custom type rosMgmtOspfReferenceBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4296967),
    )


_RosMgmtOspfReferenceBandwidth_Type.__name__ = "Unsigned32"
_RosMgmtOspfReferenceBandwidth_Object = MibTableColumn
rosMgmtOspfReferenceBandwidth = _RosMgmtOspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 13),
    _RosMgmtOspfReferenceBandwidth_Type()
)
rosMgmtOspfReferenceBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfReferenceBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfReferenceBandwidth.setUnits("millionbits per second")
_RosMgmtOspfAsLsaCount_Type = Gauge32
_RosMgmtOspfAsLsaCount_Object = MibTableColumn
rosMgmtOspfAsLsaCount = _RosMgmtOspfAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 14),
    _RosMgmtOspfAsLsaCount_Type()
)
rosMgmtOspfAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsaCount.setStatus("current")
_RosMgmtOspfAsLsaCksumSum_Type = Unsigned32
_RosMgmtOspfAsLsaCksumSum_Object = MibTableColumn
rosMgmtOspfAsLsaCksumSum = _RosMgmtOspfAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 15),
    _RosMgmtOspfAsLsaCksumSum_Type()
)
rosMgmtOspfAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsaCksumSum.setStatus("current")
_RosMgmtOspfStubRouterSupport_Type = TruthValue
_RosMgmtOspfStubRouterSupport_Object = MibTableColumn
rosMgmtOspfStubRouterSupport = _RosMgmtOspfStubRouterSupport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 16),
    _RosMgmtOspfStubRouterSupport_Type()
)
rosMgmtOspfStubRouterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfStubRouterSupport.setStatus("current")


class _RosMgmtOspfStubRouterAdvertisement_Type(Integer32):
    """Custom type rosMgmtOspfStubRouterAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotAdvertise", 1),
          ("advertise", 2))
    )


_RosMgmtOspfStubRouterAdvertisement_Type.__name__ = "Integer32"
_RosMgmtOspfStubRouterAdvertisement_Object = MibTableColumn
rosMgmtOspfStubRouterAdvertisement = _RosMgmtOspfStubRouterAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 17),
    _RosMgmtOspfStubRouterAdvertisement_Type()
)
rosMgmtOspfStubRouterAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfStubRouterAdvertisement.setStatus("current")


class _RosMgmtOspfAdminDistance_Type(Integer32):
    """Custom type rosMgmtOspfAdminDistance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RosMgmtOspfAdminDistance_Type.__name__ = "Integer32"
_RosMgmtOspfAdminDistance_Object = MibTableColumn
rosMgmtOspfAdminDistance = _RosMgmtOspfAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 18),
    _RosMgmtOspfAdminDistance_Type()
)
rosMgmtOspfAdminDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAdminDistance.setStatus("current")


class _RosMgmtOspfSpfInterval_Type(Integer32):
    """Custom type rosMgmtOspfSpfInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RosMgmtOspfSpfInterval_Type.__name__ = "Integer32"
_RosMgmtOspfSpfInterval_Object = MibTableColumn
rosMgmtOspfSpfInterval = _RosMgmtOspfSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 19),
    _RosMgmtOspfSpfInterval_Type()
)
rosMgmtOspfSpfInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfSpfInterval.setStatus("current")


class _RosMgmtOspfReset_Type(Integer32):
    """Custom type rosMgmtOspfReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("general", 1),
          ("gr", 2))
    )


_RosMgmtOspfReset_Type.__name__ = "Integer32"
_RosMgmtOspfReset_Object = MibTableColumn
rosMgmtOspfReset = _RosMgmtOspfReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 20),
    _RosMgmtOspfReset_Type()
)
rosMgmtOspfReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfReset.setStatus("current")


class _RosMgmtOspfExportMetric_Type(Integer32):
    """Custom type rosMgmtOspfExportMetric based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RosMgmtOspfExportMetric_Type.__name__ = "Integer32"
_RosMgmtOspfExportMetric_Object = MibTableColumn
rosMgmtOspfExportMetric = _RosMgmtOspfExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 21),
    _RosMgmtOspfExportMetric_Type()
)
rosMgmtOspfExportMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfExportMetric.setStatus("current")


class _RosMgmtOspfExportTag_Type(Integer32):
    """Custom type rosMgmtOspfExportTag based on Integer32"""
    defaultValue = 0


_RosMgmtOspfExportTag_Type.__name__ = "Integer32"
_RosMgmtOspfExportTag_Object = MibTableColumn
rosMgmtOspfExportTag = _RosMgmtOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 22),
    _RosMgmtOspfExportTag_Type()
)
rosMgmtOspfExportTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfExportTag.setStatus("current")


class _RosMgmtOspfExportType_Type(Integer32):
    """Custom type rosMgmtOspfExportType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_RosMgmtOspfExportType_Type.__name__ = "Integer32"
_RosMgmtOspfExportType_Object = MibTableColumn
rosMgmtOspfExportType = _RosMgmtOspfExportType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 23),
    _RosMgmtOspfExportType_Type()
)
rosMgmtOspfExportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfExportType.setStatus("current")
_RosMgmtOspfNetCounts_Type = Integer32
_RosMgmtOspfNetCounts_Object = MibTableColumn
rosMgmtOspfNetCounts = _RosMgmtOspfNetCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 24),
    _RosMgmtOspfNetCounts_Type()
)
rosMgmtOspfNetCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNetCounts.setStatus("current")
_RosMgmtOspfAreaCounts_Type = Integer32
_RosMgmtOspfAreaCounts_Object = MibTableColumn
rosMgmtOspfAreaCounts = _RosMgmtOspfAreaCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 25),
    _RosMgmtOspfAreaCounts_Type()
)
rosMgmtOspfAreaCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaCounts.setStatus("current")
_RosMgmtOspfNssaAreaCounts_Type = Integer32
_RosMgmtOspfNssaAreaCounts_Object = MibTableColumn
rosMgmtOspfNssaAreaCounts = _RosMgmtOspfNssaAreaCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 26),
    _RosMgmtOspfNssaAreaCounts_Type()
)
rosMgmtOspfNssaAreaCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNssaAreaCounts.setStatus("current")
_RosMgmtOspfSpfCounts_Type = Integer32
_RosMgmtOspfSpfCounts_Object = MibTableColumn
rosMgmtOspfSpfCounts = _RosMgmtOspfSpfCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 27),
    _RosMgmtOspfSpfCounts_Type()
)
rosMgmtOspfSpfCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfSpfCounts.setStatus("current")
_RosMgmtOspfGlobalStatus_Type = RowStatus
_RosMgmtOspfGlobalStatus_Object = MibTableColumn
rosMgmtOspfGlobalStatus = _RosMgmtOspfGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 28),
    _RosMgmtOspfGlobalStatus_Type()
)
rosMgmtOspfGlobalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfGlobalStatus.setStatus("current")


class _RosMgmtOspfRedistributeRouteLimit_Type(Integer32):
    """Custom type rosMgmtOspfRedistributeRouteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfRedistributeRouteLimit_Type.__name__ = "Integer32"
_RosMgmtOspfRedistributeRouteLimit_Object = MibTableColumn
rosMgmtOspfRedistributeRouteLimit = _RosMgmtOspfRedistributeRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 29),
    _RosMgmtOspfRedistributeRouteLimit_Type()
)
rosMgmtOspfRedistributeRouteLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeRouteLimit.setStatus("current")


class _RosMgmtOspfDistanceIntra_Type(Integer32):
    """Custom type rosMgmtOspfDistanceIntra based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RosMgmtOspfDistanceIntra_Type.__name__ = "Integer32"
_RosMgmtOspfDistanceIntra_Object = MibTableColumn
rosMgmtOspfDistanceIntra = _RosMgmtOspfDistanceIntra_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 30),
    _RosMgmtOspfDistanceIntra_Type()
)
rosMgmtOspfDistanceIntra.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistanceIntra.setStatus("current")


class _RosMgmtOspfDistanceInter_Type(Integer32):
    """Custom type rosMgmtOspfDistanceInter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RosMgmtOspfDistanceInter_Type.__name__ = "Integer32"
_RosMgmtOspfDistanceInter_Object = MibTableColumn
rosMgmtOspfDistanceInter = _RosMgmtOspfDistanceInter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 31),
    _RosMgmtOspfDistanceInter_Type()
)
rosMgmtOspfDistanceInter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistanceInter.setStatus("current")


class _RosMgmtOspfDistanceExtern_Type(Integer32):
    """Custom type rosMgmtOspfDistanceExtern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RosMgmtOspfDistanceExtern_Type.__name__ = "Integer32"
_RosMgmtOspfDistanceExtern_Object = MibTableColumn
rosMgmtOspfDistanceExtern = _RosMgmtOspfDistanceExtern_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 32),
    _RosMgmtOspfDistanceExtern_Type()
)
rosMgmtOspfDistanceExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistanceExtern.setStatus("current")


class _RosMgmtOspfRfc1583Compatible_Type(TruthValue):
    """Custom type rosMgmtOspfRfc1583Compatible based on TruthValue"""
    defaultValue = 1


_RosMgmtOspfRfc1583Compatible_Type.__name__ = "TruthValue"
_RosMgmtOspfRfc1583Compatible_Object = MibTableColumn
rosMgmtOspfRfc1583Compatible = _RosMgmtOspfRfc1583Compatible_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 33),
    _RosMgmtOspfRfc1583Compatible_Type()
)
rosMgmtOspfRfc1583Compatible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRfc1583Compatible.setStatus("current")


class _RosMgmtOspfSpfHode_Type(Integer32):
    """Custom type rosMgmtOspfSpfHode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RosMgmtOspfSpfHode_Type.__name__ = "Integer32"
_RosMgmtOspfSpfHode_Object = MibTableColumn
rosMgmtOspfSpfHode = _RosMgmtOspfSpfHode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 34),
    _RosMgmtOspfSpfHode_Type()
)
rosMgmtOspfSpfHode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfSpfHode.setStatus("current")


class _RosMgmtOspfBfdAllItfs_Type(TruthValue):
    """Custom type rosMgmtOspfBfdAllItfs based on TruthValue"""
    defaultValue = 2


_RosMgmtOspfBfdAllItfs_Type.__name__ = "TruthValue"
_RosMgmtOspfBfdAllItfs_Object = MibTableColumn
rosMgmtOspfBfdAllItfs = _RosMgmtOspfBfdAllItfs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 35),
    _RosMgmtOspfBfdAllItfs_Type()
)
rosMgmtOspfBfdAllItfs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfBfdAllItfs.setStatus("current")


class _RosMgmtOspfOpaqueCapability_Type(TruthValue):
    """Custom type rosMgmtOspfOpaqueCapability based on TruthValue"""
    defaultValue = 2


_RosMgmtOspfOpaqueCapability_Type.__name__ = "TruthValue"
_RosMgmtOspfOpaqueCapability_Object = MibTableColumn
rosMgmtOspfOpaqueCapability = _RosMgmtOspfOpaqueCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 36),
    _RosMgmtOspfOpaqueCapability_Type()
)
rosMgmtOspfOpaqueCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfOpaqueCapability.setStatus("current")


class _RosMgmtOspfTECapability_Type(TruthValue):
    """Custom type rosMgmtOspfTECapability based on TruthValue"""
    defaultValue = 2


_RosMgmtOspfTECapability_Type.__name__ = "TruthValue"
_RosMgmtOspfTECapability_Object = MibTableColumn
rosMgmtOspfTECapability = _RosMgmtOspfTECapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 37),
    _RosMgmtOspfTECapability_Type()
)
rosMgmtOspfTECapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfTECapability.setStatus("current")
_RosMgmtOspfTEAreaID_Type = IpAddress
_RosMgmtOspfTEAreaID_Object = MibTableColumn
rosMgmtOspfTEAreaID = _RosMgmtOspfTEAreaID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 38),
    _RosMgmtOspfTEAreaID_Type()
)
rosMgmtOspfTEAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfTEAreaID.setStatus("deprecated")
_RosMgmtOspfTERouterId_Type = RouterID
_RosMgmtOspfTERouterId_Object = MibTableColumn
rosMgmtOspfTERouterId = _RosMgmtOspfTERouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 39),
    _RosMgmtOspfTERouterId_Type()
)
rosMgmtOspfTERouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfTERouterId.setStatus("current")


class _RosMgmtOspfGRCapability_Type(Integer32):
    """Custom type rosMgmtOspfGRCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("graceful", 1),
          ("signaling", 2),
          ("never", 3))
    )


_RosMgmtOspfGRCapability_Type.__name__ = "Integer32"
_RosMgmtOspfGRCapability_Object = MibTableColumn
rosMgmtOspfGRCapability = _RosMgmtOspfGRCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 40),
    _RosMgmtOspfGRCapability_Type()
)
rosMgmtOspfGRCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfGRCapability.setStatus("current")


class _RosMgmtOspfGRPeriod_Type(Integer32):
    """Custom type rosMgmtOspfGRPeriod based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_RosMgmtOspfGRPeriod_Type.__name__ = "Integer32"
_RosMgmtOspfGRPeriod_Object = MibTableColumn
rosMgmtOspfGRPeriod = _RosMgmtOspfGRPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 41),
    _RosMgmtOspfGRPeriod_Type()
)
rosMgmtOspfGRPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfGRPeriod.setStatus("current")


class _RosMgmtOspfGRHelper_Type(Integer32):
    """Custom type rosMgmtOspfGRHelper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("never", 1),
          ("plannedonly", 2))
    )


_RosMgmtOspfGRHelper_Type.__name__ = "Integer32"
_RosMgmtOspfGRHelper_Object = MibTableColumn
rosMgmtOspfGRHelper = _RosMgmtOspfGRHelper_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 42),
    _RosMgmtOspfGRHelper_Type()
)
rosMgmtOspfGRHelper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfGRHelper.setStatus("current")


class _RosMgmtOspfGRHelperMaxPeriod_Type(Integer32):
    """Custom type rosMgmtOspfGRHelperMaxPeriod based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_RosMgmtOspfGRHelperMaxPeriod_Type.__name__ = "Integer32"
_RosMgmtOspfGRHelperMaxPeriod_Object = MibTableColumn
rosMgmtOspfGRHelperMaxPeriod = _RosMgmtOspfGRHelperMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 43),
    _RosMgmtOspfGRHelperMaxPeriod_Type()
)
rosMgmtOspfGRHelperMaxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfGRHelperMaxPeriod.setStatus("current")


class _RosMgmtOspfMaximumLoadBalancing_Type(Integer32):
    """Custom type rosMgmtOspfMaximumLoadBalancing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RosMgmtOspfMaximumLoadBalancing_Type.__name__ = "Integer32"
_RosMgmtOspfMaximumLoadBalancing_Object = MibTableColumn
rosMgmtOspfMaximumLoadBalancing = _RosMgmtOspfMaximumLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 44),
    _RosMgmtOspfMaximumLoadBalancing_Type()
)
rosMgmtOspfMaximumLoadBalancing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfMaximumLoadBalancing.setStatus("current")


class _RosMgmtOspfMaxMetric_Type(Integer32):
    """Custom type rosMgmtOspfMaxMetric based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RosMgmtOspfMaxMetric_Type.__name__ = "Integer32"
_RosMgmtOspfMaxMetric_Object = MibTableColumn
rosMgmtOspfMaxMetric = _RosMgmtOspfMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 45),
    _RosMgmtOspfMaxMetric_Type()
)
rosMgmtOspfMaxMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfMaxMetric.setStatus("current")


class _RosMgmtOspfMaxMetricType_Type(Integer32):
    """Custom type rosMgmtOspfMaxMetricType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RosMgmtOspfMaxMetricType_Type.__name__ = "Integer32"
_RosMgmtOspfMaxMetricType_Object = MibTableColumn
rosMgmtOspfMaxMetricType = _RosMgmtOspfMaxMetricType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 46),
    _RosMgmtOspfMaxMetricType_Type()
)
rosMgmtOspfMaxMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfMaxMetricType.setStatus("current")


class _RosMgmtOspfMaxMetricTime_Type(Integer32):
    """Custom type rosMgmtOspfMaxMetricTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(90, 86400),
    )


_RosMgmtOspfMaxMetricTime_Type.__name__ = "Integer32"
_RosMgmtOspfMaxMetricTime_Object = MibTableColumn
rosMgmtOspfMaxMetricTime = _RosMgmtOspfMaxMetricTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 47),
    _RosMgmtOspfMaxMetricTime_Type()
)
rosMgmtOspfMaxMetricTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfMaxMetricTime.setStatus("current")


class _RosMgmtOspfMaxMetricTypeStartup_Type(Integer32):
    """Custom type rosMgmtOspfMaxMetricTypeStartup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RosMgmtOspfMaxMetricTypeStartup_Type.__name__ = "Integer32"
_RosMgmtOspfMaxMetricTypeStartup_Object = MibTableColumn
rosMgmtOspfMaxMetricTypeStartup = _RosMgmtOspfMaxMetricTypeStartup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 48),
    _RosMgmtOspfMaxMetricTypeStartup_Type()
)
rosMgmtOspfMaxMetricTypeStartup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfMaxMetricTypeStartup.setStatus("current")


class _RosMgmtOspfLsdbOverflowLimit_Type(Integer32):
    """Custom type rosMgmtOspfLsdbOverflowLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RosMgmtOspfLsdbOverflowLimit_Type.__name__ = "Integer32"
_RosMgmtOspfLsdbOverflowLimit_Object = MibTableColumn
rosMgmtOspfLsdbOverflowLimit = _RosMgmtOspfLsdbOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 49),
    _RosMgmtOspfLsdbOverflowLimit_Type()
)
rosMgmtOspfLsdbOverflowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbOverflowLimit.setStatus("current")


class _RosMgmtOspfTrafficAdjustType_Type(Integer32):
    """Custom type rosMgmtOspfTrafficAdjustType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("shortcut", 1),
          ("fa", 2))
    )


_RosMgmtOspfTrafficAdjustType_Type.__name__ = "Integer32"
_RosMgmtOspfTrafficAdjustType_Object = MibTableColumn
rosMgmtOspfTrafficAdjustType = _RosMgmtOspfTrafficAdjustType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 50),
    _RosMgmtOspfTrafficAdjustType_Type()
)
rosMgmtOspfTrafficAdjustType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfTrafficAdjustType.setStatus("current")
_RosMgmtOspfRouteTagValue_Type = Unsigned32
_RosMgmtOspfRouteTagValue_Object = MibTableColumn
rosMgmtOspfRouteTagValue = _RosMgmtOspfRouteTagValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 51),
    _RosMgmtOspfRouteTagValue_Type()
)
rosMgmtOspfRouteTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteTagValue.setStatus("current")
_RosMgmtOspfRouteTagCheckDisable_Type = TruthValue
_RosMgmtOspfRouteTagCheckDisable_Object = MibTableColumn
rosMgmtOspfRouteTagCheckDisable = _RosMgmtOspfRouteTagCheckDisable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 52),
    _RosMgmtOspfRouteTagCheckDisable_Type()
)
rosMgmtOspfRouteTagCheckDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteTagCheckDisable.setStatus("current")
_RosMgmtOspfDNBitSetDisableSummary_Type = TruthValue
_RosMgmtOspfDNBitSetDisableSummary_Object = MibTableColumn
rosMgmtOspfDNBitSetDisableSummary = _RosMgmtOspfDNBitSetDisableSummary_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 53),
    _RosMgmtOspfDNBitSetDisableSummary_Type()
)
rosMgmtOspfDNBitSetDisableSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitSetDisableSummary.setStatus("current")
_RosMgmtOspfDNBitSetDisableAse_Type = TruthValue
_RosMgmtOspfDNBitSetDisableAse_Object = MibTableColumn
rosMgmtOspfDNBitSetDisableAse = _RosMgmtOspfDNBitSetDisableAse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 54),
    _RosMgmtOspfDNBitSetDisableAse_Type()
)
rosMgmtOspfDNBitSetDisableAse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitSetDisableAse.setStatus("current")
_RosMgmtOspfDNBitSetDisableNssa_Type = TruthValue
_RosMgmtOspfDNBitSetDisableNssa_Object = MibTableColumn
rosMgmtOspfDNBitSetDisableNssa = _RosMgmtOspfDNBitSetDisableNssa_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 55),
    _RosMgmtOspfDNBitSetDisableNssa_Type()
)
rosMgmtOspfDNBitSetDisableNssa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitSetDisableNssa.setStatus("current")
_RosMgmtOspfDNBitCheckDisableSummary_Type = TruthValue
_RosMgmtOspfDNBitCheckDisableSummary_Object = MibTableColumn
rosMgmtOspfDNBitCheckDisableSummary = _RosMgmtOspfDNBitCheckDisableSummary_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 56),
    _RosMgmtOspfDNBitCheckDisableSummary_Type()
)
rosMgmtOspfDNBitCheckDisableSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableSummary.setStatus("current")
_RosMgmtOspfDNBitCheckDisableAse_Type = TruthValue
_RosMgmtOspfDNBitCheckDisableAse_Object = MibTableColumn
rosMgmtOspfDNBitCheckDisableAse = _RosMgmtOspfDNBitCheckDisableAse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 57),
    _RosMgmtOspfDNBitCheckDisableAse_Type()
)
rosMgmtOspfDNBitCheckDisableAse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableAse.setStatus("current")
_RosMgmtOspfDNBitCheckDisableNssa_Type = TruthValue
_RosMgmtOspfDNBitCheckDisableNssa_Object = MibTableColumn
rosMgmtOspfDNBitCheckDisableNssa = _RosMgmtOspfDNBitCheckDisableNssa_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 58),
    _RosMgmtOspfDNBitCheckDisableNssa_Type()
)
rosMgmtOspfDNBitCheckDisableNssa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableNssa.setStatus("current")


class _RosMgmtOspfSpfMilliInterval_Type(Integer32):
    """Custom type rosMgmtOspfSpfMilliInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_RosMgmtOspfSpfMilliInterval_Type.__name__ = "Integer32"
_RosMgmtOspfSpfMilliInterval_Object = MibTableColumn
rosMgmtOspfSpfMilliInterval = _RosMgmtOspfSpfMilliInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 59),
    _RosMgmtOspfSpfMilliInterval_Type()
)
rosMgmtOspfSpfMilliInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfSpfMilliInterval.setStatus("current")


class _RosMgmtOspfSpfMilliHode_Type(Integer32):
    """Custom type rosMgmtOspfSpfMilliHode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_RosMgmtOspfSpfMilliHode_Type.__name__ = "Integer32"
_RosMgmtOspfSpfMilliHode_Object = MibTableColumn
rosMgmtOspfSpfMilliHode = _RosMgmtOspfSpfMilliHode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 60),
    _RosMgmtOspfSpfMilliHode_Type()
)
rosMgmtOspfSpfMilliHode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfSpfMilliHode.setStatus("current")
_RosMgmtOspfLoopFreeAlt_Type = TruthValue
_RosMgmtOspfLoopFreeAlt_Object = MibTableColumn
rosMgmtOspfLoopFreeAlt = _RosMgmtOspfLoopFreeAlt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 1, 1, 61),
    _RosMgmtOspfLoopFreeAlt_Type()
)
rosMgmtOspfLoopFreeAlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfLoopFreeAlt.setStatus("current")
_RosMgmtOspfAreaTable_Object = MibTable
rosMgmtOspfAreaTable = _RosMgmtOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2)
)
if mibBuilder.loadTexts:
    rosMgmtOspfAreaTable.setStatus("current")
_RosMgmtOspfAreaEntry_Object = MibTableRow
rosMgmtOspfAreaEntry = _RosMgmtOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1)
)
rosMgmtOspfAreaEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfAreaEntry.setStatus("current")
_RosMgmtOspfAreaId_Type = AreaID
_RosMgmtOspfAreaId_Object = MibTableColumn
rosMgmtOspfAreaId = _RosMgmtOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 1),
    _RosMgmtOspfAreaId_Type()
)
rosMgmtOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaId.setStatus("current")


class _RosMgmtOspfAuthType_Type(OspfAuthenticationType):
    """Custom type rosMgmtOspfAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_RosMgmtOspfAuthType_Type.__name__ = "OspfAuthenticationType"
_RosMgmtOspfAuthType_Object = MibTableColumn
rosMgmtOspfAuthType = _RosMgmtOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 2),
    _RosMgmtOspfAuthType_Type()
)
rosMgmtOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAuthType.setStatus("current")


class _RosMgmtOspfImportAsExtern_Type(Integer32):
    """Custom type rosMgmtOspfImportAsExtern based on Integer32"""
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
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_RosMgmtOspfImportAsExtern_Type.__name__ = "Integer32"
_RosMgmtOspfImportAsExtern_Object = MibTableColumn
rosMgmtOspfImportAsExtern = _RosMgmtOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 3),
    _RosMgmtOspfImportAsExtern_Type()
)
rosMgmtOspfImportAsExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfImportAsExtern.setStatus("current")
_RosMgmtOspfSpfRuns_Type = Counter32
_RosMgmtOspfSpfRuns_Object = MibTableColumn
rosMgmtOspfSpfRuns = _RosMgmtOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 4),
    _RosMgmtOspfSpfRuns_Type()
)
rosMgmtOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfSpfRuns.setStatus("current")
_RosMgmtOspfAreaBdrRtrCount_Type = Gauge32
_RosMgmtOspfAreaBdrRtrCount_Object = MibTableColumn
rosMgmtOspfAreaBdrRtrCount = _RosMgmtOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 5),
    _RosMgmtOspfAreaBdrRtrCount_Type()
)
rosMgmtOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaBdrRtrCount.setStatus("current")
_RosMgmtOspfAsBdrRtrCount_Type = Gauge32
_RosMgmtOspfAsBdrRtrCount_Object = MibTableColumn
rosMgmtOspfAsBdrRtrCount = _RosMgmtOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 6),
    _RosMgmtOspfAsBdrRtrCount_Type()
)
rosMgmtOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsBdrRtrCount.setStatus("current")
_RosMgmtOspfAreaLsaCount_Type = Gauge32
_RosMgmtOspfAreaLsaCount_Object = MibTableColumn
rosMgmtOspfAreaLsaCount = _RosMgmtOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 7),
    _RosMgmtOspfAreaLsaCount_Type()
)
rosMgmtOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCount.setStatus("current")


class _RosMgmtOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type rosMgmtOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_RosMgmtOspfAreaLsaCksumSum_Type.__name__ = "Integer32"
_RosMgmtOspfAreaLsaCksumSum_Object = MibTableColumn
rosMgmtOspfAreaLsaCksumSum = _RosMgmtOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 8),
    _RosMgmtOspfAreaLsaCksumSum_Type()
)
rosMgmtOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCksumSum.setStatus("current")


class _RosMgmtOspfAreaSummary_Type(Integer32):
    """Custom type rosMgmtOspfAreaSummary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_RosMgmtOspfAreaSummary_Type.__name__ = "Integer32"
_RosMgmtOspfAreaSummary_Object = MibTableColumn
rosMgmtOspfAreaSummary = _RosMgmtOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 9),
    _RosMgmtOspfAreaSummary_Type()
)
rosMgmtOspfAreaSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaSummary.setStatus("current")


class _RosMgmtOspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type rosMgmtOspfAreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_RosMgmtOspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_RosMgmtOspfAreaNssaTranslatorRole_Object = MibTableColumn
rosMgmtOspfAreaNssaTranslatorRole = _RosMgmtOspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 10),
    _RosMgmtOspfAreaNssaTranslatorRole_Type()
)
rosMgmtOspfAreaNssaTranslatorRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaNssaTranslatorRole.setStatus("current")


class _RosMgmtOspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type rosMgmtOspfAreaNssaTranslatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("elected", 2),
          ("disabled", 3))
    )


_RosMgmtOspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_RosMgmtOspfAreaNssaTranslatorState_Object = MibTableColumn
rosMgmtOspfAreaNssaTranslatorState = _RosMgmtOspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 11),
    _RosMgmtOspfAreaNssaTranslatorState_Type()
)
rosMgmtOspfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaNssaTranslatorState.setStatus("current")


class _RosMgmtOspfAreaNssaTranslatorStabilityInterval_Type(PositiveInteger):
    """Custom type rosMgmtOspfAreaNssaTranslatorStabilityInterval based on PositiveInteger"""
    defaultValue = 40


_RosMgmtOspfAreaNssaTranslatorStabilityInterval_Type.__name__ = "PositiveInteger"
_RosMgmtOspfAreaNssaTranslatorStabilityInterval_Object = MibTableColumn
rosMgmtOspfAreaNssaTranslatorStabilityInterval = _RosMgmtOspfAreaNssaTranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 12),
    _RosMgmtOspfAreaNssaTranslatorStabilityInterval_Type()
)
rosMgmtOspfAreaNssaTranslatorStabilityInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaNssaTranslatorStabilityInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaNssaTranslatorStabilityInterval.setUnits("seconds")
_RosMgmtOspfAreaNssaTranslatorEvents_Type = Counter32
_RosMgmtOspfAreaNssaTranslatorEvents_Object = MibTableColumn
rosMgmtOspfAreaNssaTranslatorEvents = _RosMgmtOspfAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 13),
    _RosMgmtOspfAreaNssaTranslatorEvents_Type()
)
rosMgmtOspfAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaNssaTranslatorEvents.setStatus("current")


class _RosMgmtOspfAreaDefaultCost_Type(BigMetric):
    """Custom type rosMgmtOspfAreaDefaultCost based on BigMetric"""
    defaultValue = 1


_RosMgmtOspfAreaDefaultCost_Type.__name__ = "BigMetric"
_RosMgmtOspfAreaDefaultCost_Object = MibTableColumn
rosMgmtOspfAreaDefaultCost = _RosMgmtOspfAreaDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 14),
    _RosMgmtOspfAreaDefaultCost_Type()
)
rosMgmtOspfAreaDefaultCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaDefaultCost.setStatus("current")


class _RosMgmtOspfAreaType_Type(Integer32):
    """Custom type rosMgmtOspfAreaType based on Integer32"""
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
        *(("backbone", 1),
          ("normal", 2),
          ("stub", 3),
          ("nssa", 4),
          ("transmit", 5))
    )


_RosMgmtOspfAreaType_Type.__name__ = "Integer32"
_RosMgmtOspfAreaType_Object = MibTableColumn
rosMgmtOspfAreaType = _RosMgmtOspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 15),
    _RosMgmtOspfAreaType_Type()
)
rosMgmtOspfAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaType.setStatus("current")
_RosMgmtOspfAreaStatus_Type = RowStatus
_RosMgmtOspfAreaStatus_Object = MibTableColumn
rosMgmtOspfAreaStatus = _RosMgmtOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 16),
    _RosMgmtOspfAreaStatus_Type()
)
rosMgmtOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaStatus.setStatus("current")
_RosMgmtOspfAreaFilterInIpPrefixListName_Type = OctetString
_RosMgmtOspfAreaFilterInIpPrefixListName_Object = MibTableColumn
rosMgmtOspfAreaFilterInIpPrefixListName = _RosMgmtOspfAreaFilterInIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 17),
    _RosMgmtOspfAreaFilterInIpPrefixListName_Type()
)
rosMgmtOspfAreaFilterInIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaFilterInIpPrefixListName.setStatus("current")
_RosMgmtOspfAreaFilterOutIpPrefixListName_Type = OctetString
_RosMgmtOspfAreaFilterOutIpPrefixListName_Object = MibTableColumn
rosMgmtOspfAreaFilterOutIpPrefixListName = _RosMgmtOspfAreaFilterOutIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 18),
    _RosMgmtOspfAreaFilterOutIpPrefixListName_Type()
)
rosMgmtOspfAreaFilterOutIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaFilterOutIpPrefixListName.setStatus("current")
_RosMgmtOspfAreaTeCapability_Type = TruthValue
_RosMgmtOspfAreaTeCapability_Object = MibTableColumn
rosMgmtOspfAreaTeCapability = _RosMgmtOspfAreaTeCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 2, 1, 19),
    _RosMgmtOspfAreaTeCapability_Type()
)
rosMgmtOspfAreaTeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaTeCapability.setStatus("current")
_RosMgmtOspfNetWorkTable_Object = MibTable
rosMgmtOspfNetWorkTable = _RosMgmtOspfNetWorkTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 3)
)
if mibBuilder.loadTexts:
    rosMgmtOspfNetWorkTable.setStatus("current")
_RosMgmtOspfNetWorkEntry_Object = MibTableRow
rosMgmtOspfNetWorkEntry = _RosMgmtOspfNetWorkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 3, 1)
)
rosMgmtOspfNetWorkEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNet"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfMask"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfNetWorkEntry.setStatus("current")
_RosMgmtOspfNet_Type = IpAddress
_RosMgmtOspfNet_Object = MibTableColumn
rosMgmtOspfNet = _RosMgmtOspfNet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 3, 1, 1),
    _RosMgmtOspfNet_Type()
)
rosMgmtOspfNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfNet.setStatus("current")
_RosMgmtOspfMask_Type = IpAddress
_RosMgmtOspfMask_Object = MibTableColumn
rosMgmtOspfMask = _RosMgmtOspfMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 3, 1, 2),
    _RosMgmtOspfMask_Type()
)
rosMgmtOspfMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfMask.setStatus("current")
_RosMgmtOspfNetWorkStatus_Type = RowStatus
_RosMgmtOspfNetWorkStatus_Object = MibTableColumn
rosMgmtOspfNetWorkStatus = _RosMgmtOspfNetWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 3, 1, 3),
    _RosMgmtOspfNetWorkStatus_Type()
)
rosMgmtOspfNetWorkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfNetWorkStatus.setStatus("current")
_RosMgmtOspfStubAreaTable_Object = MibTable
rosMgmtOspfStubAreaTable = _RosMgmtOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 4)
)
if mibBuilder.loadTexts:
    rosMgmtOspfStubAreaTable.setStatus("current")
_RosMgmtOspfStubAreaEntry_Object = MibTableRow
rosMgmtOspfStubAreaEntry = _RosMgmtOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 4, 1)
)
rosMgmtOspfStubAreaEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfStubAreaId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfStubAreaEntry.setStatus("current")
_RosMgmtOspfStubAreaId_Type = AreaID
_RosMgmtOspfStubAreaId_Object = MibTableColumn
rosMgmtOspfStubAreaId = _RosMgmtOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 4, 1, 1),
    _RosMgmtOspfStubAreaId_Type()
)
rosMgmtOspfStubAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfStubAreaId.setStatus("current")
_RosMgmtOspfStubAreaOption_Type = TruthValue
_RosMgmtOspfStubAreaOption_Object = MibTableColumn
rosMgmtOspfStubAreaOption = _RosMgmtOspfStubAreaOption_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 4, 1, 2),
    _RosMgmtOspfStubAreaOption_Type()
)
rosMgmtOspfStubAreaOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfStubAreaOption.setStatus("current")
_RosMgmtOspfStubAreaStatus_Type = RowStatus
_RosMgmtOspfStubAreaStatus_Object = MibTableColumn
rosMgmtOspfStubAreaStatus = _RosMgmtOspfStubAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 4, 1, 3),
    _RosMgmtOspfStubAreaStatus_Type()
)
rosMgmtOspfStubAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfStubAreaStatus.setStatus("current")
_RosMgmtOspfNssaAreaTable_Object = MibTable
rosMgmtOspfNssaAreaTable = _RosMgmtOspfNssaAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 5)
)
if mibBuilder.loadTexts:
    rosMgmtOspfNssaAreaTable.setStatus("current")
_RosMgmtOspfNssaAreaEntry_Object = MibTableRow
rosMgmtOspfNssaAreaEntry = _RosMgmtOspfNssaAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 5, 1)
)
rosMgmtOspfNssaAreaEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNssaAreaId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfNssaAreaEntry.setStatus("current")
_RosMgmtOspfNssaAreaId_Type = AreaID
_RosMgmtOspfNssaAreaId_Object = MibTableColumn
rosMgmtOspfNssaAreaId = _RosMgmtOspfNssaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 5, 1, 1),
    _RosMgmtOspfNssaAreaId_Type()
)
rosMgmtOspfNssaAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfNssaAreaId.setStatus("current")


class _RosMgmtOspfNssaAreaOption_Type(Integer32):
    """Custom type rosMgmtOspfNssaAreaOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("summarysend", 0),
          ("nosummary", 4))
    )


_RosMgmtOspfNssaAreaOption_Type.__name__ = "Integer32"
_RosMgmtOspfNssaAreaOption_Object = MibTableColumn
rosMgmtOspfNssaAreaOption = _RosMgmtOspfNssaAreaOption_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 5, 1, 2),
    _RosMgmtOspfNssaAreaOption_Type()
)
rosMgmtOspfNssaAreaOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfNssaAreaOption.setStatus("current")
_RosMgmtOspfNssaAreaStatus_Type = RowStatus
_RosMgmtOspfNssaAreaStatus_Object = MibTableColumn
rosMgmtOspfNssaAreaStatus = _RosMgmtOspfNssaAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 5, 1, 3),
    _RosMgmtOspfNssaAreaStatus_Type()
)
rosMgmtOspfNssaAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfNssaAreaStatus.setStatus("current")
_RosMgmtOspfIfTable_Object = MibTable
rosMgmtOspfIfTable = _RosMgmtOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6)
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfTable.setStatus("current")
_RosMgmtOspfIfEntry_Object = MibTableRow
rosMgmtOspfIfEntry = _RosMgmtOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1)
)
rosMgmtOspfIfEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfEntry.setStatus("current")
_RosMgmtOspfAddressLessIf_Type = InterfaceIndexOrZero
_RosMgmtOspfAddressLessIf_Object = MibTableColumn
rosMgmtOspfAddressLessIf = _RosMgmtOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 1),
    _RosMgmtOspfAddressLessIf_Type()
)
rosMgmtOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAddressLessIf.setStatus("current")
_RosMgmtOspfIfIpAddress_Type = IpAddress
_RosMgmtOspfIfIpAddress_Object = MibTableColumn
rosMgmtOspfIfIpAddress = _RosMgmtOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 2),
    _RosMgmtOspfIfIpAddress_Type()
)
rosMgmtOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfIpAddress.setStatus("current")


class _RosMgmtOspfIfAreaId_Type(AreaID):
    """Custom type rosMgmtOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_RosMgmtOspfIfAreaId_Type.__name__ = "AreaID"
_RosMgmtOspfIfAreaId_Object = MibTableColumn
rosMgmtOspfIfAreaId = _RosMgmtOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 3),
    _RosMgmtOspfIfAreaId_Type()
)
rosMgmtOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAreaId.setStatus("current")


class _RosMgmtOspfIfType_Type(Integer32):
    """Custom type rosMgmtOspfIfType based on Integer32"""
    defaultValue = 2

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
        *(("none", 0),
          ("pointToPoint", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("pointToMultipoint", 4),
          ("virtuallink", 5),
          ("loopback", 6))
    )


_RosMgmtOspfIfType_Type.__name__ = "Integer32"
_RosMgmtOspfIfType_Object = MibTableColumn
rosMgmtOspfIfType = _RosMgmtOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 4),
    _RosMgmtOspfIfType_Type()
)
rosMgmtOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfType.setStatus("current")


class _RosMgmtOspfIfAdminStat_Type(Status):
    """Custom type rosMgmtOspfIfAdminStat based on Status"""
    defaultValue = 1


_RosMgmtOspfIfAdminStat_Type.__name__ = "Status"
_RosMgmtOspfIfAdminStat_Object = MibTableColumn
rosMgmtOspfIfAdminStat = _RosMgmtOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 5),
    _RosMgmtOspfIfAdminStat_Type()
)
rosMgmtOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAdminStat.setStatus("current")


class _RosMgmtOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type rosMgmtOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RosMgmtOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_RosMgmtOspfIfRtrPriority_Object = MibTableColumn
rosMgmtOspfIfRtrPriority = _RosMgmtOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 6),
    _RosMgmtOspfIfRtrPriority_Type()
)
rosMgmtOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfRtrPriority.setStatus("current")


class _RosMgmtOspfIfTransitDelay_Type(Integer32):
    """Custom type rosMgmtOspfIfTransitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfIfTransitDelay_Type.__name__ = "Integer32"
_RosMgmtOspfIfTransitDelay_Object = MibTableColumn
rosMgmtOspfIfTransitDelay = _RosMgmtOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 7),
    _RosMgmtOspfIfTransitDelay_Type()
)
rosMgmtOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfIfTransitDelay.setUnits("seconds")


class _RosMgmtOspfIfRetransInterval_Type(Integer32):
    """Custom type rosMgmtOspfIfRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfIfRetransInterval_Type.__name__ = "Integer32"
_RosMgmtOspfIfRetransInterval_Object = MibTableColumn
rosMgmtOspfIfRetransInterval = _RosMgmtOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 8),
    _RosMgmtOspfIfRetransInterval_Type()
)
rosMgmtOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfIfRetransInterval.setUnits("seconds")


class _RosMgmtOspfIfHelloInterval_Type(Integer32):
    """Custom type rosMgmtOspfIfHelloInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfIfHelloInterval_Type.__name__ = "Integer32"
_RosMgmtOspfIfHelloInterval_Object = MibTableColumn
rosMgmtOspfIfHelloInterval = _RosMgmtOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 9),
    _RosMgmtOspfIfHelloInterval_Type()
)
rosMgmtOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfIfHelloInterval.setUnits("seconds")


class _RosMgmtOspfIfRtrDeadInterval_Type(Integer32):
    """Custom type rosMgmtOspfIfRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfIfRtrDeadInterval_Type.__name__ = "Integer32"
_RosMgmtOspfIfRtrDeadInterval_Object = MibTableColumn
rosMgmtOspfIfRtrDeadInterval = _RosMgmtOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 10),
    _RosMgmtOspfIfRtrDeadInterval_Type()
)
rosMgmtOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfIfRtrDeadInterval.setUnits("seconds")


class _RosMgmtOspfIfPollInterval_Type(Integer32):
    """Custom type rosMgmtOspfIfPollInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfIfPollInterval_Type.__name__ = "Integer32"
_RosMgmtOspfIfPollInterval_Object = MibTableColumn
rosMgmtOspfIfPollInterval = _RosMgmtOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 11),
    _RosMgmtOspfIfPollInterval_Type()
)
rosMgmtOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfIfPollInterval.setUnits("seconds")


class _RosMgmtOspfIfState_Type(Integer32):
    """Custom type rosMgmtOspfIfState based on Integer32"""
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
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_RosMgmtOspfIfState_Type.__name__ = "Integer32"
_RosMgmtOspfIfState_Object = MibTableColumn
rosMgmtOspfIfState = _RosMgmtOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 12),
    _RosMgmtOspfIfState_Type()
)
rosMgmtOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfState.setStatus("current")


class _RosMgmtOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type rosMgmtOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RosMgmtOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_RosMgmtOspfIfDesignatedRouter_Object = MibTableColumn
rosMgmtOspfIfDesignatedRouter = _RosMgmtOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 13),
    _RosMgmtOspfIfDesignatedRouter_Type()
)
rosMgmtOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfDesignatedRouter.setStatus("current")


class _RosMgmtOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type rosMgmtOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RosMgmtOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_RosMgmtOspfIfBackupDesignatedRouter_Object = MibTableColumn
rosMgmtOspfIfBackupDesignatedRouter = _RosMgmtOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 14),
    _RosMgmtOspfIfBackupDesignatedRouter_Type()
)
rosMgmtOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfBackupDesignatedRouter.setStatus("current")
_RosMgmtOspfIfEvents_Type = Counter32
_RosMgmtOspfIfEvents_Object = MibTableColumn
rosMgmtOspfIfEvents = _RosMgmtOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 15),
    _RosMgmtOspfIfEvents_Type()
)
rosMgmtOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfEvents.setStatus("current")


class _RosMgmtOspfIfAuthKeyId_Type(Integer32):
    """Custom type rosMgmtOspfIfAuthKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RosMgmtOspfIfAuthKeyId_Type.__name__ = "Integer32"
_RosMgmtOspfIfAuthKeyId_Object = MibTableColumn
rosMgmtOspfIfAuthKeyId = _RosMgmtOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 16),
    _RosMgmtOspfIfAuthKeyId_Type()
)
rosMgmtOspfIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthKeyId.setStatus("current")


class _RosMgmtOspfIfAuthSimpleKeyType_Type(Integer32):
    """Custom type rosMgmtOspfIfAuthSimpleKeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RosMgmtOspfIfAuthSimpleKeyType_Type.__name__ = "Integer32"
_RosMgmtOspfIfAuthSimpleKeyType_Object = MibTableColumn
rosMgmtOspfIfAuthSimpleKeyType = _RosMgmtOspfIfAuthSimpleKeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 17),
    _RosMgmtOspfIfAuthSimpleKeyType_Type()
)
rosMgmtOspfIfAuthSimpleKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthSimpleKeyType.setStatus("current")


class _RosMgmtOspfIfAuthMd5KeyType_Type(Integer32):
    """Custom type rosMgmtOspfIfAuthMd5KeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RosMgmtOspfIfAuthMd5KeyType_Type.__name__ = "Integer32"
_RosMgmtOspfIfAuthMd5KeyType_Object = MibTableColumn
rosMgmtOspfIfAuthMd5KeyType = _RosMgmtOspfIfAuthMd5KeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 18),
    _RosMgmtOspfIfAuthMd5KeyType_Type()
)
rosMgmtOspfIfAuthMd5KeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthMd5KeyType.setStatus("current")


class _RosMgmtOspfIfAuthSimpleKey_Type(OctetString):
    """Custom type rosMgmtOspfIfAuthSimpleKey based on OctetString"""
    defaultHexValue = ""


_RosMgmtOspfIfAuthSimpleKey_Type.__name__ = "OctetString"
_RosMgmtOspfIfAuthSimpleKey_Object = MibTableColumn
rosMgmtOspfIfAuthSimpleKey = _RosMgmtOspfIfAuthSimpleKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 19),
    _RosMgmtOspfIfAuthSimpleKey_Type()
)
rosMgmtOspfIfAuthSimpleKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthSimpleKey.setStatus("current")


class _RosMgmtOspfIfAuthMd5Key_Type(OctetString):
    """Custom type rosMgmtOspfIfAuthMd5Key based on OctetString"""
    defaultHexValue = ""


_RosMgmtOspfIfAuthMd5Key_Type.__name__ = "OctetString"
_RosMgmtOspfIfAuthMd5Key_Object = MibTableColumn
rosMgmtOspfIfAuthMd5Key = _RosMgmtOspfIfAuthMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 20),
    _RosMgmtOspfIfAuthMd5Key_Type()
)
rosMgmtOspfIfAuthMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthMd5Key.setStatus("current")


class _RosMgmtOspfIfAuthKeyChain_Type(OctetString):
    """Custom type rosMgmtOspfIfAuthKeyChain based on OctetString"""
    defaultHexValue = ""


_RosMgmtOspfIfAuthKeyChain_Type.__name__ = "OctetString"
_RosMgmtOspfIfAuthKeyChain_Object = MibTableColumn
rosMgmtOspfIfAuthKeyChain = _RosMgmtOspfIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 21),
    _RosMgmtOspfIfAuthKeyChain_Type()
)
rosMgmtOspfIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthKeyChain.setStatus("current")


class _RosMgmtOspfIfAuthType_Type(OspfAuthenticationType):
    """Custom type rosMgmtOspfIfAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_RosMgmtOspfIfAuthType_Type.__name__ = "OspfAuthenticationType"
_RosMgmtOspfIfAuthType_Object = MibTableColumn
rosMgmtOspfIfAuthType = _RosMgmtOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 22),
    _RosMgmtOspfIfAuthType_Type()
)
rosMgmtOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthType.setStatus("current")
_RosMgmtOspfIfLsaCount_Type = Gauge32
_RosMgmtOspfIfLsaCount_Object = MibTableColumn
rosMgmtOspfIfLsaCount = _RosMgmtOspfIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 23),
    _RosMgmtOspfIfLsaCount_Type()
)
rosMgmtOspfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfLsaCount.setStatus("current")
_RosMgmtOspfIfLsaCksumSum_Type = Unsigned32
_RosMgmtOspfIfLsaCksumSum_Object = MibTableColumn
rosMgmtOspfIfLsaCksumSum = _RosMgmtOspfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 24),
    _RosMgmtOspfIfLsaCksumSum_Type()
)
rosMgmtOspfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfLsaCksumSum.setStatus("current")
_RosMgmtOspfIfDesignatedRouterId_Type = RouterID
_RosMgmtOspfIfDesignatedRouterId_Object = MibTableColumn
rosMgmtOspfIfDesignatedRouterId = _RosMgmtOspfIfDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 25),
    _RosMgmtOspfIfDesignatedRouterId_Type()
)
rosMgmtOspfIfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfDesignatedRouterId.setStatus("current")
_RosMgmtOspfIfBackupDesignatedRouterId_Type = RouterID
_RosMgmtOspfIfBackupDesignatedRouterId_Object = MibTableColumn
rosMgmtOspfIfBackupDesignatedRouterId = _RosMgmtOspfIfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 26),
    _RosMgmtOspfIfBackupDesignatedRouterId_Type()
)
rosMgmtOspfIfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfIfBackupDesignatedRouterId.setStatus("current")


class _RosMgmtOspfIfPassive_Type(EnableVar):
    """Custom type rosMgmtOspfIfPassive based on EnableVar"""
    defaultValue = 2


_RosMgmtOspfIfPassive_Type.__name__ = "EnableVar"
_RosMgmtOspfIfPassive_Object = MibTableColumn
rosMgmtOspfIfPassive = _RosMgmtOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 27),
    _RosMgmtOspfIfPassive_Type()
)
rosMgmtOspfIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfPassive.setStatus("current")


class _RosMgmtOspfIfMtu_Type(EnableVar):
    """Custom type rosMgmtOspfIfMtu based on EnableVar"""
    defaultValue = 2


_RosMgmtOspfIfMtu_Type.__name__ = "EnableVar"
_RosMgmtOspfIfMtu_Object = MibTableColumn
rosMgmtOspfIfMtu = _RosMgmtOspfIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 28),
    _RosMgmtOspfIfMtu_Type()
)
rosMgmtOspfIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfMtu.setStatus("current")
_RosMgmtOspfIfMetric_Type = Metric
_RosMgmtOspfIfMetric_Object = MibTableColumn
rosMgmtOspfIfMetric = _RosMgmtOspfIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 29),
    _RosMgmtOspfIfMetric_Type()
)
rosMgmtOspfIfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfMetric.setStatus("current")


class _RosMgmtOspfIfBfd_Type(EnableVar):
    """Custom type rosMgmtOspfIfBfd based on EnableVar"""
    defaultValue = 2


_RosMgmtOspfIfBfd_Type.__name__ = "EnableVar"
_RosMgmtOspfIfBfd_Object = MibTableColumn
rosMgmtOspfIfBfd = _RosMgmtOspfIfBfd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 30),
    _RosMgmtOspfIfBfd_Type()
)
rosMgmtOspfIfBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfBfd.setStatus("current")


class _RosMgmtOspfIfGRResync_Type(Integer32):
    """Custom type rosMgmtOspfIfGRResync based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfIfGRResync_Type.__name__ = "Integer32"
_RosMgmtOspfIfGRResync_Object = MibTableColumn
rosMgmtOspfIfGRResync = _RosMgmtOspfIfGRResync_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 6, 1, 31),
    _RosMgmtOspfIfGRResync_Type()
)
rosMgmtOspfIfGRResync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfIfGRResync.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfIfGRResync.setUnits("seconds")
_RosMgmtOspfVirtIfTable_Object = MibTable
rosMgmtOspfVirtIfTable = _RosMgmtOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7)
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfTable.setStatus("current")
_RosMgmtOspfVirtIfEntry_Object = MibTableRow
rosMgmtOspfVirtIfEntry = _RosMgmtOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1)
)
rosMgmtOspfVirtIfEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfEntry.setStatus("current")
_RosMgmtOspfVirtIfAreaId_Type = AreaID
_RosMgmtOspfVirtIfAreaId_Object = MibTableColumn
rosMgmtOspfVirtIfAreaId = _RosMgmtOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 1),
    _RosMgmtOspfVirtIfAreaId_Type()
)
rosMgmtOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAreaId.setStatus("current")
_RosMgmtOspfVirtIfNeighbor_Type = RouterID
_RosMgmtOspfVirtIfNeighbor_Object = MibTableColumn
rosMgmtOspfVirtIfNeighbor = _RosMgmtOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 2),
    _RosMgmtOspfVirtIfNeighbor_Type()
)
rosMgmtOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfNeighbor.setStatus("current")


class _RosMgmtOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type rosMgmtOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_RosMgmtOspfVirtIfTransitDelay_Type.__name__ = "UpToMaxAge"
_RosMgmtOspfVirtIfTransitDelay_Object = MibTableColumn
rosMgmtOspfVirtIfTransitDelay = _RosMgmtOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 3),
    _RosMgmtOspfVirtIfTransitDelay_Type()
)
rosMgmtOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfTransitDelay.setUnits("seconds")


class _RosMgmtOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type rosMgmtOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_RosMgmtOspfVirtIfRetransInterval_Type.__name__ = "UpToMaxAge"
_RosMgmtOspfVirtIfRetransInterval_Object = MibTableColumn
rosMgmtOspfVirtIfRetransInterval = _RosMgmtOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 4),
    _RosMgmtOspfVirtIfRetransInterval_Type()
)
rosMgmtOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfRetransInterval.setUnits("seconds")


class _RosMgmtOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type rosMgmtOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RosMgmtOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_RosMgmtOspfVirtIfHelloInterval_Object = MibTableColumn
rosMgmtOspfVirtIfHelloInterval = _RosMgmtOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 5),
    _RosMgmtOspfVirtIfHelloInterval_Type()
)
rosMgmtOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfHelloInterval.setUnits("seconds")


class _RosMgmtOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type rosMgmtOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_RosMgmtOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_RosMgmtOspfVirtIfRtrDeadInterval_Object = MibTableColumn
rosMgmtOspfVirtIfRtrDeadInterval = _RosMgmtOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 6),
    _RosMgmtOspfVirtIfRtrDeadInterval_Type()
)
rosMgmtOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfRtrDeadInterval.setUnits("seconds")


class _RosMgmtOspfVirtIfState_Type(Integer32):
    """Custom type rosMgmtOspfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_RosMgmtOspfVirtIfState_Type.__name__ = "Integer32"
_RosMgmtOspfVirtIfState_Object = MibTableColumn
rosMgmtOspfVirtIfState = _RosMgmtOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 7),
    _RosMgmtOspfVirtIfState_Type()
)
rosMgmtOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfState.setStatus("current")
_RosMgmtOspfVirtIfEvents_Type = Counter32
_RosMgmtOspfVirtIfEvents_Object = MibTableColumn
rosMgmtOspfVirtIfEvents = _RosMgmtOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 8),
    _RosMgmtOspfVirtIfEvents_Type()
)
rosMgmtOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfEvents.setStatus("current")


class _RosMgmtOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type rosMgmtOspfVirtIfAuthKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RosMgmtOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_RosMgmtOspfVirtIfAuthKeyId_Object = MibTableColumn
rosMgmtOspfVirtIfAuthKeyId = _RosMgmtOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 9),
    _RosMgmtOspfVirtIfAuthKeyId_Type()
)
rosMgmtOspfVirtIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthKeyId.setStatus("current")


class _RosMgmtOspfVirtIfAuthSimpleKeyType_Type(Integer32):
    """Custom type rosMgmtOspfVirtIfAuthSimpleKeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RosMgmtOspfVirtIfAuthSimpleKeyType_Type.__name__ = "Integer32"
_RosMgmtOspfVirtIfAuthSimpleKeyType_Object = MibTableColumn
rosMgmtOspfVirtIfAuthSimpleKeyType = _RosMgmtOspfVirtIfAuthSimpleKeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 10),
    _RosMgmtOspfVirtIfAuthSimpleKeyType_Type()
)
rosMgmtOspfVirtIfAuthSimpleKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthSimpleKeyType.setStatus("current")


class _RosMgmtOspfVirtIfAuthMd5KeyType_Type(Integer32):
    """Custom type rosMgmtOspfVirtIfAuthMd5KeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RosMgmtOspfVirtIfAuthMd5KeyType_Type.__name__ = "Integer32"
_RosMgmtOspfVirtIfAuthMd5KeyType_Object = MibTableColumn
rosMgmtOspfVirtIfAuthMd5KeyType = _RosMgmtOspfVirtIfAuthMd5KeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 11),
    _RosMgmtOspfVirtIfAuthMd5KeyType_Type()
)
rosMgmtOspfVirtIfAuthMd5KeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthMd5KeyType.setStatus("current")


class _RosMgmtOspfVirtIfAuthSimpleKey_Type(OctetString):
    """Custom type rosMgmtOspfVirtIfAuthSimpleKey based on OctetString"""
    defaultHexValue = ""


_RosMgmtOspfVirtIfAuthSimpleKey_Type.__name__ = "OctetString"
_RosMgmtOspfVirtIfAuthSimpleKey_Object = MibTableColumn
rosMgmtOspfVirtIfAuthSimpleKey = _RosMgmtOspfVirtIfAuthSimpleKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 12),
    _RosMgmtOspfVirtIfAuthSimpleKey_Type()
)
rosMgmtOspfVirtIfAuthSimpleKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthSimpleKey.setStatus("current")


class _RosMgmtOspfVirtIfAuthMd5Key_Type(OctetString):
    """Custom type rosMgmtOspfVirtIfAuthMd5Key based on OctetString"""
    defaultHexValue = ""


_RosMgmtOspfVirtIfAuthMd5Key_Type.__name__ = "OctetString"
_RosMgmtOspfVirtIfAuthMd5Key_Object = MibTableColumn
rosMgmtOspfVirtIfAuthMd5Key = _RosMgmtOspfVirtIfAuthMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 13),
    _RosMgmtOspfVirtIfAuthMd5Key_Type()
)
rosMgmtOspfVirtIfAuthMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthMd5Key.setStatus("current")


class _RosMgmtOspfVirtIfAuthKeyChain_Type(OctetString):
    """Custom type rosMgmtOspfVirtIfAuthKeyChain based on OctetString"""
    defaultHexValue = ""


_RosMgmtOspfVirtIfAuthKeyChain_Type.__name__ = "OctetString"
_RosMgmtOspfVirtIfAuthKeyChain_Object = MibTableColumn
rosMgmtOspfVirtIfAuthKeyChain = _RosMgmtOspfVirtIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 14),
    _RosMgmtOspfVirtIfAuthKeyChain_Type()
)
rosMgmtOspfVirtIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthKeyChain.setStatus("current")


class _RosMgmtOspfVirtIfAuthType_Type(OspfAuthenticationType):
    """Custom type rosMgmtOspfVirtIfAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_RosMgmtOspfVirtIfAuthType_Type.__name__ = "OspfAuthenticationType"
_RosMgmtOspfVirtIfAuthType_Object = MibTableColumn
rosMgmtOspfVirtIfAuthType = _RosMgmtOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 15),
    _RosMgmtOspfVirtIfAuthType_Type()
)
rosMgmtOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthType.setStatus("current")
_RosMgmtOspfVirtIfLsaCount_Type = Gauge32
_RosMgmtOspfVirtIfLsaCount_Object = MibTableColumn
rosMgmtOspfVirtIfLsaCount = _RosMgmtOspfVirtIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 16),
    _RosMgmtOspfVirtIfLsaCount_Type()
)
rosMgmtOspfVirtIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfLsaCount.setStatus("current")
_RosMgmtOspfVirtIfLsaCksumSum_Type = Unsigned32
_RosMgmtOspfVirtIfLsaCksumSum_Object = MibTableColumn
rosMgmtOspfVirtIfLsaCksumSum = _RosMgmtOspfVirtIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 17),
    _RosMgmtOspfVirtIfLsaCksumSum_Type()
)
rosMgmtOspfVirtIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfLsaCksumSum.setStatus("current")


class _RosMgmtOspfVirtIfCost_Type(Integer32):
    """Custom type rosMgmtOspfVirtIfCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RosMgmtOspfVirtIfCost_Type.__name__ = "Integer32"
_RosMgmtOspfVirtIfCost_Object = MibTableColumn
rosMgmtOspfVirtIfCost = _RosMgmtOspfVirtIfCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 18),
    _RosMgmtOspfVirtIfCost_Type()
)
rosMgmtOspfVirtIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfCost.setStatus("current")
_RosMgmtOspfVirtIfStatus_Type = RowStatus
_RosMgmtOspfVirtIfStatus_Object = MibTableColumn
rosMgmtOspfVirtIfStatus = _RosMgmtOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 7, 1, 19),
    _RosMgmtOspfVirtIfStatus_Type()
)
rosMgmtOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfStatus.setStatus("current")
_RosMgmtOspfNbrTable_Object = MibTable
rosMgmtOspfNbrTable = _RosMgmtOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8)
)
if mibBuilder.loadTexts:
    rosMgmtOspfNbrTable.setStatus("current")
_RosMgmtOspfNbrEntry_Object = MibTableRow
rosMgmtOspfNbrEntry = _RosMgmtOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1)
)
rosMgmtOspfNbrEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrIpAddr"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfNbrEntry.setStatus("current")
_RosMgmtOspfNbrIpAddr_Type = IpAddress
_RosMgmtOspfNbrIpAddr_Object = MibTableColumn
rosMgmtOspfNbrIpAddr = _RosMgmtOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 1),
    _RosMgmtOspfNbrIpAddr_Type()
)
rosMgmtOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrIpAddr.setStatus("current")
_RosMgmtOspfNbrAddressLessIndex_Type = InterfaceIndexOrZero
_RosMgmtOspfNbrAddressLessIndex_Object = MibTableColumn
rosMgmtOspfNbrAddressLessIndex = _RosMgmtOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 2),
    _RosMgmtOspfNbrAddressLessIndex_Type()
)
rosMgmtOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrAddressLessIndex.setStatus("current")


class _RosMgmtOspfNbrRtrId_Type(RouterID):
    """Custom type rosMgmtOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_RosMgmtOspfNbrRtrId_Type.__name__ = "RouterID"
_RosMgmtOspfNbrRtrId_Object = MibTableColumn
rosMgmtOspfNbrRtrId = _RosMgmtOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 3),
    _RosMgmtOspfNbrRtrId_Type()
)
rosMgmtOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrRtrId.setStatus("current")


class _RosMgmtOspfNbrOptions_Type(Integer32):
    """Custom type rosMgmtOspfNbrOptions based on Integer32"""
    defaultValue = 0


_RosMgmtOspfNbrOptions_Type.__name__ = "Integer32"
_RosMgmtOspfNbrOptions_Object = MibTableColumn
rosMgmtOspfNbrOptions = _RosMgmtOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 4),
    _RosMgmtOspfNbrOptions_Type()
)
rosMgmtOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrOptions.setStatus("current")


class _RosMgmtOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type rosMgmtOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RosMgmtOspfNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_RosMgmtOspfNbrPriority_Object = MibTableColumn
rosMgmtOspfNbrPriority = _RosMgmtOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 5),
    _RosMgmtOspfNbrPriority_Type()
)
rosMgmtOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrPriority.setStatus("current")


class _RosMgmtOspfNbrState_Type(Integer32):
    """Custom type rosMgmtOspfNbrState based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_RosMgmtOspfNbrState_Type.__name__ = "Integer32"
_RosMgmtOspfNbrState_Object = MibTableColumn
rosMgmtOspfNbrState = _RosMgmtOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 6),
    _RosMgmtOspfNbrState_Type()
)
rosMgmtOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrState.setStatus("current")
_RosMgmtOspfNbrEvents_Type = Counter32
_RosMgmtOspfNbrEvents_Object = MibTableColumn
rosMgmtOspfNbrEvents = _RosMgmtOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 7),
    _RosMgmtOspfNbrEvents_Type()
)
rosMgmtOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrEvents.setStatus("current")
_RosMgmtOspfNbrLsRetransQLen_Type = Gauge32
_RosMgmtOspfNbrLsRetransQLen_Object = MibTableColumn
rosMgmtOspfNbrLsRetransQLen = _RosMgmtOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 8),
    _RosMgmtOspfNbrLsRetransQLen_Type()
)
rosMgmtOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrLsRetransQLen.setStatus("current")


class _RosMgmtOspfNbrMode_Type(Integer32):
    """Custom type rosMgmtOspfNbrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2))
    )


_RosMgmtOspfNbrMode_Type.__name__ = "Integer32"
_RosMgmtOspfNbrMode_Object = MibTableColumn
rosMgmtOspfNbrMode = _RosMgmtOspfNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 8, 1, 9),
    _RosMgmtOspfNbrMode_Type()
)
rosMgmtOspfNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfNbrMode.setStatus("current")
_RosMgmtOspfNbmaCfgNbrTable_Object = MibTable
rosMgmtOspfNbmaCfgNbrTable = _RosMgmtOspfNbmaCfgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 9)
)
if mibBuilder.loadTexts:
    rosMgmtOspfNbmaCfgNbrTable.setStatus("current")
_RosMgmtOspfNbmaCfgNbrEntry_Object = MibTableRow
rosMgmtOspfNbmaCfgNbrEntry = _RosMgmtOspfNbmaCfgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 9, 1)
)
rosMgmtOspfNbmaCfgNbrEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbmaCfgNbrIpAddr"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfNbmaCfgNbrEntry.setStatus("current")
_RosMgmtOspfNbmaCfgNbrIpAddr_Type = IpAddress
_RosMgmtOspfNbmaCfgNbrIpAddr_Object = MibTableColumn
rosMgmtOspfNbmaCfgNbrIpAddr = _RosMgmtOspfNbmaCfgNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 9, 1, 1),
    _RosMgmtOspfNbmaCfgNbrIpAddr_Type()
)
rosMgmtOspfNbmaCfgNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfNbmaCfgNbrIpAddr.setStatus("current")


class _RosMgmtOspfNbmaCfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type rosMgmtOspfNbmaCfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RosMgmtOspfNbmaCfgNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_RosMgmtOspfNbmaCfgNbrPriority_Object = MibTableColumn
rosMgmtOspfNbmaCfgNbrPriority = _RosMgmtOspfNbmaCfgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 9, 1, 2),
    _RosMgmtOspfNbmaCfgNbrPriority_Type()
)
rosMgmtOspfNbmaCfgNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfNbmaCfgNbrPriority.setStatus("current")
_RosMgmtOspfNbmaCfgNbrStatus_Type = RowStatus
_RosMgmtOspfNbmaCfgNbrStatus_Object = MibTableColumn
rosMgmtOspfNbmaCfgNbrStatus = _RosMgmtOspfNbmaCfgNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 9, 1, 3),
    _RosMgmtOspfNbmaCfgNbrStatus_Type()
)
rosMgmtOspfNbmaCfgNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfNbmaCfgNbrStatus.setStatus("current")
_RosMgmtOspfVirtNbrTable_Object = MibTable
rosMgmtOspfVirtNbrTable = _RosMgmtOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10)
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrTable.setStatus("current")
_RosMgmtOspfVirtNbrEntry_Object = MibTableRow
rosMgmtOspfVirtNbrEntry = _RosMgmtOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1)
)
rosMgmtOspfVirtNbrEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtNbrArea"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrEntry.setStatus("current")
_RosMgmtOspfVirtNbrArea_Type = AreaID
_RosMgmtOspfVirtNbrArea_Object = MibTableColumn
rosMgmtOspfVirtNbrArea = _RosMgmtOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 1),
    _RosMgmtOspfVirtNbrArea_Type()
)
rosMgmtOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrArea.setStatus("current")
_RosMgmtOspfVirtNbrRtrId_Type = RouterID
_RosMgmtOspfVirtNbrRtrId_Object = MibTableColumn
rosMgmtOspfVirtNbrRtrId = _RosMgmtOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 2),
    _RosMgmtOspfVirtNbrRtrId_Type()
)
rosMgmtOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrRtrId.setStatus("current")
_RosMgmtOspfVirtNbrIpAddr_Type = IpAddress
_RosMgmtOspfVirtNbrIpAddr_Object = MibTableColumn
rosMgmtOspfVirtNbrIpAddr = _RosMgmtOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 3),
    _RosMgmtOspfVirtNbrIpAddr_Type()
)
rosMgmtOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrIpAddr.setStatus("current")
_RosMgmtOspfVirtNbrOptions_Type = Integer32
_RosMgmtOspfVirtNbrOptions_Object = MibTableColumn
rosMgmtOspfVirtNbrOptions = _RosMgmtOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 4),
    _RosMgmtOspfVirtNbrOptions_Type()
)
rosMgmtOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrOptions.setStatus("current")


class _RosMgmtOspfVirtNbrState_Type(Integer32):
    """Custom type rosMgmtOspfVirtNbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_RosMgmtOspfVirtNbrState_Type.__name__ = "Integer32"
_RosMgmtOspfVirtNbrState_Object = MibTableColumn
rosMgmtOspfVirtNbrState = _RosMgmtOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 5),
    _RosMgmtOspfVirtNbrState_Type()
)
rosMgmtOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrState.setStatus("current")
_RosMgmtOspfVirtNbrEvents_Type = Counter32
_RosMgmtOspfVirtNbrEvents_Object = MibTableColumn
rosMgmtOspfVirtNbrEvents = _RosMgmtOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 6),
    _RosMgmtOspfVirtNbrEvents_Type()
)
rosMgmtOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrEvents.setStatus("current")
_RosMgmtOspfVirtNbrLsRetransQLen_Type = Gauge32
_RosMgmtOspfVirtNbrLsRetransQLen_Object = MibTableColumn
rosMgmtOspfVirtNbrLsRetransQLen = _RosMgmtOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 7),
    _RosMgmtOspfVirtNbrLsRetransQLen_Type()
)
rosMgmtOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrLsRetransQLen.setStatus("current")
_RosMgmtOspfVirtNbrLessIf_Type = Integer32
_RosMgmtOspfVirtNbrLessIf_Object = MibTableColumn
rosMgmtOspfVirtNbrLessIf = _RosMgmtOspfVirtNbrLessIf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 8),
    _RosMgmtOspfVirtNbrLessIf_Type()
)
rosMgmtOspfVirtNbrLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrLessIf.setStatus("current")


class _RosMgmtOspfVirtNbrMode_Type(Integer32):
    """Custom type rosMgmtOspfVirtNbrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2))
    )


_RosMgmtOspfVirtNbrMode_Type.__name__ = "Integer32"
_RosMgmtOspfVirtNbrMode_Object = MibTableColumn
rosMgmtOspfVirtNbrMode = _RosMgmtOspfVirtNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 10, 1, 9),
    _RosMgmtOspfVirtNbrMode_Type()
)
rosMgmtOspfVirtNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrMode.setStatus("current")
_RosMgmtOspfAreaAggregateTable_Object = MibTable
rosMgmtOspfAreaAggregateTable = _RosMgmtOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11)
)
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateTable.setStatus("current")
_RosMgmtOspfAreaAggregateEntry_Object = MibTableRow
rosMgmtOspfAreaAggregateEntry = _RosMgmtOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1)
)
rosMgmtOspfAreaAggregateEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaAggregateAreaID"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaAggregateLsdbType"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaAggregateNet"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateEntry.setStatus("current")
_RosMgmtOspfAreaAggregateAreaID_Type = AreaID
_RosMgmtOspfAreaAggregateAreaID_Object = MibTableColumn
rosMgmtOspfAreaAggregateAreaID = _RosMgmtOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1, 1),
    _RosMgmtOspfAreaAggregateAreaID_Type()
)
rosMgmtOspfAreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateAreaID.setStatus("current")


class _RosMgmtOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type rosMgmtOspfAreaAggregateLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("summaryLink", 3),
          ("nssaExternalLink", 7))
    )


_RosMgmtOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_RosMgmtOspfAreaAggregateLsdbType_Object = MibTableColumn
rosMgmtOspfAreaAggregateLsdbType = _RosMgmtOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1, 2),
    _RosMgmtOspfAreaAggregateLsdbType_Type()
)
rosMgmtOspfAreaAggregateLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateLsdbType.setStatus("current")
_RosMgmtOspfAreaAggregateNet_Type = IpAddress
_RosMgmtOspfAreaAggregateNet_Object = MibTableColumn
rosMgmtOspfAreaAggregateNet = _RosMgmtOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1, 3),
    _RosMgmtOspfAreaAggregateNet_Type()
)
rosMgmtOspfAreaAggregateNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateNet.setStatus("current")
_RosMgmtOspfAreaAggregateMask_Type = IpAddress
_RosMgmtOspfAreaAggregateMask_Object = MibTableColumn
rosMgmtOspfAreaAggregateMask = _RosMgmtOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1, 4),
    _RosMgmtOspfAreaAggregateMask_Type()
)
rosMgmtOspfAreaAggregateMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateMask.setStatus("current")


class _RosMgmtOspfAreaAggregateEffect_Type(Integer32):
    """Custom type rosMgmtOspfAreaAggregateEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_RosMgmtOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_RosMgmtOspfAreaAggregateEffect_Object = MibTableColumn
rosMgmtOspfAreaAggregateEffect = _RosMgmtOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1, 5),
    _RosMgmtOspfAreaAggregateEffect_Type()
)
rosMgmtOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateEffect.setStatus("current")
_RosMgmtOspfAreaAggregateStatus_Type = RowStatus
_RosMgmtOspfAreaAggregateStatus_Object = MibTableColumn
rosMgmtOspfAreaAggregateStatus = _RosMgmtOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 11, 1, 6),
    _RosMgmtOspfAreaAggregateStatus_Type()
)
rosMgmtOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaAggregateStatus.setStatus("current")
_RosMgmtOspfExternalAggregateTable_Object = MibTable
rosMgmtOspfExternalAggregateTable = _RosMgmtOspfExternalAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12)
)
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateTable.setStatus("current")
_RosMgmtOspfExternalAggregateEntry_Object = MibTableRow
rosMgmtOspfExternalAggregateEntry = _RosMgmtOspfExternalAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12, 1)
)
rosMgmtOspfExternalAggregateEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfExternalAggregateNet"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfExternalAggregateMask"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateEntry.setStatus("current")
_RosMgmtOspfExternalAggregateNet_Type = IpAddress
_RosMgmtOspfExternalAggregateNet_Object = MibTableColumn
rosMgmtOspfExternalAggregateNet = _RosMgmtOspfExternalAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12, 1, 1),
    _RosMgmtOspfExternalAggregateNet_Type()
)
rosMgmtOspfExternalAggregateNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateNet.setStatus("current")
_RosMgmtOspfExternalAggregateMask_Type = IpAddress
_RosMgmtOspfExternalAggregateMask_Object = MibTableColumn
rosMgmtOspfExternalAggregateMask = _RosMgmtOspfExternalAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12, 1, 2),
    _RosMgmtOspfExternalAggregateMask_Type()
)
rosMgmtOspfExternalAggregateMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateMask.setStatus("current")


class _RosMgmtOspfExternalAggregateEffect_Type(Integer32):
    """Custom type rosMgmtOspfExternalAggregateEffect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotAdvertise", 1),
          ("advertise", 2))
    )


_RosMgmtOspfExternalAggregateEffect_Type.__name__ = "Integer32"
_RosMgmtOspfExternalAggregateEffect_Object = MibTableColumn
rosMgmtOspfExternalAggregateEffect = _RosMgmtOspfExternalAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12, 1, 3),
    _RosMgmtOspfExternalAggregateEffect_Type()
)
rosMgmtOspfExternalAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateEffect.setStatus("current")


class _RosMgmtOspfExternalAggregateCost_Type(BigMetric):
    """Custom type rosMgmtOspfExternalAggregateCost based on BigMetric"""
    defaultValue = 1


_RosMgmtOspfExternalAggregateCost_Type.__name__ = "BigMetric"
_RosMgmtOspfExternalAggregateCost_Object = MibTableColumn
rosMgmtOspfExternalAggregateCost = _RosMgmtOspfExternalAggregateCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12, 1, 4),
    _RosMgmtOspfExternalAggregateCost_Type()
)
rosMgmtOspfExternalAggregateCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateCost.setStatus("current")
_RosMgmtOspfExternalAggregateStatus_Type = RowStatus
_RosMgmtOspfExternalAggregateStatus_Object = MibTableColumn
rosMgmtOspfExternalAggregateStatus = _RosMgmtOspfExternalAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 12, 1, 5),
    _RosMgmtOspfExternalAggregateStatus_Type()
)
rosMgmtOspfExternalAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfExternalAggregateStatus.setStatus("current")
_RosMgmtOspfLsdbTable_Object = MibTable
rosMgmtOspfLsdbTable = _RosMgmtOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13)
)
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbTable.setStatus("current")
_RosMgmtOspfLsdbEntry_Object = MibTableRow
rosMgmtOspfLsdbEntry = _RosMgmtOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1)
)
rosMgmtOspfLsdbEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbAreaId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbType"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbLsId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbEntry.setStatus("current")
_RosMgmtOspfLsdbAreaId_Type = AreaID
_RosMgmtOspfLsdbAreaId_Object = MibTableColumn
rosMgmtOspfLsdbAreaId = _RosMgmtOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 1),
    _RosMgmtOspfLsdbAreaId_Type()
)
rosMgmtOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbAreaId.setStatus("current")


class _RosMgmtOspfLsdbType_Type(Integer32):
    """Custom type rosMgmtOspfLsdbType based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("linkOpaqueLink", 9),
          ("areaOpaqueLink", 10),
          ("asOpaqueLink", 11))
    )


_RosMgmtOspfLsdbType_Type.__name__ = "Integer32"
_RosMgmtOspfLsdbType_Object = MibTableColumn
rosMgmtOspfLsdbType = _RosMgmtOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 2),
    _RosMgmtOspfLsdbType_Type()
)
rosMgmtOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbType.setStatus("current")
_RosMgmtOspfLsdbLsId_Type = IpAddress
_RosMgmtOspfLsdbLsId_Object = MibTableColumn
rosMgmtOspfLsdbLsId = _RosMgmtOspfLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 3),
    _RosMgmtOspfLsdbLsId_Type()
)
rosMgmtOspfLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbLsId.setStatus("current")
_RosMgmtOspfLsdbRouterId_Type = RouterID
_RosMgmtOspfLsdbRouterId_Object = MibTableColumn
rosMgmtOspfLsdbRouterId = _RosMgmtOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 4),
    _RosMgmtOspfLsdbRouterId_Type()
)
rosMgmtOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbRouterId.setStatus("current")
_RosMgmtOspfLsdbSequence_Type = Integer32
_RosMgmtOspfLsdbSequence_Object = MibTableColumn
rosMgmtOspfLsdbSequence = _RosMgmtOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 5),
    _RosMgmtOspfLsdbSequence_Type()
)
rosMgmtOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbSequence.setStatus("current")
_RosMgmtOspfLsdbAge_Type = Integer32
_RosMgmtOspfLsdbAge_Object = MibTableColumn
rosMgmtOspfLsdbAge = _RosMgmtOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 6),
    _RosMgmtOspfLsdbAge_Type()
)
rosMgmtOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbAge.setUnits("seconds")
_RosMgmtOspfLsdbChecksum_Type = Integer32
_RosMgmtOspfLsdbChecksum_Object = MibTableColumn
rosMgmtOspfLsdbChecksum = _RosMgmtOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 7),
    _RosMgmtOspfLsdbChecksum_Type()
)
rosMgmtOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbChecksum.setStatus("current")
_RosMgmtOspfLsdbAdvertisement_Type = OctetString
_RosMgmtOspfLsdbAdvertisement_Object = MibTableColumn
rosMgmtOspfLsdbAdvertisement = _RosMgmtOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 13, 1, 8),
    _RosMgmtOspfLsdbAdvertisement_Type()
)
rosMgmtOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbAdvertisement.setStatus("current")
_RosMgmtOspfAsLsdbTable_Object = MibTable
rosMgmtOspfAsLsdbTable = _RosMgmtOspfAsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14)
)
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbTable.setStatus("current")
_RosMgmtOspfAsLsdbEntry_Object = MibTableRow
rosMgmtOspfAsLsdbEntry = _RosMgmtOspfAsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1)
)
rosMgmtOspfAsLsdbEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAsLsdbType"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAsLsdbLsId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAsLsdbRouterId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbEntry.setStatus("current")


class _RosMgmtOspfAsLsdbType_Type(Integer32):
    """Custom type rosMgmtOspfAsLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_RosMgmtOspfAsLsdbType_Type.__name__ = "Integer32"
_RosMgmtOspfAsLsdbType_Object = MibTableColumn
rosMgmtOspfAsLsdbType = _RosMgmtOspfAsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 1),
    _RosMgmtOspfAsLsdbType_Type()
)
rosMgmtOspfAsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbType.setStatus("current")
_RosMgmtOspfAsLsdbLsId_Type = IpAddress
_RosMgmtOspfAsLsdbLsId_Object = MibTableColumn
rosMgmtOspfAsLsdbLsId = _RosMgmtOspfAsLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 2),
    _RosMgmtOspfAsLsdbLsId_Type()
)
rosMgmtOspfAsLsdbLsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbLsId.setStatus("current")
_RosMgmtOspfAsLsdbRouterId_Type = RouterID
_RosMgmtOspfAsLsdbRouterId_Object = MibTableColumn
rosMgmtOspfAsLsdbRouterId = _RosMgmtOspfAsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 3),
    _RosMgmtOspfAsLsdbRouterId_Type()
)
rosMgmtOspfAsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbRouterId.setStatus("current")
_RosMgmtOspfAsLsdbSequence_Type = Integer32
_RosMgmtOspfAsLsdbSequence_Object = MibTableColumn
rosMgmtOspfAsLsdbSequence = _RosMgmtOspfAsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 4),
    _RosMgmtOspfAsLsdbSequence_Type()
)
rosMgmtOspfAsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbSequence.setStatus("current")
_RosMgmtOspfAsLsdbAge_Type = Integer32
_RosMgmtOspfAsLsdbAge_Object = MibTableColumn
rosMgmtOspfAsLsdbAge = _RosMgmtOspfAsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 5),
    _RosMgmtOspfAsLsdbAge_Type()
)
rosMgmtOspfAsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbAge.setUnits("seconds")
_RosMgmtOspfAsLsdbChecksum_Type = Integer32
_RosMgmtOspfAsLsdbChecksum_Object = MibTableColumn
rosMgmtOspfAsLsdbChecksum = _RosMgmtOspfAsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 6),
    _RosMgmtOspfAsLsdbChecksum_Type()
)
rosMgmtOspfAsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbChecksum.setStatus("current")
_RosMgmtOspfAsLsdbAdvertisement_Type = OctetString
_RosMgmtOspfAsLsdbAdvertisement_Object = MibTableColumn
rosMgmtOspfAsLsdbAdvertisement = _RosMgmtOspfAsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 14, 1, 7),
    _RosMgmtOspfAsLsdbAdvertisement_Type()
)
rosMgmtOspfAsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAsLsdbAdvertisement.setStatus("current")
_RosMgmtOspfAreaLsaCountTable_Object = MibTable
rosMgmtOspfAreaLsaCountTable = _RosMgmtOspfAreaLsaCountTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 15)
)
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCountTable.setStatus("current")
_RosMgmtOspfAreaLsaCountEntry_Object = MibTableRow
rosMgmtOspfAreaLsaCountEntry = _RosMgmtOspfAreaLsaCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 15, 1)
)
rosMgmtOspfAreaLsaCountEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaLsaCountAreaId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAreaLsaCountLsaType"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCountEntry.setStatus("current")
_RosMgmtOspfAreaLsaCountAreaId_Type = AreaID
_RosMgmtOspfAreaLsaCountAreaId_Object = MibTableColumn
rosMgmtOspfAreaLsaCountAreaId = _RosMgmtOspfAreaLsaCountAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 15, 1, 1),
    _RosMgmtOspfAreaLsaCountAreaId_Type()
)
rosMgmtOspfAreaLsaCountAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCountAreaId.setStatus("current")


class _RosMgmtOspfAreaLsaCountLsaType_Type(Integer32):
    """Custom type rosMgmtOspfAreaLsaCountLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("nssaExternalLink", 7),
          ("linkOpaqueLink", 9),
          ("areaOpaqueLink", 10))
    )


_RosMgmtOspfAreaLsaCountLsaType_Type.__name__ = "Integer32"
_RosMgmtOspfAreaLsaCountLsaType_Object = MibTableColumn
rosMgmtOspfAreaLsaCountLsaType = _RosMgmtOspfAreaLsaCountLsaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 15, 1, 2),
    _RosMgmtOspfAreaLsaCountLsaType_Type()
)
rosMgmtOspfAreaLsaCountLsaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCountLsaType.setStatus("current")
_RosMgmtOspfAreaLsaCountNumber_Type = Gauge32
_RosMgmtOspfAreaLsaCountNumber_Object = MibTableColumn
rosMgmtOspfAreaLsaCountNumber = _RosMgmtOspfAreaLsaCountNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 15, 1, 3),
    _RosMgmtOspfAreaLsaCountNumber_Type()
)
rosMgmtOspfAreaLsaCountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfAreaLsaCountNumber.setStatus("current")
_RosMgmtOspfRedistributeTable_Object = MibTable
rosMgmtOspfRedistributeTable = _RosMgmtOspfRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16)
)
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeTable.setStatus("current")
_RosMgmtOspfRedistributeEntry_Object = MibTableRow
rosMgmtOspfRedistributeEntry = _RosMgmtOspfRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1)
)
rosMgmtOspfRedistributeEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeProtocol"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeEntry.setStatus("current")


class _RosMgmtOspfRedistributeProtocol_Type(Integer32):
    """Custom type rosMgmtOspfRedistributeProtocol based on Integer32"""
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
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isis", 9),
          ("esis", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14))
    )


_RosMgmtOspfRedistributeProtocol_Type.__name__ = "Integer32"
_RosMgmtOspfRedistributeProtocol_Object = MibTableColumn
rosMgmtOspfRedistributeProtocol = _RosMgmtOspfRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 1),
    _RosMgmtOspfRedistributeProtocol_Type()
)
rosMgmtOspfRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeProtocol.setStatus("current")
_RosMgmtOspfRedistributeProcessId_Type = ProcessID
_RosMgmtOspfRedistributeProcessId_Object = MibTableColumn
rosMgmtOspfRedistributeProcessId = _RosMgmtOspfRedistributeProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 2),
    _RosMgmtOspfRedistributeProcessId_Type()
)
rosMgmtOspfRedistributeProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeProcessId.setStatus("current")


class _RosMgmtOspfRedistributeCost_Type(BigMetric):
    """Custom type rosMgmtOspfRedistributeCost based on BigMetric"""
    defaultValue = 1


_RosMgmtOspfRedistributeCost_Type.__name__ = "BigMetric"
_RosMgmtOspfRedistributeCost_Object = MibTableColumn
rosMgmtOspfRedistributeCost = _RosMgmtOspfRedistributeCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 3),
    _RosMgmtOspfRedistributeCost_Type()
)
rosMgmtOspfRedistributeCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeCost.setStatus("current")


class _RosMgmtOspfRedistributeType_Type(Integer32):
    """Custom type rosMgmtOspfRedistributeType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e2", 2))
    )


_RosMgmtOspfRedistributeType_Type.__name__ = "Integer32"
_RosMgmtOspfRedistributeType_Object = MibTableColumn
rosMgmtOspfRedistributeType = _RosMgmtOspfRedistributeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 4),
    _RosMgmtOspfRedistributeType_Type()
)
rosMgmtOspfRedistributeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeType.setStatus("current")
_RosMgmtOspfRedistributeStatus_Type = RowStatus
_RosMgmtOspfRedistributeStatus_Object = MibTableColumn
rosMgmtOspfRedistributeStatus = _RosMgmtOspfRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 5),
    _RosMgmtOspfRedistributeStatus_Type()
)
rosMgmtOspfRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeStatus.setStatus("current")
_RosMgmtOspfRedistributeRouteMapName_Type = OctetString
_RosMgmtOspfRedistributeRouteMapName_Object = MibTableColumn
rosMgmtOspfRedistributeRouteMapName = _RosMgmtOspfRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 6),
    _RosMgmtOspfRedistributeRouteMapName_Type()
)
rosMgmtOspfRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeRouteMapName.setStatus("current")
_RosMgmtOspfRedistributeTag_Type = Unsigned32
_RosMgmtOspfRedistributeTag_Object = MibTableColumn
rosMgmtOspfRedistributeTag = _RosMgmtOspfRedistributeTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 16, 1, 7),
    _RosMgmtOspfRedistributeTag_Type()
)
rosMgmtOspfRedistributeTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeTag.setStatus("current")
_RosMgmtOspfDefaultInfoTable_Object = MibTable
rosMgmtOspfDefaultInfoTable = _RosMgmtOspfDefaultInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 17)
)
if mibBuilder.loadTexts:
    rosMgmtOspfDefaultInfoTable.setStatus("current")
_RosMgmtOspfDefaultInfoEntry_Object = MibTableRow
rosMgmtOspfDefaultInfoEntry = _RosMgmtOspfDefaultInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 17, 1)
)
rosMgmtOspfDefaultInfoEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfDefaultInfoEntry.setStatus("current")


class _RosMgmtOspfDefaultInfoAlways_Type(TruthValue):
    """Custom type rosMgmtOspfDefaultInfoAlways based on TruthValue"""
    defaultValue = 2


_RosMgmtOspfDefaultInfoAlways_Type.__name__ = "TruthValue"
_RosMgmtOspfDefaultInfoAlways_Object = MibTableColumn
rosMgmtOspfDefaultInfoAlways = _RosMgmtOspfDefaultInfoAlways_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 17, 1, 1),
    _RosMgmtOspfDefaultInfoAlways_Type()
)
rosMgmtOspfDefaultInfoAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDefaultInfoAlways.setStatus("current")


class _RosMgmtOspfDefaultInfoCost_Type(BigMetric):
    """Custom type rosMgmtOspfDefaultInfoCost based on BigMetric"""
    defaultValue = 1


_RosMgmtOspfDefaultInfoCost_Type.__name__ = "BigMetric"
_RosMgmtOspfDefaultInfoCost_Object = MibTableColumn
rosMgmtOspfDefaultInfoCost = _RosMgmtOspfDefaultInfoCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 17, 1, 2),
    _RosMgmtOspfDefaultInfoCost_Type()
)
rosMgmtOspfDefaultInfoCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDefaultInfoCost.setStatus("current")


class _RosMgmtOspfDefaultInfoType_Type(Integer32):
    """Custom type rosMgmtOspfDefaultInfoType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e2", 2))
    )


_RosMgmtOspfDefaultInfoType_Type.__name__ = "Integer32"
_RosMgmtOspfDefaultInfoType_Object = MibTableColumn
rosMgmtOspfDefaultInfoType = _RosMgmtOspfDefaultInfoType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 17, 1, 3),
    _RosMgmtOspfDefaultInfoType_Type()
)
rosMgmtOspfDefaultInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDefaultInfoType.setStatus("current")
_RosMgmtOspfDefaultInfoStatus_Type = RowStatus
_RosMgmtOspfDefaultInfoStatus_Object = MibTableColumn
rosMgmtOspfDefaultInfoStatus = _RosMgmtOspfDefaultInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 17, 1, 4),
    _RosMgmtOspfDefaultInfoStatus_Type()
)
rosMgmtOspfDefaultInfoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDefaultInfoStatus.setStatus("current")
_RosMgmtOspfPacketIoStatisTable_Object = MibTable
rosMgmtOspfPacketIoStatisTable = _RosMgmtOspfPacketIoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 18)
)
if mibBuilder.loadTexts:
    rosMgmtOspfPacketIoStatisTable.setStatus("current")
_RosMgmtOspfPacketIoStatisEntry_Object = MibTableRow
rosMgmtOspfPacketIoStatisEntry = _RosMgmtOspfPacketIoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 18, 1)
)
rosMgmtOspfPacketIoStatisEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketIoStatisIoType"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketIoStatisPktType"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfPacketIoStatisEntry.setStatus("current")


class _RosMgmtOspfPacketIoStatisIoType_Type(Integer32):
    """Custom type rosMgmtOspfPacketIoStatisIoType based on Integer32"""
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


_RosMgmtOspfPacketIoStatisIoType_Type.__name__ = "Integer32"
_RosMgmtOspfPacketIoStatisIoType_Object = MibTableColumn
rosMgmtOspfPacketIoStatisIoType = _RosMgmtOspfPacketIoStatisIoType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 18, 1, 1),
    _RosMgmtOspfPacketIoStatisIoType_Type()
)
rosMgmtOspfPacketIoStatisIoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfPacketIoStatisIoType.setStatus("current")


class _RosMgmtOspfPacketIoStatisPktType_Type(Integer32):
    """Custom type rosMgmtOspfPacketIoStatisPktType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5))
    )


_RosMgmtOspfPacketIoStatisPktType_Type.__name__ = "Integer32"
_RosMgmtOspfPacketIoStatisPktType_Object = MibTableColumn
rosMgmtOspfPacketIoStatisPktType = _RosMgmtOspfPacketIoStatisPktType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 18, 1, 2),
    _RosMgmtOspfPacketIoStatisPktType_Type()
)
rosMgmtOspfPacketIoStatisPktType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfPacketIoStatisPktType.setStatus("current")
_RosMgmtOspfPacketIoStatisNumber_Type = Integer32
_RosMgmtOspfPacketIoStatisNumber_Object = MibTableColumn
rosMgmtOspfPacketIoStatisNumber = _RosMgmtOspfPacketIoStatisNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 18, 1, 3),
    _RosMgmtOspfPacketIoStatisNumber_Type()
)
rosMgmtOspfPacketIoStatisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfPacketIoStatisNumber.setStatus("current")
_RosMgmtOspfRouteTable_Object = MibTable
rosMgmtOspfRouteTable = _RosMgmtOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19)
)
if mibBuilder.loadTexts:
    rosMgmtOspfRouteTable.setStatus("current")
_RosMgmtOspfRouteEntry_Object = MibTableRow
rosMgmtOspfRouteEntry = _RosMgmtOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1)
)
rosMgmtOspfRouteEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouteDest"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouteMask"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouteType"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfRouteEntry.setStatus("current")
_RosMgmtOspfRouteDest_Type = IpAddress
_RosMgmtOspfRouteDest_Object = MibTableColumn
rosMgmtOspfRouteDest = _RosMgmtOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 1),
    _RosMgmtOspfRouteDest_Type()
)
rosMgmtOspfRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteDest.setStatus("current")
_RosMgmtOspfRouteMask_Type = IpAddress
_RosMgmtOspfRouteMask_Object = MibTableColumn
rosMgmtOspfRouteMask = _RosMgmtOspfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 2),
    _RosMgmtOspfRouteMask_Type()
)
rosMgmtOspfRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteMask.setStatus("current")


class _RosMgmtOspfRouteType_Type(Integer32):
    """Custom type rosMgmtOspfRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_RosMgmtOspfRouteType_Type.__name__ = "Integer32"
_RosMgmtOspfRouteType_Object = MibTableColumn
rosMgmtOspfRouteType = _RosMgmtOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 3),
    _RosMgmtOspfRouteType_Type()
)
rosMgmtOspfRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteType.setStatus("current")


class _RosMgmtOspfRouteLsType_Type(Integer32):
    """Custom type rosMgmtOspfRouteLsType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("stub", 0),
          ("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_RosMgmtOspfRouteLsType_Type.__name__ = "Integer32"
_RosMgmtOspfRouteLsType_Object = MibTableColumn
rosMgmtOspfRouteLsType = _RosMgmtOspfRouteLsType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 4),
    _RosMgmtOspfRouteLsType_Type()
)
rosMgmtOspfRouteLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteLsType.setStatus("current")
_RosMgmtOspfRouteMetric_Type = Integer32
_RosMgmtOspfRouteMetric_Object = MibTableColumn
rosMgmtOspfRouteMetric = _RosMgmtOspfRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 5),
    _RosMgmtOspfRouteMetric_Type()
)
rosMgmtOspfRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteMetric.setStatus("current")
_RosMgmtOspfRouteNextHop_Type = IpAddress
_RosMgmtOspfRouteNextHop_Object = MibTableColumn
rosMgmtOspfRouteNextHop = _RosMgmtOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 6),
    _RosMgmtOspfRouteNextHop_Type()
)
rosMgmtOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteNextHop.setStatus("current")
_RosMgmtOspfRouteAdvRtr_Type = IpAddress
_RosMgmtOspfRouteAdvRtr_Object = MibTableColumn
rosMgmtOspfRouteAdvRtr = _RosMgmtOspfRouteAdvRtr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 7),
    _RosMgmtOspfRouteAdvRtr_Type()
)
rosMgmtOspfRouteAdvRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteAdvRtr.setStatus("current")
_RosMgmtOspfRouteArea_Type = Integer32
_RosMgmtOspfRouteArea_Object = MibTableColumn
rosMgmtOspfRouteArea = _RosMgmtOspfRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 19, 1, 8),
    _RosMgmtOspfRouteArea_Type()
)
rosMgmtOspfRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfRouteArea.setStatus("current")
_RosMgmtOspfBdrRouteTable_Object = MibTable
rosMgmtOspfBdrRouteTable = _RosMgmtOspfBdrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20)
)
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteTable.setStatus("current")
_RosMgmtOspfBdrRouteEntry_Object = MibTableRow
rosMgmtOspfBdrRouteEntry = _RosMgmtOspfBdrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1)
)
rosMgmtOspfBdrRouteEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfBdrRouteRtrType"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfBdrRouteArea"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfBdrRouteDest"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfBdrRouteNextHop"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteEntry.setStatus("current")


class _RosMgmtOspfBdrRouteRtrType_Type(Integer32):
    """Custom type rosMgmtOspfBdrRouteRtrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 119),
    )


_RosMgmtOspfBdrRouteRtrType_Type.__name__ = "Integer32"
_RosMgmtOspfBdrRouteRtrType_Object = MibTableColumn
rosMgmtOspfBdrRouteRtrType = _RosMgmtOspfBdrRouteRtrType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1, 1),
    _RosMgmtOspfBdrRouteRtrType_Type()
)
rosMgmtOspfBdrRouteRtrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteRtrType.setStatus("current")
_RosMgmtOspfBdrRouteArea_Type = IpAddress
_RosMgmtOspfBdrRouteArea_Object = MibTableColumn
rosMgmtOspfBdrRouteArea = _RosMgmtOspfBdrRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1, 2),
    _RosMgmtOspfBdrRouteArea_Type()
)
rosMgmtOspfBdrRouteArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteArea.setStatus("current")
_RosMgmtOspfBdrRouteDest_Type = IpAddress
_RosMgmtOspfBdrRouteDest_Object = MibTableColumn
rosMgmtOspfBdrRouteDest = _RosMgmtOspfBdrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1, 3),
    _RosMgmtOspfBdrRouteDest_Type()
)
rosMgmtOspfBdrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteDest.setStatus("current")
_RosMgmtOspfBdrRouteNextHop_Type = IpAddress
_RosMgmtOspfBdrRouteNextHop_Object = MibTableColumn
rosMgmtOspfBdrRouteNextHop = _RosMgmtOspfBdrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1, 4),
    _RosMgmtOspfBdrRouteNextHop_Type()
)
rosMgmtOspfBdrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteNextHop.setStatus("current")


class _RosMgmtOspfBdrRouteLsType_Type(Integer32):
    """Custom type rosMgmtOspfBdrRouteLsType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_RosMgmtOspfBdrRouteLsType_Type.__name__ = "Integer32"
_RosMgmtOspfBdrRouteLsType_Object = MibTableColumn
rosMgmtOspfBdrRouteLsType = _RosMgmtOspfBdrRouteLsType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1, 5),
    _RosMgmtOspfBdrRouteLsType_Type()
)
rosMgmtOspfBdrRouteLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteLsType.setStatus("current")
_RosMgmtOspfBdrRouteMetric_Type = Integer32
_RosMgmtOspfBdrRouteMetric_Object = MibTableColumn
rosMgmtOspfBdrRouteMetric = _RosMgmtOspfBdrRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 20, 1, 6),
    _RosMgmtOspfBdrRouteMetric_Type()
)
rosMgmtOspfBdrRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOspfBdrRouteMetric.setStatus("current")
_RosMgmtOspfDistributeListGroup_ObjectIdentity = ObjectIdentity
rosMgmtOspfDistributeListGroup = _RosMgmtOspfDistributeListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21)
)
_RosMgmtOspfDistributeListInTable_Object = MibTable
rosMgmtOspfDistributeListInTable = _RosMgmtOspfDistributeListInTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOspfDistributeListInTable.setStatus("current")
_RosMgmtOspfDistributeListInEntry_Object = MibTableRow
rosMgmtOspfDistributeListInEntry = _RosMgmtOspfDistributeListInEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 1, 1)
)
rosMgmtOspfDistributeListInEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfDistributeListInEntry.setStatus("current")
_RosMgmtOspfDistrInIpPrefixListName_Type = OctetString
_RosMgmtOspfDistrInIpPrefixListName_Object = MibTableColumn
rosMgmtOspfDistrInIpPrefixListName = _RosMgmtOspfDistrInIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 1, 1, 1),
    _RosMgmtOspfDistrInIpPrefixListName_Type()
)
rosMgmtOspfDistrInIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrInIpPrefixListName.setStatus("current")
_RosMgmtOspfDistrInAclNum_Type = Integer32
_RosMgmtOspfDistrInAclNum_Object = MibTableColumn
rosMgmtOspfDistrInAclNum = _RosMgmtOspfDistrInAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 1, 1, 2),
    _RosMgmtOspfDistrInAclNum_Type()
)
rosMgmtOspfDistrInAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrInAclNum.setStatus("current")
_RosMgmtOspfDistrInRowStatus_Type = RowStatus
_RosMgmtOspfDistrInRowStatus_Object = MibTableColumn
rosMgmtOspfDistrInRowStatus = _RosMgmtOspfDistrInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 1, 1, 3),
    _RosMgmtOspfDistrInRowStatus_Type()
)
rosMgmtOspfDistrInRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrInRowStatus.setStatus("current")
_RosMgmtOspfDistributeListOutTable_Object = MibTable
rosMgmtOspfDistributeListOutTable = _RosMgmtOspfDistributeListOutTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 2)
)
if mibBuilder.loadTexts:
    rosMgmtOspfDistributeListOutTable.setStatus("current")
_RosMgmtOspfDistributeListOutEntry_Object = MibTableRow
rosMgmtOspfDistributeListOutEntry = _RosMgmtOspfDistributeListOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 2, 1)
)
rosMgmtOspfDistributeListOutEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfDistributeListOutEntry.setStatus("current")
_RosMgmtOspfDistrOutIpPrefixListName_Type = OctetString
_RosMgmtOspfDistrOutIpPrefixListName_Object = MibTableColumn
rosMgmtOspfDistrOutIpPrefixListName = _RosMgmtOspfDistrOutIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 2, 1, 1),
    _RosMgmtOspfDistrOutIpPrefixListName_Type()
)
rosMgmtOspfDistrOutIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutIpPrefixListName.setStatus("current")
_RosMgmtOspfDistrOutAclNum_Type = Integer32
_RosMgmtOspfDistrOutAclNum_Object = MibTableColumn
rosMgmtOspfDistrOutAclNum = _RosMgmtOspfDistrOutAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 2, 1, 2),
    _RosMgmtOspfDistrOutAclNum_Type()
)
rosMgmtOspfDistrOutAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutAclNum.setStatus("current")
_RosMgmtOspfDistrOutRowStatus_Type = RowStatus
_RosMgmtOspfDistrOutRowStatus_Object = MibTableColumn
rosMgmtOspfDistrOutRowStatus = _RosMgmtOspfDistrOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 2, 1, 3),
    _RosMgmtOspfDistrOutRowStatus_Type()
)
rosMgmtOspfDistrOutRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutRowStatus.setStatus("current")
_RosMgmtOspfDistributeListOutProtocolTable_Object = MibTable
rosMgmtOspfDistributeListOutProtocolTable = _RosMgmtOspfDistributeListOutProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3)
)
if mibBuilder.loadTexts:
    rosMgmtOspfDistributeListOutProtocolTable.setStatus("current")
_RosMgmtOspfDistributeListOutProtocolEntry_Object = MibTableRow
rosMgmtOspfDistributeListOutProtocolEntry = _RosMgmtOspfDistributeListOutProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3, 1)
)
rosMgmtOspfDistributeListOutProtocolEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfDistrOutProtocol"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfDistrOutProcessId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfDistributeListOutProtocolEntry.setStatus("current")


class _RosMgmtOspfDistrOutProtocol_Type(Integer32):
    """Custom type rosMgmtOspfDistrOutProtocol based on Integer32"""
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
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isis", 9),
          ("esis", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14))
    )


_RosMgmtOspfDistrOutProtocol_Type.__name__ = "Integer32"
_RosMgmtOspfDistrOutProtocol_Object = MibTableColumn
rosMgmtOspfDistrOutProtocol = _RosMgmtOspfDistrOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3, 1, 1),
    _RosMgmtOspfDistrOutProtocol_Type()
)
rosMgmtOspfDistrOutProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutProtocol.setStatus("current")
_RosMgmtOspfDistrOutProcessId_Type = ProcessID
_RosMgmtOspfDistrOutProcessId_Object = MibTableColumn
rosMgmtOspfDistrOutProcessId = _RosMgmtOspfDistrOutProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3, 1, 2),
    _RosMgmtOspfDistrOutProcessId_Type()
)
rosMgmtOspfDistrOutProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutProcessId.setStatus("current")
_RosMgmtOspfDistrOutProIpPrefixListName_Type = OctetString
_RosMgmtOspfDistrOutProIpPrefixListName_Object = MibTableColumn
rosMgmtOspfDistrOutProIpPrefixListName = _RosMgmtOspfDistrOutProIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3, 1, 3),
    _RosMgmtOspfDistrOutProIpPrefixListName_Type()
)
rosMgmtOspfDistrOutProIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutProIpPrefixListName.setStatus("current")
_RosMgmtOspfDistrOutProAclNum_Type = Integer32
_RosMgmtOspfDistrOutProAclNum_Object = MibTableColumn
rosMgmtOspfDistrOutProAclNum = _RosMgmtOspfDistrOutProAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3, 1, 4),
    _RosMgmtOspfDistrOutProAclNum_Type()
)
rosMgmtOspfDistrOutProAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutProAclNum.setStatus("current")
_RosMgmtOspfDistrOutProRowStatus_Type = RowStatus
_RosMgmtOspfDistrOutProRowStatus_Object = MibTableColumn
rosMgmtOspfDistrOutProRowStatus = _RosMgmtOspfDistrOutProRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 21, 3, 1, 5),
    _RosMgmtOspfDistrOutProRowStatus_Type()
)
rosMgmtOspfDistrOutProRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDistrOutProRowStatus.setStatus("current")
_RosMgmtOspfDNBitCheckDisableSummaryTable_Object = MibTable
rosMgmtOspfDNBitCheckDisableSummaryTable = _RosMgmtOspfDNBitCheckDisableSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 22)
)
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableSummaryTable.setStatus("current")
_RosMgmtOspfDNBitCheckDisableSummaryEntry_Object = MibTableRow
rosMgmtOspfDNBitCheckDisableSummaryEntry = _RosMgmtOspfDNBitCheckDisableSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 22, 1)
)
rosMgmtOspfDNBitCheckDisableSummaryEntry.setIndexNames(
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
    (0, "ROSMGMT-OSPFV2-MIB", "rosMgmtOspfDNBitCheckDisableSummaryRtrId"),
)
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableSummaryEntry.setStatus("current")
_RosMgmtOspfDNBitCheckDisableSummaryRtrId_Type = RouterID
_RosMgmtOspfDNBitCheckDisableSummaryRtrId_Object = MibTableColumn
rosMgmtOspfDNBitCheckDisableSummaryRtrId = _RosMgmtOspfDNBitCheckDisableSummaryRtrId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 22, 1, 1),
    _RosMgmtOspfDNBitCheckDisableSummaryRtrId_Type()
)
rosMgmtOspfDNBitCheckDisableSummaryRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableSummaryRtrId.setStatus("current")
_RosMgmtOspfDNBitCheckDisableSummaryStatus_Type = RowStatus
_RosMgmtOspfDNBitCheckDisableSummaryStatus_Object = MibTableColumn
rosMgmtOspfDNBitCheckDisableSummaryStatus = _RosMgmtOspfDNBitCheckDisableSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 2, 22, 1, 2),
    _RosMgmtOspfDNBitCheckDisableSummaryStatus_Type()
)
rosMgmtOspfDNBitCheckDisableSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rosMgmtOspfDNBitCheckDisableSummaryStatus.setStatus("current")
_RosMgmtOspfConformance_ObjectIdentity = ObjectIdentity
rosMgmtOspfConformance = _RosMgmtOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 3)
)

# Managed Objects groups


# Notification objects

rosMgmtOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 1)
)
rosMgmtOspfIfStateChange.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfState"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfStateChange.setStatus(
        "current"
    )

rosMgmtOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 2)
)
rosMgmtOspfVirtIfStateChange.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfStateChange.setStatus(
        "current"
    )

rosMgmtOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 3)
)
rosMgmtOspfNbrStateChange.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrIpAddr"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrAddressLessIndex"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrRtrId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrState"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfNbrStateChange.setStatus(
        "current"
    )

rosMgmtOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 4)
)
rosMgmtOspfVirtNbrStateChange.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtNbrArea"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtNbrRtrId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtNbrStateChange.setStatus(
        "current"
    )

rosMgmtOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 5)
)
rosMgmtOspfIfConfigError.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketSrc"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfConfigErrorType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfConfigError.setStatus(
        "current"
    )

rosMgmtOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 6)
)
rosMgmtOspfVirtIfConfigError.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfConfigErrorType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfConfigError.setStatus(
        "current"
    )

rosMgmtOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 7)
)
rosMgmtOspfIfAuthFailure.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketSrc"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfConfigErrorType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfAuthFailure.setStatus(
        "current"
    )

rosMgmtOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 8)
)
rosMgmtOspfVirtIfAuthFailure.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfConfigErrorType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfAuthFailure.setStatus(
        "current"
    )

rosMgmtOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 9)
)
rosMgmtOspfIfRxBadPacket.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketSrc"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfRxBadPacket.setStatus(
        "current"
    )

rosMgmtOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 10)
)
rosMgmtOspfVirtIfRxBadPacket.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfRxBadPacket.setStatus(
        "current"
    )

rosMgmtOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 11)
)
rosMgmtOspfTxRetransmit.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfNbrRtrId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbLsId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfTxRetransmit.setStatus(
        "current"
    )

rosMgmtOspfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 12)
)
rosMgmtOspfVirtIfTxRetransmit.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfPacketType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbLsId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfTxRetransmit.setStatus(
        "current"
    )

rosMgmtOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 13)
)
rosMgmtOspfOriginateLsa.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbLsId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfOriginateLsa.setStatus(
        "current"
    )

rosMgmtOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 14)
)
rosMgmtOspfMaxAgeLsa.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbType"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbLsId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfMaxAgeLsa.setStatus(
        "current"
    )

rosMgmtOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 15)
)
rosMgmtOspfLsdbOverflow.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbOverflow.setStatus(
        "current"
    )

rosMgmtOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 16)
)
rosMgmtOspfLsdbApproachingOverflow.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfLsdbApproachingOverflow.setStatus(
        "current"
    )

rosMgmtOspfIfKeyValid = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 17)
)
rosMgmtOspfIfKeyValid.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfKeyValid.setStatus(
        "current"
    )

rosMgmtOspfIfLastKeyExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 18)
)
rosMgmtOspfIfLastKeyExpiration.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfIpAddress"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfAddressLessIf"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfIfLastKeyExpiration.setStatus(
        "current"
    )

rosMgmtOspfVirtIfKeyValid = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 19)
)
rosMgmtOspfVirtIfKeyValid.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfKeyValid.setStatus(
        "current"
    )

rosMgmtOspfVirtIfLastKeyExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 20)
)
rosMgmtOspfVirtIfLastKeyExpiration.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRouterId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAreaId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfNeighbor"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfVirtIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfVirtIfLastKeyExpiration.setStatus(
        "current"
    )

rosMgmtOspfRedistributeOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 21)
)
rosMgmtOspfRedistributeOverflow.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeProtocol"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeRouteLimit"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeOverflow.setStatus(
        "current"
    )

rosMgmtOspfRedistributeNotOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 47, 1, 0, 22)
)
rosMgmtOspfRedistributeNotOverflow.setObjects(
      *(("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeProtocol"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeProcessId"),
        ("ROSMGMT-OSPFV2-MIB", "rosMgmtOspfRedistributeRouteLimit"))
)
if mibBuilder.loadTexts:
    rosMgmtOspfRedistributeNotOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-OSPFV2-MIB",
    **{"ProcessID": ProcessID,
       "AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "Status": Status,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "OspfAuthenticationType": OspfAuthenticationType,
       "rosMgmtOspf": rosMgmtOspf,
       "rosMgmtOspfNotifications": rosMgmtOspfNotifications,
       "rosMgmtOspfTraps": rosMgmtOspfTraps,
       "rosMgmtOspfIfStateChange": rosMgmtOspfIfStateChange,
       "rosMgmtOspfVirtIfStateChange": rosMgmtOspfVirtIfStateChange,
       "rosMgmtOspfNbrStateChange": rosMgmtOspfNbrStateChange,
       "rosMgmtOspfVirtNbrStateChange": rosMgmtOspfVirtNbrStateChange,
       "rosMgmtOspfIfConfigError": rosMgmtOspfIfConfigError,
       "rosMgmtOspfVirtIfConfigError": rosMgmtOspfVirtIfConfigError,
       "rosMgmtOspfIfAuthFailure": rosMgmtOspfIfAuthFailure,
       "rosMgmtOspfVirtIfAuthFailure": rosMgmtOspfVirtIfAuthFailure,
       "rosMgmtOspfIfRxBadPacket": rosMgmtOspfIfRxBadPacket,
       "rosMgmtOspfVirtIfRxBadPacket": rosMgmtOspfVirtIfRxBadPacket,
       "rosMgmtOspfTxRetransmit": rosMgmtOspfTxRetransmit,
       "rosMgmtOspfVirtIfTxRetransmit": rosMgmtOspfVirtIfTxRetransmit,
       "rosMgmtOspfOriginateLsa": rosMgmtOspfOriginateLsa,
       "rosMgmtOspfMaxAgeLsa": rosMgmtOspfMaxAgeLsa,
       "rosMgmtOspfLsdbOverflow": rosMgmtOspfLsdbOverflow,
       "rosMgmtOspfLsdbApproachingOverflow": rosMgmtOspfLsdbApproachingOverflow,
       "rosMgmtOspfIfKeyValid": rosMgmtOspfIfKeyValid,
       "rosMgmtOspfIfLastKeyExpiration": rosMgmtOspfIfLastKeyExpiration,
       "rosMgmtOspfVirtIfKeyValid": rosMgmtOspfVirtIfKeyValid,
       "rosMgmtOspfVirtIfLastKeyExpiration": rosMgmtOspfVirtIfLastKeyExpiration,
       "rosMgmtOspfRedistributeOverflow": rosMgmtOspfRedistributeOverflow,
       "rosMgmtOspfRedistributeNotOverflow": rosMgmtOspfRedistributeNotOverflow,
       "rosMgmtOspfTrapControlTable": rosMgmtOspfTrapControlTable,
       "rosMgmtOspfTrapControlEntry": rosMgmtOspfTrapControlEntry,
       "rosMgmtOspfSetTrap": rosMgmtOspfSetTrap,
       "rosMgmtOspfConfigErrorType": rosMgmtOspfConfigErrorType,
       "rosMgmtOspfPacketType": rosMgmtOspfPacketType,
       "rosMgmtOspfPacketSrc": rosMgmtOspfPacketSrc,
       "rosMgmtOspfObjects": rosMgmtOspfObjects,
       "rosMgmtOspfGlobalTable": rosMgmtOspfGlobalTable,
       "rosMgmtOspfGlobalEntry": rosMgmtOspfGlobalEntry,
       "rosMgmtOspfProcessId": rosMgmtOspfProcessId,
       "rosMgmtOspfRouterId": rosMgmtOspfRouterId,
       "rosMgmtOspfAdminStat": rosMgmtOspfAdminStat,
       "rosMgmtOspfVersionNumber": rosMgmtOspfVersionNumber,
       "rosMgmtOspfAreaBdrRtrStatus": rosMgmtOspfAreaBdrRtrStatus,
       "rosMgmtOspfASBdrRtrStatus": rosMgmtOspfASBdrRtrStatus,
       "rosMgmtOspfExternLsaCount": rosMgmtOspfExternLsaCount,
       "rosMgmtOspfExternLsaCksumSum": rosMgmtOspfExternLsaCksumSum,
       "rosMgmtOspfOriginateNewLsas": rosMgmtOspfOriginateNewLsas,
       "rosMgmtOspfRxNewLsas": rosMgmtOspfRxNewLsas,
       "rosMgmtOspfExtLsdbLimit": rosMgmtOspfExtLsdbLimit,
       "rosMgmtOspfExitOverflowInterval": rosMgmtOspfExitOverflowInterval,
       "rosMgmtOspfReferenceBandwidth": rosMgmtOspfReferenceBandwidth,
       "rosMgmtOspfAsLsaCount": rosMgmtOspfAsLsaCount,
       "rosMgmtOspfAsLsaCksumSum": rosMgmtOspfAsLsaCksumSum,
       "rosMgmtOspfStubRouterSupport": rosMgmtOspfStubRouterSupport,
       "rosMgmtOspfStubRouterAdvertisement": rosMgmtOspfStubRouterAdvertisement,
       "rosMgmtOspfAdminDistance": rosMgmtOspfAdminDistance,
       "rosMgmtOspfSpfInterval": rosMgmtOspfSpfInterval,
       "rosMgmtOspfReset": rosMgmtOspfReset,
       "rosMgmtOspfExportMetric": rosMgmtOspfExportMetric,
       "rosMgmtOspfExportTag": rosMgmtOspfExportTag,
       "rosMgmtOspfExportType": rosMgmtOspfExportType,
       "rosMgmtOspfNetCounts": rosMgmtOspfNetCounts,
       "rosMgmtOspfAreaCounts": rosMgmtOspfAreaCounts,
       "rosMgmtOspfNssaAreaCounts": rosMgmtOspfNssaAreaCounts,
       "rosMgmtOspfSpfCounts": rosMgmtOspfSpfCounts,
       "rosMgmtOspfGlobalStatus": rosMgmtOspfGlobalStatus,
       "rosMgmtOspfRedistributeRouteLimit": rosMgmtOspfRedistributeRouteLimit,
       "rosMgmtOspfDistanceIntra": rosMgmtOspfDistanceIntra,
       "rosMgmtOspfDistanceInter": rosMgmtOspfDistanceInter,
       "rosMgmtOspfDistanceExtern": rosMgmtOspfDistanceExtern,
       "rosMgmtOspfRfc1583Compatible": rosMgmtOspfRfc1583Compatible,
       "rosMgmtOspfSpfHode": rosMgmtOspfSpfHode,
       "rosMgmtOspfBfdAllItfs": rosMgmtOspfBfdAllItfs,
       "rosMgmtOspfOpaqueCapability": rosMgmtOspfOpaqueCapability,
       "rosMgmtOspfTECapability": rosMgmtOspfTECapability,
       "rosMgmtOspfTEAreaID": rosMgmtOspfTEAreaID,
       "rosMgmtOspfTERouterId": rosMgmtOspfTERouterId,
       "rosMgmtOspfGRCapability": rosMgmtOspfGRCapability,
       "rosMgmtOspfGRPeriod": rosMgmtOspfGRPeriod,
       "rosMgmtOspfGRHelper": rosMgmtOspfGRHelper,
       "rosMgmtOspfGRHelperMaxPeriod": rosMgmtOspfGRHelperMaxPeriod,
       "rosMgmtOspfMaximumLoadBalancing": rosMgmtOspfMaximumLoadBalancing,
       "rosMgmtOspfMaxMetric": rosMgmtOspfMaxMetric,
       "rosMgmtOspfMaxMetricType": rosMgmtOspfMaxMetricType,
       "rosMgmtOspfMaxMetricTime": rosMgmtOspfMaxMetricTime,
       "rosMgmtOspfMaxMetricTypeStartup": rosMgmtOspfMaxMetricTypeStartup,
       "rosMgmtOspfLsdbOverflowLimit": rosMgmtOspfLsdbOverflowLimit,
       "rosMgmtOspfTrafficAdjustType": rosMgmtOspfTrafficAdjustType,
       "rosMgmtOspfRouteTagValue": rosMgmtOspfRouteTagValue,
       "rosMgmtOspfRouteTagCheckDisable": rosMgmtOspfRouteTagCheckDisable,
       "rosMgmtOspfDNBitSetDisableSummary": rosMgmtOspfDNBitSetDisableSummary,
       "rosMgmtOspfDNBitSetDisableAse": rosMgmtOspfDNBitSetDisableAse,
       "rosMgmtOspfDNBitSetDisableNssa": rosMgmtOspfDNBitSetDisableNssa,
       "rosMgmtOspfDNBitCheckDisableSummary": rosMgmtOspfDNBitCheckDisableSummary,
       "rosMgmtOspfDNBitCheckDisableAse": rosMgmtOspfDNBitCheckDisableAse,
       "rosMgmtOspfDNBitCheckDisableNssa": rosMgmtOspfDNBitCheckDisableNssa,
       "rosMgmtOspfSpfMilliInterval": rosMgmtOspfSpfMilliInterval,
       "rosMgmtOspfSpfMilliHode": rosMgmtOspfSpfMilliHode,
       "rosMgmtOspfLoopFreeAlt": rosMgmtOspfLoopFreeAlt,
       "rosMgmtOspfAreaTable": rosMgmtOspfAreaTable,
       "rosMgmtOspfAreaEntry": rosMgmtOspfAreaEntry,
       "rosMgmtOspfAreaId": rosMgmtOspfAreaId,
       "rosMgmtOspfAuthType": rosMgmtOspfAuthType,
       "rosMgmtOspfImportAsExtern": rosMgmtOspfImportAsExtern,
       "rosMgmtOspfSpfRuns": rosMgmtOspfSpfRuns,
       "rosMgmtOspfAreaBdrRtrCount": rosMgmtOspfAreaBdrRtrCount,
       "rosMgmtOspfAsBdrRtrCount": rosMgmtOspfAsBdrRtrCount,
       "rosMgmtOspfAreaLsaCount": rosMgmtOspfAreaLsaCount,
       "rosMgmtOspfAreaLsaCksumSum": rosMgmtOspfAreaLsaCksumSum,
       "rosMgmtOspfAreaSummary": rosMgmtOspfAreaSummary,
       "rosMgmtOspfAreaNssaTranslatorRole": rosMgmtOspfAreaNssaTranslatorRole,
       "rosMgmtOspfAreaNssaTranslatorState": rosMgmtOspfAreaNssaTranslatorState,
       "rosMgmtOspfAreaNssaTranslatorStabilityInterval": rosMgmtOspfAreaNssaTranslatorStabilityInterval,
       "rosMgmtOspfAreaNssaTranslatorEvents": rosMgmtOspfAreaNssaTranslatorEvents,
       "rosMgmtOspfAreaDefaultCost": rosMgmtOspfAreaDefaultCost,
       "rosMgmtOspfAreaType": rosMgmtOspfAreaType,
       "rosMgmtOspfAreaStatus": rosMgmtOspfAreaStatus,
       "rosMgmtOspfAreaFilterInIpPrefixListName": rosMgmtOspfAreaFilterInIpPrefixListName,
       "rosMgmtOspfAreaFilterOutIpPrefixListName": rosMgmtOspfAreaFilterOutIpPrefixListName,
       "rosMgmtOspfAreaTeCapability": rosMgmtOspfAreaTeCapability,
       "rosMgmtOspfNetWorkTable": rosMgmtOspfNetWorkTable,
       "rosMgmtOspfNetWorkEntry": rosMgmtOspfNetWorkEntry,
       "rosMgmtOspfNet": rosMgmtOspfNet,
       "rosMgmtOspfMask": rosMgmtOspfMask,
       "rosMgmtOspfNetWorkStatus": rosMgmtOspfNetWorkStatus,
       "rosMgmtOspfStubAreaTable": rosMgmtOspfStubAreaTable,
       "rosMgmtOspfStubAreaEntry": rosMgmtOspfStubAreaEntry,
       "rosMgmtOspfStubAreaId": rosMgmtOspfStubAreaId,
       "rosMgmtOspfStubAreaOption": rosMgmtOspfStubAreaOption,
       "rosMgmtOspfStubAreaStatus": rosMgmtOspfStubAreaStatus,
       "rosMgmtOspfNssaAreaTable": rosMgmtOspfNssaAreaTable,
       "rosMgmtOspfNssaAreaEntry": rosMgmtOspfNssaAreaEntry,
       "rosMgmtOspfNssaAreaId": rosMgmtOspfNssaAreaId,
       "rosMgmtOspfNssaAreaOption": rosMgmtOspfNssaAreaOption,
       "rosMgmtOspfNssaAreaStatus": rosMgmtOspfNssaAreaStatus,
       "rosMgmtOspfIfTable": rosMgmtOspfIfTable,
       "rosMgmtOspfIfEntry": rosMgmtOspfIfEntry,
       "rosMgmtOspfAddressLessIf": rosMgmtOspfAddressLessIf,
       "rosMgmtOspfIfIpAddress": rosMgmtOspfIfIpAddress,
       "rosMgmtOspfIfAreaId": rosMgmtOspfIfAreaId,
       "rosMgmtOspfIfType": rosMgmtOspfIfType,
       "rosMgmtOspfIfAdminStat": rosMgmtOspfIfAdminStat,
       "rosMgmtOspfIfRtrPriority": rosMgmtOspfIfRtrPriority,
       "rosMgmtOspfIfTransitDelay": rosMgmtOspfIfTransitDelay,
       "rosMgmtOspfIfRetransInterval": rosMgmtOspfIfRetransInterval,
       "rosMgmtOspfIfHelloInterval": rosMgmtOspfIfHelloInterval,
       "rosMgmtOspfIfRtrDeadInterval": rosMgmtOspfIfRtrDeadInterval,
       "rosMgmtOspfIfPollInterval": rosMgmtOspfIfPollInterval,
       "rosMgmtOspfIfState": rosMgmtOspfIfState,
       "rosMgmtOspfIfDesignatedRouter": rosMgmtOspfIfDesignatedRouter,
       "rosMgmtOspfIfBackupDesignatedRouter": rosMgmtOspfIfBackupDesignatedRouter,
       "rosMgmtOspfIfEvents": rosMgmtOspfIfEvents,
       "rosMgmtOspfIfAuthKeyId": rosMgmtOspfIfAuthKeyId,
       "rosMgmtOspfIfAuthSimpleKeyType": rosMgmtOspfIfAuthSimpleKeyType,
       "rosMgmtOspfIfAuthMd5KeyType": rosMgmtOspfIfAuthMd5KeyType,
       "rosMgmtOspfIfAuthSimpleKey": rosMgmtOspfIfAuthSimpleKey,
       "rosMgmtOspfIfAuthMd5Key": rosMgmtOspfIfAuthMd5Key,
       "rosMgmtOspfIfAuthKeyChain": rosMgmtOspfIfAuthKeyChain,
       "rosMgmtOspfIfAuthType": rosMgmtOspfIfAuthType,
       "rosMgmtOspfIfLsaCount": rosMgmtOspfIfLsaCount,
       "rosMgmtOspfIfLsaCksumSum": rosMgmtOspfIfLsaCksumSum,
       "rosMgmtOspfIfDesignatedRouterId": rosMgmtOspfIfDesignatedRouterId,
       "rosMgmtOspfIfBackupDesignatedRouterId": rosMgmtOspfIfBackupDesignatedRouterId,
       "rosMgmtOspfIfPassive": rosMgmtOspfIfPassive,
       "rosMgmtOspfIfMtu": rosMgmtOspfIfMtu,
       "rosMgmtOspfIfMetric": rosMgmtOspfIfMetric,
       "rosMgmtOspfIfBfd": rosMgmtOspfIfBfd,
       "rosMgmtOspfIfGRResync": rosMgmtOspfIfGRResync,
       "rosMgmtOspfVirtIfTable": rosMgmtOspfVirtIfTable,
       "rosMgmtOspfVirtIfEntry": rosMgmtOspfVirtIfEntry,
       "rosMgmtOspfVirtIfAreaId": rosMgmtOspfVirtIfAreaId,
       "rosMgmtOspfVirtIfNeighbor": rosMgmtOspfVirtIfNeighbor,
       "rosMgmtOspfVirtIfTransitDelay": rosMgmtOspfVirtIfTransitDelay,
       "rosMgmtOspfVirtIfRetransInterval": rosMgmtOspfVirtIfRetransInterval,
       "rosMgmtOspfVirtIfHelloInterval": rosMgmtOspfVirtIfHelloInterval,
       "rosMgmtOspfVirtIfRtrDeadInterval": rosMgmtOspfVirtIfRtrDeadInterval,
       "rosMgmtOspfVirtIfState": rosMgmtOspfVirtIfState,
       "rosMgmtOspfVirtIfEvents": rosMgmtOspfVirtIfEvents,
       "rosMgmtOspfVirtIfAuthKeyId": rosMgmtOspfVirtIfAuthKeyId,
       "rosMgmtOspfVirtIfAuthSimpleKeyType": rosMgmtOspfVirtIfAuthSimpleKeyType,
       "rosMgmtOspfVirtIfAuthMd5KeyType": rosMgmtOspfVirtIfAuthMd5KeyType,
       "rosMgmtOspfVirtIfAuthSimpleKey": rosMgmtOspfVirtIfAuthSimpleKey,
       "rosMgmtOspfVirtIfAuthMd5Key": rosMgmtOspfVirtIfAuthMd5Key,
       "rosMgmtOspfVirtIfAuthKeyChain": rosMgmtOspfVirtIfAuthKeyChain,
       "rosMgmtOspfVirtIfAuthType": rosMgmtOspfVirtIfAuthType,
       "rosMgmtOspfVirtIfLsaCount": rosMgmtOspfVirtIfLsaCount,
       "rosMgmtOspfVirtIfLsaCksumSum": rosMgmtOspfVirtIfLsaCksumSum,
       "rosMgmtOspfVirtIfCost": rosMgmtOspfVirtIfCost,
       "rosMgmtOspfVirtIfStatus": rosMgmtOspfVirtIfStatus,
       "rosMgmtOspfNbrTable": rosMgmtOspfNbrTable,
       "rosMgmtOspfNbrEntry": rosMgmtOspfNbrEntry,
       "rosMgmtOspfNbrIpAddr": rosMgmtOspfNbrIpAddr,
       "rosMgmtOspfNbrAddressLessIndex": rosMgmtOspfNbrAddressLessIndex,
       "rosMgmtOspfNbrRtrId": rosMgmtOspfNbrRtrId,
       "rosMgmtOspfNbrOptions": rosMgmtOspfNbrOptions,
       "rosMgmtOspfNbrPriority": rosMgmtOspfNbrPriority,
       "rosMgmtOspfNbrState": rosMgmtOspfNbrState,
       "rosMgmtOspfNbrEvents": rosMgmtOspfNbrEvents,
       "rosMgmtOspfNbrLsRetransQLen": rosMgmtOspfNbrLsRetransQLen,
       "rosMgmtOspfNbrMode": rosMgmtOspfNbrMode,
       "rosMgmtOspfNbmaCfgNbrTable": rosMgmtOspfNbmaCfgNbrTable,
       "rosMgmtOspfNbmaCfgNbrEntry": rosMgmtOspfNbmaCfgNbrEntry,
       "rosMgmtOspfNbmaCfgNbrIpAddr": rosMgmtOspfNbmaCfgNbrIpAddr,
       "rosMgmtOspfNbmaCfgNbrPriority": rosMgmtOspfNbmaCfgNbrPriority,
       "rosMgmtOspfNbmaCfgNbrStatus": rosMgmtOspfNbmaCfgNbrStatus,
       "rosMgmtOspfVirtNbrTable": rosMgmtOspfVirtNbrTable,
       "rosMgmtOspfVirtNbrEntry": rosMgmtOspfVirtNbrEntry,
       "rosMgmtOspfVirtNbrArea": rosMgmtOspfVirtNbrArea,
       "rosMgmtOspfVirtNbrRtrId": rosMgmtOspfVirtNbrRtrId,
       "rosMgmtOspfVirtNbrIpAddr": rosMgmtOspfVirtNbrIpAddr,
       "rosMgmtOspfVirtNbrOptions": rosMgmtOspfVirtNbrOptions,
       "rosMgmtOspfVirtNbrState": rosMgmtOspfVirtNbrState,
       "rosMgmtOspfVirtNbrEvents": rosMgmtOspfVirtNbrEvents,
       "rosMgmtOspfVirtNbrLsRetransQLen": rosMgmtOspfVirtNbrLsRetransQLen,
       "rosMgmtOspfVirtNbrLessIf": rosMgmtOspfVirtNbrLessIf,
       "rosMgmtOspfVirtNbrMode": rosMgmtOspfVirtNbrMode,
       "rosMgmtOspfAreaAggregateTable": rosMgmtOspfAreaAggregateTable,
       "rosMgmtOspfAreaAggregateEntry": rosMgmtOspfAreaAggregateEntry,
       "rosMgmtOspfAreaAggregateAreaID": rosMgmtOspfAreaAggregateAreaID,
       "rosMgmtOspfAreaAggregateLsdbType": rosMgmtOspfAreaAggregateLsdbType,
       "rosMgmtOspfAreaAggregateNet": rosMgmtOspfAreaAggregateNet,
       "rosMgmtOspfAreaAggregateMask": rosMgmtOspfAreaAggregateMask,
       "rosMgmtOspfAreaAggregateEffect": rosMgmtOspfAreaAggregateEffect,
       "rosMgmtOspfAreaAggregateStatus": rosMgmtOspfAreaAggregateStatus,
       "rosMgmtOspfExternalAggregateTable": rosMgmtOspfExternalAggregateTable,
       "rosMgmtOspfExternalAggregateEntry": rosMgmtOspfExternalAggregateEntry,
       "rosMgmtOspfExternalAggregateNet": rosMgmtOspfExternalAggregateNet,
       "rosMgmtOspfExternalAggregateMask": rosMgmtOspfExternalAggregateMask,
       "rosMgmtOspfExternalAggregateEffect": rosMgmtOspfExternalAggregateEffect,
       "rosMgmtOspfExternalAggregateCost": rosMgmtOspfExternalAggregateCost,
       "rosMgmtOspfExternalAggregateStatus": rosMgmtOspfExternalAggregateStatus,
       "rosMgmtOspfLsdbTable": rosMgmtOspfLsdbTable,
       "rosMgmtOspfLsdbEntry": rosMgmtOspfLsdbEntry,
       "rosMgmtOspfLsdbAreaId": rosMgmtOspfLsdbAreaId,
       "rosMgmtOspfLsdbType": rosMgmtOspfLsdbType,
       "rosMgmtOspfLsdbLsId": rosMgmtOspfLsdbLsId,
       "rosMgmtOspfLsdbRouterId": rosMgmtOspfLsdbRouterId,
       "rosMgmtOspfLsdbSequence": rosMgmtOspfLsdbSequence,
       "rosMgmtOspfLsdbAge": rosMgmtOspfLsdbAge,
       "rosMgmtOspfLsdbChecksum": rosMgmtOspfLsdbChecksum,
       "rosMgmtOspfLsdbAdvertisement": rosMgmtOspfLsdbAdvertisement,
       "rosMgmtOspfAsLsdbTable": rosMgmtOspfAsLsdbTable,
       "rosMgmtOspfAsLsdbEntry": rosMgmtOspfAsLsdbEntry,
       "rosMgmtOspfAsLsdbType": rosMgmtOspfAsLsdbType,
       "rosMgmtOspfAsLsdbLsId": rosMgmtOspfAsLsdbLsId,
       "rosMgmtOspfAsLsdbRouterId": rosMgmtOspfAsLsdbRouterId,
       "rosMgmtOspfAsLsdbSequence": rosMgmtOspfAsLsdbSequence,
       "rosMgmtOspfAsLsdbAge": rosMgmtOspfAsLsdbAge,
       "rosMgmtOspfAsLsdbChecksum": rosMgmtOspfAsLsdbChecksum,
       "rosMgmtOspfAsLsdbAdvertisement": rosMgmtOspfAsLsdbAdvertisement,
       "rosMgmtOspfAreaLsaCountTable": rosMgmtOspfAreaLsaCountTable,
       "rosMgmtOspfAreaLsaCountEntry": rosMgmtOspfAreaLsaCountEntry,
       "rosMgmtOspfAreaLsaCountAreaId": rosMgmtOspfAreaLsaCountAreaId,
       "rosMgmtOspfAreaLsaCountLsaType": rosMgmtOspfAreaLsaCountLsaType,
       "rosMgmtOspfAreaLsaCountNumber": rosMgmtOspfAreaLsaCountNumber,
       "rosMgmtOspfRedistributeTable": rosMgmtOspfRedistributeTable,
       "rosMgmtOspfRedistributeEntry": rosMgmtOspfRedistributeEntry,
       "rosMgmtOspfRedistributeProtocol": rosMgmtOspfRedistributeProtocol,
       "rosMgmtOspfRedistributeProcessId": rosMgmtOspfRedistributeProcessId,
       "rosMgmtOspfRedistributeCost": rosMgmtOspfRedistributeCost,
       "rosMgmtOspfRedistributeType": rosMgmtOspfRedistributeType,
       "rosMgmtOspfRedistributeStatus": rosMgmtOspfRedistributeStatus,
       "rosMgmtOspfRedistributeRouteMapName": rosMgmtOspfRedistributeRouteMapName,
       "rosMgmtOspfRedistributeTag": rosMgmtOspfRedistributeTag,
       "rosMgmtOspfDefaultInfoTable": rosMgmtOspfDefaultInfoTable,
       "rosMgmtOspfDefaultInfoEntry": rosMgmtOspfDefaultInfoEntry,
       "rosMgmtOspfDefaultInfoAlways": rosMgmtOspfDefaultInfoAlways,
       "rosMgmtOspfDefaultInfoCost": rosMgmtOspfDefaultInfoCost,
       "rosMgmtOspfDefaultInfoType": rosMgmtOspfDefaultInfoType,
       "rosMgmtOspfDefaultInfoStatus": rosMgmtOspfDefaultInfoStatus,
       "rosMgmtOspfPacketIoStatisTable": rosMgmtOspfPacketIoStatisTable,
       "rosMgmtOspfPacketIoStatisEntry": rosMgmtOspfPacketIoStatisEntry,
       "rosMgmtOspfPacketIoStatisIoType": rosMgmtOspfPacketIoStatisIoType,
       "rosMgmtOspfPacketIoStatisPktType": rosMgmtOspfPacketIoStatisPktType,
       "rosMgmtOspfPacketIoStatisNumber": rosMgmtOspfPacketIoStatisNumber,
       "rosMgmtOspfRouteTable": rosMgmtOspfRouteTable,
       "rosMgmtOspfRouteEntry": rosMgmtOspfRouteEntry,
       "rosMgmtOspfRouteDest": rosMgmtOspfRouteDest,
       "rosMgmtOspfRouteMask": rosMgmtOspfRouteMask,
       "rosMgmtOspfRouteType": rosMgmtOspfRouteType,
       "rosMgmtOspfRouteLsType": rosMgmtOspfRouteLsType,
       "rosMgmtOspfRouteMetric": rosMgmtOspfRouteMetric,
       "rosMgmtOspfRouteNextHop": rosMgmtOspfRouteNextHop,
       "rosMgmtOspfRouteAdvRtr": rosMgmtOspfRouteAdvRtr,
       "rosMgmtOspfRouteArea": rosMgmtOspfRouteArea,
       "rosMgmtOspfBdrRouteTable": rosMgmtOspfBdrRouteTable,
       "rosMgmtOspfBdrRouteEntry": rosMgmtOspfBdrRouteEntry,
       "rosMgmtOspfBdrRouteRtrType": rosMgmtOspfBdrRouteRtrType,
       "rosMgmtOspfBdrRouteArea": rosMgmtOspfBdrRouteArea,
       "rosMgmtOspfBdrRouteDest": rosMgmtOspfBdrRouteDest,
       "rosMgmtOspfBdrRouteNextHop": rosMgmtOspfBdrRouteNextHop,
       "rosMgmtOspfBdrRouteLsType": rosMgmtOspfBdrRouteLsType,
       "rosMgmtOspfBdrRouteMetric": rosMgmtOspfBdrRouteMetric,
       "rosMgmtOspfDistributeListGroup": rosMgmtOspfDistributeListGroup,
       "rosMgmtOspfDistributeListInTable": rosMgmtOspfDistributeListInTable,
       "rosMgmtOspfDistributeListInEntry": rosMgmtOspfDistributeListInEntry,
       "rosMgmtOspfDistrInIpPrefixListName": rosMgmtOspfDistrInIpPrefixListName,
       "rosMgmtOspfDistrInAclNum": rosMgmtOspfDistrInAclNum,
       "rosMgmtOspfDistrInRowStatus": rosMgmtOspfDistrInRowStatus,
       "rosMgmtOspfDistributeListOutTable": rosMgmtOspfDistributeListOutTable,
       "rosMgmtOspfDistributeListOutEntry": rosMgmtOspfDistributeListOutEntry,
       "rosMgmtOspfDistrOutIpPrefixListName": rosMgmtOspfDistrOutIpPrefixListName,
       "rosMgmtOspfDistrOutAclNum": rosMgmtOspfDistrOutAclNum,
       "rosMgmtOspfDistrOutRowStatus": rosMgmtOspfDistrOutRowStatus,
       "rosMgmtOspfDistributeListOutProtocolTable": rosMgmtOspfDistributeListOutProtocolTable,
       "rosMgmtOspfDistributeListOutProtocolEntry": rosMgmtOspfDistributeListOutProtocolEntry,
       "rosMgmtOspfDistrOutProtocol": rosMgmtOspfDistrOutProtocol,
       "rosMgmtOspfDistrOutProcessId": rosMgmtOspfDistrOutProcessId,
       "rosMgmtOspfDistrOutProIpPrefixListName": rosMgmtOspfDistrOutProIpPrefixListName,
       "rosMgmtOspfDistrOutProAclNum": rosMgmtOspfDistrOutProAclNum,
       "rosMgmtOspfDistrOutProRowStatus": rosMgmtOspfDistrOutProRowStatus,
       "rosMgmtOspfDNBitCheckDisableSummaryTable": rosMgmtOspfDNBitCheckDisableSummaryTable,
       "rosMgmtOspfDNBitCheckDisableSummaryEntry": rosMgmtOspfDNBitCheckDisableSummaryEntry,
       "rosMgmtOspfDNBitCheckDisableSummaryRtrId": rosMgmtOspfDNBitCheckDisableSummaryRtrId,
       "rosMgmtOspfDNBitCheckDisableSummaryStatus": rosMgmtOspfDNBitCheckDisableSummaryStatus,
       "rosMgmtOspfConformance": rosMgmtOspfConformance}
)
