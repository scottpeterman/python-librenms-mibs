# SNMP MIB module (A10-AX-NOTIFICATIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\a10\A10-AX-NOTIFICATIONS
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:00 2025
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

(axLogging,
 axNotification) = mibBuilder.importSymbols(
    "A10-AX-MIB",
    "axLogging",
    "axNotification")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxSyslogTrapPrefix_ObjectIdentity = ObjectIdentity
axSyslogTrapPrefix = _AxSyslogTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 100)
)
if mibBuilder.loadTexts:
    axSyslogTrapPrefix.setStatus("current")
_AxSyslogTrapObjects_ObjectIdentity = ObjectIdentity
axSyslogTrapObjects = _AxSyslogTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101)
)
if mibBuilder.loadTexts:
    axSyslogTrapObjects.setStatus("current")


class _AxSyslogModuleName_Type(DisplayString):
    """Custom type axSyslogModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AxSyslogModuleName_Type.__name__ = "DisplayString"
_AxSyslogModuleName_Object = MibScalar
axSyslogModuleName = _AxSyslogModuleName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101, 1),
    _AxSyslogModuleName_Type()
)
axSyslogModuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axSyslogModuleName.setStatus("current")


class _AxSyslogPriority_Type(Integer32):
    """Custom type axSyslogPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AxSyslogPriority_Type.__name__ = "Integer32"
_AxSyslogPriority_Object = MibScalar
axSyslogPriority = _AxSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101, 2),
    _AxSyslogPriority_Type()
)
axSyslogPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axSyslogPriority.setStatus("current")


class _AxSyslogMsg_Type(OctetString):
    """Custom type axSyslogMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_AxSyslogMsg_Type.__name__ = "OctetString"
_AxSyslogMsg_Object = MibScalar
axSyslogMsg = _AxSyslogMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101, 3),
    _AxSyslogMsg_Type()
)
axSyslogMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axSyslogMsg.setStatus("current")
_AxNotificationObjects_ObjectIdentity = ObjectIdentity
axNotificationObjects = _AxNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1)
)
_AxNotificationMsg_Type = DisplayString
_AxNotificationMsg_Object = MibScalar
axNotificationMsg = _AxNotificationMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 1),
    _AxNotificationMsg_Type()
)
axNotificationMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationMsg.setStatus("current")
_AxNotificationSLBServer_Type = DisplayString
_AxNotificationSLBServer_Object = MibScalar
axNotificationSLBServer = _AxNotificationSLBServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 2),
    _AxNotificationSLBServer_Type()
)
axNotificationSLBServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBServer.setStatus("current")
_AxNotificationSLBPort_Type = Integer32
_AxNotificationSLBPort_Object = MibScalar
axNotificationSLBPort = _AxNotificationSLBPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 3),
    _AxNotificationSLBPort_Type()
)
axNotificationSLBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBPort.setStatus("current")
_AxNotificationSLBCurConns_Type = Counter32
_AxNotificationSLBCurConns_Object = MibScalar
axNotificationSLBCurConns = _AxNotificationSLBCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 4),
    _AxNotificationSLBCurConns_Type()
)
axNotificationSLBCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBCurConns.setStatus("current")
_AxNotificationVirtualServer_Type = DisplayString
_AxNotificationVirtualServer_Object = MibScalar
axNotificationVirtualServer = _AxNotificationVirtualServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 5),
    _AxNotificationVirtualServer_Type()
)
axNotificationVirtualServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVirtualServer.setStatus("current")
_AxNotificationVirtualServerPort_Type = Integer32
_AxNotificationVirtualServerPort_Object = MibScalar
axNotificationVirtualServerPort = _AxNotificationVirtualServerPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 6),
    _AxNotificationVirtualServerPort_Type()
)
axNotificationVirtualServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVirtualServerPort.setStatus("current")


class _AxNotificationVirtualServerPortType_Type(Integer32):
    """Custom type axNotificationVirtualServerPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              8,
              9,
              10,
              11,
              12,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("firewall", 1),
          ("tcp", 2),
          ("udp", 3),
          ("others", 5),
          ("rtsp", 8),
          ("ftp", 9),
          ("mms", 10),
          ("sip", 11),
          ("fastHTTP", 12),
          ("http", 14),
          ("https", 15),
          ("sslProxy", 16),
          ("smtp", 17),
          ("sip-TCP", 18),
          ("sips", 19))
    )


_AxNotificationVirtualServerPortType_Type.__name__ = "Integer32"
_AxNotificationVirtualServerPortType_Object = MibScalar
axNotificationVirtualServerPortType = _AxNotificationVirtualServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 7),
    _AxNotificationVirtualServerPortType_Type()
)
axNotificationVirtualServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVirtualServerPortType.setStatus("current")
_AxNotificationDroppedPackets_Type = Integer32
_AxNotificationDroppedPackets_Object = MibScalar
axNotificationDroppedPackets = _AxNotificationDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 8),
    _AxNotificationDroppedPackets_Type()
)
axNotificationDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationDroppedPackets.setStatus("current")
_AxNotificationConfiguredThreshold_Type = Integer32
_AxNotificationConfiguredThreshold_Object = MibScalar
axNotificationConfiguredThreshold = _AxNotificationConfiguredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 9),
    _AxNotificationConfiguredThreshold_Type()
)
axNotificationConfiguredThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationConfiguredThreshold.setStatus("current")
_AxNotificationCurrentUsage_Type = Integer32
_AxNotificationCurrentUsage_Object = MibScalar
axNotificationCurrentUsage = _AxNotificationCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 10),
    _AxNotificationCurrentUsage_Type()
)
axNotificationCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationCurrentUsage.setStatus("current")
_AxNotificationConnLimit_Type = Integer32
_AxNotificationConnLimit_Object = MibScalar
axNotificationConnLimit = _AxNotificationConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 11),
    _AxNotificationConnLimit_Type()
)
axNotificationConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationConnLimit.setStatus("current")
_AxNotificationTrunkID_Type = Integer32
_AxNotificationTrunkID_Object = MibScalar
axNotificationTrunkID = _AxNotificationTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 12),
    _AxNotificationTrunkID_Type()
)
axNotificationTrunkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationTrunkID.setStatus("current")
_AxNotificationPortThreshold_Type = Integer32
_AxNotificationPortThreshold_Object = MibScalar
axNotificationPortThreshold = _AxNotificationPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 13),
    _AxNotificationPortThreshold_Type()
)
axNotificationPortThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPortThreshold.setStatus("current")
_AxNotificationCurrentUpPorts_Type = Integer32
_AxNotificationCurrentUpPorts_Object = MibScalar
axNotificationCurrentUpPorts = _AxNotificationCurrentUpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 14),
    _AxNotificationCurrentUpPorts_Type()
)
axNotificationCurrentUpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationCurrentUpPorts.setStatus("current")
_AxNotificationFanName_Type = DisplayString
_AxNotificationFanName_Object = MibScalar
axNotificationFanName = _AxNotificationFanName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 15),
    _AxNotificationFanName_Type()
)
axNotificationFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationFanName.setStatus("current")
_AxNotificationPowerSupplyName_Type = DisplayString
_AxNotificationPowerSupplyName_Object = MibScalar
axNotificationPowerSupplyName = _AxNotificationPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 16),
    _AxNotificationPowerSupplyName_Type()
)
axNotificationPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPowerSupplyName.setStatus("current")
_AxNotificationHAGroup_Type = Integer32
_AxNotificationHAGroup_Object = MibScalar
axNotificationHAGroup = _AxNotificationHAGroup_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 17),
    _AxNotificationHAGroup_Type()
)
axNotificationHAGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationHAGroup.setStatus("current")
_AxNotificationSLBServiceGroupName_Type = DisplayString
_AxNotificationSLBServiceGroupName_Object = MibScalar
axNotificationSLBServiceGroupName = _AxNotificationSLBServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 18),
    _AxNotificationSLBServiceGroupName_Type()
)
axNotificationSLBServiceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBServiceGroupName.setStatus("current")
_AxNotificationPartitionId_Type = Integer32
_AxNotificationPartitionId_Object = MibScalar
axNotificationPartitionId = _AxNotificationPartitionId_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 19),
    _AxNotificationPartitionId_Type()
)
axNotificationPartitionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPartitionId.setStatus("current")
_AxNotificationVrid_Type = Integer32
_AxNotificationVrid_Object = MibScalar
axNotificationVrid = _AxNotificationVrid_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 20),
    _AxNotificationVrid_Type()
)
axNotificationVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVrid.setStatus("current")
_AxNotificationPartitionName_Type = DisplayString
_AxNotificationPartitionName_Object = MibScalar
axNotificationPartitionName = _AxNotificationPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 21),
    _AxNotificationPartitionName_Type()
)
axNotificationPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPartitionName.setStatus("current")
_AxNotificationGslbSiteName_Type = DisplayString
_AxNotificationGslbSiteName_Object = MibScalar
axNotificationGslbSiteName = _AxNotificationGslbSiteName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 22),
    _AxNotificationGslbSiteName_Type()
)
axNotificationGslbSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbSiteName.setStatus("current")
_AxNotificationGslbSiteSlbDeviceName_Type = DisplayString
_AxNotificationGslbSiteSlbDeviceName_Object = MibScalar
axNotificationGslbSiteSlbDeviceName = _AxNotificationGslbSiteSlbDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 23),
    _AxNotificationGslbSiteSlbDeviceName_Type()
)
axNotificationGslbSiteSlbDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbSiteSlbDeviceName.setStatus("current")
_AxNotificationGslbSiteIpServerAddr_Type = DisplayString
_AxNotificationGslbSiteIpServerAddr_Object = MibScalar
axNotificationGslbSiteIpServerAddr = _AxNotificationGslbSiteIpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 24),
    _AxNotificationGslbSiteIpServerAddr_Type()
)
axNotificationGslbSiteIpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbSiteIpServerAddr.setStatus("current")
_AxNotificationGslbServiceIpName_Type = DisplayString
_AxNotificationGslbServiceIpName_Object = MibScalar
axNotificationGslbServiceIpName = _AxNotificationGslbServiceIpName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 25),
    _AxNotificationGslbServiceIpName_Type()
)
axNotificationGslbServiceIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbServiceIpName.setStatus("current")
_AxNotificationGslbServiceIpAddr_Type = DisplayString
_AxNotificationGslbServiceIpAddr_Object = MibScalar
axNotificationGslbServiceIpAddr = _AxNotificationGslbServiceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 26),
    _AxNotificationGslbServiceIpAddr_Type()
)
axNotificationGslbServiceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbServiceIpAddr.setStatus("current")
_AxNotificationGslbServiceIpPortType_Type = DisplayString
_AxNotificationGslbServiceIpPortType_Object = MibScalar
axNotificationGslbServiceIpPortType = _AxNotificationGslbServiceIpPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 27),
    _AxNotificationGslbServiceIpPortType_Type()
)
axNotificationGslbServiceIpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbServiceIpPortType.setStatus("current")
_AxNotificationGslbZoneName_Type = DisplayString
_AxNotificationGslbZoneName_Object = MibScalar
axNotificationGslbZoneName = _AxNotificationGslbZoneName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 28),
    _AxNotificationGslbZoneName_Type()
)
axNotificationGslbZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbZoneName.setStatus("current")
_AxNotificationGslbZoneServiceProto_Type = DisplayString
_AxNotificationGslbZoneServiceProto_Object = MibScalar
axNotificationGslbZoneServiceProto = _AxNotificationGslbZoneServiceProto_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 29),
    _AxNotificationGslbZoneServiceProto_Type()
)
axNotificationGslbZoneServiceProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbZoneServiceProto.setStatus("current")
_AxNotificationGslbZoneServiceName_Type = DisplayString
_AxNotificationGslbZoneServiceName_Object = MibScalar
axNotificationGslbZoneServiceName = _AxNotificationGslbZoneServiceName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 30),
    _AxNotificationGslbZoneServiceName_Type()
)
axNotificationGslbZoneServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbZoneServiceName.setStatus("current")
_AxNotificationGslbGroupName_Type = DisplayString
_AxNotificationGslbGroupName_Object = MibScalar
axNotificationGslbGroupName = _AxNotificationGslbGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 31),
    _AxNotificationGslbGroupName_Type()
)
axNotificationGslbGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbGroupName.setStatus("current")
_AxNotificationGslbGroupEntity_Type = DisplayString
_AxNotificationGslbGroupEntity_Object = MibScalar
axNotificationGslbGroupEntity = _AxNotificationGslbGroupEntity_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 32),
    _AxNotificationGslbGroupEntity_Type()
)
axNotificationGslbGroupEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationGslbGroupEntity.setStatus("current")
_AxNotificationLicensedModuleName_Type = DisplayString
_AxNotificationLicensedModuleName_Object = MibScalar
axNotificationLicensedModuleName = _AxNotificationLicensedModuleName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 33),
    _AxNotificationLicensedModuleName_Type()
)
axNotificationLicensedModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLicensedModuleName.setStatus("current")


class _AxNotificationShutdownReason_Type(Integer32):
    """Custom type axNotificationShutdownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tooHighSystemTemperature", 1),
          ("insufficientPowerSupply", 2))
    )


_AxNotificationShutdownReason_Type.__name__ = "Integer32"
_AxNotificationShutdownReason_Object = MibScalar
axNotificationShutdownReason = _AxNotificationShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 34),
    _AxNotificationShutdownReason_Type()
)
axNotificationShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationShutdownReason.setStatus("current")
_AxNotificationIpAddressType_Type = InetAddressType
_AxNotificationIpAddressType_Object = MibScalar
axNotificationIpAddressType = _AxNotificationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 35),
    _AxNotificationIpAddressType_Type()
)
axNotificationIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationIpAddressType.setStatus("current")
_AxNotificationLicenseDisableDuration_Type = Unsigned32
_AxNotificationLicenseDisableDuration_Object = MibScalar
axNotificationLicenseDisableDuration = _AxNotificationLicenseDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 36),
    _AxNotificationLicenseDisableDuration_Type()
)
axNotificationLicenseDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLicenseDisableDuration.setStatus("current")
_AxNotificationSslServerCertificateErrCounter_Type = Unsigned32
_AxNotificationSslServerCertificateErrCounter_Object = MibScalar
axNotificationSslServerCertificateErrCounter = _AxNotificationSslServerCertificateErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 37),
    _AxNotificationSslServerCertificateErrCounter_Type()
)
axNotificationSslServerCertificateErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSslServerCertificateErrCounter.setStatus("current")
_AxNotificationServerSelectionFailureReason_Type = DisplayString
_AxNotificationServerSelectionFailureReason_Object = MibScalar
axNotificationServerSelectionFailureReason = _AxNotificationServerSelectionFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 38),
    _AxNotificationServerSelectionFailureReason_Type()
)
axNotificationServerSelectionFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationServerSelectionFailureReason.setStatus("current")
_AxNotificationConnectionTypeName_Type = DisplayString
_AxNotificationConnectionTypeName_Object = MibScalar
axNotificationConnectionTypeName = _AxNotificationConnectionTypeName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 39),
    _AxNotificationConnectionTypeName_Type()
)
axNotificationConnectionTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationConnectionTypeName.setStatus("current")


class _AxNotificationSlbObjectChange_Type(Integer32):
    """Custom type axNotificationSlbObjectChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_AxNotificationSlbObjectChange_Type.__name__ = "Integer32"
_AxNotificationSlbObjectChange_Object = MibScalar
axNotificationSlbObjectChange = _AxNotificationSlbObjectChange_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 40),
    _AxNotificationSlbObjectChange_Type()
)
axNotificationSlbObjectChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSlbObjectChange.setStatus("current")
_AxNotificationCertificateName_Type = DisplayString
_AxNotificationCertificateName_Object = MibScalar
axNotificationCertificateName = _AxNotificationCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 41),
    _AxNotificationCertificateName_Type()
)
axNotificationCertificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationCertificateName.setStatus("current")
_AxNotificationDateTime_Type = DateAndTime
_AxNotificationDateTime_Object = MibScalar
axNotificationDateTime = _AxNotificationDateTime_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 42),
    _AxNotificationDateTime_Type()
)
axNotificationDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationDateTime.setStatus("current")


class _AxNotificationSLBServerPortType_Type(Integer32):
    """Custom type axNotificationSLBServerPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 3))
    )


_AxNotificationSLBServerPortType_Type.__name__ = "Integer32"
_AxNotificationSLBServerPortType_Object = MibScalar
axNotificationSLBServerPortType = _AxNotificationSLBServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 43),
    _AxNotificationSLBServerPortType_Type()
)
axNotificationSLBServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBServerPortType.setStatus("current")
_AxNotificationPartitionResourceName_Type = DisplayString
_AxNotificationPartitionResourceName_Object = MibScalar
axNotificationPartitionResourceName = _AxNotificationPartitionResourceName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 44),
    _AxNotificationPartitionResourceName_Type()
)
axNotificationPartitionResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPartitionResourceName.setStatus("current")


class _AxNotificationPartitionResourceUsageLevel_Type(Integer32):
    """Custom type axNotificationPartitionResourceUsageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("below", 1),
          ("above", 2))
    )


_AxNotificationPartitionResourceUsageLevel_Type.__name__ = "Integer32"
_AxNotificationPartitionResourceUsageLevel_Object = MibScalar
axNotificationPartitionResourceUsageLevel = _AxNotificationPartitionResourceUsageLevel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 45),
    _AxNotificationPartitionResourceUsageLevel_Type()
)
axNotificationPartitionResourceUsageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPartitionResourceUsageLevel.setStatus("current")
_AxNotificationTacasServerHost_Type = DisplayString
_AxNotificationTacasServerHost_Object = MibScalar
axNotificationTacasServerHost = _AxNotificationTacasServerHost_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 46),
    _AxNotificationTacasServerHost_Type()
)
axNotificationTacasServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationTacasServerHost.setStatus("current")


class _AxNotificationUpDown_Type(Integer32):
    """Custom type axNotificationUpDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AxNotificationUpDown_Type.__name__ = "Integer32"
_AxNotificationUpDown_Object = MibScalar
axNotificationUpDown = _AxNotificationUpDown_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 47),
    _AxNotificationUpDown_Type()
)
axNotificationUpDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationUpDown.setStatus("current")


class _AxNotificationTrueFalse_Type(Integer32):
    """Custom type axNotificationTrueFalse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AxNotificationTrueFalse_Type.__name__ = "Integer32"
_AxNotificationTrueFalse_Object = MibScalar
axNotificationTrueFalse = _AxNotificationTrueFalse_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 48),
    _AxNotificationTrueFalse_Type()
)
axNotificationTrueFalse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationTrueFalse.setStatus("current")
_AxNotificationLsnIpAddress_Type = DisplayString
_AxNotificationLsnIpAddress_Object = MibScalar
axNotificationLsnIpAddress = _AxNotificationLsnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 50),
    _AxNotificationLsnIpAddress_Type()
)
axNotificationLsnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnIpAddress.setStatus("current")


class _AxNotificationLsnProtoType_Type(Integer32):
    """Custom type axNotificationLsnProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("icmpV6", 5))
    )


_AxNotificationLsnProtoType_Type.__name__ = "Integer32"
_AxNotificationLsnProtoType_Object = MibScalar
axNotificationLsnProtoType = _AxNotificationLsnProtoType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 51),
    _AxNotificationLsnProtoType_Type()
)
axNotificationLsnProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnProtoType.setStatus("current")
_AxNotificationLsnCurrentUsage_Type = Integer32
_AxNotificationLsnCurrentUsage_Object = MibScalar
axNotificationLsnCurrentUsage = _AxNotificationLsnCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 52),
    _AxNotificationLsnCurrentUsage_Type()
)
axNotificationLsnCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnCurrentUsage.setStatus("current")
_AxNotificationLsnPoolName_Type = DisplayString
_AxNotificationLsnPoolName_Object = MibScalar
axNotificationLsnPoolName = _AxNotificationLsnPoolName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 53),
    _AxNotificationLsnPoolName_Type()
)
axNotificationLsnPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnPoolName.setStatus("current")
_AxNotificationLsnExceededTimes_Type = Integer32
_AxNotificationLsnExceededTimes_Object = MibScalar
axNotificationLsnExceededTimes = _AxNotificationLsnExceededTimes_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 54),
    _AxNotificationLsnExceededTimes_Type()
)
axNotificationLsnExceededTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnExceededTimes.setStatus("current")
_AxNotificationLsnFixedNatPortMappingFileName_Type = DisplayString
_AxNotificationLsnFixedNatPortMappingFileName_Object = MibScalar
axNotificationLsnFixedNatPortMappingFileName = _AxNotificationLsnFixedNatPortMappingFileName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 55),
    _AxNotificationLsnFixedNatPortMappingFileName_Type()
)
axNotificationLsnFixedNatPortMappingFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnFixedNatPortMappingFileName.setStatus("current")


class _AxNotificationLsnFixedNatPortMappingFileChangeType_Type(Integer32):
    """Custom type axNotificationLsnFixedNatPortMappingFileChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("reconfigure", 3))
    )


_AxNotificationLsnFixedNatPortMappingFileChangeType_Type.__name__ = "Integer32"
_AxNotificationLsnFixedNatPortMappingFileChangeType_Object = MibScalar
axNotificationLsnFixedNatPortMappingFileChangeType = _AxNotificationLsnFixedNatPortMappingFileChangeType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 56),
    _AxNotificationLsnFixedNatPortMappingFileChangeType_Type()
)
axNotificationLsnFixedNatPortMappingFileChangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationLsnFixedNatPortMappingFileChangeType.setStatus("current")


class _AxNotificationOldVcsState_Type(Integer32):
    """Custom type axNotificationOldVcsState based on Integer32"""
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
        *(("vmasterCandidate", 0),
          ("activatingSlave", 1),
          ("vBlade", 2),
          ("vMaster", 3),
          ("vMasterTakeover", 4))
    )


_AxNotificationOldVcsState_Type.__name__ = "Integer32"
_AxNotificationOldVcsState_Object = MibScalar
axNotificationOldVcsState = _AxNotificationOldVcsState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 57),
    _AxNotificationOldVcsState_Type()
)
axNotificationOldVcsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationOldVcsState.setStatus("current")


class _AxNotificationNewVcsState_Type(Integer32):
    """Custom type axNotificationNewVcsState based on Integer32"""
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
        *(("vmasterCandidate", 0),
          ("activatingSlave", 1),
          ("vBlade", 2),
          ("vMaster", 3),
          ("vMasterTakeover", 4))
    )


_AxNotificationNewVcsState_Type.__name__ = "Integer32"
_AxNotificationNewVcsState_Object = MibScalar
axNotificationNewVcsState = _AxNotificationNewVcsState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 58),
    _AxNotificationNewVcsState_Type()
)
axNotificationNewVcsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationNewVcsState.setStatus("current")
_AxNotifications_ObjectIdentity = ObjectIdentity
axNotifications = _AxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2)
)
_AxSystemNotifications_ObjectIdentity = ObjectIdentity
axSystemNotifications = _AxSystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1)
)
_AxAppNotifications_ObjectIdentity = ObjectIdentity
axAppNotifications = _AxAppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2)
)
_AxNetworkNotifications_ObjectIdentity = ObjectIdentity
axNetworkNotifications = _AxNetworkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 3)
)
_AxGslbNotifications_ObjectIdentity = ObjectIdentity
axGslbNotifications = _AxGslbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5)
)
_AxSlbNotifications_ObjectIdentity = ObjectIdentity
axSlbNotifications = _AxSlbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6)
)

# Managed Objects groups


# Notification objects

axSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 100, 1)
)
axSyslogTrap.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axSyslogModuleName"),
        ("A10-AX-NOTIFICATIONS", "axSyslogPriority"),
        ("A10-AX-NOTIFICATIONS", "axSyslogMsg"))
)
if mibBuilder.loadTexts:
    axSyslogTrap.setStatus(
        "current"
    )

axSystemStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    axSystemStart.setStatus(
        "current"
    )

axSystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 2)
)
if mibBuilder.loadTexts:
    axSystemShutdown.setStatus(
        "current"
    )

axSystemTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 3)
)
axSystemTempHigh.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemTempHigh.setStatus(
        "current"
    )

axFan1Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 4)
)
if mibBuilder.loadTexts:
    axFan1Failure.setStatus(
        "deprecated"
    )

axFan2Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 5)
)
if mibBuilder.loadTexts:
    axFan2Failure.setStatus(
        "deprecated"
    )

axFan3Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 6)
)
if mibBuilder.loadTexts:
    axFan3Failure.setStatus(
        "deprecated"
    )

axUpperPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 9)
)
if mibBuilder.loadTexts:
    axUpperPowerSupplyFailure.setStatus(
        "deprecated"
    )

axLowerPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 10)
)
if mibBuilder.loadTexts:
    axLowerPowerSupplyFailure.setStatus(
        "deprecated"
    )

axPrimaryHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 11)
)
if mibBuilder.loadTexts:
    axPrimaryHardDiskFailure.setStatus(
        "current"
    )

axSecondaryHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 12)
)
if mibBuilder.loadTexts:
    axSecondaryHardDiskFailure.setStatus(
        "current"
    )

axHardDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 13)
)
if mibBuilder.loadTexts:
    axHardDiskUsageHigh.setStatus(
        "current"
    )

axMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 14)
)
if mibBuilder.loadTexts:
    axMemoryUsageHigh.setStatus(
        "current"
    )

axSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 15)
)
if mibBuilder.loadTexts:
    axSystemRestart.setStatus(
        "current"
    )

axSystemDropPacketEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 16)
)
axSystemDropPacketEvent.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationDroppedPackets")
)
if mibBuilder.loadTexts:
    axSystemDropPacketEvent.setStatus(
        "current"
    )

axSystemRelieveDropPacketEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 17)
)
axSystemRelieveDropPacketEvent.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationDroppedPackets")
)
if mibBuilder.loadTexts:
    axSystemRelieveDropPacketEvent.setStatus(
        "current"
    )

axSystemControlCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 18)
)
axSystemControlCpuHigh.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemControlCpuHigh.setStatus(
        "current"
    )

axSystemDataCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 19)
)
axSystemDataCpuHigh.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemDataCpuHigh.setStatus(
        "current"
    )

axSystemFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 20)
)
axSystemFanFailure.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationFanName")
)
if mibBuilder.loadTexts:
    axSystemFanFailure.setStatus(
        "current"
    )

axSystemPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 21)
)
axSystemPowerSupplyFailure.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationPowerSupplyName")
)
if mibBuilder.loadTexts:
    axSystemPowerSupplyFailure.setStatus(
        "current"
    )

axSystemLicenseRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 22)
)
axSystemLicenseRequired.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationLicensedModuleName")
)
if mibBuilder.loadTexts:
    axSystemLicenseRequired.setStatus(
        "current"
    )

axSystemLicenseLoadSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 23)
)
axSystemLicenseLoadSuccessful.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationLicensedModuleName")
)
if mibBuilder.loadTexts:
    axSystemLicenseLoadSuccessful.setStatus(
        "current"
    )

axSystemLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 24)
)
axSystemLicenseExpired.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationLicensedModuleName")
)
if mibBuilder.loadTexts:
    axSystemLicenseExpired.setStatus(
        "current"
    )

axSystemShutdownForReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 25)
)
axSystemShutdownForReason.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationShutdownReason")
)
if mibBuilder.loadTexts:
    axSystemShutdownForReason.setStatus(
        "current"
    )

axFileSystemBecomeReadOnly = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 26)
)
if mibBuilder.loadTexts:
    axFileSystemBecomeReadOnly.setStatus(
        "current"
    )

axSystemLicensedModuleDisabledForDuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 27)
)
axSystemLicensedModuleDisabledForDuration.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationLicensedModuleName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationLicenseDisableDuration"))
)
if mibBuilder.loadTexts:
    axSystemLicensedModuleDisabledForDuration.setStatus(
        "current"
    )

axSystemControlCpuBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 28)
)
axSystemControlCpuBecomeNormal.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemControlCpuBecomeNormal.setStatus(
        "current"
    )

axSystemDataCpuBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 29)
)
axSystemDataCpuBecomeNormal.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemDataCpuBecomeNormal.setStatus(
        "current"
    )

axSystemTempBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 30)
)
axSystemTempBecomeNormal.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemTempBecomeNormal.setStatus(
        "current"
    )

axHardDiskUsageBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 31)
)
if mibBuilder.loadTexts:
    axHardDiskUsageBecomeNormal.setStatus(
        "current"
    )

axMemoryUsageBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 32)
)
if mibBuilder.loadTexts:
    axMemoryUsageBecomeNormal.setStatus(
        "current"
    )

axSystemFanRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 33)
)
axSystemFanRecover.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationFanName")
)
if mibBuilder.loadTexts:
    axSystemFanRecover.setStatus(
        "current"
    )

axSystemPowerSupplyRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 34)
)
axSystemPowerSupplyRecover.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationPowerSupplyName")
)
if mibBuilder.loadTexts:
    axSystemPowerSupplyRecover.setStatus(
        "current"
    )

axSystemConnectionResourceHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 35)
)
axSystemConnectionResourceHigh.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConnectionTypeName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemConnectionResourceHigh.setStatus(
        "current"
    )

axSystemConnectionResourceBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 36)
)
axSystemConnectionResourceBecomeNormal.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConnectionTypeName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemConnectionResourceBecomeNormal.setStatus(
        "current"
    )

axSystemSmpResourceHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 37)
)
axSystemSmpResourceHigh.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConnectionTypeName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemSmpResourceHigh.setStatus(
        "current"
    )

axSystemSmpResourceBecomeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 38)
)
axSystemSmpResourceBecomeNormal.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConnectionTypeName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemSmpResourceBecomeNormal.setStatus(
        "current"
    )

axTacacsMonitorServerUpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 39)
)
axTacacsMonitorServerUpDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationTacasServerHost"),
        ("A10-AX-NOTIFICATIONS", "axNotificationUpDown"))
)
if mibBuilder.loadTexts:
    axTacacsMonitorServerUpDown.setStatus(
        "current"
    )

axHighPrioritySyslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 41)
)
axHighPrioritySyslog.setObjects(
    ("A10-AX-NOTIFICATIONS", "axNotificationMsg")
)
if mibBuilder.loadTexts:
    axHighPrioritySyslog.setStatus(
        "current"
    )

axHAStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 1)
)
axHAStandby.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationHAGroup"))
)
if mibBuilder.loadTexts:
    axHAStandby.setStatus(
        "current"
    )

axHAActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 2)
)
axHAActive.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationHAGroup"))
)
if mibBuilder.loadTexts:
    axHAActive.setStatus(
        "current"
    )

axHAActiveActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 3)
)
axHAActiveActive.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationHAGroup"))
)
if mibBuilder.loadTexts:
    axHAActiveActive.setStatus(
        "deprecated"
    )

axServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 4)
)
axServiceDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"))
)
if mibBuilder.loadTexts:
    axServiceDown.setStatus(
        "current"
    )

axServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 5)
)
axServiceUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"))
)
if mibBuilder.loadTexts:
    axServiceUp.setStatus(
        "current"
    )

axServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 6)
)
axServerDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"))
)
if mibBuilder.loadTexts:
    axServerDown.setStatus(
        "current"
    )

axServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 7)
)
axServerUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"))
)
if mibBuilder.loadTexts:
    axServerUp.setStatus(
        "current"
    )

axServerConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 8)
)
axServerConnLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServerConnLimit.setStatus(
        "current"
    )

axServerConnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 9)
)
axServerConnResume.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServerConnResume.setStatus(
        "current"
    )

axServiceConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 10)
)
axServiceConnLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServiceConnLimit.setStatus(
        "current"
    )

axServiceConnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 11)
)
axServiceConnResume.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServiceConnResume.setStatus(
        "current"
    )

axVirtualServerPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 12)
)
axVirtualServerPortDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServerPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServerPortType"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortDown.setStatus(
        "current"
    )

axVirtualServerPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 13)
)
axVirtualServerPortUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServerPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServerPortType"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortUp.setStatus(
        "current"
    )

axApplicationBufferReachLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 14)
)
axApplicationBufferReachLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationConfiguredThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axApplicationBufferReachLimit.setStatus(
        "current"
    )

axVirtualServerPortReachConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 15)
)
axVirtualServerPortReachConnLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortReachConnLimit.setStatus(
        "current"
    )

axVirtualServerPortReachConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 16)
)
axVirtualServerPortReachConnRateLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortReachConnRateLimit.setStatus(
        "current"
    )

axVirtualServerReachConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 17)
)
axVirtualServerReachConnLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerReachConnLimit.setStatus(
        "current"
    )

axVirtualServerReachConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 18)
)
axVirtualServerReachConnRateLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerReachConnRateLimit.setStatus(
        "current"
    )

axServerConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 19)
)
axServerConnRateLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServerConnRateLimit.setStatus(
        "current"
    )

axServiceConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 20)
)
axServiceConnRateLimit.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServiceConnRateLimit.setStatus(
        "current"
    )

axServiceGroupMemberEnabledForNewConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 21)
)
axServiceGroupMemberEnabledForNewConn.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServiceGroupName"))
)
if mibBuilder.loadTexts:
    axServiceGroupMemberEnabledForNewConn.setStatus(
        "current"
    )

axServiceGroupMemberDisabledForNewConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 22)
)
axServiceGroupMemberDisabledForNewConn.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServiceGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"))
)
if mibBuilder.loadTexts:
    axServiceGroupMemberDisabledForNewConn.setStatus(
        "current"
    )

axVrrpActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 23)
)
axVrrpActive.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVrid"))
)
if mibBuilder.loadTexts:
    axVrrpActive.setStatus(
        "current"
    )

axVrrpStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 24)
)
axVrrpStandby.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVrid"))
)
if mibBuilder.loadTexts:
    axVrrpStandby.setStatus(
        "current"
    )

axSslServerCertificateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 25)
)
axSslServerCertificateErr.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSslServerCertificateErrCounter"))
)
if mibBuilder.loadTexts:
    axSslServerCertificateErr.setStatus(
        "current"
    )

axServerSelectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 26)
)
axServerSelectionFailure.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationServerSelectionFailureReason"))
)
if mibBuilder.loadTexts:
    axServerSelectionFailure.setStatus(
        "current"
    )

axVirtualServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 27)
)
axVirtualServerUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axVirtualServerUp.setStatus(
        "current"
    )

axVirtualServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 28)
)
axVirtualServerDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axVirtualServerDown.setStatus(
        "current"
    )

axServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 29)
)
axServerDisabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationTrueFalse"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axServerDisabled.setStatus(
        "current"
    )

axServiceGroupUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 30)
)
axServiceGroupUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServiceGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServerPortType"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axServiceGroupUp.setStatus(
        "current"
    )

axServiceGroupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 31)
)
axServiceGroupDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServiceGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServerPortType"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axServiceGroupDown.setStatus(
        "current"
    )

axServiceGroupMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 32)
)
axServiceGroupMemberUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServiceGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axServiceGroupMemberUp.setStatus(
        "current"
    )

axServiceGroupMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 33)
)
axServiceGroupMemberDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServiceGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axServiceGroupMemberDown.setStatus(
        "current"
    )

axVcsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 34)
)
axVcsStateChange.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationOldVcsState"),
        ("A10-AX-NOTIFICATIONS", "axNotificationNewVcsState"))
)
if mibBuilder.loadTexts:
    axVcsStateChange.setStatus(
        "current"
    )

axGatewayUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 35)
)
axGatewayUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGatewayUp.setStatus(
        "current"
    )

axGatewayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 36)
)
axGatewayDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGatewayDown.setStatus(
        "current"
    )

axNetworkTrunkPortsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 3, 1)
)
axNetworkTrunkPortsThreshold.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationTrunkID"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPortThreshold"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCurrentUpPorts"))
)
if mibBuilder.loadTexts:
    axNetworkTrunkPortsThreshold.setStatus(
        "current"
    )

axGslbSiteAdminEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 1)
)
axGslbSiteAdminEnabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbSiteAdminEnabled.setStatus(
        "current"
    )

axGslbSiteAdminDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 2)
)
axGslbSiteAdminDisabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbSiteAdminDisabled.setStatus(
        "current"
    )

axGslbSiteOperationalStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 3)
)
axGslbSiteOperationalStateUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbSiteOperationalStateUp.setStatus(
        "current"
    )

axGslbSiteOperationalStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 4)
)
axGslbSiteOperationalStateDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbSiteOperationalStateDown.setStatus(
        "current"
    )

axGslbSiteSlbDeviceStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 5)
)
axGslbSiteSlbDeviceStateUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteSlbDeviceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbSiteSlbDeviceStateUp.setStatus(
        "current"
    )

axGslbSiteSlbDeviceStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 6)
)
axGslbSiteSlbDeviceStateDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbSiteSlbDeviceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbSiteSlbDeviceStateDown.setStatus(
        "current"
    )

axGslbServiceIpAdminEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 9)
)
axGslbServiceIpAdminEnabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpAddr"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbServiceIpAdminEnabled.setStatus(
        "current"
    )

axGslbServiceIpAdminDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 10)
)
axGslbServiceIpAdminDisabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpAddr"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbServiceIpAdminDisabled.setStatus(
        "current"
    )

axGslbServiceIpOperationalStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 11)
)
axGslbServiceIpOperationalStateUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpAddr"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbServiceIpOperationalStateUp.setStatus(
        "current"
    )

axGslbServiceIpOperationalStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 12)
)
axGslbServiceIpOperationalStateDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpAddr"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbServiceIpOperationalStateDown.setStatus(
        "current"
    )

axGslbServiceIpPortStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 13)
)
axGslbServiceIpPortStateUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpAddr"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpPortType"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbServiceIpPortStateUp.setStatus(
        "current"
    )

axGslbServiceIpPortStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 14)
)
axGslbServiceIpPortStateDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpAddr"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbServiceIpPortType"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbServiceIpPortStateDown.setStatus(
        "current"
    )

axGslbZoneAdminEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 15)
)
axGslbZoneAdminEnabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneAdminEnabled.setStatus(
        "current"
    )

axGslbZoneAdminDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 16)
)
axGslbZoneAdminDisabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneAdminDisabled.setStatus(
        "current"
    )

axGslbZoneOperationalStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 17)
)
axGslbZoneOperationalStateUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneOperationalStateUp.setStatus(
        "current"
    )

axGslbZoneOperationalStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 18)
)
axGslbZoneOperationalStateDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneOperationalStateDown.setStatus(
        "current"
    )

axGslbZoneServiceAdminEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 19)
)
axGslbZoneServiceAdminEnabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceProto"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneServiceAdminEnabled.setStatus(
        "current"
    )

axGslbZoneServiceAdminDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 20)
)
axGslbZoneServiceAdminDisabled.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceProto"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneServiceAdminDisabled.setStatus(
        "current"
    )

axGslbZoneServiceOperationalStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 21)
)
axGslbZoneServiceOperationalStateUp.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceProto"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneServiceOperationalStateUp.setStatus(
        "current"
    )

axGslbZoneServiceOperationalStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 22)
)
axGslbZoneServiceOperationalStateDown.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceProto"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbZoneServiceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axGslbZoneServiceOperationalStateDown.setStatus(
        "current"
    )

axGslbGroupBecomeMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 23)
)
axGslbGroupBecomeMaster.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupEntity"))
)
if mibBuilder.loadTexts:
    axGslbGroupBecomeMaster.setStatus(
        "current"
    )

axGslbGroupRemovedMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 24)
)
axGslbGroupRemovedMaster.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupEntity"))
)
if mibBuilder.loadTexts:
    axGslbGroupRemovedMaster.setStatus(
        "current"
    )

axGslbGroupMemberJoinGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 25)
)
axGslbGroupMemberJoinGroup.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupEntity"))
)
if mibBuilder.loadTexts:
    axGslbGroupMemberJoinGroup.setStatus(
        "current"
    )

axGslbGroupMemberLeaveGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 5, 26)
)
axGslbGroupMemberLeaveGroup.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationGslbGroupEntity"))
)
if mibBuilder.loadTexts:
    axGslbGroupMemberLeaveGroup.setStatus(
        "current"
    )

axVirtualServerCreateDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 1)
)
axVirtualServerCreateDelete.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSlbObjectChange"))
)
if mibBuilder.loadTexts:
    axVirtualServerCreateDelete.setStatus(
        "current"
    )

axVirtualServerPortCreateDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 2)
)
axVirtualServerPortCreateDelete.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServerPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationVirtualServerPortType"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSlbObjectChange"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortCreateDelete.setStatus(
        "current"
    )

axServerCreateDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 3)
)
axServerCreateDelete.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSlbObjectChange"))
)
if mibBuilder.loadTexts:
    axServerCreateDelete.setStatus(
        "current"
    )

axServerPortCreateDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 4)
)
axServerPortCreateDelete.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServer"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBPort"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSLBServerPortType"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSlbObjectChange"))
)
if mibBuilder.loadTexts:
    axServerPortCreateDelete.setStatus(
        "current"
    )

axSslCertificateCreateDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 5)
)
axSslCertificateCreateDelete.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCertificateName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationSlbObjectChange"))
)
if mibBuilder.loadTexts:
    axSslCertificateCreateDelete.setStatus(
        "current"
    )

axSslCertificateExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 6)
)
axSslCertificateExpiring.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationCertificateName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationDateTime"))
)
if mibBuilder.loadTexts:
    axSslCertificateExpiring.setStatus(
        "current"
    )

axPartitionResourceUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 6, 7)
)
axPartitionResourceUsageWarning.setObjects(
      *(("A10-AX-NOTIFICATIONS", "axNotificationMsg"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionResourceName"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionResourceUsageLevel"),
        ("A10-AX-NOTIFICATIONS", "axNotificationPartitionName"))
)
if mibBuilder.loadTexts:
    axPartitionResourceUsageWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A10-AX-NOTIFICATIONS",
    **{"axSyslogTrapPrefix": axSyslogTrapPrefix,
       "axSyslogTrap": axSyslogTrap,
       "axSyslogTrapObjects": axSyslogTrapObjects,
       "axSyslogModuleName": axSyslogModuleName,
       "axSyslogPriority": axSyslogPriority,
       "axSyslogMsg": axSyslogMsg,
       "axNotificationObjects": axNotificationObjects,
       "axNotificationMsg": axNotificationMsg,
       "axNotificationSLBServer": axNotificationSLBServer,
       "axNotificationSLBPort": axNotificationSLBPort,
       "axNotificationSLBCurConns": axNotificationSLBCurConns,
       "axNotificationVirtualServer": axNotificationVirtualServer,
       "axNotificationVirtualServerPort": axNotificationVirtualServerPort,
       "axNotificationVirtualServerPortType": axNotificationVirtualServerPortType,
       "axNotificationDroppedPackets": axNotificationDroppedPackets,
       "axNotificationConfiguredThreshold": axNotificationConfiguredThreshold,
       "axNotificationCurrentUsage": axNotificationCurrentUsage,
       "axNotificationConnLimit": axNotificationConnLimit,
       "axNotificationTrunkID": axNotificationTrunkID,
       "axNotificationPortThreshold": axNotificationPortThreshold,
       "axNotificationCurrentUpPorts": axNotificationCurrentUpPorts,
       "axNotificationFanName": axNotificationFanName,
       "axNotificationPowerSupplyName": axNotificationPowerSupplyName,
       "axNotificationHAGroup": axNotificationHAGroup,
       "axNotificationSLBServiceGroupName": axNotificationSLBServiceGroupName,
       "axNotificationPartitionId": axNotificationPartitionId,
       "axNotificationVrid": axNotificationVrid,
       "axNotificationPartitionName": axNotificationPartitionName,
       "axNotificationGslbSiteName": axNotificationGslbSiteName,
       "axNotificationGslbSiteSlbDeviceName": axNotificationGslbSiteSlbDeviceName,
       "axNotificationGslbSiteIpServerAddr": axNotificationGslbSiteIpServerAddr,
       "axNotificationGslbServiceIpName": axNotificationGslbServiceIpName,
       "axNotificationGslbServiceIpAddr": axNotificationGslbServiceIpAddr,
       "axNotificationGslbServiceIpPortType": axNotificationGslbServiceIpPortType,
       "axNotificationGslbZoneName": axNotificationGslbZoneName,
       "axNotificationGslbZoneServiceProto": axNotificationGslbZoneServiceProto,
       "axNotificationGslbZoneServiceName": axNotificationGslbZoneServiceName,
       "axNotificationGslbGroupName": axNotificationGslbGroupName,
       "axNotificationGslbGroupEntity": axNotificationGslbGroupEntity,
       "axNotificationLicensedModuleName": axNotificationLicensedModuleName,
       "axNotificationShutdownReason": axNotificationShutdownReason,
       "axNotificationIpAddressType": axNotificationIpAddressType,
       "axNotificationLicenseDisableDuration": axNotificationLicenseDisableDuration,
       "axNotificationSslServerCertificateErrCounter": axNotificationSslServerCertificateErrCounter,
       "axNotificationServerSelectionFailureReason": axNotificationServerSelectionFailureReason,
       "axNotificationConnectionTypeName": axNotificationConnectionTypeName,
       "axNotificationSlbObjectChange": axNotificationSlbObjectChange,
       "axNotificationCertificateName": axNotificationCertificateName,
       "axNotificationDateTime": axNotificationDateTime,
       "axNotificationSLBServerPortType": axNotificationSLBServerPortType,
       "axNotificationPartitionResourceName": axNotificationPartitionResourceName,
       "axNotificationPartitionResourceUsageLevel": axNotificationPartitionResourceUsageLevel,
       "axNotificationTacasServerHost": axNotificationTacasServerHost,
       "axNotificationUpDown": axNotificationUpDown,
       "axNotificationTrueFalse": axNotificationTrueFalse,
       "axNotificationLsnIpAddress": axNotificationLsnIpAddress,
       "axNotificationLsnProtoType": axNotificationLsnProtoType,
       "axNotificationLsnCurrentUsage": axNotificationLsnCurrentUsage,
       "axNotificationLsnPoolName": axNotificationLsnPoolName,
       "axNotificationLsnExceededTimes": axNotificationLsnExceededTimes,
       "axNotificationLsnFixedNatPortMappingFileName": axNotificationLsnFixedNatPortMappingFileName,
       "axNotificationLsnFixedNatPortMappingFileChangeType": axNotificationLsnFixedNatPortMappingFileChangeType,
       "axNotificationOldVcsState": axNotificationOldVcsState,
       "axNotificationNewVcsState": axNotificationNewVcsState,
       "axNotifications": axNotifications,
       "axSystemNotifications": axSystemNotifications,
       "axSystemStart": axSystemStart,
       "axSystemShutdown": axSystemShutdown,
       "axSystemTempHigh": axSystemTempHigh,
       "axFan1Failure": axFan1Failure,
       "axFan2Failure": axFan2Failure,
       "axFan3Failure": axFan3Failure,
       "axUpperPowerSupplyFailure": axUpperPowerSupplyFailure,
       "axLowerPowerSupplyFailure": axLowerPowerSupplyFailure,
       "axPrimaryHardDiskFailure": axPrimaryHardDiskFailure,
       "axSecondaryHardDiskFailure": axSecondaryHardDiskFailure,
       "axHardDiskUsageHigh": axHardDiskUsageHigh,
       "axMemoryUsageHigh": axMemoryUsageHigh,
       "axSystemRestart": axSystemRestart,
       "axSystemDropPacketEvent": axSystemDropPacketEvent,
       "axSystemRelieveDropPacketEvent": axSystemRelieveDropPacketEvent,
       "axSystemControlCpuHigh": axSystemControlCpuHigh,
       "axSystemDataCpuHigh": axSystemDataCpuHigh,
       "axSystemFanFailure": axSystemFanFailure,
       "axSystemPowerSupplyFailure": axSystemPowerSupplyFailure,
       "axSystemLicenseRequired": axSystemLicenseRequired,
       "axSystemLicenseLoadSuccessful": axSystemLicenseLoadSuccessful,
       "axSystemLicenseExpired": axSystemLicenseExpired,
       "axSystemShutdownForReason": axSystemShutdownForReason,
       "axFileSystemBecomeReadOnly": axFileSystemBecomeReadOnly,
       "axSystemLicensedModuleDisabledForDuration": axSystemLicensedModuleDisabledForDuration,
       "axSystemControlCpuBecomeNormal": axSystemControlCpuBecomeNormal,
       "axSystemDataCpuBecomeNormal": axSystemDataCpuBecomeNormal,
       "axSystemTempBecomeNormal": axSystemTempBecomeNormal,
       "axHardDiskUsageBecomeNormal": axHardDiskUsageBecomeNormal,
       "axMemoryUsageBecomeNormal": axMemoryUsageBecomeNormal,
       "axSystemFanRecover": axSystemFanRecover,
       "axSystemPowerSupplyRecover": axSystemPowerSupplyRecover,
       "axSystemConnectionResourceHigh": axSystemConnectionResourceHigh,
       "axSystemConnectionResourceBecomeNormal": axSystemConnectionResourceBecomeNormal,
       "axSystemSmpResourceHigh": axSystemSmpResourceHigh,
       "axSystemSmpResourceBecomeNormal": axSystemSmpResourceBecomeNormal,
       "axTacacsMonitorServerUpDown": axTacacsMonitorServerUpDown,
       "axHighPrioritySyslog": axHighPrioritySyslog,
       "axAppNotifications": axAppNotifications,
       "axHAStandby": axHAStandby,
       "axHAActive": axHAActive,
       "axHAActiveActive": axHAActiveActive,
       "axServiceDown": axServiceDown,
       "axServiceUp": axServiceUp,
       "axServerDown": axServerDown,
       "axServerUp": axServerUp,
       "axServerConnLimit": axServerConnLimit,
       "axServerConnResume": axServerConnResume,
       "axServiceConnLimit": axServiceConnLimit,
       "axServiceConnResume": axServiceConnResume,
       "axVirtualServerPortDown": axVirtualServerPortDown,
       "axVirtualServerPortUp": axVirtualServerPortUp,
       "axApplicationBufferReachLimit": axApplicationBufferReachLimit,
       "axVirtualServerPortReachConnLimit": axVirtualServerPortReachConnLimit,
       "axVirtualServerPortReachConnRateLimit": axVirtualServerPortReachConnRateLimit,
       "axVirtualServerReachConnLimit": axVirtualServerReachConnLimit,
       "axVirtualServerReachConnRateLimit": axVirtualServerReachConnRateLimit,
       "axServerConnRateLimit": axServerConnRateLimit,
       "axServiceConnRateLimit": axServiceConnRateLimit,
       "axServiceGroupMemberEnabledForNewConn": axServiceGroupMemberEnabledForNewConn,
       "axServiceGroupMemberDisabledForNewConn": axServiceGroupMemberDisabledForNewConn,
       "axVrrpActive": axVrrpActive,
       "axVrrpStandby": axVrrpStandby,
       "axSslServerCertificateErr": axSslServerCertificateErr,
       "axServerSelectionFailure": axServerSelectionFailure,
       "axVirtualServerUp": axVirtualServerUp,
       "axVirtualServerDown": axVirtualServerDown,
       "axServerDisabled": axServerDisabled,
       "axServiceGroupUp": axServiceGroupUp,
       "axServiceGroupDown": axServiceGroupDown,
       "axServiceGroupMemberUp": axServiceGroupMemberUp,
       "axServiceGroupMemberDown": axServiceGroupMemberDown,
       "axVcsStateChange": axVcsStateChange,
       "axGatewayUp": axGatewayUp,
       "axGatewayDown": axGatewayDown,
       "axNetworkNotifications": axNetworkNotifications,
       "axNetworkTrunkPortsThreshold": axNetworkTrunkPortsThreshold,
       "axGslbNotifications": axGslbNotifications,
       "axGslbSiteAdminEnabled": axGslbSiteAdminEnabled,
       "axGslbSiteAdminDisabled": axGslbSiteAdminDisabled,
       "axGslbSiteOperationalStateUp": axGslbSiteOperationalStateUp,
       "axGslbSiteOperationalStateDown": axGslbSiteOperationalStateDown,
       "axGslbSiteSlbDeviceStateUp": axGslbSiteSlbDeviceStateUp,
       "axGslbSiteSlbDeviceStateDown": axGslbSiteSlbDeviceStateDown,
       "axGslbServiceIpAdminEnabled": axGslbServiceIpAdminEnabled,
       "axGslbServiceIpAdminDisabled": axGslbServiceIpAdminDisabled,
       "axGslbServiceIpOperationalStateUp": axGslbServiceIpOperationalStateUp,
       "axGslbServiceIpOperationalStateDown": axGslbServiceIpOperationalStateDown,
       "axGslbServiceIpPortStateUp": axGslbServiceIpPortStateUp,
       "axGslbServiceIpPortStateDown": axGslbServiceIpPortStateDown,
       "axGslbZoneAdminEnabled": axGslbZoneAdminEnabled,
       "axGslbZoneAdminDisabled": axGslbZoneAdminDisabled,
       "axGslbZoneOperationalStateUp": axGslbZoneOperationalStateUp,
       "axGslbZoneOperationalStateDown": axGslbZoneOperationalStateDown,
       "axGslbZoneServiceAdminEnabled": axGslbZoneServiceAdminEnabled,
       "axGslbZoneServiceAdminDisabled": axGslbZoneServiceAdminDisabled,
       "axGslbZoneServiceOperationalStateUp": axGslbZoneServiceOperationalStateUp,
       "axGslbZoneServiceOperationalStateDown": axGslbZoneServiceOperationalStateDown,
       "axGslbGroupBecomeMaster": axGslbGroupBecomeMaster,
       "axGslbGroupRemovedMaster": axGslbGroupRemovedMaster,
       "axGslbGroupMemberJoinGroup": axGslbGroupMemberJoinGroup,
       "axGslbGroupMemberLeaveGroup": axGslbGroupMemberLeaveGroup,
       "axSlbNotifications": axSlbNotifications,
       "axVirtualServerCreateDelete": axVirtualServerCreateDelete,
       "axVirtualServerPortCreateDelete": axVirtualServerPortCreateDelete,
       "axServerCreateDelete": axServerCreateDelete,
       "axServerPortCreateDelete": axServerPortCreateDelete,
       "axSslCertificateCreateDelete": axSslCertificateCreateDelete,
       "axSslCertificateExpiring": axSslCertificateExpiring,
       "axPartitionResourceUsageWarning": axPartitionResourceUsageWarning}
)
