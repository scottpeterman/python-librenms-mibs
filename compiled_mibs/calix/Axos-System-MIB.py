# SNMP MIB module (Axos-System-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\Axos-System-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:47 2025
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

(axosModules,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "axosModules")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

axosSystemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    axosSystemModule.setRevisions(
        ("2020-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxosSystemId_Type = OctetString
_AxosSystemId_Object = MibScalar
axosSystemId = _AxosSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 1),
    _AxosSystemId_Type()
)
axosSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemId.setStatus("current")
_AxosSystemLocation_Type = OctetString
_AxosSystemLocation_Object = MibScalar
axosSystemLocation = _AxosSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 2),
    _AxosSystemLocation_Type()
)
axosSystemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemLocation.setStatus("current")


class _AxosSystemAutoUpgrade_Type(Integer32):
    """Custom type axosSystemAutoUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AxosSystemAutoUpgrade_Type.__name__ = "Integer32"
_AxosSystemAutoUpgrade_Object = MibScalar
axosSystemAutoUpgrade = _AxosSystemAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 3),
    _AxosSystemAutoUpgrade_Type()
)
axosSystemAutoUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemAutoUpgrade.setStatus("current")


class _AxosSystemTelnetServer_Type(Integer32):
    """Custom type axosSystemTelnetServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AxosSystemTelnetServer_Type.__name__ = "Integer32"
_AxosSystemTelnetServer_Object = MibScalar
axosSystemTelnetServer = _AxosSystemTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 4),
    _AxosSystemTelnetServer_Type()
)
axosSystemTelnetServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemTelnetServer.setStatus("current")


class _AxosSystemUnsecuredWeb_Type(Integer32):
    """Custom type axosSystemUnsecuredWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AxosSystemUnsecuredWeb_Type.__name__ = "Integer32"
_AxosSystemUnsecuredWeb_Object = MibScalar
axosSystemUnsecuredWeb = _AxosSystemUnsecuredWeb_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 5),
    _AxosSystemUnsecuredWeb_Type()
)
axosSystemUnsecuredWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemUnsecuredWeb.setStatus("current")
_AxosSystemPasswordExpiry_Type = Integer32
_AxosSystemPasswordExpiry_Object = MibScalar
axosSystemPasswordExpiry = _AxosSystemPasswordExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 6),
    _AxosSystemPasswordExpiry_Type()
)
axosSystemPasswordExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemPasswordExpiry.setStatus("current")
_AxosSystemDnsPrimary_Type = IpAddress
_AxosSystemDnsPrimary_Object = MibScalar
axosSystemDnsPrimary = _AxosSystemDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 7),
    _AxosSystemDnsPrimary_Type()
)
axosSystemDnsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemDnsPrimary.setStatus("current")
_AxosSystemDnsSecondary_Type = IpAddress
_AxosSystemDnsSecondary_Object = MibScalar
axosSystemDnsSecondary = _AxosSystemDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 8),
    _AxosSystemDnsSecondary_Type()
)
axosSystemDnsSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemDnsSecondary.setStatus("current")
_AxosSystemTimezone_Type = OctetString
_AxosSystemTimezone_Object = MibScalar
axosSystemTimezone = _AxosSystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 9),
    _AxosSystemTimezone_Type()
)
axosSystemTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemTimezone.setStatus("current")
_AxosSystemChassisSerialNumber_Type = OctetString
_AxosSystemChassisSerialNumber_Object = MibScalar
axosSystemChassisSerialNumber = _AxosSystemChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 10),
    _AxosSystemChassisSerialNumber_Type()
)
axosSystemChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemChassisSerialNumber.setStatus("current")
_AxosSystemChassisMacAddress_Type = OctetString
_AxosSystemChassisMacAddress_Object = MibScalar
axosSystemChassisMacAddress = _AxosSystemChassisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 11),
    _AxosSystemChassisMacAddress_Type()
)
axosSystemChassisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemChassisMacAddress.setStatus("current")
_AxosSystemTime_Type = DisplayString
_AxosSystemTime_Object = MibScalar
axosSystemTime = _AxosSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 12),
    _AxosSystemTime_Type()
)
axosSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemTime.setStatus("current")
_AxosSystemDate_Type = DisplayString
_AxosSystemDate_Object = MibScalar
axosSystemDate = _AxosSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 5, 13),
    _AxosSystemDate_Type()
)
axosSystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosSystemDate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Axos-System-MIB",
    **{"axosSystemModule": axosSystemModule,
       "axosSystemId": axosSystemId,
       "axosSystemLocation": axosSystemLocation,
       "axosSystemAutoUpgrade": axosSystemAutoUpgrade,
       "axosSystemTelnetServer": axosSystemTelnetServer,
       "axosSystemUnsecuredWeb": axosSystemUnsecuredWeb,
       "axosSystemPasswordExpiry": axosSystemPasswordExpiry,
       "axosSystemDnsPrimary": axosSystemDnsPrimary,
       "axosSystemDnsSecondary": axosSystemDnsSecondary,
       "axosSystemTimezone": axosSystemTimezone,
       "axosSystemChassisSerialNumber": axosSystemChassisSerialNumber,
       "axosSystemChassisMacAddress": axosSystemChassisMacAddress,
       "axosSystemTime": axosSystemTime,
       "axosSystemDate": axosSystemDate}
)
