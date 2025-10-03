# SNMP MIB module (MERU-CONFIG-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-SECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:09 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAclEnvState,
 MwlAuthenticationType,
 MwlCaptivePortalAuthMethod,
 MwlCaptivePortalAuthenticationType,
 MwlCaptivePortalExternalServerType,
 MwlCaptivePortalMode,
 MwlCypherSuiteBits,
 MwlFirewallCapability,
 MwlKDDI,
 MwlL2SecurityModeBits,
 MwlManagementFrameProtection,
 MwlOnOffSwitch,
 MwlProfileOwner,
 MwlRadiusCalledStationIdType,
 MwlRadiusMacDelimiter,
 MwlRadiusPasswordType,
 MwlTunnelTerminationModeBits) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAclEnvState",
    "MwlAuthenticationType",
    "MwlCaptivePortalAuthMethod",
    "MwlCaptivePortalAuthenticationType",
    "MwlCaptivePortalExternalServerType",
    "MwlCaptivePortalMode",
    "MwlCypherSuiteBits",
    "MwlFirewallCapability",
    "MwlKDDI",
    "MwlL2SecurityModeBits",
    "MwlManagementFrameProtection",
    "MwlOnOffSwitch",
    "MwlProfileOwner",
    "MwlRadiusCalledStationIdType",
    "MwlRadiusMacDelimiter",
    "MwlRadiusPasswordType",
    "MwlTunnelTerminationModeBits")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwSecurityProfileTable_Object = MibTable
mwSecurityProfileTable = _MwSecurityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1)
)
if mibBuilder.loadTexts:
    mwSecurityProfileTable.setStatus("current")
_MwSecurityProfileEntry_Object = MibTableRow
mwSecurityProfileEntry = _MwSecurityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1)
)
mwSecurityProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwSecurityProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwSecurityProfileEntry.setStatus("current")
_MwSecurityProfileTableIndex_Type = Integer32
_MwSecurityProfileTableIndex_Object = MibTableColumn
mwSecurityProfileTableIndex = _MwSecurityProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 1),
    _MwSecurityProfileTableIndex_Type()
)
mwSecurityProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwSecurityProfileTableIndex.setStatus("current")


class _MwSecurityProfileName_Type(DisplayString):
    """Custom type mwSecurityProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwSecurityProfileName_Type.__name__ = "DisplayString"
_MwSecurityProfileName_Object = MibTableColumn
mwSecurityProfileName = _MwSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 2),
    _MwSecurityProfileName_Type()
)
mwSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileName.setStatus("current")
_MwSecurityProfileKDDI_Type = MwlKDDI
_MwSecurityProfileKDDI_Object = MibTableColumn
mwSecurityProfileKDDI = _MwSecurityProfileKDDI_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 3),
    _MwSecurityProfileKDDI_Type()
)
mwSecurityProfileKDDI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileKDDI.setStatus("current")
_MwSecurityProfileReKeyPeriod_Type = Unsigned32
_MwSecurityProfileReKeyPeriod_Object = MibTableColumn
mwSecurityProfileReKeyPeriod = _MwSecurityProfileReKeyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 5),
    _MwSecurityProfileReKeyPeriod_Type()
)
mwSecurityProfileReKeyPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileReKeyPeriod.setStatus("current")
_MwSecurityProfileCypherSuites_Type = MwlCypherSuiteBits
_MwSecurityProfileCypherSuites_Object = MibTableColumn
mwSecurityProfileCypherSuites = _MwSecurityProfileCypherSuites_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 6),
    _MwSecurityProfileCypherSuites_Type()
)
mwSecurityProfileCypherSuites.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileCypherSuites.setStatus("current")
_MwSecurityProfileReAuthEnable_Type = MwlOnOffSwitch
_MwSecurityProfileReAuthEnable_Object = MibTableColumn
mwSecurityProfileReAuthEnable = _MwSecurityProfileReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 7),
    _MwSecurityProfileReAuthEnable_Type()
)
mwSecurityProfileReAuthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileReAuthEnable.setStatus("current")
_MwSecurityProfileL2ModesAllowed_Type = MwlL2SecurityModeBits
_MwSecurityProfileL2ModesAllowed_Object = MibTableColumn
mwSecurityProfileL2ModesAllowed = _MwSecurityProfileL2ModesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 8),
    _MwSecurityProfileL2ModesAllowed_Type()
)
mwSecurityProfileL2ModesAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileL2ModesAllowed.setStatus("current")


class _MwSecurityProfileStaticWepKeyPos_Type(Integer32):
    """Custom type mwSecurityProfileStaticWepKeyPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MwSecurityProfileStaticWepKeyPos_Type.__name__ = "Integer32"
_MwSecurityProfileStaticWepKeyPos_Object = MibTableColumn
mwSecurityProfileStaticWepKeyPos = _MwSecurityProfileStaticWepKeyPos_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 10),
    _MwSecurityProfileStaticWepKeyPos_Type()
)
mwSecurityProfileStaticWepKeyPos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileStaticWepKeyPos.setStatus("current")
_MwSecurityProfileSecurityLogging_Type = MwlOnOffSwitch
_MwSecurityProfileSecurityLogging_Object = MibTableColumn
mwSecurityProfileSecurityLogging = _MwSecurityProfileSecurityLogging_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 11),
    _MwSecurityProfileSecurityLogging_Type()
)
mwSecurityProfileSecurityLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileSecurityLogging.setStatus("current")
_MwSecurityProfileGroupKeyInterval_Type = Unsigned32
_MwSecurityProfileGroupKeyInterval_Object = MibTableColumn
mwSecurityProfileGroupKeyInterval = _MwSecurityProfileGroupKeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 12),
    _MwSecurityProfileGroupKeyInterval_Type()
)
mwSecurityProfileGroupKeyInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileGroupKeyInterval.setStatus("current")


class _MwSecurityProfileFirewallFilterId_Type(DisplayString):
    """Custom type mwSecurityProfileFirewallFilterId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MwSecurityProfileFirewallFilterId_Type.__name__ = "DisplayString"
_MwSecurityProfileFirewallFilterId_Object = MibTableColumn
mwSecurityProfileFirewallFilterId = _MwSecurityProfileFirewallFilterId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 13),
    _MwSecurityProfileFirewallFilterId_Type()
)
mwSecurityProfileFirewallFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileFirewallFilterId.setStatus("current")
_MwSecurityProfileSharedAuthEnabled_Type = MwlOnOffSwitch
_MwSecurityProfileSharedAuthEnabled_Object = MibTableColumn
mwSecurityProfileSharedAuthEnabled = _MwSecurityProfileSharedAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 14),
    _MwSecurityProfileSharedAuthEnabled_Type()
)
mwSecurityProfileSharedAuthEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileSharedAuthEnabled.setStatus("current")
_MwSecurityProfileEnableMacFiltering_Type = MwlOnOffSwitch
_MwSecurityProfileEnableMacFiltering_Object = MibTableColumn
mwSecurityProfileEnableMacFiltering = _MwSecurityProfileEnableMacFiltering_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 15),
    _MwSecurityProfileEnableMacFiltering_Type()
)
mwSecurityProfileEnableMacFiltering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileEnableMacFiltering.setStatus("current")
_MwSecurityProfileFirewallCapability_Type = MwlFirewallCapability
_MwSecurityProfileFirewallCapability_Object = MibTableColumn
mwSecurityProfileFirewallCapability = _MwSecurityProfileFirewallCapability_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 16),
    _MwSecurityProfileFirewallCapability_Type()
)
mwSecurityProfileFirewallCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileFirewallCapability.setStatus("current")
_MwSecurityProfileCaptivePortalEnabled_Type = MwlCaptivePortalMode
_MwSecurityProfileCaptivePortalEnabled_Object = MibTableColumn
mwSecurityProfileCaptivePortalEnabled = _MwSecurityProfileCaptivePortalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 17),
    _MwSecurityProfileCaptivePortalEnabled_Type()
)
mwSecurityProfileCaptivePortalEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileCaptivePortalEnabled.setStatus("current")
_MwSecurityProfileNetworkInitiation8021x_Type = MwlOnOffSwitch
_MwSecurityProfileNetworkInitiation8021x_Object = MibTableColumn
mwSecurityProfileNetworkInitiation8021x = _MwSecurityProfileNetworkInitiation8021x_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 18),
    _MwSecurityProfileNetworkInitiation8021x_Type()
)
mwSecurityProfileNetworkInitiation8021x.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileNetworkInitiation8021x.setStatus("current")


class _MwSecurityProfilePrimaryRadiusProfileName_Type(DisplayString):
    """Custom type mwSecurityProfilePrimaryRadiusProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MwSecurityProfilePrimaryRadiusProfileName_Type.__name__ = "DisplayString"
_MwSecurityProfilePrimaryRadiusProfileName_Object = MibTableColumn
mwSecurityProfilePrimaryRadiusProfileName = _MwSecurityProfilePrimaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 19),
    _MwSecurityProfilePrimaryRadiusProfileName_Type()
)
mwSecurityProfilePrimaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfilePrimaryRadiusProfileName.setStatus("current")


class _MwSecurityProfileSecondaryRadiusProfileName_Type(DisplayString):
    """Custom type mwSecurityProfileSecondaryRadiusProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MwSecurityProfileSecondaryRadiusProfileName_Type.__name__ = "DisplayString"
_MwSecurityProfileSecondaryRadiusProfileName_Object = MibTableColumn
mwSecurityProfileSecondaryRadiusProfileName = _MwSecurityProfileSecondaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 20),
    _MwSecurityProfileSecondaryRadiusProfileName_Type()
)
mwSecurityProfileSecondaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileSecondaryRadiusProfileName.setStatus("current")


class _MwSecurityProfilePskKey_Type(DisplayString):
    """Custom type mwSecurityProfilePskKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_MwSecurityProfilePskKey_Type.__name__ = "DisplayString"
_MwSecurityProfilePskKey_Object = MibTableColumn
mwSecurityProfilePskKey = _MwSecurityProfilePskKey_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 21),
    _MwSecurityProfilePskKey_Type()
)
mwSecurityProfilePskKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfilePskKey.setStatus("current")


class _MwSecurityProfileStaticWepKey_Type(DisplayString):
    """Custom type mwSecurityProfileStaticWepKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_MwSecurityProfileStaticWepKey_Type.__name__ = "DisplayString"
_MwSecurityProfileStaticWepKey_Object = MibTableColumn
mwSecurityProfileStaticWepKey = _MwSecurityProfileStaticWepKey_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 22),
    _MwSecurityProfileStaticWepKey_Type()
)
mwSecurityProfileStaticWepKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileStaticWepKey.setStatus("current")


class _MwSecurityProfilePassthroughFirewallFilterId_Type(DisplayString):
    """Custom type mwSecurityProfilePassthroughFirewallFilterId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MwSecurityProfilePassthroughFirewallFilterId_Type.__name__ = "DisplayString"
_MwSecurityProfilePassthroughFirewallFilterId_Object = MibTableColumn
mwSecurityProfilePassthroughFirewallFilterId = _MwSecurityProfilePassthroughFirewallFilterId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 23),
    _MwSecurityProfilePassthroughFirewallFilterId_Type()
)
mwSecurityProfilePassthroughFirewallFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfilePassthroughFirewallFilterId.setStatus("current")
_MwSecurityProfileOwner_Type = MwlProfileOwner
_MwSecurityProfileOwner_Object = MibTableColumn
mwSecurityProfileOwner = _MwSecurityProfileOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 25),
    _MwSecurityProfileOwner_Type()
)
mwSecurityProfileOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSecurityProfileOwner.setStatus("current")
_MwSecurityProfileCaptivePortalAuthenticationMethod_Type = MwlCaptivePortalAuthMethod
_MwSecurityProfileCaptivePortalAuthenticationMethod_Object = MibTableColumn
mwSecurityProfileCaptivePortalAuthenticationMethod = _MwSecurityProfileCaptivePortalAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 27),
    _MwSecurityProfileCaptivePortalAuthenticationMethod_Type()
)
mwSecurityProfileCaptivePortalAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileCaptivePortalAuthenticationMethod.setStatus("current")
_MwSecurityProfileTunnelTermination_Type = MwlTunnelTerminationModeBits
_MwSecurityProfileTunnelTermination_Object = MibTableColumn
mwSecurityProfileTunnelTermination = _MwSecurityProfileTunnelTermination_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 31),
    _MwSecurityProfileTunnelTermination_Type()
)
mwSecurityProfileTunnelTermination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileTunnelTermination.setStatus("current")
_MwSecurityProfileBKSACachingPeriod_Type = Unsigned32
_MwSecurityProfileBKSACachingPeriod_Object = MibTableColumn
mwSecurityProfileBKSACachingPeriod = _MwSecurityProfileBKSACachingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 32),
    _MwSecurityProfileBKSACachingPeriod_Type()
)
mwSecurityProfileBKSACachingPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileBKSACachingPeriod.setStatus("current")
_MwSecurityProfilePMKCachingStatus_Type = MwlOnOffSwitch
_MwSecurityProfilePMKCachingStatus_Object = MibTableColumn
mwSecurityProfilePMKCachingStatus = _MwSecurityProfilePMKCachingStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 33),
    _MwSecurityProfilePMKCachingStatus_Type()
)
mwSecurityProfilePMKCachingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfilePMKCachingStatus.setStatus("current")
_MwSecurityProfileEnvState_Type = MwlAclEnvState
_MwSecurityProfileEnvState_Object = MibTableColumn
mwSecurityProfileEnvState = _MwSecurityProfileEnvState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 47),
    _MwSecurityProfileEnvState_Type()
)
mwSecurityProfileEnvState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileEnvState.setStatus("current")
_MwSecurityProfileMACAuthPrimaryRadiusProfileName_Type = DisplayString
_MwSecurityProfileMACAuthPrimaryRadiusProfileName_Object = MibTableColumn
mwSecurityProfileMACAuthPrimaryRadiusProfileName = _MwSecurityProfileMACAuthPrimaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 48),
    _MwSecurityProfileMACAuthPrimaryRadiusProfileName_Type()
)
mwSecurityProfileMACAuthPrimaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileMACAuthPrimaryRadiusProfileName.setStatus("current")
_MwSecurityProfileMACAuthSecondaryRadiusProfileName_Type = DisplayString
_MwSecurityProfileMACAuthSecondaryRadiusProfileName_Object = MibTableColumn
mwSecurityProfileMACAuthSecondaryRadiusProfileName = _MwSecurityProfileMACAuthSecondaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 49),
    _MwSecurityProfileMACAuthSecondaryRadiusProfileName_Type()
)
mwSecurityProfileMACAuthSecondaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileMACAuthSecondaryRadiusProfileName.setStatus("current")


class _MwSecurityProfileCaptivePortalProfile_Type(DisplayString):
    """Custom type mwSecurityProfileCaptivePortalProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwSecurityProfileCaptivePortalProfile_Type.__name__ = "DisplayString"
_MwSecurityProfileCaptivePortalProfile_Object = MibTableColumn
mwSecurityProfileCaptivePortalProfile = _MwSecurityProfileCaptivePortalProfile_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 50),
    _MwSecurityProfileCaptivePortalProfile_Type()
)
mwSecurityProfileCaptivePortalProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileCaptivePortalProfile.setStatus("current")
_MwSecurityProfileMFP11wSupport_Type = MwlManagementFrameProtection
_MwSecurityProfileMFP11wSupport_Object = MibTableColumn
mwSecurityProfileMFP11wSupport = _MwSecurityProfileMFP11wSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 51),
    _MwSecurityProfileMFP11wSupport_Type()
)
mwSecurityProfileMFP11wSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileMFP11wSupport.setStatus("current")
_MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Type = DisplayString
_MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Object = MibTableColumn
mwSecurityProfileMACAccountingPrimaryRadiusProfileName = _MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 52),
    _MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Type()
)
mwSecurityProfileMACAccountingPrimaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileMACAccountingPrimaryRadiusProfileName.setStatus("current")
_MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Type = DisplayString
_MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Object = MibTableColumn
mwSecurityProfileMACAccountingSecondaryRadiusProfileName = _MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 53),
    _MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Type()
)
mwSecurityProfileMACAccountingSecondaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileMACAccountingSecondaryRadiusProfileName.setStatus("current")
_MwSecurityProfileCaptivePortalBypassForMAC_Type = MwlOnOffSwitch
_MwSecurityProfileCaptivePortalBypassForMAC_Object = MibTableColumn
mwSecurityProfileCaptivePortalBypassForMAC = _MwSecurityProfileCaptivePortalBypassForMAC_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 54),
    _MwSecurityProfileCaptivePortalBypassForMAC_Type()
)
mwSecurityProfileCaptivePortalBypassForMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileCaptivePortalBypassForMAC.setStatus("current")
_MwSecurityProfileRowStatus_Type = RowStatus
_MwSecurityProfileRowStatus_Object = MibTableColumn
mwSecurityProfileRowStatus = _MwSecurityProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 1, 1, 61),
    _MwSecurityProfileRowStatus_Type()
)
mwSecurityProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwSecurityProfileRowStatus.setStatus("current")
_MwSslVarsTable_Object = MibTable
mwSslVarsTable = _MwSslVarsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 2)
)
if mibBuilder.loadTexts:
    mwSslVarsTable.setStatus("current")
_MwSslVarsEntry_Object = MibTableRow
mwSslVarsEntry = _MwSslVarsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 2, 1)
)
mwSslVarsEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwSslVarsTableIndex"),
)
if mibBuilder.loadTexts:
    mwSslVarsEntry.setStatus("current")
_MwSslVarsTableIndex_Type = Integer32
_MwSslVarsTableIndex_Object = MibTableColumn
mwSslVarsTableIndex = _MwSslVarsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 2, 1, 1),
    _MwSslVarsTableIndex_Type()
)
mwSslVarsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwSslVarsTableIndex.setStatus("current")
_MwSslVarsSslLifeTime_Type = Unsigned32
_MwSslVarsSslLifeTime_Object = MibTableColumn
mwSslVarsSslLifeTime = _MwSslVarsSslLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 2, 1, 12),
    _MwSslVarsSslLifeTime_Type()
)
mwSslVarsSslLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslVarsSslLifeTime.setStatus("current")


class _MwSslVarsCertificateFileName_Type(DisplayString):
    """Custom type mwSslVarsCertificateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MwSslVarsCertificateFileName_Type.__name__ = "DisplayString"
_MwSslVarsCertificateFileName_Object = MibTableColumn
mwSslVarsCertificateFileName = _MwSslVarsCertificateFileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 2, 1, 15),
    _MwSslVarsCertificateFileName_Type()
)
mwSslVarsCertificateFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslVarsCertificateFileName.setStatus("current")


class _MwSslVarsCPCertificate_Type(DisplayString):
    """Custom type mwSslVarsCPCertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MwSslVarsCPCertificate_Type.__name__ = "DisplayString"
_MwSslVarsCPCertificate_Object = MibTableColumn
mwSslVarsCPCertificate = _MwSslVarsCPCertificate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 2, 1, 26),
    _MwSslVarsCPCertificate_Type()
)
mwSslVarsCPCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslVarsCPCertificate.setStatus("current")
_MwRadiusProfileTable_Object = MibTable
mwRadiusProfileTable = _MwRadiusProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3)
)
if mibBuilder.loadTexts:
    mwRadiusProfileTable.setStatus("current")
_MwRadiusProfileEntry_Object = MibTableRow
mwRadiusProfileEntry = _MwRadiusProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1)
)
mwRadiusProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwRadiusProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwRadiusProfileEntry.setStatus("current")
_MwRadiusProfileTableIndex_Type = Integer32
_MwRadiusProfileTableIndex_Object = MibTableColumn
mwRadiusProfileTableIndex = _MwRadiusProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 1),
    _MwRadiusProfileTableIndex_Type()
)
mwRadiusProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwRadiusProfileTableIndex.setStatus("current")


class _MwRadiusProfileName_Type(DisplayString):
    """Custom type mwRadiusProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MwRadiusProfileName_Type.__name__ = "DisplayString"
_MwRadiusProfileName_Object = MibTableColumn
mwRadiusProfileName = _MwRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 2),
    _MwRadiusProfileName_Type()
)
mwRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileName.setStatus("current")


class _MwRadiusProfileDescr_Type(DisplayString):
    """Custom type mwRadiusProfileDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MwRadiusProfileDescr_Type.__name__ = "DisplayString"
_MwRadiusProfileDescr_Object = MibTableColumn
mwRadiusProfileDescr = _MwRadiusProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 3),
    _MwRadiusProfileDescr_Type()
)
mwRadiusProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileDescr.setStatus("current")
_MwRadiusProfileRadiusIp_Type = IpAddress
_MwRadiusProfileRadiusIp_Object = MibTableColumn
mwRadiusProfileRadiusIp = _MwRadiusProfileRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 4),
    _MwRadiusProfileRadiusIp_Type()
)
mwRadiusProfileRadiusIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusIp.setStatus("current")
_MwRadiusProfileRadiusPort_Type = Unsigned32
_MwRadiusProfileRadiusPort_Object = MibTableColumn
mwRadiusProfileRadiusPort = _MwRadiusProfileRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 5),
    _MwRadiusProfileRadiusPort_Type()
)
mwRadiusProfileRadiusPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusPort.setStatus("current")
_MwRadiusProfileRadiusMacDelimiter_Type = MwlRadiusMacDelimiter
_MwRadiusProfileRadiusMacDelimiter_Object = MibTableColumn
mwRadiusProfileRadiusMacDelimiter = _MwRadiusProfileRadiusMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 6),
    _MwRadiusProfileRadiusMacDelimiter_Type()
)
mwRadiusProfileRadiusMacDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusMacDelimiter.setStatus("current")
_MwRadiusProfileRadiusPasswordType_Type = MwlRadiusPasswordType
_MwRadiusProfileRadiusPasswordType_Object = MibTableColumn
mwRadiusProfileRadiusPasswordType = _MwRadiusProfileRadiusPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 7),
    _MwRadiusProfileRadiusPasswordType_Type()
)
mwRadiusProfileRadiusPasswordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusPasswordType.setStatus("current")


class _MwRadiusProfileRadiusSecret_Type(DisplayString):
    """Custom type mwRadiusProfileRadiusSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MwRadiusProfileRadiusSecret_Type.__name__ = "DisplayString"
_MwRadiusProfileRadiusSecret_Object = MibTableColumn
mwRadiusProfileRadiusSecret = _MwRadiusProfileRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 8),
    _MwRadiusProfileRadiusSecret_Type()
)
mwRadiusProfileRadiusSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusSecret.setStatus("current")
_MwRadiusProfileOwner_Type = MwlProfileOwner
_MwRadiusProfileOwner_Object = MibTableColumn
mwRadiusProfileOwner = _MwRadiusProfileOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 9),
    _MwRadiusProfileOwner_Type()
)
mwRadiusProfileOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRadiusProfileOwner.setStatus("current")
_MwRadiusProfileCalledStationIdType_Type = MwlRadiusCalledStationIdType
_MwRadiusProfileCalledStationIdType_Object = MibTableColumn
mwRadiusProfileCalledStationIdType = _MwRadiusProfileCalledStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 10),
    _MwRadiusProfileCalledStationIdType_Type()
)
mwRadiusProfileCalledStationIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileCalledStationIdType.setStatus("current")
_MwRadiusProfileCoaFlag_Type = MwlOnOffSwitch
_MwRadiusProfileCoaFlag_Object = MibTableColumn
mwRadiusProfileCoaFlag = _MwRadiusProfileCoaFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 11),
    _MwRadiusProfileCoaFlag_Type()
)
mwRadiusProfileCoaFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileCoaFlag.setStatus("current")
_MwRadiusProfileRadiusRelayApId_Type = Unsigned32
_MwRadiusProfileRadiusRelayApId_Object = MibTableColumn
mwRadiusProfileRadiusRelayApId = _MwRadiusProfileRadiusRelayApId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 12),
    _MwRadiusProfileRadiusRelayApId_Type()
)
mwRadiusProfileRadiusRelayApId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusRelayApId.setStatus("current")
_MwRadiusProfileRemoteRadiusServerFlag_Type = MwlOnOffSwitch
_MwRadiusProfileRemoteRadiusServerFlag_Object = MibTableColumn
mwRadiusProfileRemoteRadiusServerFlag = _MwRadiusProfileRemoteRadiusServerFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 13),
    _MwRadiusProfileRemoteRadiusServerFlag_Type()
)
mwRadiusProfileRemoteRadiusServerFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRemoteRadiusServerFlag.setStatus("current")


class _MwRadiusProfileRadiusServerTimeout_Type(Integer32):
    """Custom type mwRadiusProfileRadiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MwRadiusProfileRadiusServerTimeout_Type.__name__ = "Integer32"
_MwRadiusProfileRadiusServerTimeout_Object = MibTableColumn
mwRadiusProfileRadiusServerTimeout = _MwRadiusProfileRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 14),
    _MwRadiusProfileRadiusServerTimeout_Type()
)
mwRadiusProfileRadiusServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusServerTimeout.setStatus("current")


class _MwRadiusProfileRadiusServerRetries_Type(Integer32):
    """Custom type mwRadiusProfileRadiusServerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MwRadiusProfileRadiusServerRetries_Type.__name__ = "Integer32"
_MwRadiusProfileRadiusServerRetries_Object = MibTableColumn
mwRadiusProfileRadiusServerRetries = _MwRadiusProfileRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 15),
    _MwRadiusProfileRadiusServerRetries_Type()
)
mwRadiusProfileRadiusServerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRadiusServerRetries.setStatus("current")
_MwRadiusProfileRowStatus_Type = RowStatus
_MwRadiusProfileRowStatus_Object = MibTableColumn
mwRadiusProfileRowStatus = _MwRadiusProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 3, 1, 19),
    _MwRadiusProfileRowStatus_Type()
)
mwRadiusProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRadiusProfileRowStatus.setStatus("current")
_MwGuestUserTable_Object = MibTable
mwGuestUserTable = _MwGuestUserTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4)
)
if mibBuilder.loadTexts:
    mwGuestUserTable.setStatus("current")
_MwGuestUserEntry_Object = MibTableRow
mwGuestUserEntry = _MwGuestUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1)
)
mwGuestUserEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwGuestUserTableIndex"),
)
if mibBuilder.loadTexts:
    mwGuestUserEntry.setStatus("current")
_MwGuestUserTableIndex_Type = Integer32
_MwGuestUserTableIndex_Object = MibTableColumn
mwGuestUserTableIndex = _MwGuestUserTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1, 1),
    _MwGuestUserTableIndex_Type()
)
mwGuestUserTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwGuestUserTableIndex.setStatus("current")


class _MwGuestUserGuestName_Type(DisplayString):
    """Custom type mwGuestUserGuestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MwGuestUserGuestName_Type.__name__ = "DisplayString"
_MwGuestUserGuestName_Object = MibTableColumn
mwGuestUserGuestName = _MwGuestUserGuestName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1, 2),
    _MwGuestUserGuestName_Type()
)
mwGuestUserGuestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGuestUserGuestName.setStatus("current")
_MwGuestUserEndTimestamp_Type = DateAndTime
_MwGuestUserEndTimestamp_Object = MibTableColumn
mwGuestUserEndTimestamp = _MwGuestUserEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1, 3),
    _MwGuestUserEndTimestamp_Type()
)
mwGuestUserEndTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGuestUserEndTimestamp.setStatus("current")
_MwGuestUserStartTimestamp_Type = DateAndTime
_MwGuestUserStartTimestamp_Object = MibTableColumn
mwGuestUserStartTimestamp = _MwGuestUserStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1, 4),
    _MwGuestUserStartTimestamp_Type()
)
mwGuestUserStartTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGuestUserStartTimestamp.setStatus("current")


class _MwGuestUserGuestPasswd_Type(DisplayString):
    """Custom type mwGuestUserGuestPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MwGuestUserGuestPasswd_Type.__name__ = "DisplayString"
_MwGuestUserGuestPasswd_Object = MibTableColumn
mwGuestUserGuestPasswd = _MwGuestUserGuestPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1, 5),
    _MwGuestUserGuestPasswd_Type()
)
mwGuestUserGuestPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGuestUserGuestPasswd.setStatus("current")
_MwGuestUserRowStatus_Type = RowStatus
_MwGuestUserRowStatus_Object = MibTableColumn
mwGuestUserRowStatus = _MwGuestUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 4, 1, 6),
    _MwGuestUserRowStatus_Type()
)
mwGuestUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGuestUserRowStatus.setStatus("current")
_MwAuthModeTable_Object = MibTable
mwAuthModeTable = _MwAuthModeTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5)
)
if mibBuilder.loadTexts:
    mwAuthModeTable.setStatus("current")
_MwAuthModeEntry_Object = MibTableRow
mwAuthModeEntry = _MwAuthModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1)
)
mwAuthModeEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwAuthModeTableIndex"),
)
if mibBuilder.loadTexts:
    mwAuthModeEntry.setStatus("current")
_MwAuthModeTableIndex_Type = Integer32
_MwAuthModeTableIndex_Object = MibTableColumn
mwAuthModeTableIndex = _MwAuthModeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 1),
    _MwAuthModeTableIndex_Type()
)
mwAuthModeTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAuthModeTableIndex.setStatus("current")
_MwAuthModeAuthType_Type = MwlAuthenticationType
_MwAuthModeAuthType_Object = MibTableColumn
mwAuthModeAuthType = _MwAuthModeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 2),
    _MwAuthModeAuthType_Type()
)
mwAuthModeAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeAuthType.setStatus("current")
_MwAuthModePrimaryRadiusIp_Type = IpAddress
_MwAuthModePrimaryRadiusIp_Object = MibTableColumn
mwAuthModePrimaryRadiusIp = _MwAuthModePrimaryRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 5),
    _MwAuthModePrimaryRadiusIp_Type()
)
mwAuthModePrimaryRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModePrimaryRadiusIp.setStatus("current")
_MwAuthModePrimaryRadiusPort_Type = Unsigned32
_MwAuthModePrimaryRadiusPort_Object = MibTableColumn
mwAuthModePrimaryRadiusPort = _MwAuthModePrimaryRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 6),
    _MwAuthModePrimaryRadiusPort_Type()
)
mwAuthModePrimaryRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModePrimaryRadiusPort.setStatus("current")


class _MwAuthModePrimaryRadiusSecret_Type(DisplayString):
    """Custom type mwAuthModePrimaryRadiusSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwAuthModePrimaryRadiusSecret_Type.__name__ = "DisplayString"
_MwAuthModePrimaryRadiusSecret_Object = MibTableColumn
mwAuthModePrimaryRadiusSecret = _MwAuthModePrimaryRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 7),
    _MwAuthModePrimaryRadiusSecret_Type()
)
mwAuthModePrimaryRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModePrimaryRadiusSecret.setStatus("current")
_MwAuthModeSecondaryRadiusIp_Type = IpAddress
_MwAuthModeSecondaryRadiusIp_Object = MibTableColumn
mwAuthModeSecondaryRadiusIp = _MwAuthModeSecondaryRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 8),
    _MwAuthModeSecondaryRadiusIp_Type()
)
mwAuthModeSecondaryRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeSecondaryRadiusIp.setStatus("current")
_MwAuthModeSecondaryRadiusPort_Type = Unsigned32
_MwAuthModeSecondaryRadiusPort_Object = MibTableColumn
mwAuthModeSecondaryRadiusPort = _MwAuthModeSecondaryRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 9),
    _MwAuthModeSecondaryRadiusPort_Type()
)
mwAuthModeSecondaryRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeSecondaryRadiusPort.setStatus("current")


class _MwAuthModeSecondaryRadiusSecret_Type(DisplayString):
    """Custom type mwAuthModeSecondaryRadiusSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwAuthModeSecondaryRadiusSecret_Type.__name__ = "DisplayString"
_MwAuthModeSecondaryRadiusSecret_Object = MibTableColumn
mwAuthModeSecondaryRadiusSecret = _MwAuthModeSecondaryRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 10),
    _MwAuthModeSecondaryRadiusSecret_Type()
)
mwAuthModeSecondaryRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeSecondaryRadiusSecret.setStatus("current")
_MwAuthModePrimaryTacacsIp_Type = IpAddress
_MwAuthModePrimaryTacacsIp_Object = MibTableColumn
mwAuthModePrimaryTacacsIp = _MwAuthModePrimaryTacacsIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 11),
    _MwAuthModePrimaryTacacsIp_Type()
)
mwAuthModePrimaryTacacsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModePrimaryTacacsIp.setStatus("current")
_MwAuthModePrimaryTacacsPort_Type = Unsigned32
_MwAuthModePrimaryTacacsPort_Object = MibTableColumn
mwAuthModePrimaryTacacsPort = _MwAuthModePrimaryTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 12),
    _MwAuthModePrimaryTacacsPort_Type()
)
mwAuthModePrimaryTacacsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModePrimaryTacacsPort.setStatus("current")


class _MwAuthModePrimaryTacacsSecret_Type(DisplayString):
    """Custom type mwAuthModePrimaryTacacsSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwAuthModePrimaryTacacsSecret_Type.__name__ = "DisplayString"
_MwAuthModePrimaryTacacsSecret_Object = MibTableColumn
mwAuthModePrimaryTacacsSecret = _MwAuthModePrimaryTacacsSecret_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 13),
    _MwAuthModePrimaryTacacsSecret_Type()
)
mwAuthModePrimaryTacacsSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModePrimaryTacacsSecret.setStatus("current")
_MwAuthModeSecondaryTacacsIp_Type = IpAddress
_MwAuthModeSecondaryTacacsIp_Object = MibTableColumn
mwAuthModeSecondaryTacacsIp = _MwAuthModeSecondaryTacacsIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 14),
    _MwAuthModeSecondaryTacacsIp_Type()
)
mwAuthModeSecondaryTacacsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeSecondaryTacacsIp.setStatus("current")
_MwAuthModeSecondaryTacacsPort_Type = Unsigned32
_MwAuthModeSecondaryTacacsPort_Object = MibTableColumn
mwAuthModeSecondaryTacacsPort = _MwAuthModeSecondaryTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 15),
    _MwAuthModeSecondaryTacacsPort_Type()
)
mwAuthModeSecondaryTacacsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeSecondaryTacacsPort.setStatus("current")


class _MwAuthModeSecondaryTacacsSecret_Type(DisplayString):
    """Custom type mwAuthModeSecondaryTacacsSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwAuthModeSecondaryTacacsSecret_Type.__name__ = "DisplayString"
_MwAuthModeSecondaryTacacsSecret_Object = MibTableColumn
mwAuthModeSecondaryTacacsSecret = _MwAuthModeSecondaryTacacsSecret_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 5, 1, 16),
    _MwAuthModeSecondaryTacacsSecret_Type()
)
mwAuthModeSecondaryTacacsSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAuthModeSecondaryTacacsSecret.setStatus("current")
_MwWapiServer_ObjectIdentity = ObjectIdentity
mwWapiServer = _MwWapiServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 6)
)
_MwWapiServerServerIp_Type = IpAddress
_MwWapiServerServerIp_Object = MibScalar
mwWapiServerServerIp = _MwWapiServerServerIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 6, 1),
    _MwWapiServerServerIp_Type()
)
mwWapiServerServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWapiServerServerIp.setStatus("current")


class _MwWapiServerServerPort_Type(Integer32):
    """Custom type mwWapiServerServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_MwWapiServerServerPort_Type.__name__ = "Integer32"
_MwWapiServerServerPort_Object = MibScalar
mwWapiServerServerPort = _MwWapiServerServerPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 6, 2),
    _MwWapiServerServerPort_Type()
)
mwWapiServerServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWapiServerServerPort.setStatus("current")
_MwCaptivePortalProfileTable_Object = MibTable
mwCaptivePortalProfileTable = _MwCaptivePortalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7)
)
if mibBuilder.loadTexts:
    mwCaptivePortalProfileTable.setStatus("current")
_MwCaptivePortalProfileEntry_Object = MibTableRow
mwCaptivePortalProfileEntry = _MwCaptivePortalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1)
)
mwCaptivePortalProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwCaptivePortalProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwCaptivePortalProfileEntry.setStatus("current")
_MwCaptivePortalProfileTableIndex_Type = Integer32
_MwCaptivePortalProfileTableIndex_Object = MibTableColumn
mwCaptivePortalProfileTableIndex = _MwCaptivePortalProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 1),
    _MwCaptivePortalProfileTableIndex_Type()
)
mwCaptivePortalProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileTableIndex.setStatus("current")


class _MwCaptivePortalProfileName_Type(DisplayString):
    """Custom type mwCaptivePortalProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwCaptivePortalProfileName_Type.__name__ = "DisplayString"
_MwCaptivePortalProfileName_Object = MibTableColumn
mwCaptivePortalProfileName = _MwCaptivePortalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 2),
    _MwCaptivePortalProfileName_Type()
)
mwCaptivePortalProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileName.setStatus("current")


class _MwCaptivePortalProfileRadiusProfileName_Type(DisplayString):
    """Custom type mwCaptivePortalProfileRadiusProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwCaptivePortalProfileRadiusProfileName_Type.__name__ = "DisplayString"
_MwCaptivePortalProfileRadiusProfileName_Object = MibTableColumn
mwCaptivePortalProfileRadiusProfileName = _MwCaptivePortalProfileRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 3),
    _MwCaptivePortalProfileRadiusProfileName_Type()
)
mwCaptivePortalProfileRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileRadiusProfileName.setStatus("current")


class _MwCaptivePortalProfileSecondaryRadiusProfileName_Type(DisplayString):
    """Custom type mwCaptivePortalProfileSecondaryRadiusProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwCaptivePortalProfileSecondaryRadiusProfileName_Type.__name__ = "DisplayString"
_MwCaptivePortalProfileSecondaryRadiusProfileName_Object = MibTableColumn
mwCaptivePortalProfileSecondaryRadiusProfileName = _MwCaptivePortalProfileSecondaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 4),
    _MwCaptivePortalProfileSecondaryRadiusProfileName_Type()
)
mwCaptivePortalProfileSecondaryRadiusProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileSecondaryRadiusProfileName.setStatus("current")


class _MwCaptivePortalProfilePrimaryAccountingRadiusServer_Type(DisplayString):
    """Custom type mwCaptivePortalProfilePrimaryAccountingRadiusServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwCaptivePortalProfilePrimaryAccountingRadiusServer_Type.__name__ = "DisplayString"
_MwCaptivePortalProfilePrimaryAccountingRadiusServer_Object = MibTableColumn
mwCaptivePortalProfilePrimaryAccountingRadiusServer = _MwCaptivePortalProfilePrimaryAccountingRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 5),
    _MwCaptivePortalProfilePrimaryAccountingRadiusServer_Type()
)
mwCaptivePortalProfilePrimaryAccountingRadiusServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfilePrimaryAccountingRadiusServer.setStatus("current")


class _MwCaptivePortalProfileSecondaryAccountingRadiusServer_Type(DisplayString):
    """Custom type mwCaptivePortalProfileSecondaryAccountingRadiusServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwCaptivePortalProfileSecondaryAccountingRadiusServer_Type.__name__ = "DisplayString"
_MwCaptivePortalProfileSecondaryAccountingRadiusServer_Object = MibTableColumn
mwCaptivePortalProfileSecondaryAccountingRadiusServer = _MwCaptivePortalProfileSecondaryAccountingRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 6),
    _MwCaptivePortalProfileSecondaryAccountingRadiusServer_Type()
)
mwCaptivePortalProfileSecondaryAccountingRadiusServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileSecondaryAccountingRadiusServer.setStatus("current")
_MwCaptivePortalProfileAccountingInterimInterval_Type = Unsigned32
_MwCaptivePortalProfileAccountingInterimInterval_Object = MibTableColumn
mwCaptivePortalProfileAccountingInterimInterval = _MwCaptivePortalProfileAccountingInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 7),
    _MwCaptivePortalProfileAccountingInterimInterval_Type()
)
mwCaptivePortalProfileAccountingInterimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileAccountingInterimInterval.setStatus("current")
_MwCaptivePortalProfileOverrideRadius_Type = MwlCaptivePortalAuthenticationType
_MwCaptivePortalProfileOverrideRadius_Object = MibTableColumn
mwCaptivePortalProfileOverrideRadius = _MwCaptivePortalProfileOverrideRadius_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 8),
    _MwCaptivePortalProfileOverrideRadius_Type()
)
mwCaptivePortalProfileOverrideRadius.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileOverrideRadius.setStatus("current")


class _MwCaptivePortalProfileExternalCPURL_Type(DisplayString):
    """Custom type mwCaptivePortalProfileExternalCPURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MwCaptivePortalProfileExternalCPURL_Type.__name__ = "DisplayString"
_MwCaptivePortalProfileExternalCPURL_Object = MibTableColumn
mwCaptivePortalProfileExternalCPURL = _MwCaptivePortalProfileExternalCPURL_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 9),
    _MwCaptivePortalProfileExternalCPURL_Type()
)
mwCaptivePortalProfileExternalCPURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileExternalCPURL.setStatus("current")
_MwCaptivePortalProfileExternalCPIP_Type = IpAddress
_MwCaptivePortalProfileExternalCPIP_Object = MibTableColumn
mwCaptivePortalProfileExternalCPIP = _MwCaptivePortalProfileExternalCPIP_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 10),
    _MwCaptivePortalProfileExternalCPIP_Type()
)
mwCaptivePortalProfileExternalCPIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileExternalCPIP.setStatus("current")


class _MwCaptivePortalProfileCaptivePortalSessionTimeout_Type(Integer32):
    """Custom type mwCaptivePortalProfileCaptivePortalSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_MwCaptivePortalProfileCaptivePortalSessionTimeout_Type.__name__ = "Integer32"
_MwCaptivePortalProfileCaptivePortalSessionTimeout_Object = MibTableColumn
mwCaptivePortalProfileCaptivePortalSessionTimeout = _MwCaptivePortalProfileCaptivePortalSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 15),
    _MwCaptivePortalProfileCaptivePortalSessionTimeout_Type()
)
mwCaptivePortalProfileCaptivePortalSessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileCaptivePortalSessionTimeout.setStatus("current")


class _MwCaptivePortalProfileCaptivePortalActivityTimeout_Type(Integer32):
    """Custom type mwCaptivePortalProfileCaptivePortalActivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MwCaptivePortalProfileCaptivePortalActivityTimeout_Type.__name__ = "Integer32"
_MwCaptivePortalProfileCaptivePortalActivityTimeout_Object = MibTableColumn
mwCaptivePortalProfileCaptivePortalActivityTimeout = _MwCaptivePortalProfileCaptivePortalActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 16),
    _MwCaptivePortalProfileCaptivePortalActivityTimeout_Type()
)
mwCaptivePortalProfileCaptivePortalActivityTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileCaptivePortalActivityTimeout.setStatus("current")


class _MwCaptivePortalProfileL3UserSessionTimeout_Type(Integer32):
    """Custom type mwCaptivePortalProfileL3UserSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_MwCaptivePortalProfileL3UserSessionTimeout_Type.__name__ = "Integer32"
_MwCaptivePortalProfileL3UserSessionTimeout_Object = MibTableColumn
mwCaptivePortalProfileL3UserSessionTimeout = _MwCaptivePortalProfileL3UserSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 17),
    _MwCaptivePortalProfileL3UserSessionTimeout_Type()
)
mwCaptivePortalProfileL3UserSessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileL3UserSessionTimeout.setStatus("current")
_MwCaptivePortalProfileAutoLogin_Type = MwlOnOffSwitch
_MwCaptivePortalProfileAutoLogin_Object = MibTableColumn
mwCaptivePortalProfileAutoLogin = _MwCaptivePortalProfileAutoLogin_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 18),
    _MwCaptivePortalProfileAutoLogin_Type()
)
mwCaptivePortalProfileAutoLogin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileAutoLogin.setStatus("current")
_MwCaptivePortalProfileOwner_Type = MwlProfileOwner
_MwCaptivePortalProfileOwner_Object = MibTableColumn
mwCaptivePortalProfileOwner = _MwCaptivePortalProfileOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 19),
    _MwCaptivePortalProfileOwner_Type()
)
mwCaptivePortalProfileOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileOwner.setStatus("current")
_MwCaptivePortalProfileExternalServer_Type = MwlCaptivePortalExternalServerType
_MwCaptivePortalProfileExternalServer_Object = MibTableColumn
mwCaptivePortalProfileExternalServer = _MwCaptivePortalProfileExternalServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 20),
    _MwCaptivePortalProfileExternalServer_Type()
)
mwCaptivePortalProfileExternalServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileExternalServer.setStatus("current")


class _MwCaptivePortalProfileCpExemptionProfile_Type(DisplayString):
    """Custom type mwCaptivePortalProfileCpExemptionProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwCaptivePortalProfileCpExemptionProfile_Type.__name__ = "DisplayString"
_MwCaptivePortalProfileCpExemptionProfile_Object = MibTableColumn
mwCaptivePortalProfileCpExemptionProfile = _MwCaptivePortalProfileCpExemptionProfile_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 21),
    _MwCaptivePortalProfileCpExemptionProfile_Type()
)
mwCaptivePortalProfileCpExemptionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileCpExemptionProfile.setStatus("current")
_MwCaptivePortalProfileRowStatus_Type = RowStatus
_MwCaptivePortalProfileRowStatus_Object = MibTableColumn
mwCaptivePortalProfileRowStatus = _MwCaptivePortalProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 7, 1, 58),
    _MwCaptivePortalProfileRowStatus_Type()
)
mwCaptivePortalProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalProfileRowStatus.setStatus("current")
_MwCaptivePortalExemptionTable_Object = MibTable
mwCaptivePortalExemptionTable = _MwCaptivePortalExemptionTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8)
)
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionTable.setStatus("current")
_MwCaptivePortalExemptionEntry_Object = MibTableRow
mwCaptivePortalExemptionEntry = _MwCaptivePortalExemptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1)
)
mwCaptivePortalExemptionEntry.setIndexNames(
    (0, "MERU-CONFIG-SECURITY-MIB", "mwCaptivePortalExemptionTableIndex"),
)
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionEntry.setStatus("current")
_MwCaptivePortalExemptionTableIndex_Type = Integer32
_MwCaptivePortalExemptionTableIndex_Object = MibTableColumn
mwCaptivePortalExemptionTableIndex = _MwCaptivePortalExemptionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1, 1),
    _MwCaptivePortalExemptionTableIndex_Type()
)
mwCaptivePortalExemptionTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionTableIndex.setStatus("current")


class _MwCaptivePortalExemptionName_Type(DisplayString):
    """Custom type mwCaptivePortalExemptionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwCaptivePortalExemptionName_Type.__name__ = "DisplayString"
_MwCaptivePortalExemptionName_Object = MibTableColumn
mwCaptivePortalExemptionName = _MwCaptivePortalExemptionName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1, 2),
    _MwCaptivePortalExemptionName_Type()
)
mwCaptivePortalExemptionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionName.setStatus("current")


class _MwCaptivePortalExemptionDescr_Type(DisplayString):
    """Custom type mwCaptivePortalExemptionDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MwCaptivePortalExemptionDescr_Type.__name__ = "DisplayString"
_MwCaptivePortalExemptionDescr_Object = MibTableColumn
mwCaptivePortalExemptionDescr = _MwCaptivePortalExemptionDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1, 3),
    _MwCaptivePortalExemptionDescr_Type()
)
mwCaptivePortalExemptionDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionDescr.setStatus("current")
_MwCaptivePortalExemptionFqdn_Type = DisplayString
_MwCaptivePortalExemptionFqdn_Object = MibTableColumn
mwCaptivePortalExemptionFqdn = _MwCaptivePortalExemptionFqdn_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1, 4),
    _MwCaptivePortalExemptionFqdn_Type()
)
mwCaptivePortalExemptionFqdn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionFqdn.setStatus("current")
_MwCaptivePortalExemptionOwner_Type = MwlProfileOwner
_MwCaptivePortalExemptionOwner_Object = MibTableColumn
mwCaptivePortalExemptionOwner = _MwCaptivePortalExemptionOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1, 5),
    _MwCaptivePortalExemptionOwner_Type()
)
mwCaptivePortalExemptionOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionOwner.setStatus("current")
_MwCaptivePortalExemptionRowStatus_Type = RowStatus
_MwCaptivePortalExemptionRowStatus_Object = MibTableColumn
mwCaptivePortalExemptionRowStatus = _MwCaptivePortalExemptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 9, 8, 1, 7),
    _MwCaptivePortalExemptionRowStatus_Type()
)
mwCaptivePortalExemptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwCaptivePortalExemptionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-SECURITY-MIB",
    **{"mwConfigSecurity": mwConfigSecurity,
       "mwSecurityProfileTable": mwSecurityProfileTable,
       "mwSecurityProfileEntry": mwSecurityProfileEntry,
       "mwSecurityProfileTableIndex": mwSecurityProfileTableIndex,
       "mwSecurityProfileName": mwSecurityProfileName,
       "mwSecurityProfileKDDI": mwSecurityProfileKDDI,
       "mwSecurityProfileReKeyPeriod": mwSecurityProfileReKeyPeriod,
       "mwSecurityProfileCypherSuites": mwSecurityProfileCypherSuites,
       "mwSecurityProfileReAuthEnable": mwSecurityProfileReAuthEnable,
       "mwSecurityProfileL2ModesAllowed": mwSecurityProfileL2ModesAllowed,
       "mwSecurityProfileStaticWepKeyPos": mwSecurityProfileStaticWepKeyPos,
       "mwSecurityProfileSecurityLogging": mwSecurityProfileSecurityLogging,
       "mwSecurityProfileGroupKeyInterval": mwSecurityProfileGroupKeyInterval,
       "mwSecurityProfileFirewallFilterId": mwSecurityProfileFirewallFilterId,
       "mwSecurityProfileSharedAuthEnabled": mwSecurityProfileSharedAuthEnabled,
       "mwSecurityProfileEnableMacFiltering": mwSecurityProfileEnableMacFiltering,
       "mwSecurityProfileFirewallCapability": mwSecurityProfileFirewallCapability,
       "mwSecurityProfileCaptivePortalEnabled": mwSecurityProfileCaptivePortalEnabled,
       "mwSecurityProfileNetworkInitiation8021x": mwSecurityProfileNetworkInitiation8021x,
       "mwSecurityProfilePrimaryRadiusProfileName": mwSecurityProfilePrimaryRadiusProfileName,
       "mwSecurityProfileSecondaryRadiusProfileName": mwSecurityProfileSecondaryRadiusProfileName,
       "mwSecurityProfilePskKey": mwSecurityProfilePskKey,
       "mwSecurityProfileStaticWepKey": mwSecurityProfileStaticWepKey,
       "mwSecurityProfilePassthroughFirewallFilterId": mwSecurityProfilePassthroughFirewallFilterId,
       "mwSecurityProfileOwner": mwSecurityProfileOwner,
       "mwSecurityProfileCaptivePortalAuthenticationMethod": mwSecurityProfileCaptivePortalAuthenticationMethod,
       "mwSecurityProfileTunnelTermination": mwSecurityProfileTunnelTermination,
       "mwSecurityProfileBKSACachingPeriod": mwSecurityProfileBKSACachingPeriod,
       "mwSecurityProfilePMKCachingStatus": mwSecurityProfilePMKCachingStatus,
       "mwSecurityProfileEnvState": mwSecurityProfileEnvState,
       "mwSecurityProfileMACAuthPrimaryRadiusProfileName": mwSecurityProfileMACAuthPrimaryRadiusProfileName,
       "mwSecurityProfileMACAuthSecondaryRadiusProfileName": mwSecurityProfileMACAuthSecondaryRadiusProfileName,
       "mwSecurityProfileCaptivePortalProfile": mwSecurityProfileCaptivePortalProfile,
       "mwSecurityProfileMFP11wSupport": mwSecurityProfileMFP11wSupport,
       "mwSecurityProfileMACAccountingPrimaryRadiusProfileName": mwSecurityProfileMACAccountingPrimaryRadiusProfileName,
       "mwSecurityProfileMACAccountingSecondaryRadiusProfileName": mwSecurityProfileMACAccountingSecondaryRadiusProfileName,
       "mwSecurityProfileCaptivePortalBypassForMAC": mwSecurityProfileCaptivePortalBypassForMAC,
       "mwSecurityProfileRowStatus": mwSecurityProfileRowStatus,
       "mwSslVarsTable": mwSslVarsTable,
       "mwSslVarsEntry": mwSslVarsEntry,
       "mwSslVarsTableIndex": mwSslVarsTableIndex,
       "mwSslVarsSslLifeTime": mwSslVarsSslLifeTime,
       "mwSslVarsCertificateFileName": mwSslVarsCertificateFileName,
       "mwSslVarsCPCertificate": mwSslVarsCPCertificate,
       "mwRadiusProfileTable": mwRadiusProfileTable,
       "mwRadiusProfileEntry": mwRadiusProfileEntry,
       "mwRadiusProfileTableIndex": mwRadiusProfileTableIndex,
       "mwRadiusProfileName": mwRadiusProfileName,
       "mwRadiusProfileDescr": mwRadiusProfileDescr,
       "mwRadiusProfileRadiusIp": mwRadiusProfileRadiusIp,
       "mwRadiusProfileRadiusPort": mwRadiusProfileRadiusPort,
       "mwRadiusProfileRadiusMacDelimiter": mwRadiusProfileRadiusMacDelimiter,
       "mwRadiusProfileRadiusPasswordType": mwRadiusProfileRadiusPasswordType,
       "mwRadiusProfileRadiusSecret": mwRadiusProfileRadiusSecret,
       "mwRadiusProfileOwner": mwRadiusProfileOwner,
       "mwRadiusProfileCalledStationIdType": mwRadiusProfileCalledStationIdType,
       "mwRadiusProfileCoaFlag": mwRadiusProfileCoaFlag,
       "mwRadiusProfileRadiusRelayApId": mwRadiusProfileRadiusRelayApId,
       "mwRadiusProfileRemoteRadiusServerFlag": mwRadiusProfileRemoteRadiusServerFlag,
       "mwRadiusProfileRadiusServerTimeout": mwRadiusProfileRadiusServerTimeout,
       "mwRadiusProfileRadiusServerRetries": mwRadiusProfileRadiusServerRetries,
       "mwRadiusProfileRowStatus": mwRadiusProfileRowStatus,
       "mwGuestUserTable": mwGuestUserTable,
       "mwGuestUserEntry": mwGuestUserEntry,
       "mwGuestUserTableIndex": mwGuestUserTableIndex,
       "mwGuestUserGuestName": mwGuestUserGuestName,
       "mwGuestUserEndTimestamp": mwGuestUserEndTimestamp,
       "mwGuestUserStartTimestamp": mwGuestUserStartTimestamp,
       "mwGuestUserGuestPasswd": mwGuestUserGuestPasswd,
       "mwGuestUserRowStatus": mwGuestUserRowStatus,
       "mwAuthModeTable": mwAuthModeTable,
       "mwAuthModeEntry": mwAuthModeEntry,
       "mwAuthModeTableIndex": mwAuthModeTableIndex,
       "mwAuthModeAuthType": mwAuthModeAuthType,
       "mwAuthModePrimaryRadiusIp": mwAuthModePrimaryRadiusIp,
       "mwAuthModePrimaryRadiusPort": mwAuthModePrimaryRadiusPort,
       "mwAuthModePrimaryRadiusSecret": mwAuthModePrimaryRadiusSecret,
       "mwAuthModeSecondaryRadiusIp": mwAuthModeSecondaryRadiusIp,
       "mwAuthModeSecondaryRadiusPort": mwAuthModeSecondaryRadiusPort,
       "mwAuthModeSecondaryRadiusSecret": mwAuthModeSecondaryRadiusSecret,
       "mwAuthModePrimaryTacacsIp": mwAuthModePrimaryTacacsIp,
       "mwAuthModePrimaryTacacsPort": mwAuthModePrimaryTacacsPort,
       "mwAuthModePrimaryTacacsSecret": mwAuthModePrimaryTacacsSecret,
       "mwAuthModeSecondaryTacacsIp": mwAuthModeSecondaryTacacsIp,
       "mwAuthModeSecondaryTacacsPort": mwAuthModeSecondaryTacacsPort,
       "mwAuthModeSecondaryTacacsSecret": mwAuthModeSecondaryTacacsSecret,
       "mwWapiServer": mwWapiServer,
       "mwWapiServerServerIp": mwWapiServerServerIp,
       "mwWapiServerServerPort": mwWapiServerServerPort,
       "mwCaptivePortalProfileTable": mwCaptivePortalProfileTable,
       "mwCaptivePortalProfileEntry": mwCaptivePortalProfileEntry,
       "mwCaptivePortalProfileTableIndex": mwCaptivePortalProfileTableIndex,
       "mwCaptivePortalProfileName": mwCaptivePortalProfileName,
       "mwCaptivePortalProfileRadiusProfileName": mwCaptivePortalProfileRadiusProfileName,
       "mwCaptivePortalProfileSecondaryRadiusProfileName": mwCaptivePortalProfileSecondaryRadiusProfileName,
       "mwCaptivePortalProfilePrimaryAccountingRadiusServer": mwCaptivePortalProfilePrimaryAccountingRadiusServer,
       "mwCaptivePortalProfileSecondaryAccountingRadiusServer": mwCaptivePortalProfileSecondaryAccountingRadiusServer,
       "mwCaptivePortalProfileAccountingInterimInterval": mwCaptivePortalProfileAccountingInterimInterval,
       "mwCaptivePortalProfileOverrideRadius": mwCaptivePortalProfileOverrideRadius,
       "mwCaptivePortalProfileExternalCPURL": mwCaptivePortalProfileExternalCPURL,
       "mwCaptivePortalProfileExternalCPIP": mwCaptivePortalProfileExternalCPIP,
       "mwCaptivePortalProfileCaptivePortalSessionTimeout": mwCaptivePortalProfileCaptivePortalSessionTimeout,
       "mwCaptivePortalProfileCaptivePortalActivityTimeout": mwCaptivePortalProfileCaptivePortalActivityTimeout,
       "mwCaptivePortalProfileL3UserSessionTimeout": mwCaptivePortalProfileL3UserSessionTimeout,
       "mwCaptivePortalProfileAutoLogin": mwCaptivePortalProfileAutoLogin,
       "mwCaptivePortalProfileOwner": mwCaptivePortalProfileOwner,
       "mwCaptivePortalProfileExternalServer": mwCaptivePortalProfileExternalServer,
       "mwCaptivePortalProfileCpExemptionProfile": mwCaptivePortalProfileCpExemptionProfile,
       "mwCaptivePortalProfileRowStatus": mwCaptivePortalProfileRowStatus,
       "mwCaptivePortalExemptionTable": mwCaptivePortalExemptionTable,
       "mwCaptivePortalExemptionEntry": mwCaptivePortalExemptionEntry,
       "mwCaptivePortalExemptionTableIndex": mwCaptivePortalExemptionTableIndex,
       "mwCaptivePortalExemptionName": mwCaptivePortalExemptionName,
       "mwCaptivePortalExemptionDescr": mwCaptivePortalExemptionDescr,
       "mwCaptivePortalExemptionFqdn": mwCaptivePortalExemptionFqdn,
       "mwCaptivePortalExemptionOwner": mwCaptivePortalExemptionOwner,
       "mwCaptivePortalExemptionRowStatus": mwCaptivePortalExemptionRowStatus}
)
