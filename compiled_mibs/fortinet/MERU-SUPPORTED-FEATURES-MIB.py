# SNMP MIB module (MERU-SUPPORTED-FEATURES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-SUPPORTED-FEATURES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:16 2025
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

(MwlIpProxyType,
 MwlOnOffSwitch) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlIpProxyType",
    "MwlOnOffSwitch")

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

mwSupportedFeatures = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwSupport_ObjectIdentity = ObjectIdentity
mwSupport = _MwSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1)
)
_MwSupportChannelDomainCheck_Type = MwlOnOffSwitch
_MwSupportChannelDomainCheck_Object = MibScalar
mwSupportChannelDomainCheck = _MwSupportChannelDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 1),
    _MwSupportChannelDomainCheck_Type()
)
mwSupportChannelDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSupportChannelDomainCheck.setStatus("current")
_MwSupportLicensingMgmt_Type = MwlOnOffSwitch
_MwSupportLicensingMgmt_Object = MibScalar
mwSupportLicensingMgmt = _MwSupportLicensingMgmt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 2),
    _MwSupportLicensingMgmt_Type()
)
mwSupportLicensingMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSupportLicensingMgmt.setStatus("current")
_MwSupportSipProxy_Type = MwlIpProxyType
_MwSupportSipProxy_Object = MibScalar
mwSupportSipProxy = _MwSupportSipProxy_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 3),
    _MwSupportSipProxy_Type()
)
mwSupportSipProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSupportSipProxy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-SUPPORTED-FEATURES-MIB",
    **{"mwSupportedFeatures": mwSupportedFeatures,
       "mwSupport": mwSupport,
       "mwSupportChannelDomainCheck": mwSupportChannelDomainCheck,
       "mwSupportLicensingMgmt": mwSupportLicensingMgmt,
       "mwSupportSipProxy": mwSupportSipProxy}
)
