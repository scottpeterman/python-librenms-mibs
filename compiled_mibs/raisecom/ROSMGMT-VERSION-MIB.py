# SNMP MIB module (ROSMGMT-VERSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-VERSION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:09 2025
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

(rosMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "rosMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rosMgmtVersion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131)
)
if mibBuilder.loadTexts:
    rosMgmtVersion.setRevisions(
        ("2019-09-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RosMgmtVersionObjects_ObjectIdentity = ObjectIdentity
rosMgmtVersionObjects = _RosMgmtVersionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1)
)
_RosMgmtVersionScalarGroup_ObjectIdentity = ObjectIdentity
rosMgmtVersionScalarGroup = _RosMgmtVersionScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1)
)
_RosMgmtRosVersion_Type = OctetString
_RosMgmtRosVersion_Object = MibScalar
rosMgmtRosVersion = _RosMgmtRosVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 1),
    _RosMgmtRosVersion_Type()
)
rosMgmtRosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtRosVersion.setStatus("current")
_RosMgmtHardwareVersion_Type = OctetString
_RosMgmtHardwareVersion_Object = MibScalar
rosMgmtHardwareVersion = _RosMgmtHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 2),
    _RosMgmtHardwareVersion_Type()
)
rosMgmtHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtHardwareVersion.setStatus("current")
_RosMgmtBootstrapVersion_Type = OctetString
_RosMgmtBootstrapVersion_Object = MibScalar
rosMgmtBootstrapVersion = _RosMgmtBootstrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 3),
    _RosMgmtBootstrapVersion_Type()
)
rosMgmtBootstrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtBootstrapVersion.setStatus("current")
_RosMgmtSerialNumber_Type = OctetString
_RosMgmtSerialNumber_Object = MibScalar
rosMgmtSerialNumber = _RosMgmtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 4),
    _RosMgmtSerialNumber_Type()
)
rosMgmtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtSerialNumber.setStatus("current")
_RosMgmtFpgaVersion_Type = OctetString
_RosMgmtFpgaVersion_Object = MibScalar
rosMgmtFpgaVersion = _RosMgmtFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 5),
    _RosMgmtFpgaVersion_Type()
)
rosMgmtFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtFpgaVersion.setStatus("current")
_RosMgmtProductVersion_Type = OctetString
_RosMgmtProductVersion_Object = MibScalar
rosMgmtProductVersion = _RosMgmtProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 6),
    _RosMgmtProductVersion_Type()
)
rosMgmtProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProductVersion.setStatus("current")
_RosMgmtCmpAbName_Type = OctetString
_RosMgmtCmpAbName_Object = MibScalar
rosMgmtCmpAbName = _RosMgmtCmpAbName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 7),
    _RosMgmtCmpAbName_Type()
)
rosMgmtCmpAbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCmpAbName.setStatus("current")
_RosMgmtCmpFullName_Type = OctetString
_RosMgmtCmpFullName_Object = MibScalar
rosMgmtCmpFullName = _RosMgmtCmpFullName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 8),
    _RosMgmtCmpFullName_Type()
)
rosMgmtCmpFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCmpFullName.setStatus("current")
_RosMgmtDeviceName_Type = OctetString
_RosMgmtDeviceName_Object = MibScalar
rosMgmtDeviceName = _RosMgmtDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 9),
    _RosMgmtDeviceName_Type()
)
rosMgmtDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtDeviceName.setStatus("current")
_RosMgmtMacAddress_Type = MacAddress
_RosMgmtMacAddress_Object = MibScalar
rosMgmtMacAddress = _RosMgmtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 10),
    _RosMgmtMacAddress_Type()
)
rosMgmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtMacAddress.setStatus("current")
_RosMgmtSoftVersion_Type = OctetString
_RosMgmtSoftVersion_Object = MibScalar
rosMgmtSoftVersion = _RosMgmtSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 131, 1, 1, 11),
    _RosMgmtSoftVersion_Type()
)
rosMgmtSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtSoftVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-VERSION-MIB",
    **{"rosMgmtVersion": rosMgmtVersion,
       "rosMgmtVersionObjects": rosMgmtVersionObjects,
       "rosMgmtVersionScalarGroup": rosMgmtVersionScalarGroup,
       "rosMgmtRosVersion": rosMgmtRosVersion,
       "rosMgmtHardwareVersion": rosMgmtHardwareVersion,
       "rosMgmtBootstrapVersion": rosMgmtBootstrapVersion,
       "rosMgmtSerialNumber": rosMgmtSerialNumber,
       "rosMgmtFpgaVersion": rosMgmtFpgaVersion,
       "rosMgmtProductVersion": rosMgmtProductVersion,
       "rosMgmtCmpAbName": rosMgmtCmpAbName,
       "rosMgmtCmpFullName": rosMgmtCmpFullName,
       "rosMgmtDeviceName": rosMgmtDeviceName,
       "rosMgmtMacAddress": rosMgmtMacAddress,
       "rosMgmtSoftVersion": rosMgmtSoftVersion}
)
