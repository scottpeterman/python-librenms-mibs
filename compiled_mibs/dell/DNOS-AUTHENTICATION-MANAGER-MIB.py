# SNMP MIB module (DNOS-AUTHENTICATION-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DNOS-AUTHENTICATION-MANAGER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:01 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathAuthMgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61)
)
if mibBuilder.loadTexts:
    fastPathAuthMgr.setRevisions(
        ("2020-10-08 00:00",
         "2020-08-25 00:00",
         "2018-12-26 00:00",
         "2018-09-24 00:00",
         "2018-05-15 00:00",
         "2017-09-05 00:00",
         "2012-12-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AuthMgrPortControlMode(TextualConvention, Integer32):
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
        *(("forceUnauthorized", 1),
          ("auto", 2),
          ("forceAuthorized", 3))
    )



class AuthMgrPortHostMode(TextualConvention, Integer32):
    status = "current"
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
        *(("singleHost", 1),
          ("multiHost", 2),
          ("multiAuth", 3),
          ("multiDomain", 4),
          ("multiDomainMultiHost", 5))
    )



class AuthMgrSessionTerminationAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reauthenticate", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FastpathAuthMgrTraps_ObjectIdentity = ObjectIdentity
fastpathAuthMgrTraps = _FastpathAuthMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 0)
)
_AgentAuthMgrGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrGlobalConfigGroup = _AgentAuthMgrGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1)
)


class _AgentAuthMgrAdminMode_Type(Integer32):
    """Custom type agentAuthMgrAdminMode based on Integer32"""
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


_AgentAuthMgrAdminMode_Type.__name__ = "Integer32"
_AgentAuthMgrAdminMode_Object = MibScalar
agentAuthMgrAdminMode = _AgentAuthMgrAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1, 1),
    _AgentAuthMgrAdminMode_Type()
)
agentAuthMgrAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrAdminMode.setStatus("current")


class _AgentAuthMgrRadiusVlanAssignment_Type(Integer32):
    """Custom type agentAuthMgrRadiusVlanAssignment based on Integer32"""
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


_AgentAuthMgrRadiusVlanAssignment_Type.__name__ = "Integer32"
_AgentAuthMgrRadiusVlanAssignment_Object = MibScalar
agentAuthMgrRadiusVlanAssignment = _AgentAuthMgrRadiusVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1, 2),
    _AgentAuthMgrRadiusVlanAssignment_Type()
)
agentAuthMgrRadiusVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrRadiusVlanAssignment.setStatus("current")


class _AgentAuthMgrDynamicVlanCreationMode_Type(Integer32):
    """Custom type agentAuthMgrDynamicVlanCreationMode based on Integer32"""
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


_AgentAuthMgrDynamicVlanCreationMode_Type.__name__ = "Integer32"
_AgentAuthMgrDynamicVlanCreationMode_Object = MibScalar
agentAuthMgrDynamicVlanCreationMode = _AgentAuthMgrDynamicVlanCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1, 3),
    _AgentAuthMgrDynamicVlanCreationMode_Type()
)
agentAuthMgrDynamicVlanCreationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrDynamicVlanCreationMode.setStatus("current")
_AgentAuthMgrCriticalRecoveryMaxReauth_Type = Unsigned32
_AgentAuthMgrCriticalRecoveryMaxReauth_Object = MibScalar
agentAuthMgrCriticalRecoveryMaxReauth = _AgentAuthMgrCriticalRecoveryMaxReauth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1, 4),
    _AgentAuthMgrCriticalRecoveryMaxReauth_Type()
)
agentAuthMgrCriticalRecoveryMaxReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrCriticalRecoveryMaxReauth.setStatus("current")
_AgentAuthMgrInterfaceConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrInterfaceConfigGroup = _AgentAuthMgrInterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2)
)
_AgentAuthMgrInterfaceConfigMethodTable_Object = MibTable
agentAuthMgrInterfaceConfigMethodTable = _AgentAuthMgrInterfaceConfigMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigMethodTable.setStatus("current")
_AgentAuthMgrInterfaceConfigMethodEntry_Object = MibTableRow
agentAuthMgrInterfaceConfigMethodEntry = _AgentAuthMgrInterfaceConfigMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1)
)
agentAuthMgrInterfaceConfigMethodEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrIfIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "methodIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigMethodEntry.setStatus("current")
_AgentAuthMgrIfIndex_Type = InterfaceIndex
_AgentAuthMgrIfIndex_Object = MibTableColumn
agentAuthMgrIfIndex = _AgentAuthMgrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 1),
    _AgentAuthMgrIfIndex_Type()
)
agentAuthMgrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrIfIndex.setStatus("current")
_MethodIndex_Type = Unsigned32
_MethodIndex_Object = MibTableColumn
methodIndex = _MethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 2),
    _MethodIndex_Type()
)
methodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    methodIndex.setStatus("current")


class _AgentAuthMgrMethodOrder_Type(Integer32):
    """Custom type agentAuthMgrMethodOrder based on Integer32"""
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
        *(("undefined", 0),
          ("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrMethodOrder_Type.__name__ = "Integer32"
_AgentAuthMgrMethodOrder_Object = MibTableColumn
agentAuthMgrMethodOrder = _AgentAuthMgrMethodOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 3),
    _AgentAuthMgrMethodOrder_Type()
)
agentAuthMgrMethodOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentAuthMgrMethodOrder.setStatus("current")


class _AgentAuthMgrMethodPriority_Type(Integer32):
    """Custom type agentAuthMgrMethodPriority based on Integer32"""
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
        *(("undefined", 0),
          ("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrMethodPriority_Type.__name__ = "Integer32"
_AgentAuthMgrMethodPriority_Object = MibTableColumn
agentAuthMgrMethodPriority = _AgentAuthMgrMethodPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 4),
    _AgentAuthMgrMethodPriority_Type()
)
agentAuthMgrMethodPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentAuthMgrMethodPriority.setStatus("current")
_AgentAuthMgrInterfaceConfigTimerTable_Object = MibTable
agentAuthMgrInterfaceConfigTimerTable = _AgentAuthMgrInterfaceConfigTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigTimerTable.setStatus("current")
_AgentAuthMgrInterfaceConfigTimerEntry_Object = MibTableRow
agentAuthMgrInterfaceConfigTimerEntry = _AgentAuthMgrInterfaceConfigTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2, 1)
)
agentAuthMgrInterfaceConfigTimerEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrTimerIfIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigTimerEntry.setStatus("current")
_AgentAuthMgrTimerIfIndex_Type = InterfaceIndex
_AgentAuthMgrTimerIfIndex_Object = MibTableColumn
agentAuthMgrTimerIfIndex = _AgentAuthMgrTimerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2, 1, 1),
    _AgentAuthMgrTimerIfIndex_Type()
)
agentAuthMgrTimerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrTimerIfIndex.setStatus("current")


class _AgentAuthMgrRestart_Type(Unsigned32):
    """Custom type agentAuthMgrRestart based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AgentAuthMgrRestart_Type.__name__ = "Unsigned32"
_AgentAuthMgrRestart_Object = MibTableColumn
agentAuthMgrRestart = _AgentAuthMgrRestart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2, 1, 2),
    _AgentAuthMgrRestart_Type()
)
agentAuthMgrRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrRestart.setStatus("current")
if mibBuilder.loadTexts:
    agentAuthMgrRestart.setUnits("seconds")
_AgentAuthMgrInterfaceConfigAuthenticationTable_Object = MibTable
agentAuthMgrInterfaceConfigAuthenticationTable = _AgentAuthMgrInterfaceConfigAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigAuthenticationTable.setStatus("current")
_AgentAuthMgrInterfaceConfigAuthenticationEntry_Object = MibTableRow
agentAuthMgrInterfaceConfigAuthenticationEntry = _AgentAuthMgrInterfaceConfigAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1)
)
agentAuthMgrInterfaceConfigAuthenticationEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrIfIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigAuthenticationEntry.setStatus("current")


class _AgentAuthMgrPortControlMode_Type(AuthMgrPortControlMode):
    """Custom type agentAuthMgrPortControlMode based on AuthMgrPortControlMode"""
    defaultValue = 2


_AgentAuthMgrPortControlMode_Type.__name__ = "AuthMgrPortControlMode"
_AgentAuthMgrPortControlMode_Object = MibTableColumn
agentAuthMgrPortControlMode = _AgentAuthMgrPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 1),
    _AgentAuthMgrPortControlMode_Type()
)
agentAuthMgrPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortControlMode.setStatus("current")


class _AgentAuthMgrPortHostMode_Type(AuthMgrPortHostMode):
    """Custom type agentAuthMgrPortHostMode based on AuthMgrPortHostMode"""
    defaultValue = 2


_AgentAuthMgrPortHostMode_Type.__name__ = "AuthMgrPortHostMode"
_AgentAuthMgrPortHostMode_Object = MibTableColumn
agentAuthMgrPortHostMode = _AgentAuthMgrPortHostMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 2),
    _AgentAuthMgrPortHostMode_Type()
)
agentAuthMgrPortHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortHostMode.setStatus("current")


class _AgentAuthMgrPortNoResponseVlanId_Type(Unsigned32):
    """Custom type agentAuthMgrPortNoResponseVlanId based on Unsigned32"""
    defaultValue = 0


_AgentAuthMgrPortNoResponseVlanId_Type.__name__ = "Unsigned32"
_AgentAuthMgrPortNoResponseVlanId_Object = MibTableColumn
agentAuthMgrPortNoResponseVlanId = _AgentAuthMgrPortNoResponseVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 3),
    _AgentAuthMgrPortNoResponseVlanId_Type()
)
agentAuthMgrPortNoResponseVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortNoResponseVlanId.setStatus("current")


class _AgentAuthMgrPortAuthFailVlanId_Type(Unsigned32):
    """Custom type agentAuthMgrPortAuthFailVlanId based on Unsigned32"""
    defaultValue = 0


_AgentAuthMgrPortAuthFailVlanId_Type.__name__ = "Unsigned32"
_AgentAuthMgrPortAuthFailVlanId_Object = MibTableColumn
agentAuthMgrPortAuthFailVlanId = _AgentAuthMgrPortAuthFailVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 4),
    _AgentAuthMgrPortAuthFailVlanId_Type()
)
agentAuthMgrPortAuthFailVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthFailVlanId.setStatus("current")
_AgentAuthMgrPortMaxUsers_Type = Unsigned32
_AgentAuthMgrPortMaxUsers_Object = MibTableColumn
agentAuthMgrPortMaxUsers = _AgentAuthMgrPortMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 5),
    _AgentAuthMgrPortMaxUsers_Type()
)
agentAuthMgrPortMaxUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortMaxUsers.setStatus("current")


class _AgentAuthMgrPortAuthViolationMode_Type(Integer32):
    """Custom type agentAuthMgrPortAuthViolationMode based on Integer32"""
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
        *(("protect", 1),
          ("restrict", 2),
          ("shutdown", 3))
    )


_AgentAuthMgrPortAuthViolationMode_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthViolationMode_Object = MibTableColumn
agentAuthMgrPortAuthViolationMode = _AgentAuthMgrPortAuthViolationMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 6),
    _AgentAuthMgrPortAuthViolationMode_Type()
)
agentAuthMgrPortAuthViolationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthViolationMode.setStatus("current")


class _AgentAuthMgrPortCriticalVlanId_Type(Unsigned32):
    """Custom type agentAuthMgrPortCriticalVlanId based on Unsigned32"""
    defaultValue = 0


_AgentAuthMgrPortCriticalVlanId_Type.__name__ = "Unsigned32"
_AgentAuthMgrPortCriticalVlanId_Object = MibTableColumn
agentAuthMgrPortCriticalVlanId = _AgentAuthMgrPortCriticalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 7),
    _AgentAuthMgrPortCriticalVlanId_Type()
)
agentAuthMgrPortCriticalVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortCriticalVlanId.setStatus("current")


class _AgentAuthMgrPortAuthServerDeadAction_Type(Integer32):
    """Custom type agentAuthMgrPortAuthServerDeadAction based on Integer32"""
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
        *(("reinitialize", 1),
          ("authorize", 2),
          ("none", 3))
    )


_AgentAuthMgrPortAuthServerDeadAction_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthServerDeadAction_Object = MibTableColumn
agentAuthMgrPortAuthServerDeadAction = _AgentAuthMgrPortAuthServerDeadAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 8),
    _AgentAuthMgrPortAuthServerDeadAction_Type()
)
agentAuthMgrPortAuthServerDeadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthServerDeadAction.setStatus("current")


class _AgentAuthMgrPortAuthServerAliveAction_Type(Integer32):
    """Custom type agentAuthMgrPortAuthServerAliveAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reinitialize", 1),
          ("none", 2))
    )


_AgentAuthMgrPortAuthServerAliveAction_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthServerAliveAction_Object = MibTableColumn
agentAuthMgrPortAuthServerAliveAction = _AgentAuthMgrPortAuthServerAliveAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 9),
    _AgentAuthMgrPortAuthServerAliveAction_Type()
)
agentAuthMgrPortAuthServerAliveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthServerAliveAction.setStatus("current")


class _AgentAuthMgrPortAuthServerDeadVoiceAction_Type(Integer32):
    """Custom type agentAuthMgrPortAuthServerDeadVoiceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorize", 1),
          ("none", 2))
    )


_AgentAuthMgrPortAuthServerDeadVoiceAction_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthServerDeadVoiceAction_Object = MibTableColumn
agentAuthMgrPortAuthServerDeadVoiceAction = _AgentAuthMgrPortAuthServerDeadVoiceAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 10),
    _AgentAuthMgrPortAuthServerDeadVoiceAction_Type()
)
agentAuthMgrPortAuthServerDeadVoiceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthServerDeadVoiceAction.setStatus("current")
_AgentAuthMgrPortInitialize_Type = TruthValue
_AgentAuthMgrPortInitialize_Object = MibTableColumn
agentAuthMgrPortInitialize = _AgentAuthMgrPortInitialize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 11),
    _AgentAuthMgrPortInitialize_Type()
)
agentAuthMgrPortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortInitialize.setStatus("current")


class _AgentAuthMgrPortUnauthDHCPAllow_Type(Integer32):
    """Custom type agentAuthMgrPortUnauthDHCPAllow based on Integer32"""
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


_AgentAuthMgrPortUnauthDHCPAllow_Type.__name__ = "Integer32"
_AgentAuthMgrPortUnauthDHCPAllow_Object = MibTableColumn
agentAuthMgrPortUnauthDHCPAllow = _AgentAuthMgrPortUnauthDHCPAllow_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 12),
    _AgentAuthMgrPortUnauthDHCPAllow_Type()
)
agentAuthMgrPortUnauthDHCPAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortUnauthDHCPAllow.setStatus("current")


class _AgentAuthMgrPortAuthenticationOpen_Type(Integer32):
    """Custom type agentAuthMgrPortAuthenticationOpen based on Integer32"""
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


_AgentAuthMgrPortAuthenticationOpen_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthenticationOpen_Object = MibTableColumn
agentAuthMgrPortAuthenticationOpen = _AgentAuthMgrPortAuthenticationOpen_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 13),
    _AgentAuthMgrPortAuthenticationOpen_Type()
)
agentAuthMgrPortAuthenticationOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthenticationOpen.setStatus("current")


class _AgentAuthMgrPortAuthControlDirection_Type(Integer32):
    """Custom type agentAuthMgrPortAuthControlDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2))
    )


_AgentAuthMgrPortAuthControlDirection_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthControlDirection_Object = MibTableColumn
agentAuthMgrPortAuthControlDirection = _AgentAuthMgrPortAuthControlDirection_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 14),
    _AgentAuthMgrPortAuthControlDirection_Type()
)
agentAuthMgrPortAuthControlDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthControlDirection.setStatus("current")


class _AgentAuthMgrPortLinkSecPolicy_Type(Integer32):
    """Custom type agentAuthMgrPortLinkSecPolicy based on Integer32"""
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
        *(("shouldSecure", 1),
          ("mustSecure", 2),
          ("mustNotSecure", 3))
    )


_AgentAuthMgrPortLinkSecPolicy_Type.__name__ = "Integer32"
_AgentAuthMgrPortLinkSecPolicy_Object = MibTableColumn
agentAuthMgrPortLinkSecPolicy = _AgentAuthMgrPortLinkSecPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 3, 1, 15),
    _AgentAuthMgrPortLinkSecPolicy_Type()
)
agentAuthMgrPortLinkSecPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortLinkSecPolicy.setStatus("current")
_AgentAuthMgrInterfaceStatusGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrInterfaceStatusGroup = _AgentAuthMgrInterfaceStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3)
)
_AgentAuthMgrInterfaceStatusTable_Object = MibTable
agentAuthMgrInterfaceStatusTable = _AgentAuthMgrInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceStatusTable.setStatus("current")
_AgentAuthMgrInterfaceStatusEntry_Object = MibTableRow
agentAuthMgrInterfaceStatusEntry = _AgentAuthMgrInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1, 1)
)
agentAuthMgrInterfaceStatusEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrIfIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "methodIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceStatusEntry.setStatus("current")


class _AgentAuthMgrStatusMethodOrder_Type(Integer32):
    """Custom type agentAuthMgrStatusMethodOrder based on Integer32"""
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
        *(("undefined", 0),
          ("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrStatusMethodOrder_Type.__name__ = "Integer32"
_AgentAuthMgrStatusMethodOrder_Object = MibTableColumn
agentAuthMgrStatusMethodOrder = _AgentAuthMgrStatusMethodOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1, 1, 1),
    _AgentAuthMgrStatusMethodOrder_Type()
)
agentAuthMgrStatusMethodOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrStatusMethodOrder.setStatus("current")


class _AgentAuthMgrStatusMethodPriority_Type(Integer32):
    """Custom type agentAuthMgrStatusMethodPriority based on Integer32"""
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
        *(("undefined", 0),
          ("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrStatusMethodPriority_Type.__name__ = "Integer32"
_AgentAuthMgrStatusMethodPriority_Object = MibTableColumn
agentAuthMgrStatusMethodPriority = _AgentAuthMgrStatusMethodPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1, 1, 2),
    _AgentAuthMgrStatusMethodPriority_Type()
)
agentAuthMgrStatusMethodPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrStatusMethodPriority.setStatus("current")
_AgentAuthMgrClientStatusGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrClientStatusGroup = _AgentAuthMgrClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4)
)
_AgentAuthMgrClientStatusTable_Object = MibTable
agentAuthMgrClientStatusTable = _AgentAuthMgrClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrClientStatusTable.setStatus("current")
_AgentAuthMgrClientStatusEntry_Object = MibTableRow
agentAuthMgrClientStatusEntry = _AgentAuthMgrClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1)
)
agentAuthMgrClientStatusEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientMacAddress"),
)
if mibBuilder.loadTexts:
    agentAuthMgrClientStatusEntry.setStatus("current")
_AgentAuthMgrClientMacAddress_Type = MacAddress
_AgentAuthMgrClientMacAddress_Object = MibTableColumn
agentAuthMgrClientMacAddress = _AgentAuthMgrClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 1),
    _AgentAuthMgrClientMacAddress_Type()
)
agentAuthMgrClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientMacAddress.setStatus("current")
_AgentAuthMgrLogicalPort_Type = Unsigned32
_AgentAuthMgrLogicalPort_Object = MibTableColumn
agentAuthMgrLogicalPort = _AgentAuthMgrLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 2),
    _AgentAuthMgrLogicalPort_Type()
)
agentAuthMgrLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrLogicalPort.setStatus("current")
_AgentAuthMgrInterface_Type = Unsigned32
_AgentAuthMgrInterface_Object = MibTableColumn
agentAuthMgrInterface = _AgentAuthMgrInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 3),
    _AgentAuthMgrInterface_Type()
)
agentAuthMgrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrInterface.setStatus("current")


class _AgentAuthMgrClientAuthstatus_Type(Integer32):
    """Custom type agentAuthMgrClientAuthstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_AgentAuthMgrClientAuthstatus_Type.__name__ = "Integer32"
_AgentAuthMgrClientAuthstatus_Object = MibTableColumn
agentAuthMgrClientAuthstatus = _AgentAuthMgrClientAuthstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 4),
    _AgentAuthMgrClientAuthstatus_Type()
)
agentAuthMgrClientAuthstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthstatus.setStatus("current")


class _AgentAuthMgrClientAuthMethod_Type(Integer32):
    """Custom type agentAuthMgrClientAuthMethod based on Integer32"""
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
        *(("undefined", 0),
          ("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrClientAuthMethod_Type.__name__ = "Integer32"
_AgentAuthMgrClientAuthMethod_Object = MibTableColumn
agentAuthMgrClientAuthMethod = _AgentAuthMgrClientAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 5),
    _AgentAuthMgrClientAuthMethod_Type()
)
agentAuthMgrClientAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthMethod.setStatus("current")


class _AgentAuthMgrClientAuthState_Type(Integer32):
    """Custom type agentAuthMgrClientAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("running", 3))
    )


_AgentAuthMgrClientAuthState_Type.__name__ = "Integer32"
_AgentAuthMgrClientAuthState_Object = MibTableColumn
agentAuthMgrClientAuthState = _AgentAuthMgrClientAuthState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 6),
    _AgentAuthMgrClientAuthState_Type()
)
agentAuthMgrClientAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthState.setStatus("current")
_AgentAuthMgrClientUserName_Type = DisplayString
_AgentAuthMgrClientUserName_Object = MibTableColumn
agentAuthMgrClientUserName = _AgentAuthMgrClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 7),
    _AgentAuthMgrClientUserName_Type()
)
agentAuthMgrClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientUserName.setStatus("current")
_AgentAuthMgrClientVlanAssigned_Type = Unsigned32
_AgentAuthMgrClientVlanAssigned_Object = MibTableColumn
agentAuthMgrClientVlanAssigned = _AgentAuthMgrClientVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 8),
    _AgentAuthMgrClientVlanAssigned_Type()
)
agentAuthMgrClientVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientVlanAssigned.setStatus("current")


class _AgentAuthMgrClientAuthVlanAssignedReason_Type(Integer32):
    """Custom type agentAuthMgrClientAuthVlanAssignedReason based on Integer32"""
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
        *(("radius", 1),
          ("authFailVlan", 2),
          ("noResponseVlan", 3),
          ("voiceVlan", 4),
          ("monitorVlan", 5),
          ("criticalVlan", 6),
          ("none", 7))
    )


_AgentAuthMgrClientAuthVlanAssignedReason_Type.__name__ = "Integer32"
_AgentAuthMgrClientAuthVlanAssignedReason_Object = MibTableColumn
agentAuthMgrClientAuthVlanAssignedReason = _AgentAuthMgrClientAuthVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 9),
    _AgentAuthMgrClientAuthVlanAssignedReason_Type()
)
agentAuthMgrClientAuthVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthVlanAssignedReason.setStatus("current")
_AgentAuthMgrClientSessionTime_Type = Unsigned32
_AgentAuthMgrClientSessionTime_Object = MibTableColumn
agentAuthMgrClientSessionTime = _AgentAuthMgrClientSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 10),
    _AgentAuthMgrClientSessionTime_Type()
)
agentAuthMgrClientSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientSessionTime.setStatus("current")
_AgentAuthMgrClientFilterID_Type = DisplayString
_AgentAuthMgrClientFilterID_Object = MibTableColumn
agentAuthMgrClientFilterID = _AgentAuthMgrClientFilterID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 11),
    _AgentAuthMgrClientFilterID_Type()
)
agentAuthMgrClientFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientFilterID.setStatus("current")
_AgentAuthMgrClientDACL_Type = DisplayString
_AgentAuthMgrClientDACL_Object = MibTableColumn
agentAuthMgrClientDACL = _AgentAuthMgrClientDACL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 12),
    _AgentAuthMgrClientDACL_Type()
)
agentAuthMgrClientDACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientDACL.setStatus("current")
_AgentAuthMgrClientSessionTimeout_Type = Unsigned32
_AgentAuthMgrClientSessionTimeout_Object = MibTableColumn
agentAuthMgrClientSessionTimeout = _AgentAuthMgrClientSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 13),
    _AgentAuthMgrClientSessionTimeout_Type()
)
agentAuthMgrClientSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientSessionTimeout.setStatus("current")
_AgentAuthMgrClientTerminationAction_Type = AuthMgrSessionTerminationAction
_AgentAuthMgrClientTerminationAction_Object = MibTableColumn
agentAuthMgrClientTerminationAction = _AgentAuthMgrClientTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 14),
    _AgentAuthMgrClientTerminationAction_Type()
)
agentAuthMgrClientTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientTerminationAction.setStatus("current")
_AgentAuthMgrClientAcctSessionId_Type = DisplayString
_AgentAuthMgrClientAcctSessionId_Object = MibTableColumn
agentAuthMgrClientAcctSessionId = _AgentAuthMgrClientAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 15),
    _AgentAuthMgrClientAcctSessionId_Type()
)
agentAuthMgrClientAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAcctSessionId.setStatus("current")
_AgentAuthMgrClientRedirectACL_Type = DisplayString
_AgentAuthMgrClientRedirectACL_Object = MibTableColumn
agentAuthMgrClientRedirectACL = _AgentAuthMgrClientRedirectACL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 16),
    _AgentAuthMgrClientRedirectACL_Type()
)
agentAuthMgrClientRedirectACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientRedirectACL.setStatus("current")
_AgentAuthMgrClientRedirectURL_Type = DisplayString
_AgentAuthMgrClientRedirectURL_Object = MibTableColumn
agentAuthMgrClientRedirectURL = _AgentAuthMgrClientRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 17),
    _AgentAuthMgrClientRedirectURL_Type()
)
agentAuthMgrClientRedirectURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientRedirectURL.setStatus("current")


class _AgentAuthMgrClientLinkSecPolicy_Type(Integer32):
    """Custom type agentAuthMgrClientLinkSecPolicy based on Integer32"""
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
        *(("shouldSecure", 1),
          ("mustSecure", 2),
          ("mustNotSecure", 3))
    )


_AgentAuthMgrClientLinkSecPolicy_Type.__name__ = "Integer32"
_AgentAuthMgrClientLinkSecPolicy_Object = MibTableColumn
agentAuthMgrClientLinkSecPolicy = _AgentAuthMgrClientLinkSecPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 18),
    _AgentAuthMgrClientLinkSecPolicy_Type()
)
agentAuthMgrClientLinkSecPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientLinkSecPolicy.setStatus("current")
_AgentAuthMgrClientSessionTimeLeft_Type = Unsigned32
_AgentAuthMgrClientSessionTimeLeft_Object = MibTableColumn
agentAuthMgrClientSessionTimeLeft = _AgentAuthMgrClientSessionTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 19),
    _AgentAuthMgrClientSessionTimeLeft_Type()
)
agentAuthMgrClientSessionTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientSessionTimeLeft.setStatus("current")
_AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrAuthHistoryResultsGroup = _AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5)
)
_AgentAuthMgrPortAuthHistoryResultTable_Object = MibTable
agentAuthMgrPortAuthHistoryResultTable = _AgentAuthMgrPortAuthHistoryResultTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultTable.setStatus("current")
_AgentAuthMgrPortAuthHistoryResultEntry_Object = MibTableRow
agentAuthMgrPortAuthHistoryResultEntry = _AgentAuthMgrPortAuthHistoryResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1)
)
agentAuthMgrPortAuthHistoryResultEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrAuthHistoryResultIfaceIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrAuthHistoryResultIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultEntry.setStatus("current")
_AgentAuthMgrAuthHistoryResultIfaceIndex_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultIfaceIndex_Object = MibTableColumn
agentAuthMgrAuthHistoryResultIfaceIndex = _AgentAuthMgrAuthHistoryResultIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 1),
    _AgentAuthMgrAuthHistoryResultIfaceIndex_Type()
)
agentAuthMgrAuthHistoryResultIfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultIfaceIndex.setStatus("current")
_AgentAuthMgrAuthHistoryResultIndex_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultIndex_Object = MibTableColumn
agentAuthMgrAuthHistoryResultIndex = _AgentAuthMgrAuthHistoryResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 2),
    _AgentAuthMgrAuthHistoryResultIndex_Type()
)
agentAuthMgrAuthHistoryResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultIndex.setStatus("current")
_AgentAuthMgrAuthHistoryResultTimeStamp_Type = DateAndTime
_AgentAuthMgrAuthHistoryResultTimeStamp_Object = MibTableColumn
agentAuthMgrAuthHistoryResultTimeStamp = _AgentAuthMgrAuthHistoryResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 3),
    _AgentAuthMgrAuthHistoryResultTimeStamp_Type()
)
agentAuthMgrAuthHistoryResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultTimeStamp.setStatus("current")
_AgentAuthMgrAuthHistoryResultMacAddress_Type = MacAddress
_AgentAuthMgrAuthHistoryResultMacAddress_Object = MibTableColumn
agentAuthMgrAuthHistoryResultMacAddress = _AgentAuthMgrAuthHistoryResultMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 4),
    _AgentAuthMgrAuthHistoryResultMacAddress_Type()
)
agentAuthMgrAuthHistoryResultMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultMacAddress.setStatus("current")


class _AgentAuthMgrAuthHistoryResultAuthMethod_Type(Integer32):
    """Custom type agentAuthMgrAuthHistoryResultAuthMethod based on Integer32"""
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
        *(("undefined", 0),
          ("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrAuthHistoryResultAuthMethod_Type.__name__ = "Integer32"
_AgentAuthMgrAuthHistoryResultAuthMethod_Object = MibTableColumn
agentAuthMgrAuthHistoryResultAuthMethod = _AgentAuthMgrAuthHistoryResultAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 5),
    _AgentAuthMgrAuthHistoryResultAuthMethod_Type()
)
agentAuthMgrAuthHistoryResultAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultAuthMethod.setStatus("current")


class _AgentAuthMgrAuthHistoryResultAuthStatus_Type(Integer32):
    """Custom type agentAuthMgrAuthHistoryResultAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_AgentAuthMgrAuthHistoryResultAuthStatus_Type.__name__ = "Integer32"
_AgentAuthMgrAuthHistoryResultAuthStatus_Object = MibTableColumn
agentAuthMgrAuthHistoryResultAuthStatus = _AgentAuthMgrAuthHistoryResultAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 6),
    _AgentAuthMgrAuthHistoryResultAuthStatus_Type()
)
agentAuthMgrAuthHistoryResultAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultAuthStatus.setStatus("current")
_AgentAuthMgrAuthHistoryResultAge_Type = TimeTicks
_AgentAuthMgrAuthHistoryResultAge_Object = MibTableColumn
agentAuthMgrAuthHistoryResultAge = _AgentAuthMgrAuthHistoryResultAge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 7),
    _AgentAuthMgrAuthHistoryResultAge_Type()
)
agentAuthMgrAuthHistoryResultAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultAge.setStatus("current")
_AgentAuthMgrAuthHistoryResultVlanId_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultVlanId_Object = MibTableColumn
agentAuthMgrAuthHistoryResultVlanId = _AgentAuthMgrAuthHistoryResultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 8),
    _AgentAuthMgrAuthHistoryResultVlanId_Type()
)
agentAuthMgrAuthHistoryResultVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultVlanId.setStatus("current")


class _AgentAuthMgrAuthHistoryResultAccessStatus_Type(Integer32):
    """Custom type agentAuthMgrAuthHistoryResultAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("granted", 1),
          ("denied", 2))
    )


_AgentAuthMgrAuthHistoryResultAccessStatus_Type.__name__ = "Integer32"
_AgentAuthMgrAuthHistoryResultAccessStatus_Object = MibTableColumn
agentAuthMgrAuthHistoryResultAccessStatus = _AgentAuthMgrAuthHistoryResultAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 9),
    _AgentAuthMgrAuthHistoryResultAccessStatus_Type()
)
agentAuthMgrAuthHistoryResultAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultAccessStatus.setStatus("current")
_AgentAuthMgrAuthHistoryResultFilterID_Type = DisplayString
_AgentAuthMgrAuthHistoryResultFilterID_Object = MibTableColumn
agentAuthMgrAuthHistoryResultFilterID = _AgentAuthMgrAuthHistoryResultFilterID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 10),
    _AgentAuthMgrAuthHistoryResultFilterID_Type()
)
agentAuthMgrAuthHistoryResultFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultFilterID.setStatus("current")
_AgentAuthMgrAuthHistoryResultDACL_Type = DisplayString
_AgentAuthMgrAuthHistoryResultDACL_Object = MibTableColumn
agentAuthMgrAuthHistoryResultDACL = _AgentAuthMgrAuthHistoryResultDACL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 11),
    _AgentAuthMgrAuthHistoryResultDACL_Type()
)
agentAuthMgrAuthHistoryResultDACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultDACL.setStatus("current")


class _AgentAuthMgrAuthHistoryResultVlanAssignedType_Type(Integer32):
    """Custom type agentAuthMgrAuthHistoryResultVlanAssignedType based on Integer32"""
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
        *(("default", 1),
          ("radius", 2),
          ("unauthenticatedVlan", 3),
          ("guestVlan", 4),
          ("voiceVlan", 5),
          ("monitorVlan", 6),
          ("notAssigned", 7))
    )


_AgentAuthMgrAuthHistoryResultVlanAssignedType_Type.__name__ = "Integer32"
_AgentAuthMgrAuthHistoryResultVlanAssignedType_Object = MibTableColumn
agentAuthMgrAuthHistoryResultVlanAssignedType = _AgentAuthMgrAuthHistoryResultVlanAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 12),
    _AgentAuthMgrAuthHistoryResultVlanAssignedType_Type()
)
agentAuthMgrAuthHistoryResultVlanAssignedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultVlanAssignedType.setStatus("current")


class _AgentAuthMgrAuthHistoryResultReasonCode_Type(Integer32):
    """Custom type agentAuthMgrAuthHistoryResultReasonCode based on Integer32"""
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("supplicant-timeout", 1),
          ("eapol-timeout", 2),
          ("radius-request-timeout", 3),
          ("radius-auth-failure", 4),
          ("radius-auth-comm-failure", 5),
          ("radius-challenge-process-invalid-nas-port", 6),
          ("radius-challenge-process-wrong-eap-msg", 7),
          ("radius-request-send-msg-error", 8),
          ("radius-accept-process-invalid-nas-port", 9),
          ("radius-accept-process-wrong-eap-msg", 10),
          ("radius-accept-filter-assignment-failure", 11),
          ("radius-accept-diffserv-not-present", 12),
          ("radius-accept-vlan-assignment-failure", 13),
          ("vlan-assignment-feature-not-enabled", 14),
          ("radius-success", 15),
          ("local-auth-user-not-found", 16),
          ("local-auth-user-no-access", 17),
          ("local-auth-md5-validation-failure", 18),
          ("local-auth-invalid-eap-type", 19),
          ("local-failure", 20),
          ("local-success", 21),
          ("radius-invalid-radius-status", 22),
          ("guest-vlan-timer-expiry", 23),
          ("undefined-auth-method", 24),
          ("reject-auth-method", 25),
          ("invalid-auth-method", 26),
          ("auth-method-not-configured", 27),
          ("unauth-vlan-not-created", 28),
          ("guest-vlan-not-created", 29),
          ("radius-accept-invalid-vlan-failure", 30),
          ("eapol-request-id-timeout", 31),
          ("all-radius-servers-dead", 32),
          ("client-disconnected", 33),
          ("guest-vlan-success", 34),
          ("unauth-vlan-success", 35),
          ("critical-vlan-success", 36),
          ("monitor-success", 37),
          ("dacl-apply-failure", 38),
          ("open-success", 39))
    )


_AgentAuthMgrAuthHistoryResultReasonCode_Type.__name__ = "Integer32"
_AgentAuthMgrAuthHistoryResultReasonCode_Object = MibTableColumn
agentAuthMgrAuthHistoryResultReasonCode = _AgentAuthMgrAuthHistoryResultReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 13),
    _AgentAuthMgrAuthHistoryResultReasonCode_Type()
)
agentAuthMgrAuthHistoryResultReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultReasonCode.setStatus("current")
_AgentAuthMgrPortAuthHistoryResultClearTable_Object = MibTable
agentAuthMgrPortAuthHistoryResultClearTable = _AgentAuthMgrPortAuthHistoryResultClearTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultClearTable.setStatus("current")
_AgentAuthMgrPortAuthHistoryResultClearEntry_Object = MibTableRow
agentAuthMgrPortAuthHistoryResultClearEntry = _AgentAuthMgrPortAuthHistoryResultClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3, 1)
)
agentAuthMgrPortAuthHistoryResultClearEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrAuthHistoryResultIfIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultClearEntry.setStatus("current")
_AgentAuthMgrAuthHistoryResultIfIndex_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultIfIndex_Object = MibTableColumn
agentAuthMgrAuthHistoryResultIfIndex = _AgentAuthMgrAuthHistoryResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3, 1, 1),
    _AgentAuthMgrAuthHistoryResultIfIndex_Type()
)
agentAuthMgrAuthHistoryResultIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultIfIndex.setStatus("current")


class _AgentAuthMgrPortAuthHistoryResultsClear_Type(Integer32):
    """Custom type agentAuthMgrPortAuthHistoryResultsClear based on Integer32"""
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


_AgentAuthMgrPortAuthHistoryResultsClear_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthHistoryResultsClear_Object = MibTableColumn
agentAuthMgrPortAuthHistoryResultsClear = _AgentAuthMgrPortAuthHistoryResultsClear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3, 1, 2),
    _AgentAuthMgrPortAuthHistoryResultsClear_Type()
)
agentAuthMgrPortAuthHistoryResultsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultsClear.setStatus("current")
_AgentAuthMgrAuthStatsGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrAuthStatsGroup = _AgentAuthMgrAuthStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6)
)
_AgentAuthMgrPortStatsTable_Object = MibTable
agentAuthMgrPortStatsTable = _AgentAuthMgrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsTable.setStatus("current")
_AgentAuthMgrPortStatsEntry_Object = MibTableRow
agentAuthMgrPortStatsEntry = _AgentAuthMgrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1)
)
agentAuthMgrPortStatsEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrPortIfaceIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrPortMethodIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsEntry.setStatus("current")
_AgentAuthMgrPortIfaceIndex_Type = Unsigned32
_AgentAuthMgrPortIfaceIndex_Object = MibTableColumn
agentAuthMgrPortIfaceIndex = _AgentAuthMgrPortIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 1),
    _AgentAuthMgrPortIfaceIndex_Type()
)
agentAuthMgrPortIfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrPortIfaceIndex.setStatus("current")


class _AgentAuthMgrPortMethodIndex_Type(Integer32):
    """Custom type agentAuthMgrPortMethodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 1),
          ("mab", 2),
          ("captivePortal", 3))
    )


_AgentAuthMgrPortMethodIndex_Type.__name__ = "Integer32"
_AgentAuthMgrPortMethodIndex_Object = MibTableColumn
agentAuthMgrPortMethodIndex = _AgentAuthMgrPortMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 2),
    _AgentAuthMgrPortMethodIndex_Type()
)
agentAuthMgrPortMethodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrPortMethodIndex.setStatus("current")
_AgentAuthMgrPortStatsAttempts_Type = Unsigned32
_AgentAuthMgrPortStatsAttempts_Object = MibTableColumn
agentAuthMgrPortStatsAttempts = _AgentAuthMgrPortStatsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 3),
    _AgentAuthMgrPortStatsAttempts_Type()
)
agentAuthMgrPortStatsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsAttempts.setStatus("current")
_AgentAuthMgrPortStatsFailedAttempts_Type = Unsigned32
_AgentAuthMgrPortStatsFailedAttempts_Object = MibTableColumn
agentAuthMgrPortStatsFailedAttempts = _AgentAuthMgrPortStatsFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 4),
    _AgentAuthMgrPortStatsFailedAttempts_Type()
)
agentAuthMgrPortStatsFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsFailedAttempts.setStatus("current")
_AgentAuthMgrPortStatsClearTable_Object = MibTable
agentAuthMgrPortStatsClearTable = _AgentAuthMgrPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 2)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsClearTable.setStatus("current")
_AgentAuthMgrPortStatsClearEntry_Object = MibTableRow
agentAuthMgrPortStatsClearEntry = _AgentAuthMgrPortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 2, 1)
)
agentAuthMgrPortStatsClearEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrPortIfaceIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsClearEntry.setStatus("current")


class _AgentAuthMgrPortStatsClear_Type(Integer32):
    """Custom type agentAuthMgrPortStatsClear based on Integer32"""
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


_AgentAuthMgrPortStatsClear_Type.__name__ = "Integer32"
_AgentAuthMgrPortStatsClear_Object = MibTableColumn
agentAuthMgrPortStatsClear = _AgentAuthMgrPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 2, 1, 2),
    _AgentAuthMgrPortStatsClear_Type()
)
agentAuthMgrPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsClear.setStatus("current")
_AgentAuthMgrTrapsConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrTrapsConfigGroup = _AgentAuthMgrTrapsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 7)
)


class _AuthMgrTrapMode_Type(Integer32):
    """Custom type authMgrTrapMode based on Integer32"""
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


_AuthMgrTrapMode_Type.__name__ = "Integer32"
_AuthMgrTrapMode_Object = MibScalar
authMgrTrapMode = _AuthMgrTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 7, 1),
    _AuthMgrTrapMode_Type()
)
authMgrTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMgrTrapMode.setStatus("current")
_AgentAuthMgrMonitorModeConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrMonitorModeConfigGroup = _AgentAuthMgrMonitorModeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 8)
)


class _AgentAuthMgrMonitorModeEnabled_Type(Integer32):
    """Custom type agentAuthMgrMonitorModeEnabled based on Integer32"""
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


_AgentAuthMgrMonitorModeEnabled_Type.__name__ = "Integer32"
_AgentAuthMgrMonitorModeEnabled_Object = MibScalar
agentAuthMgrMonitorModeEnabled = _AgentAuthMgrMonitorModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 8, 1),
    _AgentAuthMgrMonitorModeEnabled_Type()
)
agentAuthMgrMonitorModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrMonitorModeEnabled.setStatus("current")
_AgentAuthMgrMonitorModeClients_Type = Unsigned32
_AgentAuthMgrMonitorModeClients_Object = MibScalar
agentAuthMgrMonitorModeClients = _AgentAuthMgrMonitorModeClients_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 8, 2),
    _AgentAuthMgrMonitorModeClients_Type()
)
agentAuthMgrMonitorModeClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrMonitorModeClients.setStatus("current")
_AgentAuthMgrNonMonitorModeClients_Type = Unsigned32
_AgentAuthMgrNonMonitorModeClients_Object = MibScalar
agentAuthMgrNonMonitorModeClients = _AgentAuthMgrNonMonitorModeClients_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 8, 3),
    _AgentAuthMgrNonMonitorModeClients_Type()
)
agentAuthMgrNonMonitorModeClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrNonMonitorModeClients.setStatus("current")

# Managed Objects groups


# Notification objects

agentAuthMgrClientAuthStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 0, 1)
)
agentAuthMgrClientAuthStatusTrap.setObjects(
      *(("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrInterface"),
        ("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientMacAddress"),
        ("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientAuthMethod"),
        ("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientAuthstatus"))
)
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-AUTHENTICATION-MANAGER-MIB",
    **{"AuthMgrPortControlMode": AuthMgrPortControlMode,
       "AuthMgrPortHostMode": AuthMgrPortHostMode,
       "AuthMgrSessionTerminationAction": AuthMgrSessionTerminationAction,
       "fastPathAuthMgr": fastPathAuthMgr,
       "fastpathAuthMgrTraps": fastpathAuthMgrTraps,
       "agentAuthMgrClientAuthStatusTrap": agentAuthMgrClientAuthStatusTrap,
       "agentAuthMgrGlobalConfigGroup": agentAuthMgrGlobalConfigGroup,
       "agentAuthMgrAdminMode": agentAuthMgrAdminMode,
       "agentAuthMgrRadiusVlanAssignment": agentAuthMgrRadiusVlanAssignment,
       "agentAuthMgrDynamicVlanCreationMode": agentAuthMgrDynamicVlanCreationMode,
       "agentAuthMgrCriticalRecoveryMaxReauth": agentAuthMgrCriticalRecoveryMaxReauth,
       "agentAuthMgrInterfaceConfigGroup": agentAuthMgrInterfaceConfigGroup,
       "agentAuthMgrInterfaceConfigMethodTable": agentAuthMgrInterfaceConfigMethodTable,
       "agentAuthMgrInterfaceConfigMethodEntry": agentAuthMgrInterfaceConfigMethodEntry,
       "agentAuthMgrIfIndex": agentAuthMgrIfIndex,
       "methodIndex": methodIndex,
       "agentAuthMgrMethodOrder": agentAuthMgrMethodOrder,
       "agentAuthMgrMethodPriority": agentAuthMgrMethodPriority,
       "agentAuthMgrInterfaceConfigTimerTable": agentAuthMgrInterfaceConfigTimerTable,
       "agentAuthMgrInterfaceConfigTimerEntry": agentAuthMgrInterfaceConfigTimerEntry,
       "agentAuthMgrTimerIfIndex": agentAuthMgrTimerIfIndex,
       "agentAuthMgrRestart": agentAuthMgrRestart,
       "agentAuthMgrInterfaceConfigAuthenticationTable": agentAuthMgrInterfaceConfigAuthenticationTable,
       "agentAuthMgrInterfaceConfigAuthenticationEntry": agentAuthMgrInterfaceConfigAuthenticationEntry,
       "agentAuthMgrPortControlMode": agentAuthMgrPortControlMode,
       "agentAuthMgrPortHostMode": agentAuthMgrPortHostMode,
       "agentAuthMgrPortNoResponseVlanId": agentAuthMgrPortNoResponseVlanId,
       "agentAuthMgrPortAuthFailVlanId": agentAuthMgrPortAuthFailVlanId,
       "agentAuthMgrPortMaxUsers": agentAuthMgrPortMaxUsers,
       "agentAuthMgrPortAuthViolationMode": agentAuthMgrPortAuthViolationMode,
       "agentAuthMgrPortCriticalVlanId": agentAuthMgrPortCriticalVlanId,
       "agentAuthMgrPortAuthServerDeadAction": agentAuthMgrPortAuthServerDeadAction,
       "agentAuthMgrPortAuthServerAliveAction": agentAuthMgrPortAuthServerAliveAction,
       "agentAuthMgrPortAuthServerDeadVoiceAction": agentAuthMgrPortAuthServerDeadVoiceAction,
       "agentAuthMgrPortInitialize": agentAuthMgrPortInitialize,
       "agentAuthMgrPortUnauthDHCPAllow": agentAuthMgrPortUnauthDHCPAllow,
       "agentAuthMgrPortAuthenticationOpen": agentAuthMgrPortAuthenticationOpen,
       "agentAuthMgrPortAuthControlDirection": agentAuthMgrPortAuthControlDirection,
       "agentAuthMgrPortLinkSecPolicy": agentAuthMgrPortLinkSecPolicy,
       "agentAuthMgrInterfaceStatusGroup": agentAuthMgrInterfaceStatusGroup,
       "agentAuthMgrInterfaceStatusTable": agentAuthMgrInterfaceStatusTable,
       "agentAuthMgrInterfaceStatusEntry": agentAuthMgrInterfaceStatusEntry,
       "agentAuthMgrStatusMethodOrder": agentAuthMgrStatusMethodOrder,
       "agentAuthMgrStatusMethodPriority": agentAuthMgrStatusMethodPriority,
       "agentAuthMgrClientStatusGroup": agentAuthMgrClientStatusGroup,
       "agentAuthMgrClientStatusTable": agentAuthMgrClientStatusTable,
       "agentAuthMgrClientStatusEntry": agentAuthMgrClientStatusEntry,
       "agentAuthMgrClientMacAddress": agentAuthMgrClientMacAddress,
       "agentAuthMgrLogicalPort": agentAuthMgrLogicalPort,
       "agentAuthMgrInterface": agentAuthMgrInterface,
       "agentAuthMgrClientAuthstatus": agentAuthMgrClientAuthstatus,
       "agentAuthMgrClientAuthMethod": agentAuthMgrClientAuthMethod,
       "agentAuthMgrClientAuthState": agentAuthMgrClientAuthState,
       "agentAuthMgrClientUserName": agentAuthMgrClientUserName,
       "agentAuthMgrClientVlanAssigned": agentAuthMgrClientVlanAssigned,
       "agentAuthMgrClientAuthVlanAssignedReason": agentAuthMgrClientAuthVlanAssignedReason,
       "agentAuthMgrClientSessionTime": agentAuthMgrClientSessionTime,
       "agentAuthMgrClientFilterID": agentAuthMgrClientFilterID,
       "agentAuthMgrClientDACL": agentAuthMgrClientDACL,
       "agentAuthMgrClientSessionTimeout": agentAuthMgrClientSessionTimeout,
       "agentAuthMgrClientTerminationAction": agentAuthMgrClientTerminationAction,
       "agentAuthMgrClientAcctSessionId": agentAuthMgrClientAcctSessionId,
       "agentAuthMgrClientRedirectACL": agentAuthMgrClientRedirectACL,
       "agentAuthMgrClientRedirectURL": agentAuthMgrClientRedirectURL,
       "agentAuthMgrClientLinkSecPolicy": agentAuthMgrClientLinkSecPolicy,
       "agentAuthMgrClientSessionTimeLeft": agentAuthMgrClientSessionTimeLeft,
       "agentAuthMgrAuthHistoryResultsGroup": agentAuthMgrAuthHistoryResultsGroup,
       "agentAuthMgrPortAuthHistoryResultTable": agentAuthMgrPortAuthHistoryResultTable,
       "agentAuthMgrPortAuthHistoryResultEntry": agentAuthMgrPortAuthHistoryResultEntry,
       "agentAuthMgrAuthHistoryResultIfaceIndex": agentAuthMgrAuthHistoryResultIfaceIndex,
       "agentAuthMgrAuthHistoryResultIndex": agentAuthMgrAuthHistoryResultIndex,
       "agentAuthMgrAuthHistoryResultTimeStamp": agentAuthMgrAuthHistoryResultTimeStamp,
       "agentAuthMgrAuthHistoryResultMacAddress": agentAuthMgrAuthHistoryResultMacAddress,
       "agentAuthMgrAuthHistoryResultAuthMethod": agentAuthMgrAuthHistoryResultAuthMethod,
       "agentAuthMgrAuthHistoryResultAuthStatus": agentAuthMgrAuthHistoryResultAuthStatus,
       "agentAuthMgrAuthHistoryResultAge": agentAuthMgrAuthHistoryResultAge,
       "agentAuthMgrAuthHistoryResultVlanId": agentAuthMgrAuthHistoryResultVlanId,
       "agentAuthMgrAuthHistoryResultAccessStatus": agentAuthMgrAuthHistoryResultAccessStatus,
       "agentAuthMgrAuthHistoryResultFilterID": agentAuthMgrAuthHistoryResultFilterID,
       "agentAuthMgrAuthHistoryResultDACL": agentAuthMgrAuthHistoryResultDACL,
       "agentAuthMgrAuthHistoryResultVlanAssignedType": agentAuthMgrAuthHistoryResultVlanAssignedType,
       "agentAuthMgrAuthHistoryResultReasonCode": agentAuthMgrAuthHistoryResultReasonCode,
       "agentAuthMgrPortAuthHistoryResultClearTable": agentAuthMgrPortAuthHistoryResultClearTable,
       "agentAuthMgrPortAuthHistoryResultClearEntry": agentAuthMgrPortAuthHistoryResultClearEntry,
       "agentAuthMgrAuthHistoryResultIfIndex": agentAuthMgrAuthHistoryResultIfIndex,
       "agentAuthMgrPortAuthHistoryResultsClear": agentAuthMgrPortAuthHistoryResultsClear,
       "agentAuthMgrAuthStatsGroup": agentAuthMgrAuthStatsGroup,
       "agentAuthMgrPortStatsTable": agentAuthMgrPortStatsTable,
       "agentAuthMgrPortStatsEntry": agentAuthMgrPortStatsEntry,
       "agentAuthMgrPortIfaceIndex": agentAuthMgrPortIfaceIndex,
       "agentAuthMgrPortMethodIndex": agentAuthMgrPortMethodIndex,
       "agentAuthMgrPortStatsAttempts": agentAuthMgrPortStatsAttempts,
       "agentAuthMgrPortStatsFailedAttempts": agentAuthMgrPortStatsFailedAttempts,
       "agentAuthMgrPortStatsClearTable": agentAuthMgrPortStatsClearTable,
       "agentAuthMgrPortStatsClearEntry": agentAuthMgrPortStatsClearEntry,
       "agentAuthMgrPortStatsClear": agentAuthMgrPortStatsClear,
       "agentAuthMgrTrapsConfigGroup": agentAuthMgrTrapsConfigGroup,
       "authMgrTrapMode": authMgrTrapMode,
       "agentAuthMgrMonitorModeConfigGroup": agentAuthMgrMonitorModeConfigGroup,
       "agentAuthMgrMonitorModeEnabled": agentAuthMgrMonitorModeEnabled,
       "agentAuthMgrMonitorModeClients": agentAuthMgrMonitorModeClients,
       "agentAuthMgrNonMonitorModeClients": agentAuthMgrNonMonitorModeClients}
)
