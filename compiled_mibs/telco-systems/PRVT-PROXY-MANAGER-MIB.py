# SNMP MIB module (PRVT-PROXY-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-PROXY-MANAGER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:53 2025
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

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

prvtProxyManager = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6)
)
if mibBuilder.loadTexts:
    prvtProxyManager.setRevisions(
        ("2009-01-16 00:00",
         "2007-11-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtProxyManStates(TextualConvention, Integer32):
    status = "current"
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



class PrvtProxyManProtocols(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("snmp-udp", 1),
          ("snmptrap-udp", 2),
          ("telnet-tcp", 3),
          ("ssh-tcp", 4),
          ("tftp-udp", 5),
          ("syslog-udp", 6))
    )



class PrvtProxyManPortTypes(TextualConvention, Integer32):
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
          ("tcp", 1),
          ("udp", 2))
    )



class PrvtProxyManDirection(TextualConvention, Integer32):
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
        *(("noDirection", 0),
          ("inbound", 1),
          ("outbound", 2))
    )



class PrvtProxyManAuthentication(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 0),
          ("unauthenticated", 1))
    )



class PrvtProxySecurity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("securityEnabled", 0),
          ("securityDisabled", 1))
    )



class PrvtProxyAcceptInformsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("informsEnabled", 0),
          ("informsDisabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtProxyManNotifications_ObjectIdentity = ObjectIdentity
prvtProxyManNotifications = _PrvtProxyManNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0)
)
_PrvtProxyManObjects_ObjectIdentity = ObjectIdentity
prvtProxyManObjects = _PrvtProxyManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1)
)
_PrvtProxyManDeviceAddress_Type = MacAddress
_PrvtProxyManDeviceAddress_Object = MibScalar
prvtProxyManDeviceAddress = _PrvtProxyManDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 1),
    _PrvtProxyManDeviceAddress_Type()
)
prvtProxyManDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtProxyManDeviceAddress.setStatus("current")
_PrvtProxyManConfigTable_Object = MibTable
prvtProxyManConfigTable = _PrvtProxyManConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    prvtProxyManConfigTable.setStatus("current")
_PrvtProxyManConfigEntry_Object = MibTableRow
prvtProxyManConfigEntry = _PrvtProxyManConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1)
)
prvtProxyManConfigEntry.setIndexNames(
    (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManIndex"),
)
if mibBuilder.loadTexts:
    prvtProxyManConfigEntry.setStatus("current")
_PrvtProxyManIndex_Type = Unsigned32
_PrvtProxyManIndex_Object = MibTableColumn
prvtProxyManIndex = _PrvtProxyManIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 1),
    _PrvtProxyManIndex_Type()
)
prvtProxyManIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtProxyManIndex.setStatus("current")
_PrvtProxyManStatus_Type = PrvtProxyManStates
_PrvtProxyManStatus_Object = MibTableColumn
prvtProxyManStatus = _PrvtProxyManStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 2),
    _PrvtProxyManStatus_Type()
)
prvtProxyManStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManStatus.setStatus("current")


class _PrvtProxyManAutoMapMode_Type(PrvtProxyManStates):
    """Custom type prvtProxyManAutoMapMode based on PrvtProxyManStates"""
    defaultValue = 1


_PrvtProxyManAutoMapMode_Type.__name__ = "PrvtProxyManStates"
_PrvtProxyManAutoMapMode_Object = MibTableColumn
prvtProxyManAutoMapMode = _PrvtProxyManAutoMapMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 3),
    _PrvtProxyManAutoMapMode_Type()
)
prvtProxyManAutoMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManAutoMapMode.setStatus("current")
_PrvtProxyManVlan_Type = Unsigned32
_PrvtProxyManVlan_Object = MibTableColumn
prvtProxyManVlan = _PrvtProxyManVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 4),
    _PrvtProxyManVlan_Type()
)
prvtProxyManVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManVlan.setStatus("current")
_PrvtProxyManIpAddr_Type = IpAddress
_PrvtProxyManIpAddr_Object = MibTableColumn
prvtProxyManIpAddr = _PrvtProxyManIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 5),
    _PrvtProxyManIpAddr_Type()
)
prvtProxyManIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManIpAddr.setStatus("current")
_PrvtProxyManIpMask_Type = Unsigned32
_PrvtProxyManIpMask_Object = MibTableColumn
prvtProxyManIpMask = _PrvtProxyManIpMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 6),
    _PrvtProxyManIpMask_Type()
)
prvtProxyManIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManIpMask.setStatus("current")
_PrvtProxyManIpRangeStart_Type = IpAddress
_PrvtProxyManIpRangeStart_Object = MibTableColumn
prvtProxyManIpRangeStart = _PrvtProxyManIpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 7),
    _PrvtProxyManIpRangeStart_Type()
)
prvtProxyManIpRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManIpRangeStart.setStatus("current")
_PrvtProxyManIpRangeEnd_Type = IpAddress
_PrvtProxyManIpRangeEnd_Object = MibTableColumn
prvtProxyManIpRangeEnd = _PrvtProxyManIpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 8),
    _PrvtProxyManIpRangeEnd_Type()
)
prvtProxyManIpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManIpRangeEnd.setStatus("current")
_PrvtProxyManLeasePeriod_Type = Unsigned32
_PrvtProxyManLeasePeriod_Object = MibTableColumn
prvtProxyManLeasePeriod = _PrvtProxyManLeasePeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 9),
    _PrvtProxyManLeasePeriod_Type()
)
prvtProxyManLeasePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManLeasePeriod.setStatus("current")
_PrvtProxyManRowStatus_Type = RowStatus
_PrvtProxyManRowStatus_Object = MibTableColumn
prvtProxyManRowStatus = _PrvtProxyManRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 10),
    _PrvtProxyManRowStatus_Type()
)
prvtProxyManRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtProxyManRowStatus.setStatus("current")
_PrvtProxySecurityEnabled_Type = PrvtProxySecurity
_PrvtProxySecurityEnabled_Object = MibTableColumn
prvtProxySecurityEnabled = _PrvtProxySecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 11),
    _PrvtProxySecurityEnabled_Type()
)
prvtProxySecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxySecurityEnabled.setStatus("current")
_PrvtProxyAcceptInforms_Type = PrvtProxyAcceptInformsType
_PrvtProxyAcceptInforms_Object = MibTableColumn
prvtProxyAcceptInforms = _PrvtProxyAcceptInforms_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 12),
    _PrvtProxyAcceptInforms_Type()
)
prvtProxyAcceptInforms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyAcceptInforms.setStatus("current")
_PrvtProxyManProtoTable_Object = MibTable
prvtProxyManProtoTable = _PrvtProxyManProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    prvtProxyManProtoTable.setStatus("current")
_PrvtProxyManProtoEntry_Object = MibTableRow
prvtProxyManProtoEntry = _PrvtProxyManProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1)
)
prvtProxyManProtoEntry.setIndexNames(
    (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManProtoIndex"),
)
if mibBuilder.loadTexts:
    prvtProxyManProtoEntry.setStatus("current")
_PrvtProxyManProtoIndex_Type = PrvtProxyManProtocols
_PrvtProxyManProtoIndex_Object = MibTableColumn
prvtProxyManProtoIndex = _PrvtProxyManProtoIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 1),
    _PrvtProxyManProtoIndex_Type()
)
prvtProxyManProtoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtProxyManProtoIndex.setStatus("current")


class _PrvtProxyManProtoSvcPort_Type(Integer32):
    """Custom type prvtProxyManProtoSvcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtProxyManProtoSvcPort_Type.__name__ = "Integer32"
_PrvtProxyManProtoSvcPort_Object = MibTableColumn
prvtProxyManProtoSvcPort = _PrvtProxyManProtoSvcPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 2),
    _PrvtProxyManProtoSvcPort_Type()
)
prvtProxyManProtoSvcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManProtoSvcPort.setStatus("current")
_PrvtProxyManProtoSvcPortType_Type = PrvtProxyManPortTypes
_PrvtProxyManProtoSvcPortType_Object = MibTableColumn
prvtProxyManProtoSvcPortType = _PrvtProxyManProtoSvcPortType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 3),
    _PrvtProxyManProtoSvcPortType_Type()
)
prvtProxyManProtoSvcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManProtoSvcPortType.setStatus("current")


class _PrvtProxyManProtoSrcPort_Type(Integer32):
    """Custom type prvtProxyManProtoSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtProxyManProtoSrcPort_Type.__name__ = "Integer32"
_PrvtProxyManProtoSrcPort_Object = MibTableColumn
prvtProxyManProtoSrcPort = _PrvtProxyManProtoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 4),
    _PrvtProxyManProtoSrcPort_Type()
)
prvtProxyManProtoSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManProtoSrcPort.setStatus("current")
_PrvtProxyManProtoDirection_Type = PrvtProxyManDirection
_PrvtProxyManProtoDirection_Object = MibTableColumn
prvtProxyManProtoDirection = _PrvtProxyManProtoDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 5),
    _PrvtProxyManProtoDirection_Type()
)
prvtProxyManProtoDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManProtoDirection.setStatus("current")
_PrvtProxyManProtoStatus_Type = PrvtProxyManStates
_PrvtProxyManProtoStatus_Object = MibTableColumn
prvtProxyManProtoStatus = _PrvtProxyManProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 6),
    _PrvtProxyManProtoStatus_Type()
)
prvtProxyManProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManProtoStatus.setStatus("current")
_PrvtProxyManMappingTable_Object = MibTable
prvtProxyManMappingTable = _PrvtProxyManMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4)
)
if mibBuilder.loadTexts:
    prvtProxyManMappingTable.setStatus("current")
_PrvtProxyManMappingEntry_Object = MibTableRow
prvtProxyManMappingEntry = _PrvtProxyManMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1)
)
prvtProxyManMappingEntry.setIndexNames(
    (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManMappingDevice"),
    (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManMappingIndex"),
    (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManMappingProto"),
)
if mibBuilder.loadTexts:
    prvtProxyManMappingEntry.setStatus("current")
_PrvtProxyManMappingDevice_Type = Unsigned32
_PrvtProxyManMappingDevice_Object = MibTableColumn
prvtProxyManMappingDevice = _PrvtProxyManMappingDevice_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 1),
    _PrvtProxyManMappingDevice_Type()
)
prvtProxyManMappingDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtProxyManMappingDevice.setStatus("current")
_PrvtProxyManMappingIndex_Type = Unsigned32
_PrvtProxyManMappingIndex_Object = MibTableColumn
prvtProxyManMappingIndex = _PrvtProxyManMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 2),
    _PrvtProxyManMappingIndex_Type()
)
prvtProxyManMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtProxyManMappingIndex.setStatus("current")
_PrvtProxyManMappingProto_Type = PrvtProxyManProtocols
_PrvtProxyManMappingProto_Object = MibTableColumn
prvtProxyManMappingProto = _PrvtProxyManMappingProto_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 3),
    _PrvtProxyManMappingProto_Type()
)
prvtProxyManMappingProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtProxyManMappingProto.setStatus("current")
_PrvtProxyManMappingDirection_Type = PrvtProxyManDirection
_PrvtProxyManMappingDirection_Object = MibTableColumn
prvtProxyManMappingDirection = _PrvtProxyManMappingDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 4),
    _PrvtProxyManMappingDirection_Type()
)
prvtProxyManMappingDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManMappingDirection.setStatus("current")


class _PrvtProxyManMappingGlobalPort_Type(Integer32):
    """Custom type prvtProxyManMappingGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtProxyManMappingGlobalPort_Type.__name__ = "Integer32"
_PrvtProxyManMappingGlobalPort_Object = MibTableColumn
prvtProxyManMappingGlobalPort = _PrvtProxyManMappingGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 5),
    _PrvtProxyManMappingGlobalPort_Type()
)
prvtProxyManMappingGlobalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManMappingGlobalPort.setStatus("current")


class _PrvtProxyManMappingLocalSrcPort_Type(Integer32):
    """Custom type prvtProxyManMappingLocalSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtProxyManMappingLocalSrcPort_Type.__name__ = "Integer32"
_PrvtProxyManMappingLocalSrcPort_Object = MibTableColumn
prvtProxyManMappingLocalSrcPort = _PrvtProxyManMappingLocalSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 6),
    _PrvtProxyManMappingLocalSrcPort_Type()
)
prvtProxyManMappingLocalSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManMappingLocalSrcPort.setStatus("current")


class _PrvtProxyManMappingLocalDstPort_Type(Integer32):
    """Custom type prvtProxyManMappingLocalDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtProxyManMappingLocalDstPort_Type.__name__ = "Integer32"
_PrvtProxyManMappingLocalDstPort_Object = MibTableColumn
prvtProxyManMappingLocalDstPort = _PrvtProxyManMappingLocalDstPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 7),
    _PrvtProxyManMappingLocalDstPort_Type()
)
prvtProxyManMappingLocalDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManMappingLocalDstPort.setStatus("current")
_PrvtProxyManMappingRowStatus_Type = RowStatus
_PrvtProxyManMappingRowStatus_Object = MibTableColumn
prvtProxyManMappingRowStatus = _PrvtProxyManMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 8),
    _PrvtProxyManMappingRowStatus_Type()
)
prvtProxyManMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtProxyManMappingRowStatus.setStatus("current")
_PrvtProxyManMappingMAC_Type = MacAddress
_PrvtProxyManMappingMAC_Object = MibTableColumn
prvtProxyManMappingMAC = _PrvtProxyManMappingMAC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 9),
    _PrvtProxyManMappingMAC_Type()
)
prvtProxyManMappingMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtProxyManMappingMAC.setStatus("current")
_PrvtProxyManMappingIfIndex_Type = Integer32
_PrvtProxyManMappingIfIndex_Object = MibTableColumn
prvtProxyManMappingIfIndex = _PrvtProxyManMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 10),
    _PrvtProxyManMappingIfIndex_Type()
)
prvtProxyManMappingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManMappingIfIndex.setStatus("current")
_PrvtProxyManMappingAuthenticated_Type = PrvtProxyManAuthentication
_PrvtProxyManMappingAuthenticated_Object = MibTableColumn
prvtProxyManMappingAuthenticated = _PrvtProxyManMappingAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 11),
    _PrvtProxyManMappingAuthenticated_Type()
)
prvtProxyManMappingAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtProxyManMappingAuthenticated.setStatus("current")

# Managed Objects groups


# Notification objects

prvtProxyManagerNewDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0, 1)
)
prvtProxyManagerNewDevice.setObjects(
    ("PRVT-PROXY-MANAGER-MIB", "prvtProxyManDeviceAddress")
)
if mibBuilder.loadTexts:
    prvtProxyManagerNewDevice.setStatus(
        "current"
    )

prvtProxyManagerRemovedDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0, 2)
)
prvtProxyManagerRemovedDevice.setObjects(
    ("PRVT-PROXY-MANAGER-MIB", "prvtProxyManDeviceAddress")
)
if mibBuilder.loadTexts:
    prvtProxyManagerRemovedDevice.setStatus(
        "current"
    )

prvtProxyManagerUnauthenticatedDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0, 3)
)
prvtProxyManagerUnauthenticatedDevice.setObjects(
    ("PRVT-PROXY-MANAGER-MIB", "prvtProxyManDeviceAddress")
)
if mibBuilder.loadTexts:
    prvtProxyManagerUnauthenticatedDevice.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-PROXY-MANAGER-MIB",
    **{"PrvtProxyManStates": PrvtProxyManStates,
       "PrvtProxyManProtocols": PrvtProxyManProtocols,
       "PrvtProxyManPortTypes": PrvtProxyManPortTypes,
       "PrvtProxyManDirection": PrvtProxyManDirection,
       "PrvtProxyManAuthentication": PrvtProxyManAuthentication,
       "PrvtProxySecurity": PrvtProxySecurity,
       "PrvtProxyAcceptInformsType": PrvtProxyAcceptInformsType,
       "prvtProxyManager": prvtProxyManager,
       "prvtProxyManNotifications": prvtProxyManNotifications,
       "prvtProxyManagerNewDevice": prvtProxyManagerNewDevice,
       "prvtProxyManagerRemovedDevice": prvtProxyManagerRemovedDevice,
       "prvtProxyManagerUnauthenticatedDevice": prvtProxyManagerUnauthenticatedDevice,
       "prvtProxyManObjects": prvtProxyManObjects,
       "prvtProxyManDeviceAddress": prvtProxyManDeviceAddress,
       "prvtProxyManConfigTable": prvtProxyManConfigTable,
       "prvtProxyManConfigEntry": prvtProxyManConfigEntry,
       "prvtProxyManIndex": prvtProxyManIndex,
       "prvtProxyManStatus": prvtProxyManStatus,
       "prvtProxyManAutoMapMode": prvtProxyManAutoMapMode,
       "prvtProxyManVlan": prvtProxyManVlan,
       "prvtProxyManIpAddr": prvtProxyManIpAddr,
       "prvtProxyManIpMask": prvtProxyManIpMask,
       "prvtProxyManIpRangeStart": prvtProxyManIpRangeStart,
       "prvtProxyManIpRangeEnd": prvtProxyManIpRangeEnd,
       "prvtProxyManLeasePeriod": prvtProxyManLeasePeriod,
       "prvtProxyManRowStatus": prvtProxyManRowStatus,
       "prvtProxySecurityEnabled": prvtProxySecurityEnabled,
       "prvtProxyAcceptInforms": prvtProxyAcceptInforms,
       "prvtProxyManProtoTable": prvtProxyManProtoTable,
       "prvtProxyManProtoEntry": prvtProxyManProtoEntry,
       "prvtProxyManProtoIndex": prvtProxyManProtoIndex,
       "prvtProxyManProtoSvcPort": prvtProxyManProtoSvcPort,
       "prvtProxyManProtoSvcPortType": prvtProxyManProtoSvcPortType,
       "prvtProxyManProtoSrcPort": prvtProxyManProtoSrcPort,
       "prvtProxyManProtoDirection": prvtProxyManProtoDirection,
       "prvtProxyManProtoStatus": prvtProxyManProtoStatus,
       "prvtProxyManMappingTable": prvtProxyManMappingTable,
       "prvtProxyManMappingEntry": prvtProxyManMappingEntry,
       "prvtProxyManMappingDevice": prvtProxyManMappingDevice,
       "prvtProxyManMappingIndex": prvtProxyManMappingIndex,
       "prvtProxyManMappingProto": prvtProxyManMappingProto,
       "prvtProxyManMappingDirection": prvtProxyManMappingDirection,
       "prvtProxyManMappingGlobalPort": prvtProxyManMappingGlobalPort,
       "prvtProxyManMappingLocalSrcPort": prvtProxyManMappingLocalSrcPort,
       "prvtProxyManMappingLocalDstPort": prvtProxyManMappingLocalDstPort,
       "prvtProxyManMappingRowStatus": prvtProxyManMappingRowStatus,
       "prvtProxyManMappingMAC": prvtProxyManMappingMAC,
       "prvtProxyManMappingIfIndex": prvtProxyManMappingIfIndex,
       "prvtProxyManMappingAuthenticated": prvtProxyManMappingAuthenticated}
)
