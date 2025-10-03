# SNMP MIB module (STORMSHIELD-PROPERTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-PROPERTY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:12 2025
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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsProductProperty = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0)
)
if mibBuilder.loadTexts:
    snsProductProperty.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SnsModel_Type(DisplayString):
    """Custom type snsModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsModel_Type.__name__ = "DisplayString"
_SnsModel_Object = MibScalar
snsModel = _SnsModel_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 1),
    _SnsModel_Type()
)
snsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsModel.setStatus("current")


class _SnsVersion_Type(DisplayString):
    """Custom type snsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsVersion_Type.__name__ = "DisplayString"
_SnsVersion_Object = MibScalar
snsVersion = _SnsVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 2),
    _SnsVersion_Type()
)
snsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVersion.setStatus("current")


class _SnsSerialNumber_Type(DisplayString):
    """Custom type snsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSerialNumber_Type.__name__ = "DisplayString"
_SnsSerialNumber_Object = MibScalar
snsSerialNumber = _SnsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 3),
    _SnsSerialNumber_Type()
)
snsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSerialNumber.setStatus("current")


class _SnsSystemName_Type(DisplayString):
    """Custom type snsSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSystemName_Type.__name__ = "DisplayString"
_SnsSystemName_Object = MibScalar
snsSystemName = _SnsSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 4),
    _SnsSystemName_Type()
)
snsSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSystemName.setStatus("current")


class _SnsSystemLanguage_Type(DisplayString):
    """Custom type snsSystemLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSystemLanguage_Type.__name__ = "DisplayString"
_SnsSystemLanguage_Object = MibScalar
snsSystemLanguage = _SnsSystemLanguage_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 5),
    _SnsSystemLanguage_Type()
)
snsSystemLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSystemLanguage.setStatus("current")
_SnsNbEther_Type = Integer32
_SnsNbEther_Object = MibScalar
snsNbEther = _SnsNbEther_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 6),
    _SnsNbEther_Type()
)
snsNbEther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbEther.setStatus("current")
_SnsNbVlan_Type = Integer32
_SnsNbVlan_Object = MibScalar
snsNbVlan = _SnsNbVlan_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 7),
    _SnsNbVlan_Type()
)
snsNbVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbVlan.setStatus("current")
_SnsNbDialup_Type = Integer32
_SnsNbDialup_Object = MibScalar
snsNbDialup = _SnsNbDialup_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 8),
    _SnsNbDialup_Type()
)
snsNbDialup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbDialup.setStatus("current")
_SnsNbPPTP_Type = Integer32
_SnsNbPPTP_Object = MibScalar
snsNbPPTP = _SnsNbPPTP_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 9),
    _SnsNbPPTP_Type()
)
snsNbPPTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbPPTP.setStatus("current")
_SnsNbSerial_Type = Integer32
_SnsNbSerial_Object = MibScalar
snsNbSerial = _SnsNbSerial_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 10),
    _SnsNbSerial_Type()
)
snsNbSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbSerial.setStatus("current")
_SnsNbLoopback_Type = Integer32
_SnsNbLoopback_Object = MibScalar
snsNbLoopback = _SnsNbLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 11),
    _SnsNbLoopback_Type()
)
snsNbLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbLoopback.setStatus("current")
_SnsWatchdog_Type = Integer32
_SnsWatchdog_Object = MibScalar
snsWatchdog = _SnsWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 12),
    _SnsWatchdog_Type()
)
snsWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsWatchdog.setStatus("current")
_SnsLed_Type = Integer32
_SnsLed_Object = MibScalar
snsLed = _SnsLed_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 13),
    _SnsLed_Type()
)
snsLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsLed.setStatus("current")
_SnsClone_Type = Integer32
_SnsClone_Object = MibScalar
snsClone = _SnsClone_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 14),
    _SnsClone_Type()
)
snsClone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsClone.setStatus("current")
_SnsHADialup_Type = Integer32
_SnsHADialup_Object = MibScalar
snsHADialup = _SnsHADialup_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 15),
    _SnsHADialup_Type()
)
snsHADialup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHADialup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-PROPERTY-MIB",
    **{"snsProductProperty": snsProductProperty,
       "snsModel": snsModel,
       "snsVersion": snsVersion,
       "snsSerialNumber": snsSerialNumber,
       "snsSystemName": snsSystemName,
       "snsSystemLanguage": snsSystemLanguage,
       "snsNbEther": snsNbEther,
       "snsNbVlan": snsNbVlan,
       "snsNbDialup": snsNbDialup,
       "snsNbPPTP": snsNbPPTP,
       "snsNbSerial": snsNbSerial,
       "snsNbLoopback": snsNbLoopback,
       "snsWatchdog": snsWatchdog,
       "snsLed": snsLed,
       "snsClone": snsClone,
       "snsHADialup": snsHADialup}
)
