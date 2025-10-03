# SNMP MIB module (CIENA-CES-NOTIFICATIONS-CONTROL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-NOTIFICATIONS-CONTROL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:43 2025
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

(cienaCesNotificationsControlModule,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesNotificationsControlModule")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesNotificationsControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesNotificationsControlMIB.setRevisions(
        ("2017-06-07 00:00",
         "2016-10-27 00:00",
         "2016-10-07 00:00",
         "2016-03-06 00:00",
         "2015-05-06 00:00",
         "2015-01-07 00:00",
         "2014-12-10 00:00",
         "2014-02-25 00:00",
         "2013-12-18 00:00",
         "2013-11-05 00:00",
         "2013-10-28 00:00",
         "2011-03-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesNotificationsControl_ObjectIdentity = ObjectIdentity
cienaCesNotificationsControl = _CienaCesNotificationsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1)
)


class _CienaCesPortEnhancedLinkTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortEnhancedLinkTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortEnhancedLinkTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortEnhancedLinkTrapState_Object = MibScalar
cienaCesPortEnhancedLinkTrapState = _CienaCesPortEnhancedLinkTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 1),
    _CienaCesPortEnhancedLinkTrapState_Type()
)
cienaCesPortEnhancedLinkTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortEnhancedLinkTrapState.setStatus("current")


class _CienaCesPortStdLinkTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortStdLinkTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortStdLinkTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortStdLinkTrapState_Object = MibScalar
cienaCesPortStdLinkTrapState = _CienaCesPortStdLinkTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 2),
    _CienaCesPortStdLinkTrapState_Type()
)
cienaCesPortStdLinkTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortStdLinkTrapState.setStatus("current")


class _CienaCesPortAllTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortAllTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortAllTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortAllTrapState_Object = MibScalar
cienaCesPortAllTrapState = _CienaCesPortAllTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 3),
    _CienaCesPortAllTrapState_Type()
)
cienaCesPortAllTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortAllTrapState.setStatus("current")


class _CienaCesModuleAllModulesTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleAllModulesTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModuleAllModulesTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModuleAllModulesTrapState_Object = MibScalar
cienaCesModuleAllModulesTrapState = _CienaCesModuleAllModulesTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 6),
    _CienaCesModuleAllModulesTrapState_Type()
)
cienaCesModuleAllModulesTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleAllModulesTrapState.setStatus("current")


class _CienaCesModuleAllModulesHealthTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleAllModulesHealthTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModuleAllModulesHealthTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModuleAllModulesHealthTrapState_Object = MibScalar
cienaCesModuleAllModulesHealthTrapState = _CienaCesModuleAllModulesHealthTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 7),
    _CienaCesModuleAllModulesHealthTrapState_Type()
)
cienaCesModuleAllModulesHealthTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleAllModulesHealthTrapState.setStatus("current")


class _CienaCesModuleSensorTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleSensorTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModuleSensorTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModuleSensorTrapState_Object = MibScalar
cienaCesModuleSensorTrapState = _CienaCesModuleSensorTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 8),
    _CienaCesModuleSensorTrapState_Type()
)
cienaCesModuleSensorTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleSensorTrapState.setStatus("current")


class _CienaCesModuleHATrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleHATrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModuleHATrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModuleHATrapState_Object = MibScalar
cienaCesModuleHATrapState = _CienaCesModuleHATrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 9),
    _CienaCesModuleHATrapState_Type()
)
cienaCesModuleHATrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleHATrapState.setStatus("current")


class _CienaCesModuleProtectionModeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleProtectionModeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModuleProtectionModeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModuleProtectionModeTrapState_Object = MibScalar
cienaCesModuleProtectionModeTrapState = _CienaCesModuleProtectionModeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 10),
    _CienaCesModuleProtectionModeTrapState_Type()
)
cienaCesModuleProtectionModeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleProtectionModeTrapState.setStatus("current")


class _CienaCesModulePOSTErrorTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModulePOSTErrorTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModulePOSTErrorTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModulePOSTErrorTrapState_Object = MibScalar
cienaCesModulePOSTErrorTrapState = _CienaCesModulePOSTErrorTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 11),
    _CienaCesModulePOSTErrorTrapState_Type()
)
cienaCesModulePOSTErrorTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorTrapState.setStatus("current")


class _CienaCesModuleSwitchFabricDisruptedTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleSwitchFabricDisruptedTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesModuleSwitchFabricDisruptedTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesModuleSwitchFabricDisruptedTrapState_Object = MibScalar
cienaCesModuleSwitchFabricDisruptedTrapState = _CienaCesModuleSwitchFabricDisruptedTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 12),
    _CienaCesModuleSwitchFabricDisruptedTrapState_Type()
)
cienaCesModuleSwitchFabricDisruptedTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleSwitchFabricDisruptedTrapState.setStatus("current")


class _CienaCesChassisAllPowerSupplyTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisAllPowerSupplyTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisAllPowerSupplyTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisAllPowerSupplyTrapState_Object = MibScalar
cienaCesChassisAllPowerSupplyTrapState = _CienaCesChassisAllPowerSupplyTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 14),
    _CienaCesChassisAllPowerSupplyTrapState_Type()
)
cienaCesChassisAllPowerSupplyTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisAllPowerSupplyTrapState.setStatus("current")


class _CienaCesChassisAllFanTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisAllFanTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisAllFanTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisAllFanTrapState_Object = MibScalar
cienaCesChassisAllFanTrapState = _CienaCesChassisAllFanTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 15),
    _CienaCesChassisAllFanTrapState_Type()
)
cienaCesChassisAllFanTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisAllFanTrapState.setStatus("current")


class _CienaCesChassisAllFanTrayTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisAllFanTrayTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisAllFanTrayTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisAllFanTrayTrapState_Object = MibScalar
cienaCesChassisAllFanTrayTrapState = _CienaCesChassisAllFanTrayTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 16),
    _CienaCesChassisAllFanTrayTrapState_Type()
)
cienaCesChassisAllFanTrayTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisAllFanTrayTrapState.setStatus("current")


class _CienaCesChassisAllFanTempTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisAllFanTempTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisAllFanTempTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisAllFanTempTrapState_Object = MibScalar
cienaCesChassisAllFanTempTrapState = _CienaCesChassisAllFanTempTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 17),
    _CienaCesChassisAllFanTempTrapState_Type()
)
cienaCesChassisAllFanTempTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisAllFanTempTrapState.setStatus("current")


class _CienaCesChassisHealthTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisHealthTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisHealthTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisHealthTrapState_Object = MibScalar
cienaCesChassisHealthTrapState = _CienaCesChassisHealthTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 18),
    _CienaCesChassisHealthTrapState_Type()
)
cienaCesChassisHealthTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisHealthTrapState.setStatus("current")


class _CienaCesRapsAlarmTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRapsAlarmTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRapsAlarmTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRapsAlarmTrapState_Object = MibScalar
cienaCesRapsAlarmTrapState = _CienaCesRapsAlarmTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 19),
    _CienaCesRapsAlarmTrapState_Type()
)
cienaCesRapsAlarmTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRapsAlarmTrapState.setStatus("current")


class _CienaCesMplsTrapState_Type(CienaGlobalState):
    """Custom type cienaCesMplsTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesMplsTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesMplsTrapState_Object = MibScalar
cienaCesMplsTrapState = _CienaCesMplsTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 20),
    _CienaCesMplsTrapState_Type()
)
cienaCesMplsTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesMplsTrapState.setStatus("current")


class _CienaCesCfmFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmFaultTrapState_Object = MibScalar
cienaCesCfmFaultTrapState = _CienaCesCfmFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 21),
    _CienaCesCfmFaultTrapState_Type()
)
cienaCesCfmFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmFaultTrapState.setStatus("current")


class _CienaCesCfmDelayFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmDelayFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmDelayFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmDelayFaultTrapState_Object = MibScalar
cienaCesCfmDelayFaultTrapState = _CienaCesCfmDelayFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 22),
    _CienaCesCfmDelayFaultTrapState_Type()
)
cienaCesCfmDelayFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmDelayFaultTrapState.setStatus("current")


class _CienaCesCfmJitterFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmJitterFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmJitterFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmJitterFaultTrapState_Object = MibScalar
cienaCesCfmJitterFaultTrapState = _CienaCesCfmJitterFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 23),
    _CienaCesCfmJitterFaultTrapState_Type()
)
cienaCesCfmJitterFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmJitterFaultTrapState.setStatus("current")


class _CienaCesCfmFrameLossNearFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmFrameLossNearFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmFrameLossNearFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmFrameLossNearFaultTrapState_Object = MibScalar
cienaCesCfmFrameLossNearFaultTrapState = _CienaCesCfmFrameLossNearFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 24),
    _CienaCesCfmFrameLossNearFaultTrapState_Type()
)
cienaCesCfmFrameLossNearFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossNearFaultTrapState.setStatus("current")


class _CienaCesCfmFrameLossFarFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmFrameLossFarFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmFrameLossFarFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmFrameLossFarFaultTrapState_Object = MibScalar
cienaCesCfmFrameLossFarFaultTrapState = _CienaCesCfmFrameLossFarFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 25),
    _CienaCesCfmFrameLossFarFaultTrapState_Type()
)
cienaCesCfmFrameLossFarFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossFarFaultTrapState.setStatus("current")


class _CienaCesCfmSyntheticLossNearFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmSyntheticLossNearFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmSyntheticLossNearFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmSyntheticLossNearFaultTrapState_Object = MibScalar
cienaCesCfmSyntheticLossNearFaultTrapState = _CienaCesCfmSyntheticLossNearFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 26),
    _CienaCesCfmSyntheticLossNearFaultTrapState_Type()
)
cienaCesCfmSyntheticLossNearFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossNearFaultTrapState.setStatus("current")


class _CienaCesCfmSyntheticLossFarFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmSyntheticLossFarFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmSyntheticLossFarFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmSyntheticLossFarFaultTrapState_Object = MibScalar
cienaCesCfmSyntheticLossFarFaultTrapState = _CienaCesCfmSyntheticLossFarFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 27),
    _CienaCesCfmSyntheticLossFarFaultTrapState_Type()
)
cienaCesCfmSyntheticLossFarFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossFarFaultTrapState.setStatus("current")


class _CienaCesPbtFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPbtFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPbtFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPbtFaultTrapState_Object = MibScalar
cienaCesPbtFaultTrapState = _CienaCesPbtFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 28),
    _CienaCesPbtFaultTrapState_Type()
)
cienaCesPbtFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPbtFaultTrapState.setStatus("current")


class _CienaCesBfdTrapState_Type(CienaGlobalState):
    """Custom type cienaCesBfdTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesBfdTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesBfdTrapState_Object = MibScalar
cienaCesBfdTrapState = _CienaCesBfdTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 29),
    _CienaCesBfdTrapState_Type()
)
cienaCesBfdTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBfdTrapState.setStatus("current")


class _CienaCesIPMgmtInterfaceAddrChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIPMgmtInterfaceAddrChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIPMgmtInterfaceAddrChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIPMgmtInterfaceAddrChangeTrapState_Object = MibScalar
cienaCesIPMgmtInterfaceAddrChangeTrapState = _CienaCesIPMgmtInterfaceAddrChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 31),
    _CienaCesIPMgmtInterfaceAddrChangeTrapState_Type()
)
cienaCesIPMgmtInterfaceAddrChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIPMgmtInterfaceAddrChangeTrapState.setStatus("current")


class _CienaCesIPMgmtInterfaceGatewayAddrChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIPMgmtInterfaceGatewayAddrChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIPMgmtInterfaceGatewayAddrChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIPMgmtInterfaceGatewayAddrChangeTrapState_Object = MibScalar
cienaCesIPMgmtInterfaceGatewayAddrChangeTrapState = _CienaCesIPMgmtInterfaceGatewayAddrChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 32),
    _CienaCesIPMgmtInterfaceGatewayAddrChangeTrapState_Type()
)
cienaCesIPMgmtInterfaceGatewayAddrChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIPMgmtInterfaceGatewayAddrChangeTrapState.setStatus("current")


class _CienaCesDataplaneUcastTrapState_Type(CienaGlobalState):
    """Custom type cienaCesDataplaneUcastTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesDataplaneUcastTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesDataplaneUcastTrapState_Object = MibScalar
cienaCesDataplaneUcastTrapState = _CienaCesDataplaneUcastTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 35),
    _CienaCesDataplaneUcastTrapState_Type()
)
cienaCesDataplaneUcastTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDataplaneUcastTrapState.setStatus("current")


class _CienaCesDataplaneBcastTrapState_Type(CienaGlobalState):
    """Custom type cienaCesDataplaneBcastTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesDataplaneBcastTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesDataplaneBcastTrapState_Object = MibScalar
cienaCesDataplaneBcastTrapState = _CienaCesDataplaneBcastTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 36),
    _CienaCesDataplaneBcastTrapState_Type()
)
cienaCesDataplaneBcastTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDataplaneBcastTrapState.setStatus("current")


class _CienaCesDataplaneMcastTrapState_Type(CienaGlobalState):
    """Custom type cienaCesDataplaneMcastTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesDataplaneMcastTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesDataplaneMcastTrapState_Object = MibScalar
cienaCesDataplaneMcastTrapState = _CienaCesDataplaneMcastTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 37),
    _CienaCesDataplaneMcastTrapState_Type()
)
cienaCesDataplaneMcastTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDataplaneMcastTrapState.setStatus("current")


class _CienaCesPortXcvrLinkStateChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrLinkStateChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrLinkStateChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrLinkStateChangeTrapState_Object = MibScalar
cienaCesPortXcvrLinkStateChangeTrapState = _CienaCesPortXcvrLinkStateChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 40),
    _CienaCesPortXcvrLinkStateChangeTrapState_Type()
)
cienaCesPortXcvrLinkStateChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLinkStateChangeTrapState.setStatus("current")


class _CienaCesPortXcvrErrorTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrErrorTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrErrorTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrErrorTrapState_Object = MibScalar
cienaCesPortXcvrErrorTrapState = _CienaCesPortXcvrErrorTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 41),
    _CienaCesPortXcvrErrorTrapState_Type()
)
cienaCesPortXcvrErrorTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrErrorTrapState.setStatus("current")


class _CienaCesPortXcvrTempChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrTempChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrTempChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrTempChangeTrapState_Object = MibScalar
cienaCesPortXcvrTempChangeTrapState = _CienaCesPortXcvrTempChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 42),
    _CienaCesPortXcvrTempChangeTrapState_Type()
)
cienaCesPortXcvrTempChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTempChangeTrapState.setStatus("current")


class _CienaCesPortXcvrVoltageChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrVoltageChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrVoltageChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrVoltageChangeTrapState_Object = MibScalar
cienaCesPortXcvrVoltageChangeTrapState = _CienaCesPortXcvrVoltageChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 43),
    _CienaCesPortXcvrVoltageChangeTrapState_Type()
)
cienaCesPortXcvrVoltageChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrVoltageChangeTrapState.setStatus("current")


class _CienaCesPortXcvrBiasChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrBiasChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrBiasChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrBiasChangeTrapState_Object = MibScalar
cienaCesPortXcvrBiasChangeTrapState = _CienaCesPortXcvrBiasChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 44),
    _CienaCesPortXcvrBiasChangeTrapState_Type()
)
cienaCesPortXcvrBiasChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrBiasChangeTrapState.setStatus("current")


class _CienaCesPortXcvrTxPowerChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrTxPowerChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrTxPowerChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrTxPowerChangeTrapState_Object = MibScalar
cienaCesPortXcvrTxPowerChangeTrapState = _CienaCesPortXcvrTxPowerChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 45),
    _CienaCesPortXcvrTxPowerChangeTrapState_Type()
)
cienaCesPortXcvrTxPowerChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxPowerChangeTrapState.setStatus("current")


class _CienaCesPortXcvrRxPowerChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrRxPowerChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrRxPowerChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrRxPowerChangeTrapState_Object = MibScalar
cienaCesPortXcvrRxPowerChangeTrapState = _CienaCesPortXcvrRxPowerChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 46),
    _CienaCesPortXcvrRxPowerChangeTrapState_Type()
)
cienaCesPortXcvrRxPowerChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrRxPowerChangeTrapState.setStatus("current")


class _CienaCesPortXcvrSpeedInfoTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrSpeedInfoTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPortXcvrSpeedInfoTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrSpeedInfoTrapState_Object = MibScalar
cienaCesPortXcvrSpeedInfoTrapState = _CienaCesPortXcvrSpeedInfoTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 47),
    _CienaCesPortXcvrSpeedInfoTrapState_Type()
)
cienaCesPortXcvrSpeedInfoTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrSpeedInfoTrapState.setStatus("current")


class _CienaCesRstpPortBackupTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRstpPortBackupTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRstpPortBackupTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRstpPortBackupTrapState_Object = MibScalar
cienaCesRstpPortBackupTrapState = _CienaCesRstpPortBackupTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 48),
    _CienaCesRstpPortBackupTrapState_Type()
)
cienaCesRstpPortBackupTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRstpPortBackupTrapState.setStatus("current")


class _CienaCesRstpPortPvstBPduReceivedTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRstpPortPvstBPduReceivedTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRstpPortPvstBPduReceivedTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRstpPortPvstBPduReceivedTrapState_Object = MibScalar
cienaCesRstpPortPvstBPduReceivedTrapState = _CienaCesRstpPortPvstBPduReceivedTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 49),
    _CienaCesRstpPortPvstBPduReceivedTrapState_Type()
)
cienaCesRstpPortPvstBPduReceivedTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRstpPortPvstBPduReceivedTrapState.setStatus("current")


class _CienaCesRstpPortSelfLoopTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRstpPortSelfLoopTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRstpPortSelfLoopTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRstpPortSelfLoopTrapState_Object = MibScalar
cienaCesRstpPortSelfLoopTrapState = _CienaCesRstpPortSelfLoopTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 50),
    _CienaCesRstpPortSelfLoopTrapState_Type()
)
cienaCesRstpPortSelfLoopTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRstpPortSelfLoopTrapState.setStatus("current")


class _CienaCesRstpPortOperEdgeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRstpPortOperEdgeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRstpPortOperEdgeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRstpPortOperEdgeTrapState_Object = MibScalar
cienaCesRstpPortOperEdgeTrapState = _CienaCesRstpPortOperEdgeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 51),
    _CienaCesRstpPortOperEdgeTrapState_Type()
)
cienaCesRstpPortOperEdgeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRstpPortOperEdgeTrapState.setStatus("current")


class _CienaCesRstpPortFlapTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRstpPortFlapTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRstpPortFlapTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRstpPortFlapTrapState_Object = MibScalar
cienaCesRstpPortFlapTrapState = _CienaCesRstpPortFlapTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 52),
    _CienaCesRstpPortFlapTrapState_Type()
)
cienaCesRstpPortFlapTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRstpPortFlapTrapState.setStatus("current")


class _CienaCesRstpBridgeRootPortLostTrapState_Type(CienaGlobalState):
    """Custom type cienaCesRstpBridgeRootPortLostTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRstpBridgeRootPortLostTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesRstpBridgeRootPortLostTrapState_Object = MibScalar
cienaCesRstpBridgeRootPortLostTrapState = _CienaCesRstpBridgeRootPortLostTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 53),
    _CienaCesRstpBridgeRootPortLostTrapState_Type()
)
cienaCesRstpBridgeRootPortLostTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRstpBridgeRootPortLostTrapState.setStatus("current")


class _CienaCesFeatureLicenseStatusTrapState_Type(CienaGlobalState):
    """Custom type cienaCesFeatureLicenseStatusTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesFeatureLicenseStatusTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesFeatureLicenseStatusTrapState_Object = MibScalar
cienaCesFeatureLicenseStatusTrapState = _CienaCesFeatureLicenseStatusTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 54),
    _CienaCesFeatureLicenseStatusTrapState_Type()
)
cienaCesFeatureLicenseStatusTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesFeatureLicenseStatusTrapState.setStatus("current")


class _CienaCesFeatureLicenseInstallErrorTrapState_Type(CienaGlobalState):
    """Custom type cienaCesFeatureLicenseInstallErrorTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesFeatureLicenseInstallErrorTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesFeatureLicenseInstallErrorTrapState_Object = MibScalar
cienaCesFeatureLicenseInstallErrorTrapState = _CienaCesFeatureLicenseInstallErrorTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 55),
    _CienaCesFeatureLicenseInstallErrorTrapState_Type()
)
cienaCesFeatureLicenseInstallErrorTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesFeatureLicenseInstallErrorTrapState.setStatus("current")


class _CienaCesFileTransferCompletionTrapState_Type(CienaGlobalState):
    """Custom type cienaCesFileTransferCompletionTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesFileTransferCompletionTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesFileTransferCompletionTrapState_Object = MibScalar
cienaCesFileTransferCompletionTrapState = _CienaCesFileTransferCompletionTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 56),
    _CienaCesFileTransferCompletionTrapState_Type()
)
cienaCesFileTransferCompletionTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesFileTransferCompletionTrapState.setStatus("current")


class _CienaCesSwXgradeCompletionTrapState_Type(CienaGlobalState):
    """Custom type cienaCesSwXgradeCompletionTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesSwXgradeCompletionTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesSwXgradeCompletionTrapState_Object = MibScalar
cienaCesSwXgradeCompletionTrapState = _CienaCesSwXgradeCompletionTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 57),
    _CienaCesSwXgradeCompletionTrapState_Type()
)
cienaCesSwXgradeCompletionTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesSwXgradeCompletionTrapState.setStatus("current")


class _CienaCesSystemConfigImproperCmdTrapState_Type(CienaGlobalState):
    """Custom type cienaCesSystemConfigImproperCmdTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesSystemConfigImproperCmdTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesSystemConfigImproperCmdTrapState_Object = MibScalar
cienaCesSystemConfigImproperCmdTrapState = _CienaCesSystemConfigImproperCmdTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 58),
    _CienaCesSystemConfigImproperCmdTrapState_Type()
)
cienaCesSystemConfigImproperCmdTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesSystemConfigImproperCmdTrapState.setStatus("current")


class _CienaCesOamLinkEventTrapState_Type(CienaGlobalState):
    """Custom type cienaCesOamLinkEventTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesOamLinkEventTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesOamLinkEventTrapState_Object = MibScalar
cienaCesOamLinkEventTrapState = _CienaCesOamLinkEventTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 59),
    _CienaCesOamLinkEventTrapState_Type()
)
cienaCesOamLinkEventTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesOamLinkEventTrapState.setStatus("current")


class _CienaCesCfmDelayVariationFaultTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCfmDelayVariationFaultTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmDelayVariationFaultTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmDelayVariationFaultTrapState_Object = MibScalar
cienaCesCfmDelayVariationFaultTrapState = _CienaCesCfmDelayVariationFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 60),
    _CienaCesCfmDelayVariationFaultTrapState_Type()
)
cienaCesCfmDelayVariationFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmDelayVariationFaultTrapState.setStatus("current")


class _CienaCesIOMStateChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIOMStateChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIOMStateChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIOMStateChangeTrapState_Object = MibScalar
cienaCesIOMStateChangeTrapState = _CienaCesIOMStateChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 61),
    _CienaCesIOMStateChangeTrapState_Type()
)
cienaCesIOMStateChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIOMStateChangeTrapState.setStatus("current")


class _CienaCesIOMBuzzerEnableChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIOMBuzzerEnableChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIOMBuzzerEnableChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIOMBuzzerEnableChangeTrapState_Object = MibScalar
cienaCesIOMBuzzerEnableChangeTrapState = _CienaCesIOMBuzzerEnableChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 62),
    _CienaCesIOMBuzzerEnableChangeTrapState_Type()
)
cienaCesIOMBuzzerEnableChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIOMBuzzerEnableChangeTrapState.setStatus("current")


class _CienaCesIOMBuzzerStateChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIOMBuzzerStateChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIOMBuzzerStateChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIOMBuzzerStateChangeTrapState_Object = MibScalar
cienaCesIOMBuzzerStateChangeTrapState = _CienaCesIOMBuzzerStateChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 63),
    _CienaCesIOMBuzzerStateChangeTrapState_Type()
)
cienaCesIOMBuzzerStateChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIOMBuzzerStateChangeTrapState.setStatus("current")


class _CienaCesIOMAlarmOutputStateChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIOMAlarmOutputStateChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIOMAlarmOutputStateChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIOMAlarmOutputStateChangeTrapState_Object = MibScalar
cienaCesIOMAlarmOutputStateChangeTrapState = _CienaCesIOMAlarmOutputStateChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 64),
    _CienaCesIOMAlarmOutputStateChangeTrapState_Type()
)
cienaCesIOMAlarmOutputStateChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIOMAlarmOutputStateChangeTrapState.setStatus("current")


class _CienaCesIOMAlarmInputStateChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesIOMAlarmInputStateChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIOMAlarmInputStateChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesIOMAlarmInputStateChangeTrapState_Object = MibScalar
cienaCesIOMAlarmInputStateChangeTrapState = _CienaCesIOMAlarmInputStateChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 65),
    _CienaCesIOMAlarmInputStateChangeTrapState_Type()
)
cienaCesIOMAlarmInputStateChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesIOMAlarmInputStateChangeTrapState.setStatus("current")


class _CienaCesChassisUsbFlashEnableChangeTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisUsbFlashEnableChangeTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisUsbFlashEnableChangeTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisUsbFlashEnableChangeTrapState_Object = MibScalar
cienaCesChassisUsbFlashEnableChangeTrapState = _CienaCesChassisUsbFlashEnableChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 66),
    _CienaCesChassisUsbFlashEnableChangeTrapState_Type()
)
cienaCesChassisUsbFlashEnableChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashEnableChangeTrapState.setStatus("current")


class _CienaCesChassisAirFilterTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisAirFilterTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisAirFilterTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisAirFilterTrapState_Object = MibScalar
cienaCesChassisAirFilterTrapState = _CienaCesChassisAirFilterTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 67),
    _CienaCesChassisAirFilterTrapState_Type()
)
cienaCesChassisAirFilterTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisAirFilterTrapState.setStatus("current")


class _CienaCesSyncInputProtectionUnitTrapState_Type(CienaGlobalState):
    """Custom type cienaCesSyncInputProtectionUnitTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesSyncInputProtectionUnitTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesSyncInputProtectionUnitTrapState_Object = MibScalar
cienaCesSyncInputProtectionUnitTrapState = _CienaCesSyncInputProtectionUnitTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 68),
    _CienaCesSyncInputProtectionUnitTrapState_Type()
)
cienaCesSyncInputProtectionUnitTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionUnitTrapState.setStatus("current")


class _CienaCesSyncInputProtectionGroupTrapState_Type(CienaGlobalState):
    """Custom type cienaCesSyncInputProtectionGroupTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesSyncInputProtectionGroupTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesSyncInputProtectionGroupTrapState_Object = MibScalar
cienaCesSyncInputProtectionGroupTrapState = _CienaCesSyncInputProtectionGroupTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 69),
    _CienaCesSyncInputProtectionGroupTrapState_Type()
)
cienaCesSyncInputProtectionGroupTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupTrapState.setStatus("current")


class _CienaCesSyncModuleSlotTrapState_Type(CienaGlobalState):
    """Custom type cienaCesSyncModuleSlotTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesSyncModuleSlotTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesSyncModuleSlotTrapState_Object = MibScalar
cienaCesSyncModuleSlotTrapState = _CienaCesSyncModuleSlotTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 70),
    _CienaCesSyncModuleSlotTrapState_Type()
)
cienaCesSyncModuleSlotTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesSyncModuleSlotTrapState.setStatus("current")


class _CienaCesChassisAlarmCutoffTrapState_Type(CienaGlobalState):
    """Custom type cienaCesChassisAlarmCutoffTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesChassisAlarmCutoffTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesChassisAlarmCutoffTrapState_Object = MibScalar
cienaCesChassisAlarmCutoffTrapState = _CienaCesChassisAlarmCutoffTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 71),
    _CienaCesChassisAlarmCutoffTrapState_Type()
)
cienaCesChassisAlarmCutoffTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisAlarmCutoffTrapState.setStatus("current")


class _CienaCesDataplanePortShapingSubscriptionTrapState_Type(CienaGlobalState):
    """Custom type cienaCesDataplanePortShapingSubscriptionTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesDataplanePortShapingSubscriptionTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesDataplanePortShapingSubscriptionTrapState_Object = MibScalar
cienaCesDataplanePortShapingSubscriptionTrapState = _CienaCesDataplanePortShapingSubscriptionTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 72),
    _CienaCesDataplanePortShapingSubscriptionTrapState_Type()
)
cienaCesDataplanePortShapingSubscriptionTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDataplanePortShapingSubscriptionTrapState.setStatus("current")


class _CienaCesPortXcvrUncertifiedTrapState_Type(CienaGlobalState):
    """Custom type cienaCesPortXcvrUncertifiedTrapState based on CienaGlobalState"""
    defaultValue = 2


_CienaCesPortXcvrUncertifiedTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesPortXcvrUncertifiedTrapState_Object = MibScalar
cienaCesPortXcvrUncertifiedTrapState = _CienaCesPortXcvrUncertifiedTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 73),
    _CienaCesPortXcvrUncertifiedTrapState_Type()
)
cienaCesPortXcvrUncertifiedTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesPortXcvrUncertifiedTrapState.setStatus("current")


class _CienaCesCommandFileCompletedTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCommandFileCompletedTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCommandFileCompletedTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCommandFileCompletedTrapState_Object = MibScalar
cienaCesCommandFileCompletedTrapState = _CienaCesCommandFileCompletedTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 74),
    _CienaCesCommandFileCompletedTrapState_Type()
)
cienaCesCommandFileCompletedTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCommandFileCompletedTrapState.setStatus("current")


class _CienaCesCommandFileFailedTrapState_Type(CienaGlobalState):
    """Custom type cienaCesCommandFileFailedTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCommandFileFailedTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesCommandFileFailedTrapState_Object = MibScalar
cienaCesCommandFileFailedTrapState = _CienaCesCommandFileFailedTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1, 1, 1, 75),
    _CienaCesCommandFileFailedTrapState_Type()
)
cienaCesCommandFileFailedTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCommandFileFailedTrapState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-NOTIFICATIONS-CONTROL",
    **{"cienaCesNotificationsControlMIB": cienaCesNotificationsControlMIB,
       "cienaCesNotificationsControl": cienaCesNotificationsControl,
       "cienaCesPortEnhancedLinkTrapState": cienaCesPortEnhancedLinkTrapState,
       "cienaCesPortStdLinkTrapState": cienaCesPortStdLinkTrapState,
       "cienaCesPortAllTrapState": cienaCesPortAllTrapState,
       "cienaCesModuleAllModulesTrapState": cienaCesModuleAllModulesTrapState,
       "cienaCesModuleAllModulesHealthTrapState": cienaCesModuleAllModulesHealthTrapState,
       "cienaCesModuleSensorTrapState": cienaCesModuleSensorTrapState,
       "cienaCesModuleHATrapState": cienaCesModuleHATrapState,
       "cienaCesModuleProtectionModeTrapState": cienaCesModuleProtectionModeTrapState,
       "cienaCesModulePOSTErrorTrapState": cienaCesModulePOSTErrorTrapState,
       "cienaCesModuleSwitchFabricDisruptedTrapState": cienaCesModuleSwitchFabricDisruptedTrapState,
       "cienaCesChassisAllPowerSupplyTrapState": cienaCesChassisAllPowerSupplyTrapState,
       "cienaCesChassisAllFanTrapState": cienaCesChassisAllFanTrapState,
       "cienaCesChassisAllFanTrayTrapState": cienaCesChassisAllFanTrayTrapState,
       "cienaCesChassisAllFanTempTrapState": cienaCesChassisAllFanTempTrapState,
       "cienaCesChassisHealthTrapState": cienaCesChassisHealthTrapState,
       "cienaCesRapsAlarmTrapState": cienaCesRapsAlarmTrapState,
       "cienaCesMplsTrapState": cienaCesMplsTrapState,
       "cienaCesCfmFaultTrapState": cienaCesCfmFaultTrapState,
       "cienaCesCfmDelayFaultTrapState": cienaCesCfmDelayFaultTrapState,
       "cienaCesCfmJitterFaultTrapState": cienaCesCfmJitterFaultTrapState,
       "cienaCesCfmFrameLossNearFaultTrapState": cienaCesCfmFrameLossNearFaultTrapState,
       "cienaCesCfmFrameLossFarFaultTrapState": cienaCesCfmFrameLossFarFaultTrapState,
       "cienaCesCfmSyntheticLossNearFaultTrapState": cienaCesCfmSyntheticLossNearFaultTrapState,
       "cienaCesCfmSyntheticLossFarFaultTrapState": cienaCesCfmSyntheticLossFarFaultTrapState,
       "cienaCesPbtFaultTrapState": cienaCesPbtFaultTrapState,
       "cienaCesBfdTrapState": cienaCesBfdTrapState,
       "cienaCesIPMgmtInterfaceAddrChangeTrapState": cienaCesIPMgmtInterfaceAddrChangeTrapState,
       "cienaCesIPMgmtInterfaceGatewayAddrChangeTrapState": cienaCesIPMgmtInterfaceGatewayAddrChangeTrapState,
       "cienaCesDataplaneUcastTrapState": cienaCesDataplaneUcastTrapState,
       "cienaCesDataplaneBcastTrapState": cienaCesDataplaneBcastTrapState,
       "cienaCesDataplaneMcastTrapState": cienaCesDataplaneMcastTrapState,
       "cienaCesPortXcvrLinkStateChangeTrapState": cienaCesPortXcvrLinkStateChangeTrapState,
       "cienaCesPortXcvrErrorTrapState": cienaCesPortXcvrErrorTrapState,
       "cienaCesPortXcvrTempChangeTrapState": cienaCesPortXcvrTempChangeTrapState,
       "cienaCesPortXcvrVoltageChangeTrapState": cienaCesPortXcvrVoltageChangeTrapState,
       "cienaCesPortXcvrBiasChangeTrapState": cienaCesPortXcvrBiasChangeTrapState,
       "cienaCesPortXcvrTxPowerChangeTrapState": cienaCesPortXcvrTxPowerChangeTrapState,
       "cienaCesPortXcvrRxPowerChangeTrapState": cienaCesPortXcvrRxPowerChangeTrapState,
       "cienaCesPortXcvrSpeedInfoTrapState": cienaCesPortXcvrSpeedInfoTrapState,
       "cienaCesRstpPortBackupTrapState": cienaCesRstpPortBackupTrapState,
       "cienaCesRstpPortPvstBPduReceivedTrapState": cienaCesRstpPortPvstBPduReceivedTrapState,
       "cienaCesRstpPortSelfLoopTrapState": cienaCesRstpPortSelfLoopTrapState,
       "cienaCesRstpPortOperEdgeTrapState": cienaCesRstpPortOperEdgeTrapState,
       "cienaCesRstpPortFlapTrapState": cienaCesRstpPortFlapTrapState,
       "cienaCesRstpBridgeRootPortLostTrapState": cienaCesRstpBridgeRootPortLostTrapState,
       "cienaCesFeatureLicenseStatusTrapState": cienaCesFeatureLicenseStatusTrapState,
       "cienaCesFeatureLicenseInstallErrorTrapState": cienaCesFeatureLicenseInstallErrorTrapState,
       "cienaCesFileTransferCompletionTrapState": cienaCesFileTransferCompletionTrapState,
       "cienaCesSwXgradeCompletionTrapState": cienaCesSwXgradeCompletionTrapState,
       "cienaCesSystemConfigImproperCmdTrapState": cienaCesSystemConfigImproperCmdTrapState,
       "cienaCesOamLinkEventTrapState": cienaCesOamLinkEventTrapState,
       "cienaCesCfmDelayVariationFaultTrapState": cienaCesCfmDelayVariationFaultTrapState,
       "cienaCesIOMStateChangeTrapState": cienaCesIOMStateChangeTrapState,
       "cienaCesIOMBuzzerEnableChangeTrapState": cienaCesIOMBuzzerEnableChangeTrapState,
       "cienaCesIOMBuzzerStateChangeTrapState": cienaCesIOMBuzzerStateChangeTrapState,
       "cienaCesIOMAlarmOutputStateChangeTrapState": cienaCesIOMAlarmOutputStateChangeTrapState,
       "cienaCesIOMAlarmInputStateChangeTrapState": cienaCesIOMAlarmInputStateChangeTrapState,
       "cienaCesChassisUsbFlashEnableChangeTrapState": cienaCesChassisUsbFlashEnableChangeTrapState,
       "cienaCesChassisAirFilterTrapState": cienaCesChassisAirFilterTrapState,
       "cienaCesSyncInputProtectionUnitTrapState": cienaCesSyncInputProtectionUnitTrapState,
       "cienaCesSyncInputProtectionGroupTrapState": cienaCesSyncInputProtectionGroupTrapState,
       "cienaCesSyncModuleSlotTrapState": cienaCesSyncModuleSlotTrapState,
       "cienaCesChassisAlarmCutoffTrapState": cienaCesChassisAlarmCutoffTrapState,
       "cienaCesDataplanePortShapingSubscriptionTrapState": cienaCesDataplanePortShapingSubscriptionTrapState,
       "cienaCesPortXcvrUncertifiedTrapState": cienaCesPortXcvrUncertifiedTrapState,
       "cienaCesCommandFileCompletedTrapState": cienaCesCommandFileCompletedTrapState,
       "cienaCesCommandFileFailedTrapState": cienaCesCommandFileFailedTrapState}
)
