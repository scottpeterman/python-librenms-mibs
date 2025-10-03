# SNMP MIB module (SIAE-PMFTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-PMFTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:13 2025
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(alarmTrap,) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "alarmTrap")

(equipIpSnmpAgentAddress,) = mibBuilder.importSymbols(
    "SIAE-EQUIP-MIB",
    "equipIpSnmpAgentAddress")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

(accessControlLoginIpAddress,) = mibBuilder.importSymbols(
    "SIAE-USER-MIB",
    "accessControlLoginIpAddress")

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

pmFTP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31)
)
if mibBuilder.loadTexts:
    pmFTP.setRevisions(
        ("2015-03-23 00:00",
         "2014-09-29 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PmFTPMibVersion_Type(Integer32):
    """Custom type pmFTPMibVersion based on Integer32"""
    defaultValue = 1


_PmFTPMibVersion_Type.__name__ = "Integer32"
_PmFTPMibVersion_Object = MibScalar
pmFTPMibVersion = _PmFTPMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 1),
    _PmFTPMibVersion_Type()
)
pmFTPMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFTPMibVersion.setStatus("current")


class _PmFTPfileName_Type(DisplayString):
    """Custom type pmFTPfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PmFTPfileName_Type.__name__ = "DisplayString"
_PmFTPfileName_Object = MibScalar
pmFTPfileName = _PmFTPfileName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 2),
    _PmFTPfileName_Type()
)
pmFTPfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPfileName.setStatus("current")
_PmFTPTpClass_Type = ObjectIdentifier
_PmFTPTpClass_Object = MibScalar
pmFTPTpClass = _PmFTPTpClass_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 3),
    _PmFTPTpClass_Type()
)
pmFTPTpClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPTpClass.setStatus("current")


class _PmFTPTpRmonOwner_Type(OwnerString):
    """Custom type pmFTPTpRmonOwner based on OwnerString"""
    defaultValue = OctetString("")


_PmFTPTpRmonOwner_Type.__name__ = "OwnerString"
_PmFTPTpRmonOwner_Object = MibScalar
pmFTPTpRmonOwner = _PmFTPTpRmonOwner_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 4),
    _PmFTPTpRmonOwner_Type()
)
pmFTPTpRmonOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPTpRmonOwner.setStatus("current")


class _PmFTPActionRequest_Type(Integer32):
    """Custom type pmFTPActionRequest based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dayBeforeRead", 1),
          ("currentDayRead", 3),
          ("readAll", 5),
          ("readAbort", 6),
          ("readInterval", 7))
    )


_PmFTPActionRequest_Type.__name__ = "Integer32"
_PmFTPActionRequest_Object = MibScalar
pmFTPActionRequest = _PmFTPActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 5),
    _PmFTPActionRequest_Type()
)
pmFTPActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPActionRequest.setStatus("current")


class _PmFTPStatus_Type(Integer32):
    """Custom type pmFTPStatus based on Integer32"""
    defaultValue = 2

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
        *(("transferring", 1),
          ("completed", 2),
          ("interrupted", 3),
          ("empty", 4),
          ("deleting", 5))
    )


_PmFTPStatus_Type.__name__ = "Integer32"
_PmFTPStatus_Object = MibScalar
pmFTPStatus = _PmFTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 6),
    _PmFTPStatus_Type()
)
pmFTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFTPStatus.setStatus("current")


class _PmFTPStatusTrapNotification_Type(Integer32):
    """Custom type pmFTPStatusTrapNotification based on Integer32"""
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


_PmFTPStatusTrapNotification_Type.__name__ = "Integer32"
_PmFTPStatusTrapNotification_Object = MibScalar
pmFTPStatusTrapNotification = _PmFTPStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 7),
    _PmFTPStatusTrapNotification_Type()
)
pmFTPStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPStatusTrapNotification.setStatus("current")


class _PmFTPCompressedFile_Type(Integer32):
    """Custom type pmFTPCompressedFile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PmFTPCompressedFile_Type.__name__ = "Integer32"
_PmFTPCompressedFile_Object = MibScalar
pmFTPCompressedFile = _PmFTPCompressedFile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 8),
    _PmFTPCompressedFile_Type()
)
pmFTPCompressedFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPCompressedFile.setStatus("current")


class _PmFTPBeginInterval_Type(Integer32):
    """Custom type pmFTPBeginInterval based on Integer32"""
    defaultValue = 0


_PmFTPBeginInterval_Type.__name__ = "Integer32"
_PmFTPBeginInterval_Object = MibScalar
pmFTPBeginInterval = _PmFTPBeginInterval_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 9),
    _PmFTPBeginInterval_Type()
)
pmFTPBeginInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPBeginInterval.setStatus("current")


class _PmFTPEndInterval_Type(Integer32):
    """Custom type pmFTPEndInterval based on Integer32"""
    defaultValue = 0


_PmFTPEndInterval_Type.__name__ = "Integer32"
_PmFTPEndInterval_Object = MibScalar
pmFTPEndInterval = _PmFTPEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 31, 10),
    _PmFTPEndInterval_Type()
)
pmFTPEndInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFTPEndInterval.setStatus("current")

# Managed Objects groups


# Notification objects

pmFTPStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3101)
)
pmFTPStatusTrap.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-PMFTP-MIB", "pmFTPStatus"),
        ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
)
if mibBuilder.loadTexts:
    pmFTPStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-PMFTP-MIB",
    **{"pmFTPStatusTrap": pmFTPStatusTrap,
       "pmFTP": pmFTP,
       "pmFTPMibVersion": pmFTPMibVersion,
       "pmFTPfileName": pmFTPfileName,
       "pmFTPTpClass": pmFTPTpClass,
       "pmFTPTpRmonOwner": pmFTPTpRmonOwner,
       "pmFTPActionRequest": pmFTPActionRequest,
       "pmFTPStatus": pmFTPStatus,
       "pmFTPStatusTrapNotification": pmFTPStatusTrapNotification,
       "pmFTPCompressedFile": pmFTPCompressedFile,
       "pmFTPBeginInterval": pmFTPBeginInterval,
       "pmFTPEndInterval": pmFTPEndInterval}
)
