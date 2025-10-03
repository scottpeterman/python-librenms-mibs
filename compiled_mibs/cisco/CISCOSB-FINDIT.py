# SNMP MIB module (CISCOSB-FINDIT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-FINDIT
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:44 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlFindit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235)
)
if mibBuilder.loadTexts:
    rlFindit.setRevisions(
        ("2021-05-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlFinditState_Type(Integer32):
    """Custom type rlFinditState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlFinditState_Type.__name__ = "Integer32"
_RlFinditState_Object = MibScalar
rlFinditState = _RlFinditState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 1),
    _RlFinditState_Type()
)
rlFinditState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditState.setStatus("current")


class _RlFinditOperState_Type(Integer32):
    """Custom type rlFinditOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlFinditOperState_Type.__name__ = "Integer32"
_RlFinditOperState_Object = MibScalar
rlFinditOperState = _RlFinditOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 2),
    _RlFinditOperState_Type()
)
rlFinditOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFinditOperState.setStatus("current")
_RlFinditTable_Object = MibTable
rlFinditTable = _RlFinditTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3)
)
if mibBuilder.loadTexts:
    rlFinditTable.setStatus("current")
_RlFinditTableEntry_Object = MibTableRow
rlFinditTableEntry = _RlFinditTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1)
)
rlFinditTableEntry.setIndexNames(
    (0, "CISCOSB-FINDIT", "rlApplication"),
)
if mibBuilder.loadTexts:
    rlFinditTableEntry.setStatus("current")


class _RlApplication_Type(Integer32):
    """Custom type rlApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlApplication_Type.__name__ = "Integer32"
_RlApplication_Object = MibTableColumn
rlApplication = _RlApplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 1),
    _RlApplication_Type()
)
rlApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlApplication.setStatus("current")


class _RlFinditOrganization_Type(DisplayString):
    """Custom type rlFinditOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlFinditOrganization_Type.__name__ = "DisplayString"
_RlFinditOrganization_Object = MibTableColumn
rlFinditOrganization = _RlFinditOrganization_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 2),
    _RlFinditOrganization_Type()
)
rlFinditOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditOrganization.setStatus("current")


class _RlFinditNetwork_Type(DisplayString):
    """Custom type rlFinditNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlFinditNetwork_Type.__name__ = "DisplayString"
_RlFinditNetwork_Object = MibTableColumn
rlFinditNetwork = _RlFinditNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 3),
    _RlFinditNetwork_Type()
)
rlFinditNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditNetwork.setStatus("current")
_RlFinditInetAddress_Type = InetAddress
_RlFinditInetAddress_Object = MibTableColumn
rlFinditInetAddress = _RlFinditInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 4),
    _RlFinditInetAddress_Type()
)
rlFinditInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditInetAddress.setStatus("current")


class _RlFinditManagerPort_Type(Integer32):
    """Custom type rlFinditManagerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlFinditManagerPort_Type.__name__ = "Integer32"
_RlFinditManagerPort_Object = MibTableColumn
rlFinditManagerPort = _RlFinditManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 5),
    _RlFinditManagerPort_Type()
)
rlFinditManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditManagerPort.setStatus("current")


class _RlFinditManagerKeyId_Type(DisplayString):
    """Custom type rlFinditManagerKeyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RlFinditManagerKeyId_Type.__name__ = "DisplayString"
_RlFinditManagerKeyId_Object = MibTableColumn
rlFinditManagerKeyId = _RlFinditManagerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 6),
    _RlFinditManagerKeyId_Type()
)
rlFinditManagerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditManagerKeyId.setStatus("current")


class _RlFinditManagerSecret_Type(DisplayString):
    """Custom type rlFinditManagerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlFinditManagerSecret_Type.__name__ = "DisplayString"
_RlFinditManagerSecret_Object = MibTableColumn
rlFinditManagerSecret = _RlFinditManagerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 7),
    _RlFinditManagerSecret_Type()
)
rlFinditManagerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditManagerSecret.setStatus("current")


class _RlFinditVersion_Type(DisplayString):
    """Custom type rlFinditVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlFinditVersion_Type.__name__ = "DisplayString"
_RlFinditVersion_Object = MibTableColumn
rlFinditVersion = _RlFinditVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 8),
    _RlFinditVersion_Type()
)
rlFinditVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditVersion.setStatus("current")


class _RlFinditManagerConnection_Type(Integer32):
    """Custom type rlFinditManagerConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlFinditManagerConnection_Type.__name__ = "Integer32"
_RlFinditManagerConnection_Object = MibTableColumn
rlFinditManagerConnection = _RlFinditManagerConnection_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 3, 1, 9),
    _RlFinditManagerConnection_Type()
)
rlFinditManagerConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditManagerConnection.setStatus("current")


class _RlFinditManagerReconnect_Type(Integer32):
    """Custom type rlFinditManagerReconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renew", 1))
    )


_RlFinditManagerReconnect_Type.__name__ = "Integer32"
_RlFinditManagerReconnect_Object = MibScalar
rlFinditManagerReconnect = _RlFinditManagerReconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 4),
    _RlFinditManagerReconnect_Type()
)
rlFinditManagerReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditManagerReconnect.setStatus("current")


class _RlFinditManagerConnectionOpertional_Type(Integer32):
    """Custom type rlFinditManagerConnectionOpertional based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlFinditManagerConnectionOpertional_Type.__name__ = "Integer32"
_RlFinditManagerConnectionOpertional_Object = MibScalar
rlFinditManagerConnectionOpertional = _RlFinditManagerConnectionOpertional_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 5),
    _RlFinditManagerConnectionOpertional_Type()
)
rlFinditManagerConnectionOpertional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFinditManagerConnectionOpertional.setStatus("current")


class _RlFinditProbeErrorReportAction_Type(Integer32):
    """Custom type rlFinditProbeErrorReportAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("disableAndSyslog", 1))
    )


_RlFinditProbeErrorReportAction_Type.__name__ = "Integer32"
_RlFinditProbeErrorReportAction_Object = MibScalar
rlFinditProbeErrorReportAction = _RlFinditProbeErrorReportAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 6),
    _RlFinditProbeErrorReportAction_Type()
)
rlFinditProbeErrorReportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditProbeErrorReportAction.setStatus("current")
_RlFinditProbeMemoryClear_Type = TruthValue
_RlFinditProbeMemoryClear_Object = MibScalar
rlFinditProbeMemoryClear = _RlFinditProbeMemoryClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 235, 7),
    _RlFinditProbeMemoryClear_Type()
)
rlFinditProbeMemoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFinditProbeMemoryClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-FINDIT",
    **{"rlFindit": rlFindit,
       "rlFinditState": rlFinditState,
       "rlFinditOperState": rlFinditOperState,
       "rlFinditTable": rlFinditTable,
       "rlFinditTableEntry": rlFinditTableEntry,
       "rlApplication": rlApplication,
       "rlFinditOrganization": rlFinditOrganization,
       "rlFinditNetwork": rlFinditNetwork,
       "rlFinditInetAddress": rlFinditInetAddress,
       "rlFinditManagerPort": rlFinditManagerPort,
       "rlFinditManagerKeyId": rlFinditManagerKeyId,
       "rlFinditManagerSecret": rlFinditManagerSecret,
       "rlFinditVersion": rlFinditVersion,
       "rlFinditManagerConnection": rlFinditManagerConnection,
       "rlFinditManagerReconnect": rlFinditManagerReconnect,
       "rlFinditManagerConnectionOpertional": rlFinditManagerConnectionOpertional,
       "rlFinditProbeErrorReportAction": rlFinditProbeErrorReportAction,
       "rlFinditProbeMemoryClear": rlFinditProbeMemoryClear}
)
