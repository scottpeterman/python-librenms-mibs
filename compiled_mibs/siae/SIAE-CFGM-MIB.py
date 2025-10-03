# SNMP MIB module (SIAE-CFGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-CFGM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:43 2025
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

(alarmTrap,) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "alarmTrap")

(equipIpSnmpAgentAddress,) = mibBuilder.importSymbols(
    "SIAE-EQUIP-MIB",
    "equipIpSnmpAgentAddress")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

configManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30)
)
if mibBuilder.loadTexts:
    configManagement.setRevisions(
        ("2014-07-25 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ConfigManagementMibVersion_Type(Integer32):
    """Custom type configManagementMibVersion based on Integer32"""
    defaultValue = 1


_ConfigManagementMibVersion_Type.__name__ = "Integer32"
_ConfigManagementMibVersion_Object = MibScalar
configManagementMibVersion = _ConfigManagementMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 1),
    _ConfigManagementMibVersion_Type()
)
configManagementMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configManagementMibVersion.setStatus("current")


class _ConfigManagementFileName_Type(DisplayString):
    """Custom type configManagementFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigManagementFileName_Type.__name__ = "DisplayString"
_ConfigManagementFileName_Object = MibScalar
configManagementFileName = _ConfigManagementFileName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 2),
    _ConfigManagementFileName_Type()
)
configManagementFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configManagementFileName.setStatus("current")
_ConfigManagementServerIpAddress_Type = IpAddress
_ConfigManagementServerIpAddress_Object = MibScalar
configManagementServerIpAddress = _ConfigManagementServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 3),
    _ConfigManagementServerIpAddress_Type()
)
configManagementServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configManagementServerIpAddress.setStatus("current")


class _ConfigManagementAction_Type(Integer32):
    """Custom type configManagementAction based on Integer32"""
    defaultValue = 0

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
        *(("configNone", 0),
          ("configSave", 1),
          ("configUse", 2),
          ("configBack", 3),
          ("configAbort", 4),
          ("configUseAndSwitch", 5))
    )


_ConfigManagementAction_Type.__name__ = "Integer32"
_ConfigManagementAction_Object = MibScalar
configManagementAction = _ConfigManagementAction_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 4),
    _ConfigManagementAction_Type()
)
configManagementAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configManagementAction.setStatus("current")


class _ConfigManagementState_Type(Integer32):
    """Custom type configManagementState based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("configCompleted", 1),
          ("configInterrupted", 2),
          ("configVerifying", 3),
          ("configSaving", 4),
          ("configDownloading", 5),
          ("configUploading", 6),
          ("configUsing", 7),
          ("configMakingCopy", 8),
          ("configAborting", 9),
          ("configRestarting", 10),
          ("configStarted", 11))
    )


_ConfigManagementState_Type.__name__ = "Integer32"
_ConfigManagementState_Object = MibScalar
configManagementState = _ConfigManagementState_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 5),
    _ConfigManagementState_Type()
)
configManagementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configManagementState.setStatus("current")


class _ConfigManagementFailure_Type(Integer32):
    """Custom type configManagementFailure based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("configNoFailure", 0),
          ("configVerifying", 3),
          ("configSaving", 4),
          ("configDownloading", 5),
          ("configUploading", 6),
          ("configUsing", 7),
          ("configMakingCopy", 8),
          ("configAborted", 9))
    )


_ConfigManagementFailure_Type.__name__ = "Integer32"
_ConfigManagementFailure_Object = MibScalar
configManagementFailure = _ConfigManagementFailure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 6),
    _ConfigManagementFailure_Type()
)
configManagementFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configManagementFailure.setStatus("current")


class _ConfigManagementBackupFileDate_Type(Unsigned32):
    """Custom type configManagementBackupFileDate based on Unsigned32"""
    defaultValue = 0


_ConfigManagementBackupFileDate_Type.__name__ = "Unsigned32"
_ConfigManagementBackupFileDate_Object = MibScalar
configManagementBackupFileDate = _ConfigManagementBackupFileDate_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 7),
    _ConfigManagementBackupFileDate_Type()
)
configManagementBackupFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configManagementBackupFileDate.setStatus("current")


class _ConfigManagementTrapNotification_Type(Integer32):
    """Custom type configManagementTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2))
    )


_ConfigManagementTrapNotification_Type.__name__ = "Integer32"
_ConfigManagementTrapNotification_Object = MibScalar
configManagementTrapNotification = _ConfigManagementTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 30, 8),
    _ConfigManagementTrapNotification_Type()
)
configManagementTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configManagementTrapNotification.setStatus("current")

# Managed Objects groups


# Notification objects

configManagementFtpStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3001)
)
configManagementFtpStatusTrap.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-CFGM-MIB", "configManagementState"),
        ("SIAE-CFGM-MIB", "configManagementFailure"))
)
if mibBuilder.loadTexts:
    configManagementFtpStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-CFGM-MIB",
    **{"configManagementFtpStatusTrap": configManagementFtpStatusTrap,
       "configManagement": configManagement,
       "configManagementMibVersion": configManagementMibVersion,
       "configManagementFileName": configManagementFileName,
       "configManagementServerIpAddress": configManagementServerIpAddress,
       "configManagementAction": configManagementAction,
       "configManagementState": configManagementState,
       "configManagementFailure": configManagementFailure,
       "configManagementBackupFileDate": configManagementBackupFileDate,
       "configManagementTrapNotification": configManagementTrapNotification}
)
