# SNMP MIB module (AT-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-FLASH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:24 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

flash = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31)
)
if mibBuilder.loadTexts:
    flash.setRevisions(
        ("2006-06-28 12:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlashTrap_ObjectIdentity = ObjectIdentity
flashTrap = _FlashTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 0)
)
_FlashGetFailure_Type = Integer32
_FlashGetFailure_Object = MibScalar
flashGetFailure = _FlashGetFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 1),
    _FlashGetFailure_Type()
)
flashGetFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashGetFailure.setStatus("current")
_FlashOpenFailure_Type = Integer32
_FlashOpenFailure_Object = MibScalar
flashOpenFailure = _FlashOpenFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 2),
    _FlashOpenFailure_Type()
)
flashOpenFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashOpenFailure.setStatus("current")
_FlashReadFailure_Type = Integer32
_FlashReadFailure_Object = MibScalar
flashReadFailure = _FlashReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 3),
    _FlashReadFailure_Type()
)
flashReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashReadFailure.setStatus("current")
_FlashCloseFailure_Type = Integer32
_FlashCloseFailure_Object = MibScalar
flashCloseFailure = _FlashCloseFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 4),
    _FlashCloseFailure_Type()
)
flashCloseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCloseFailure.setStatus("current")
_FlashCompleteFailure_Type = Integer32
_FlashCompleteFailure_Object = MibScalar
flashCompleteFailure = _FlashCompleteFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 5),
    _FlashCompleteFailure_Type()
)
flashCompleteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCompleteFailure.setStatus("current")
_FlashWriteFailure_Type = Integer32
_FlashWriteFailure_Object = MibScalar
flashWriteFailure = _FlashWriteFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 6),
    _FlashWriteFailure_Type()
)
flashWriteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashWriteFailure.setStatus("current")
_FlashCreateFailure_Type = Integer32
_FlashCreateFailure_Object = MibScalar
flashCreateFailure = _FlashCreateFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 7),
    _FlashCreateFailure_Type()
)
flashCreateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCreateFailure.setStatus("current")
_FlashPutFailure_Type = Integer32
_FlashPutFailure_Object = MibScalar
flashPutFailure = _FlashPutFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 8),
    _FlashPutFailure_Type()
)
flashPutFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPutFailure.setStatus("current")
_FlashDeleteFailure_Type = Integer32
_FlashDeleteFailure_Object = MibScalar
flashDeleteFailure = _FlashDeleteFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 9),
    _FlashDeleteFailure_Type()
)
flashDeleteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeleteFailure.setStatus("current")
_FlashCheckFailure_Type = Integer32
_FlashCheckFailure_Object = MibScalar
flashCheckFailure = _FlashCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 10),
    _FlashCheckFailure_Type()
)
flashCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCheckFailure.setStatus("current")
_FlashEraseFailure_Type = Integer32
_FlashEraseFailure_Object = MibScalar
flashEraseFailure = _FlashEraseFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 11),
    _FlashEraseFailure_Type()
)
flashEraseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseFailure.setStatus("current")
_FlashCompactFailure_Type = Integer32
_FlashCompactFailure_Object = MibScalar
flashCompactFailure = _FlashCompactFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 12),
    _FlashCompactFailure_Type()
)
flashCompactFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCompactFailure.setStatus("current")
_FlashVerifyFailure_Type = Integer32
_FlashVerifyFailure_Object = MibScalar
flashVerifyFailure = _FlashVerifyFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 13),
    _FlashVerifyFailure_Type()
)
flashVerifyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVerifyFailure.setStatus("current")

# Managed Objects groups


# Notification objects

flashFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 0, 1)
)
flashFailureTrap.setObjects(
      *(("AT-FLASH-MIB", "flashGetFailure"),
        ("AT-FLASH-MIB", "flashOpenFailure"),
        ("AT-FLASH-MIB", "flashReadFailure"),
        ("AT-FLASH-MIB", "flashCloseFailure"),
        ("AT-FLASH-MIB", "flashCompleteFailure"),
        ("AT-FLASH-MIB", "flashWriteFailure"),
        ("AT-FLASH-MIB", "flashCreateFailure"),
        ("AT-FLASH-MIB", "flashPutFailure"),
        ("AT-FLASH-MIB", "flashDeleteFailure"),
        ("AT-FLASH-MIB", "flashCheckFailure"),
        ("AT-FLASH-MIB", "flashEraseFailure"),
        ("AT-FLASH-MIB", "flashCompactFailure"),
        ("AT-FLASH-MIB", "flashVerifyFailure"))
)
if mibBuilder.loadTexts:
    flashFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-FLASH-MIB",
    **{"flash": flash,
       "flashTrap": flashTrap,
       "flashFailureTrap": flashFailureTrap,
       "flashGetFailure": flashGetFailure,
       "flashOpenFailure": flashOpenFailure,
       "flashReadFailure": flashReadFailure,
       "flashCloseFailure": flashCloseFailure,
       "flashCompleteFailure": flashCompleteFailure,
       "flashWriteFailure": flashWriteFailure,
       "flashCreateFailure": flashCreateFailure,
       "flashPutFailure": flashPutFailure,
       "flashDeleteFailure": flashDeleteFailure,
       "flashCheckFailure": flashCheckFailure,
       "flashEraseFailure": flashEraseFailure,
       "flashCompactFailure": flashCompactFailure,
       "flashVerifyFailure": flashVerifyFailure}
)
