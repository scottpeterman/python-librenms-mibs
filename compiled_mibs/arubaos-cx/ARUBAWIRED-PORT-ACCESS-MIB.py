# SNMP MIB module (ARUBAWIRED-PORT-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-PORT-ACCESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:21 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arubaWiredPortAccessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessMIB.setRevisions(
        ("2020-10-14 00:00",
         "2021-02-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPortAccessNotifications_ObjectIdentity = ObjectIdentity
arubaWiredPortAccessNotifications = _ArubaWiredPortAccessNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 0)
)
_ArubaWiredPortAccessObjects_ObjectIdentity = ObjectIdentity
arubaWiredPortAccessObjects = _ArubaWiredPortAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1)
)
_ArubaWiredPortAccessClientTable_Object = MibTable
arubaWiredPortAccessClientTable = _ArubaWiredPortAccessClientTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessClientTable.setStatus("current")
_ArubaWiredPortAccessClientEntry_Object = MibTableRow
arubaWiredPortAccessClientEntry = _ArubaWiredPortAccessClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1)
)
arubaWiredPortAccessClientEntry.setIndexNames(
    (0, "ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacPortName"),
    (0, "ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacMac"),
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessClientEntry.setStatus("current")


class _ArubaWiredPacPortName_Type(DisplayString):
    """Custom type arubaWiredPacPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ArubaWiredPacPortName_Type.__name__ = "DisplayString"
_ArubaWiredPacPortName_Object = MibTableColumn
arubaWiredPacPortName = _ArubaWiredPacPortName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 1),
    _ArubaWiredPacPortName_Type()
)
arubaWiredPacPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPacPortName.setStatus("current")
_ArubaWiredPacMac_Type = MacAddress
_ArubaWiredPacMac_Object = MibTableColumn
arubaWiredPacMac = _ArubaWiredPacMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 2),
    _ArubaWiredPacMac_Type()
)
arubaWiredPacMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPacMac.setStatus("current")


class _ArubaWiredPacUserName_Type(DisplayString):
    """Custom type arubaWiredPacUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArubaWiredPacUserName_Type.__name__ = "DisplayString"
_ArubaWiredPacUserName_Object = MibTableColumn
arubaWiredPacUserName = _ArubaWiredPacUserName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 3),
    _ArubaWiredPacUserName_Type()
)
arubaWiredPacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacUserName.setStatus("current")


class _ArubaWiredPacAppliedRole_Type(DisplayString):
    """Custom type arubaWiredPacAppliedRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArubaWiredPacAppliedRole_Type.__name__ = "DisplayString"
_ArubaWiredPacAppliedRole_Object = MibTableColumn
arubaWiredPacAppliedRole = _ArubaWiredPacAppliedRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 4),
    _ArubaWiredPacAppliedRole_Type()
)
arubaWiredPacAppliedRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacAppliedRole.setStatus("current")


class _ArubaWiredPacAppliedRoleType_Type(DisplayString):
    """Custom type arubaWiredPacAppliedRoleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPacAppliedRoleType_Type.__name__ = "DisplayString"
_ArubaWiredPacAppliedRoleType_Object = MibTableColumn
arubaWiredPacAppliedRoleType = _ArubaWiredPacAppliedRoleType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 5),
    _ArubaWiredPacAppliedRoleType_Type()
)
arubaWiredPacAppliedRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacAppliedRoleType.setStatus("current")


class _ArubaWiredPacOnboardedMethods_Type(DisplayString):
    """Custom type arubaWiredPacOnboardedMethods based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArubaWiredPacOnboardedMethods_Type.__name__ = "DisplayString"
_ArubaWiredPacOnboardedMethods_Object = MibTableColumn
arubaWiredPacOnboardedMethods = _ArubaWiredPacOnboardedMethods_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 6),
    _ArubaWiredPacOnboardedMethods_Type()
)
arubaWiredPacOnboardedMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacOnboardedMethods.setStatus("current")


class _ArubaWiredPacAuthState_Type(DisplayString):
    """Custom type arubaWiredPacAuthState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPacAuthState_Type.__name__ = "DisplayString"
_ArubaWiredPacAuthState_Object = MibTableColumn
arubaWiredPacAuthState = _ArubaWiredPacAuthState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 7),
    _ArubaWiredPacAuthState_Type()
)
arubaWiredPacAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacAuthState.setStatus("current")


class _ArubaWiredPacAutzFailureReason_Type(DisplayString):
    """Custom type arubaWiredPacAutzFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredPacAutzFailureReason_Type.__name__ = "DisplayString"
_ArubaWiredPacAutzFailureReason_Object = MibTableColumn
arubaWiredPacAutzFailureReason = _ArubaWiredPacAutzFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 8),
    _ArubaWiredPacAutzFailureReason_Type()
)
arubaWiredPacAutzFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacAutzFailureReason.setStatus("current")
_ArubaWiredPacVlanId_Type = Integer32
_ArubaWiredPacVlanId_Object = MibTableColumn
arubaWiredPacVlanId = _ArubaWiredPacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 1, 1, 9),
    _ArubaWiredPacVlanId_Type()
)
arubaWiredPacVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPacVlanId.setStatus("current")
_ArubaWiredPortAccessRoleTable_Object = MibTable
arubaWiredPortAccessRoleTable = _ArubaWiredPortAccessRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessRoleTable.setStatus("current")
_ArubaWiredPortAccessRoleEntry_Object = MibTableRow
arubaWiredPortAccessRoleEntry = _ArubaWiredPortAccessRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1)
)
arubaWiredPortAccessRoleEntry.setIndexNames(
    (0, "ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParName"),
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessRoleEntry.setStatus("current")


class _ArubaWiredParName_Type(DisplayString):
    """Custom type arubaWiredParName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 110),
    )


_ArubaWiredParName_Type.__name__ = "DisplayString"
_ArubaWiredParName_Object = MibTableColumn
arubaWiredParName = _ArubaWiredParName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 1),
    _ArubaWiredParName_Type()
)
arubaWiredParName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredParName.setStatus("current")


class _ArubaWiredParOrigin_Type(DisplayString):
    """Custom type arubaWiredParOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArubaWiredParOrigin_Type.__name__ = "DisplayString"
_ArubaWiredParOrigin_Object = MibTableColumn
arubaWiredParOrigin = _ArubaWiredParOrigin_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 2),
    _ArubaWiredParOrigin_Type()
)
arubaWiredParOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredParOrigin.setStatus("current")


class _ArubaWiredParUbtGatewayRole_Type(DisplayString):
    """Custom type arubaWiredParUbtGatewayRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ArubaWiredParUbtGatewayRole_Type.__name__ = "DisplayString"
_ArubaWiredParUbtGatewayRole_Object = MibTableColumn
arubaWiredParUbtGatewayRole = _ArubaWiredParUbtGatewayRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 3),
    _ArubaWiredParUbtGatewayRole_Type()
)
arubaWiredParUbtGatewayRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredParUbtGatewayRole.setStatus("current")


class _ArubaWiredParUbtGatewayClearpassRole_Type(DisplayString):
    """Custom type arubaWiredParUbtGatewayClearpassRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArubaWiredParUbtGatewayClearpassRole_Type.__name__ = "DisplayString"
_ArubaWiredParUbtGatewayClearpassRole_Object = MibTableColumn
arubaWiredParUbtGatewayClearpassRole = _ArubaWiredParUbtGatewayClearpassRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 4),
    _ArubaWiredParUbtGatewayClearpassRole_Type()
)
arubaWiredParUbtGatewayClearpassRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredParUbtGatewayClearpassRole.setStatus("current")


class _ArubaWiredParGatewayZone_Type(DisplayString):
    """Custom type arubaWiredParGatewayZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArubaWiredParGatewayZone_Type.__name__ = "DisplayString"
_ArubaWiredParGatewayZone_Object = MibTableColumn
arubaWiredParGatewayZone = _ArubaWiredParGatewayZone_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 5),
    _ArubaWiredParGatewayZone_Type()
)
arubaWiredParGatewayZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredParGatewayZone.setStatus("current")
_ArubaWiredParVlanId_Type = Integer32
_ArubaWiredParVlanId_Object = MibTableColumn
arubaWiredParVlanId = _ArubaWiredParVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 6),
    _ArubaWiredParVlanId_Type()
)
arubaWiredParVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredParVlanId.setStatus("current")


class _ArubaWiredParVlanMode_Type(DisplayString):
    """Custom type arubaWiredParVlanMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArubaWiredParVlanMode_Type.__name__ = "DisplayString"
_ArubaWiredParVlanMode_Object = MibTableColumn
arubaWiredParVlanMode = _ArubaWiredParVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 1, 2, 1, 7),
    _ArubaWiredParVlanMode_Type()
)
arubaWiredParVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredParVlanMode.setStatus("current")
_ArubaWiredPortAccessConformance_ObjectIdentity = ObjectIdentity
arubaWiredPortAccessConformance = _ArubaWiredPortAccessConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 2)
)
_ArubaWiredPortAccessGroups_ObjectIdentity = ObjectIdentity
arubaWiredPortAccessGroups = _ArubaWiredPortAccessGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 2, 1)
)
_ArubaWiredPortAccessCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPortAccessCompliances = _ArubaWiredPortAccessCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 2, 2)
)

# Managed Objects groups

arubaWiredPortAccessClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 2, 1, 1)
)
arubaWiredPortAccessClientGroup.setObjects(
      *(("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacUserName"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacAppliedRole"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacAppliedRoleType"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacOnboardedMethods"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacAuthState"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacAutzFailureReason"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPacVlanId"))
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessClientGroup.setStatus("current")

arubaWiredPortAccessRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 2, 1, 2)
)
arubaWiredPortAccessRoleGroup.setObjects(
      *(("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParOrigin"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParUbtGatewayRole"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParUbtGatewayClearpassRole"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParGatewayZone"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParVlanId"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredParVlanMode"))
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessRoleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredPortAccessCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17, 2, 2, 1)
)
arubaWiredPortAccessCompliance.setObjects(
      *(("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPortAccessClientGroup"),
        ("ARUBAWIRED-PORT-ACCESS-MIB", "arubaWiredPortAccessRoleGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredPortAccessCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-PORT-ACCESS-MIB",
    **{"arubaWiredPortAccessMIB": arubaWiredPortAccessMIB,
       "arubaWiredPortAccessNotifications": arubaWiredPortAccessNotifications,
       "arubaWiredPortAccessObjects": arubaWiredPortAccessObjects,
       "arubaWiredPortAccessClientTable": arubaWiredPortAccessClientTable,
       "arubaWiredPortAccessClientEntry": arubaWiredPortAccessClientEntry,
       "arubaWiredPacPortName": arubaWiredPacPortName,
       "arubaWiredPacMac": arubaWiredPacMac,
       "arubaWiredPacUserName": arubaWiredPacUserName,
       "arubaWiredPacAppliedRole": arubaWiredPacAppliedRole,
       "arubaWiredPacAppliedRoleType": arubaWiredPacAppliedRoleType,
       "arubaWiredPacOnboardedMethods": arubaWiredPacOnboardedMethods,
       "arubaWiredPacAuthState": arubaWiredPacAuthState,
       "arubaWiredPacAutzFailureReason": arubaWiredPacAutzFailureReason,
       "arubaWiredPacVlanId": arubaWiredPacVlanId,
       "arubaWiredPortAccessRoleTable": arubaWiredPortAccessRoleTable,
       "arubaWiredPortAccessRoleEntry": arubaWiredPortAccessRoleEntry,
       "arubaWiredParName": arubaWiredParName,
       "arubaWiredParOrigin": arubaWiredParOrigin,
       "arubaWiredParUbtGatewayRole": arubaWiredParUbtGatewayRole,
       "arubaWiredParUbtGatewayClearpassRole": arubaWiredParUbtGatewayClearpassRole,
       "arubaWiredParGatewayZone": arubaWiredParGatewayZone,
       "arubaWiredParVlanId": arubaWiredParVlanId,
       "arubaWiredParVlanMode": arubaWiredParVlanMode,
       "arubaWiredPortAccessConformance": arubaWiredPortAccessConformance,
       "arubaWiredPortAccessGroups": arubaWiredPortAccessGroups,
       "arubaWiredPortAccessClientGroup": arubaWiredPortAccessClientGroup,
       "arubaWiredPortAccessRoleGroup": arubaWiredPortAccessRoleGroup,
       "arubaWiredPortAccessCompliances": arubaWiredPortAccessCompliances,
       "arubaWiredPortAccessCompliance": arubaWiredPortAccessCompliance}
)
