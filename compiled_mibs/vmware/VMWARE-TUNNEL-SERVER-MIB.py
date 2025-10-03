# SNMP MIB module (VMWARE-TUNNEL-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-TUNNEL-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:32 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(vmwPerAppTunnel,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwPerAppTunnel")

(VmwLongDisplayString,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwLongDisplayString")


# MODULE-IDENTITY

vmwTunnelServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1)
)
if mibBuilder.loadTexts:
    vmwTunnelServerMIB.setRevisions(
        ("2022-10-28 00:00",
         "2020-08-21 00:00",
         "2020-07-21 00:00",
         "2019-10-30 00:00",
         "2018-08-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwTunnelUpDownState(TextualConvention, Integer32):
    status = "current"
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



class VmwTunnelCascadeModeState(TextualConvention, Integer32):
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
        *(("off", 1),
          ("frontend", 2),
          ("backend", 3))
    )



class VmwTunnelLogState(TextualConvention, Integer32):
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
        *(("off", 0),
          ("error", 1),
          ("warning", 2),
          ("info", 3),
          ("debug", 4))
    )



# MIB Managed Objects in the order of their OIDs

_VmwTunnelServerStat_ObjectIdentity = ObjectIdentity
vmwTunnelServerStat = _VmwTunnelServerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1)
)


class _VmwTunnelNumDevices_Type(Gauge32):
    """Custom type vmwTunnelNumDevices based on Gauge32"""
    defaultValue = 0


_VmwTunnelNumDevices_Type.__name__ = "Gauge32"
_VmwTunnelNumDevices_Object = MibScalar
vmwTunnelNumDevices = _VmwTunnelNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 1),
    _VmwTunnelNumDevices_Type()
)
vmwTunnelNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumDevices.setStatus("current")


class _VmwTunnelNumDevicesPeak_Type(Unsigned32):
    """Custom type vmwTunnelNumDevicesPeak based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumDevicesPeak_Type.__name__ = "Unsigned32"
_VmwTunnelNumDevicesPeak_Object = MibScalar
vmwTunnelNumDevicesPeak = _VmwTunnelNumDevicesPeak_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 2),
    _VmwTunnelNumDevicesPeak_Type()
)
vmwTunnelNumDevicesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumDevicesPeak.setStatus("current")


class _VmwTunnelNumConnections_Type(Gauge32):
    """Custom type vmwTunnelNumConnections based on Gauge32"""
    defaultValue = 0


_VmwTunnelNumConnections_Type.__name__ = "Gauge32"
_VmwTunnelNumConnections_Object = MibScalar
vmwTunnelNumConnections = _VmwTunnelNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 3),
    _VmwTunnelNumConnections_Type()
)
vmwTunnelNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumConnections.setStatus("current")


class _VmwTunnelNumConnectionsPeak_Type(Unsigned32):
    """Custom type vmwTunnelNumConnectionsPeak based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumConnectionsPeak_Type.__name__ = "Unsigned32"
_VmwTunnelNumConnectionsPeak_Object = MibScalar
vmwTunnelNumConnectionsPeak = _VmwTunnelNumConnectionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 4),
    _VmwTunnelNumConnectionsPeak_Type()
)
vmwTunnelNumConnectionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumConnectionsPeak.setStatus("current")
_VmwTunnelDownstreamBitRate_Type = Unsigned32
_VmwTunnelDownstreamBitRate_Object = MibScalar
vmwTunnelDownstreamBitRate = _VmwTunnelDownstreamBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 20),
    _VmwTunnelDownstreamBitRate_Type()
)
vmwTunnelDownstreamBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelDownstreamBitRate.setStatus("current")
if mibBuilder.loadTexts:
    vmwTunnelDownstreamBitRate.setUnits("kB/s")
_VmwTunnelUpstreamBitRate_Type = Unsigned32
_VmwTunnelUpstreamBitRate_Object = MibScalar
vmwTunnelUpstreamBitRate = _VmwTunnelUpstreamBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 21),
    _VmwTunnelUpstreamBitRate_Type()
)
vmwTunnelUpstreamBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelUpstreamBitRate.setStatus("current")
if mibBuilder.loadTexts:
    vmwTunnelUpstreamBitRate.setUnits("kB/s")


class _VmwTunnelNumProxies_Type(Unsigned32):
    """Custom type vmwTunnelNumProxies based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumProxies_Type.__name__ = "Unsigned32"
_VmwTunnelNumProxies_Object = MibScalar
vmwTunnelNumProxies = _VmwTunnelNumProxies_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 40),
    _VmwTunnelNumProxies_Type()
)
vmwTunnelNumProxies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumProxies.setStatus("current")


class _VmwTunnelNumProxiesDown_Type(Unsigned32):
    """Custom type vmwTunnelNumProxiesDown based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumProxiesDown_Type.__name__ = "Unsigned32"
_VmwTunnelNumProxiesDown_Object = MibScalar
vmwTunnelNumProxiesDown = _VmwTunnelNumProxiesDown_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 41),
    _VmwTunnelNumProxiesDown_Type()
)
vmwTunnelNumProxiesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumProxiesDown.setStatus("current")


class _VmwTunnelNumTrafficRules_Type(Unsigned32):
    """Custom type vmwTunnelNumTrafficRules based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumTrafficRules_Type.__name__ = "Unsigned32"
_VmwTunnelNumTrafficRules_Object = MibScalar
vmwTunnelNumTrafficRules = _VmwTunnelNumTrafficRules_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 50),
    _VmwTunnelNumTrafficRules_Type()
)
vmwTunnelNumTrafficRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumTrafficRules.setStatus("current")


class _VmwTunnelNumAllowListedDevices_Type(Unsigned32):
    """Custom type vmwTunnelNumAllowListedDevices based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumAllowListedDevices_Type.__name__ = "Unsigned32"
_VmwTunnelNumAllowListedDevices_Object = MibScalar
vmwTunnelNumAllowListedDevices = _VmwTunnelNumAllowListedDevices_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 60),
    _VmwTunnelNumAllowListedDevices_Type()
)
vmwTunnelNumAllowListedDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumAllowListedDevices.setStatus("current")
_VmwTunnelNumClosedHandshakes_Type = Counter64
_VmwTunnelNumClosedHandshakes_Object = MibScalar
vmwTunnelNumClosedHandshakes = _VmwTunnelNumClosedHandshakes_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 70),
    _VmwTunnelNumClosedHandshakes_Type()
)
vmwTunnelNumClosedHandshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumClosedHandshakes.setStatus("current")
_VmwTunnelNumFailedHandshakes_Type = Counter64
_VmwTunnelNumFailedHandshakes_Object = MibScalar
vmwTunnelNumFailedHandshakes = _VmwTunnelNumFailedHandshakes_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 71),
    _VmwTunnelNumFailedHandshakes_Type()
)
vmwTunnelNumFailedHandshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumFailedHandshakes.setStatus("current")
_VmwTunnelNumNotInAllowlist_Type = Counter64
_VmwTunnelNumNotInAllowlist_Object = MibScalar
vmwTunnelNumNotInAllowlist = _VmwTunnelNumNotInAllowlist_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 72),
    _VmwTunnelNumNotInAllowlist_Type()
)
vmwTunnelNumNotInAllowlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumNotInAllowlist.setStatus("current")
_VmwTunnelNumNonCompliant_Type = Counter64
_VmwTunnelNumNonCompliant_Object = MibScalar
vmwTunnelNumNonCompliant = _VmwTunnelNumNonCompliant_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 73),
    _VmwTunnelNumNonCompliant_Type()
)
vmwTunnelNumNonCompliant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumNonCompliant.setStatus("current")
_VmwTunnelNumNonManaged_Type = Counter64
_VmwTunnelNumNonManaged_Object = MibScalar
vmwTunnelNumNonManaged = _VmwTunnelNumNonManaged_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 74),
    _VmwTunnelNumNonManaged_Type()
)
vmwTunnelNumNonManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumNonManaged.setStatus("current")
_VmwTunnelNumDDoSRejected_Type = Counter64
_VmwTunnelNumDDoSRejected_Object = MibScalar
vmwTunnelNumDDoSRejected = _VmwTunnelNumDDoSRejected_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 75),
    _VmwTunnelNumDDoSRejected_Type()
)
vmwTunnelNumDDoSRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumDDoSRejected.setStatus("current")
_VmwTunnelNumDevicesBlockedByZTNA_Type = Counter64
_VmwTunnelNumDevicesBlockedByZTNA_Object = MibScalar
vmwTunnelNumDevicesBlockedByZTNA = _VmwTunnelNumDevicesBlockedByZTNA_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 76),
    _VmwTunnelNumDevicesBlockedByZTNA_Type()
)
vmwTunnelNumDevicesBlockedByZTNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumDevicesBlockedByZTNA.setStatus("current")
_VmwTunnelNumDevicesBlockedByAdm_Type = Counter64
_VmwTunnelNumDevicesBlockedByAdm_Object = MibScalar
vmwTunnelNumDevicesBlockedByAdm = _VmwTunnelNumDevicesBlockedByAdm_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 77),
    _VmwTunnelNumDevicesBlockedByAdm_Type()
)
vmwTunnelNumDevicesBlockedByAdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumDevicesBlockedByAdm.setStatus("current")
_VmwTunnelNumDevicesSinceStart_Type = Counter64
_VmwTunnelNumDevicesSinceStart_Object = MibScalar
vmwTunnelNumDevicesSinceStart = _VmwTunnelNumDevicesSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 80),
    _VmwTunnelNumDevicesSinceStart_Type()
)
vmwTunnelNumDevicesSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumDevicesSinceStart.setStatus("current")
_VmwTunnelNumConnSuccessful_Type = Counter64
_VmwTunnelNumConnSuccessful_Object = MibScalar
vmwTunnelNumConnSuccessful = _VmwTunnelNumConnSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 90),
    _VmwTunnelNumConnSuccessful_Type()
)
vmwTunnelNumConnSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumConnSuccessful.setStatus("current")
_VmwTunnelNumConnFailed_Type = Counter64
_VmwTunnelNumConnFailed_Object = MibScalar
vmwTunnelNumConnFailed = _VmwTunnelNumConnFailed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 91),
    _VmwTunnelNumConnFailed_Type()
)
vmwTunnelNumConnFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumConnFailed.setStatus("current")
_VmwTunnelNumConnBlockedByZTNA_Type = Counter64
_VmwTunnelNumConnBlockedByZTNA_Object = MibScalar
vmwTunnelNumConnBlockedByZTNA = _VmwTunnelNumConnBlockedByZTNA_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 92),
    _VmwTunnelNumConnBlockedByZTNA_Type()
)
vmwTunnelNumConnBlockedByZTNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumConnBlockedByZTNA.setStatus("current")


class _VmwTunnelNumBackEnds_Type(Unsigned32):
    """Custom type vmwTunnelNumBackEnds based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumBackEnds_Type.__name__ = "Unsigned32"
_VmwTunnelNumBackEnds_Object = MibScalar
vmwTunnelNumBackEnds = _VmwTunnelNumBackEnds_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 100),
    _VmwTunnelNumBackEnds_Type()
)
vmwTunnelNumBackEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumBackEnds.setStatus("current")


class _VmwTunnelNumBackEndsDown_Type(Unsigned32):
    """Custom type vmwTunnelNumBackEndsDown based on Unsigned32"""
    defaultValue = 0


_VmwTunnelNumBackEndsDown_Type.__name__ = "Unsigned32"
_VmwTunnelNumBackEndsDown_Object = MibScalar
vmwTunnelNumBackEndsDown = _VmwTunnelNumBackEndsDown_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 101),
    _VmwTunnelNumBackEndsDown_Type()
)
vmwTunnelNumBackEndsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumBackEndsDown.setStatus("current")


class _VmwTunnelMemoryVirtual_Type(Counter64):
    """Custom type vmwTunnelMemoryVirtual based on Counter64"""
    defaultValue = 0


_VmwTunnelMemoryVirtual_Type.__name__ = "Counter64"
_VmwTunnelMemoryVirtual_Object = MibScalar
vmwTunnelMemoryVirtual = _VmwTunnelMemoryVirtual_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 110),
    _VmwTunnelMemoryVirtual_Type()
)
vmwTunnelMemoryVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelMemoryVirtual.setStatus("current")


class _VmwTunnelMemoryResident_Type(Counter64):
    """Custom type vmwTunnelMemoryResident based on Counter64"""
    defaultValue = 0


_VmwTunnelMemoryResident_Type.__name__ = "Counter64"
_VmwTunnelMemoryResident_Object = MibScalar
vmwTunnelMemoryResident = _VmwTunnelMemoryResident_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 111),
    _VmwTunnelMemoryResident_Type()
)
vmwTunnelMemoryResident.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelMemoryResident.setStatus("current")


class _VmwTunnelMemoryShared_Type(Counter64):
    """Custom type vmwTunnelMemoryShared based on Counter64"""
    defaultValue = 0


_VmwTunnelMemoryShared_Type.__name__ = "Counter64"
_VmwTunnelMemoryShared_Object = MibScalar
vmwTunnelMemoryShared = _VmwTunnelMemoryShared_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 1, 112),
    _VmwTunnelMemoryShared_Type()
)
vmwTunnelMemoryShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelMemoryShared.setStatus("current")
_VmwTunnelServerInfo_ObjectIdentity = ObjectIdentity
vmwTunnelServerInfo = _VmwTunnelServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2)
)
_VmwTunnelServerVersion_Type = VmwLongDisplayString
_VmwTunnelServerVersion_Object = MibScalar
vmwTunnelServerVersion = _VmwTunnelServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 1),
    _VmwTunnelServerVersion_Type()
)
vmwTunnelServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelServerVersion.setStatus("current")
_VmwTunnelConsoleVersion_Type = VmwLongDisplayString
_VmwTunnelConsoleVersion_Object = MibScalar
vmwTunnelConsoleVersion = _VmwTunnelConsoleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 2),
    _VmwTunnelConsoleVersion_Type()
)
vmwTunnelConsoleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelConsoleVersion.setStatus("current")
_VmwTunnelOperatingSystem_Type = VmwLongDisplayString
_VmwTunnelOperatingSystem_Object = MibScalar
vmwTunnelOperatingSystem = _VmwTunnelOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 3),
    _VmwTunnelOperatingSystem_Type()
)
vmwTunnelOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelOperatingSystem.setStatus("current")
_VmwTunnelAPIConnectivity_Type = VmwTunnelUpDownState
_VmwTunnelAPIConnectivity_Object = MibScalar
vmwTunnelAPIConnectivity = _VmwTunnelAPIConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 10),
    _VmwTunnelAPIConnectivity_Type()
)
vmwTunnelAPIConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelAPIConnectivity.setStatus("current")
_VmwTunnelAWCMConnectivity_Type = VmwTunnelUpDownState
_VmwTunnelAWCMConnectivity_Object = MibScalar
vmwTunnelAWCMConnectivity = _VmwTunnelAWCMConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 11),
    _VmwTunnelAWCMConnectivity_Type()
)
vmwTunnelAWCMConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelAWCMConnectivity.setStatus("current")
_VmwTunnelAPILastResponse_Type = VmwLongDisplayString
_VmwTunnelAPILastResponse_Object = MibScalar
vmwTunnelAPILastResponse = _VmwTunnelAPILastResponse_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 12),
    _VmwTunnelAPILastResponse_Type()
)
vmwTunnelAPILastResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelAPILastResponse.setStatus("current")
_VmwTunnelAWCMLastResponse_Type = VmwLongDisplayString
_VmwTunnelAWCMLastResponse_Object = MibScalar
vmwTunnelAWCMLastResponse = _VmwTunnelAWCMLastResponse_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 13),
    _VmwTunnelAWCMLastResponse_Type()
)
vmwTunnelAWCMLastResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelAWCMLastResponse.setStatus("current")
_VmwTunnelAPILastSyncTime_Type = DateAndTime
_VmwTunnelAPILastSyncTime_Object = MibScalar
vmwTunnelAPILastSyncTime = _VmwTunnelAPILastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 14),
    _VmwTunnelAPILastSyncTime_Type()
)
vmwTunnelAPILastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelAPILastSyncTime.setStatus("current")
_VmwTunnelAWCMLastSyncTime_Type = DateAndTime
_VmwTunnelAWCMLastSyncTime_Object = MibScalar
vmwTunnelAWCMLastSyncTime = _VmwTunnelAWCMLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 15),
    _VmwTunnelAWCMLastSyncTime_Type()
)
vmwTunnelAWCMLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelAWCMLastSyncTime.setStatus("current")
_VmwTunnelProcessStartTime_Type = DateAndTime
_VmwTunnelProcessStartTime_Object = MibScalar
vmwTunnelProcessStartTime = _VmwTunnelProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 20),
    _VmwTunnelProcessStartTime_Type()
)
vmwTunnelProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelProcessStartTime.setStatus("current")
_VmwTunnelProcessUpTime_Type = Counter64
_VmwTunnelProcessUpTime_Object = MibScalar
vmwTunnelProcessUpTime = _VmwTunnelProcessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 21),
    _VmwTunnelProcessUpTime_Type()
)
vmwTunnelProcessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelProcessUpTime.setStatus("current")
_VmwTunnelCascadeMode_Type = VmwTunnelCascadeModeState
_VmwTunnelCascadeMode_Object = MibScalar
vmwTunnelCascadeMode = _VmwTunnelCascadeMode_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 30),
    _VmwTunnelCascadeMode_Type()
)
vmwTunnelCascadeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelCascadeMode.setStatus("current")
_VmwTunnelDeploymentMode_Type = VmwLongDisplayString
_VmwTunnelDeploymentMode_Object = MibScalar
vmwTunnelDeploymentMode = _VmwTunnelDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 40),
    _VmwTunnelDeploymentMode_Type()
)
vmwTunnelDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelDeploymentMode.setStatus("current")
_VmwTunnelTrafficRulesEnabled_Type = TruthValue
_VmwTunnelTrafficRulesEnabled_Object = MibScalar
vmwTunnelTrafficRulesEnabled = _VmwTunnelTrafficRulesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 50),
    _VmwTunnelTrafficRulesEnabled_Type()
)
vmwTunnelTrafficRulesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelTrafficRulesEnabled.setStatus("current")
_VmwTunnelFIPSEnabled_Type = TruthValue
_VmwTunnelFIPSEnabled_Object = MibScalar
vmwTunnelFIPSEnabled = _VmwTunnelFIPSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 60),
    _VmwTunnelFIPSEnabled_Type()
)
vmwTunnelFIPSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelFIPSEnabled.setStatus("current")
_VmwTunnelNSXEnabled_Type = TruthValue
_VmwTunnelNSXEnabled_Object = MibScalar
vmwTunnelNSXEnabled = _VmwTunnelNSXEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 70),
    _VmwTunnelNSXEnabled_Type()
)
vmwTunnelNSXEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNSXEnabled.setStatus("current")
_VmwTunnelLogLevel_Type = VmwTunnelLogState
_VmwTunnelLogLevel_Object = MibScalar
vmwTunnelLogLevel = _VmwTunnelLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 80),
    _VmwTunnelLogLevel_Type()
)
vmwTunnelLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelLogLevel.setStatus("current")
_VmwTunnelServerStatus_Type = VmwTunnelUpDownState
_VmwTunnelServerStatus_Object = MibScalar
vmwTunnelServerStatus = _VmwTunnelServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 90),
    _VmwTunnelServerStatus_Type()
)
vmwTunnelServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelServerStatus.setStatus("current")
_VmwTunnelTLSPortSharing_Type = TruthValue
_VmwTunnelTLSPortSharing_Object = MibScalar
vmwTunnelTLSPortSharing = _VmwTunnelTLSPortSharing_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 100),
    _VmwTunnelTLSPortSharing_Type()
)
vmwTunnelTLSPortSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelTLSPortSharing.setStatus("current")
_VmwTunnelZTNADTR_Type = TruthValue
_VmwTunnelZTNADTR_Object = MibScalar
vmwTunnelZTNADTR = _VmwTunnelZTNADTR_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 110),
    _VmwTunnelZTNADTR_Type()
)
vmwTunnelZTNADTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelZTNADTR.setStatus("current")
_VmwTunnelZTNAPDTR_Type = TruthValue
_VmwTunnelZTNAPDTR_Object = MibScalar
vmwTunnelZTNAPDTR = _VmwTunnelZTNAPDTR_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 111),
    _VmwTunnelZTNAPDTR_Type()
)
vmwTunnelZTNAPDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelZTNAPDTR.setStatus("current")
_VmwTunnelNumZTNADTR_Type = Unsigned32
_VmwTunnelNumZTNADTR_Object = MibScalar
vmwTunnelNumZTNADTR = _VmwTunnelNumZTNADTR_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 112),
    _VmwTunnelNumZTNADTR_Type()
)
vmwTunnelNumZTNADTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumZTNADTR.setStatus("current")
_VmwTunnelNumZTNAPDTR_Type = Unsigned32
_VmwTunnelNumZTNAPDTR_Object = MibScalar
vmwTunnelNumZTNAPDTR = _VmwTunnelNumZTNAPDTR_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 113),
    _VmwTunnelNumZTNAPDTR_Type()
)
vmwTunnelNumZTNAPDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelNumZTNAPDTR.setStatus("current")
_VmwTunnelIsAppliance_Type = TruthValue
_VmwTunnelIsAppliance_Object = MibScalar
vmwTunnelIsAppliance = _VmwTunnelIsAppliance_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 120),
    _VmwTunnelIsAppliance_Type()
)
vmwTunnelIsAppliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelIsAppliance.setStatus("current")
_VmwTunnelIsContainer_Type = TruthValue
_VmwTunnelIsContainer_Object = MibScalar
vmwTunnelIsContainer = _VmwTunnelIsContainer_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 130),
    _VmwTunnelIsContainer_Type()
)
vmwTunnelIsContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelIsContainer.setStatus("current")
_VmwTunnelGeneveMetadata_Type = TruthValue
_VmwTunnelGeneveMetadata_Object = MibScalar
vmwTunnelGeneveMetadata = _VmwTunnelGeneveMetadata_Object(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 2, 140),
    _VmwTunnelGeneveMetadata_Type()
)
vmwTunnelGeneveMetadata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwTunnelGeneveMetadata.setStatus("current")
_VmwTunnelServerMIBConformance_ObjectIdentity = ObjectIdentity
vmwTunnelServerMIBConformance = _VmwTunnelServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3)
)
_VmwTunnelServerMIBCompliances_ObjectIdentity = ObjectIdentity
vmwTunnelServerMIBCompliances = _VmwTunnelServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 1)
)
_VmwTunnelServerMIBGroups_ObjectIdentity = ObjectIdentity
vmwTunnelServerMIBGroups = _VmwTunnelServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2)
)

# Managed Objects groups

vmwTunnelServerStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 1)
)
vmwTunnelServerStatGroup.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumDevices"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumDevicesPeak"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumConnections"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumConnectionsPeak"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelDownstreamBitRate"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelUpstreamBitRate"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumProxies"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumProxiesDown"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumTrafficRules"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumAllowListedDevices"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumClosedHandshakes"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumFailedHandshakes"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumDevicesSinceStart"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerStatGroup.setStatus("current")

vmwTunnelServerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 2)
)
vmwTunnelServerInfoGroup.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerVersion"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelConsoleVersion"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelOperatingSystem"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelAPIConnectivity"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelAWCMConnectivity"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelAPILastResponse"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelAWCMLastResponse"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelAPILastSyncTime"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelAWCMLastSyncTime"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelProcessStartTime"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelCascadeMode"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelDeploymentMode"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelTrafficRulesEnabled"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelFIPSEnabled"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNSXEnabled"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerInfoGroup.setStatus("current")

vmwTunnelServerStatGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 3)
)
vmwTunnelServerStatGroup2.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumNotInAllowlist"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumNonCompliant"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumNonManaged"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerStatGroup2.setStatus("current")

vmwTunnelServerInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 4)
)
vmwTunnelServerInfoGroup2.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelLogLevel"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelProcessUpTime"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerStatus"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerInfoGroup2.setStatus("current")

vmwTunnelServerStatGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 5)
)
vmwTunnelServerStatGroup3.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumDDoSRejected"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumConnSuccessful"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumConnFailed"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumBackEnds"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumBackEndsDown"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelMemoryVirtual"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelMemoryResident"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelMemoryShared"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerStatGroup3.setStatus("current")

vmwTunnelServerInfoGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 6)
)
vmwTunnelServerInfoGroup3.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelTLSPortSharing"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelZTNADTR"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelZTNAPDTR"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumZTNADTR"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumZTNAPDTR"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelIsAppliance"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelIsContainer"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelGeneveMetadata"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerInfoGroup3.setStatus("current")

vmwTunnelServerStatGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 2, 7)
)
vmwTunnelServerStatGroup4.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumDevicesBlockedByZTNA"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumDevicesBlockedByAdm"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelNumConnBlockedByZTNA"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerStatGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vmwTunnelServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 130, 1, 3, 1, 1)
)
vmwTunnelServerMIBCompliance.setObjects(
      *(("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerInfoGroup"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerInfoGroup2"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerInfoGroup3"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerStatGroup"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerStatGroup2"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerStatGroup3"),
        ("VMWARE-TUNNEL-SERVER-MIB", "vmwTunnelServerStatGroup4"))
)
if mibBuilder.loadTexts:
    vmwTunnelServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-TUNNEL-SERVER-MIB",
    **{"VmwTunnelUpDownState": VmwTunnelUpDownState,
       "VmwTunnelCascadeModeState": VmwTunnelCascadeModeState,
       "VmwTunnelLogState": VmwTunnelLogState,
       "vmwTunnelServerMIB": vmwTunnelServerMIB,
       "vmwTunnelServerStat": vmwTunnelServerStat,
       "vmwTunnelNumDevices": vmwTunnelNumDevices,
       "vmwTunnelNumDevicesPeak": vmwTunnelNumDevicesPeak,
       "vmwTunnelNumConnections": vmwTunnelNumConnections,
       "vmwTunnelNumConnectionsPeak": vmwTunnelNumConnectionsPeak,
       "vmwTunnelDownstreamBitRate": vmwTunnelDownstreamBitRate,
       "vmwTunnelUpstreamBitRate": vmwTunnelUpstreamBitRate,
       "vmwTunnelNumProxies": vmwTunnelNumProxies,
       "vmwTunnelNumProxiesDown": vmwTunnelNumProxiesDown,
       "vmwTunnelNumTrafficRules": vmwTunnelNumTrafficRules,
       "vmwTunnelNumAllowListedDevices": vmwTunnelNumAllowListedDevices,
       "vmwTunnelNumClosedHandshakes": vmwTunnelNumClosedHandshakes,
       "vmwTunnelNumFailedHandshakes": vmwTunnelNumFailedHandshakes,
       "vmwTunnelNumNotInAllowlist": vmwTunnelNumNotInAllowlist,
       "vmwTunnelNumNonCompliant": vmwTunnelNumNonCompliant,
       "vmwTunnelNumNonManaged": vmwTunnelNumNonManaged,
       "vmwTunnelNumDDoSRejected": vmwTunnelNumDDoSRejected,
       "vmwTunnelNumDevicesBlockedByZTNA": vmwTunnelNumDevicesBlockedByZTNA,
       "vmwTunnelNumDevicesBlockedByAdm": vmwTunnelNumDevicesBlockedByAdm,
       "vmwTunnelNumDevicesSinceStart": vmwTunnelNumDevicesSinceStart,
       "vmwTunnelNumConnSuccessful": vmwTunnelNumConnSuccessful,
       "vmwTunnelNumConnFailed": vmwTunnelNumConnFailed,
       "vmwTunnelNumConnBlockedByZTNA": vmwTunnelNumConnBlockedByZTNA,
       "vmwTunnelNumBackEnds": vmwTunnelNumBackEnds,
       "vmwTunnelNumBackEndsDown": vmwTunnelNumBackEndsDown,
       "vmwTunnelMemoryVirtual": vmwTunnelMemoryVirtual,
       "vmwTunnelMemoryResident": vmwTunnelMemoryResident,
       "vmwTunnelMemoryShared": vmwTunnelMemoryShared,
       "vmwTunnelServerInfo": vmwTunnelServerInfo,
       "vmwTunnelServerVersion": vmwTunnelServerVersion,
       "vmwTunnelConsoleVersion": vmwTunnelConsoleVersion,
       "vmwTunnelOperatingSystem": vmwTunnelOperatingSystem,
       "vmwTunnelAPIConnectivity": vmwTunnelAPIConnectivity,
       "vmwTunnelAWCMConnectivity": vmwTunnelAWCMConnectivity,
       "vmwTunnelAPILastResponse": vmwTunnelAPILastResponse,
       "vmwTunnelAWCMLastResponse": vmwTunnelAWCMLastResponse,
       "vmwTunnelAPILastSyncTime": vmwTunnelAPILastSyncTime,
       "vmwTunnelAWCMLastSyncTime": vmwTunnelAWCMLastSyncTime,
       "vmwTunnelProcessStartTime": vmwTunnelProcessStartTime,
       "vmwTunnelProcessUpTime": vmwTunnelProcessUpTime,
       "vmwTunnelCascadeMode": vmwTunnelCascadeMode,
       "vmwTunnelDeploymentMode": vmwTunnelDeploymentMode,
       "vmwTunnelTrafficRulesEnabled": vmwTunnelTrafficRulesEnabled,
       "vmwTunnelFIPSEnabled": vmwTunnelFIPSEnabled,
       "vmwTunnelNSXEnabled": vmwTunnelNSXEnabled,
       "vmwTunnelLogLevel": vmwTunnelLogLevel,
       "vmwTunnelServerStatus": vmwTunnelServerStatus,
       "vmwTunnelTLSPortSharing": vmwTunnelTLSPortSharing,
       "vmwTunnelZTNADTR": vmwTunnelZTNADTR,
       "vmwTunnelZTNAPDTR": vmwTunnelZTNAPDTR,
       "vmwTunnelNumZTNADTR": vmwTunnelNumZTNADTR,
       "vmwTunnelNumZTNAPDTR": vmwTunnelNumZTNAPDTR,
       "vmwTunnelIsAppliance": vmwTunnelIsAppliance,
       "vmwTunnelIsContainer": vmwTunnelIsContainer,
       "vmwTunnelGeneveMetadata": vmwTunnelGeneveMetadata,
       "vmwTunnelServerMIBConformance": vmwTunnelServerMIBConformance,
       "vmwTunnelServerMIBCompliances": vmwTunnelServerMIBCompliances,
       "vmwTunnelServerMIBCompliance": vmwTunnelServerMIBCompliance,
       "vmwTunnelServerMIBGroups": vmwTunnelServerMIBGroups,
       "vmwTunnelServerStatGroup": vmwTunnelServerStatGroup,
       "vmwTunnelServerInfoGroup": vmwTunnelServerInfoGroup,
       "vmwTunnelServerStatGroup2": vmwTunnelServerStatGroup2,
       "vmwTunnelServerInfoGroup2": vmwTunnelServerInfoGroup2,
       "vmwTunnelServerStatGroup3": vmwTunnelServerStatGroup3,
       "vmwTunnelServerInfoGroup3": vmwTunnelServerInfoGroup3,
       "vmwTunnelServerStatGroup4": vmwTunnelServerStatGroup4}
)
