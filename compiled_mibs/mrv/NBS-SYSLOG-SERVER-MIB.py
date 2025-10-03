# SNMP MIB module (NBS-SYSLOG-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-SYSLOG-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:37 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsSyslogServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 206)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsSyslogServerGrp_ObjectIdentity = ObjectIdentity
nbsSyslogServerGrp = _NbsSyslogServerGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 206, 1)
)
if mibBuilder.loadTexts:
    nbsSyslogServerGrp.setStatus("current")
_NbsSyslogServerTableSize_Type = Integer32
_NbsSyslogServerTableSize_Object = MibScalar
nbsSyslogServerTableSize = _NbsSyslogServerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 1),
    _NbsSyslogServerTableSize_Type()
)
nbsSyslogServerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSyslogServerTableSize.setStatus("current")
_NbsSyslogServerTable_Object = MibTable
nbsSyslogServerTable = _NbsSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2)
)
if mibBuilder.loadTexts:
    nbsSyslogServerTable.setStatus("current")
_NbsSyslogServerEntry_Object = MibTableRow
nbsSyslogServerEntry = _NbsSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1)
)
nbsSyslogServerEntry.setIndexNames(
    (0, "NBS-SYSLOG-SERVER-MIB", "nbsSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    nbsSyslogServerEntry.setStatus("current")


class _NbsSyslogServerIndex_Type(Integer32):
    """Custom type nbsSyslogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NbsSyslogServerIndex_Type.__name__ = "Integer32"
_NbsSyslogServerIndex_Object = MibTableColumn
nbsSyslogServerIndex = _NbsSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 1),
    _NbsSyslogServerIndex_Type()
)
nbsSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSyslogServerIndex.setStatus("current")


class _NbsSyslogServerStatus_Type(Integer32):
    """Custom type nbsSyslogServerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("active", 2))
    )


_NbsSyslogServerStatus_Type.__name__ = "Integer32"
_NbsSyslogServerStatus_Object = MibTableColumn
nbsSyslogServerStatus = _NbsSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 2),
    _NbsSyslogServerStatus_Type()
)
nbsSyslogServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyslogServerStatus.setStatus("current")


class _NbsSyslogServerAddressType_Type(InetAddressType):
    """Custom type nbsSyslogServerAddressType based on InetAddressType"""
    defaultValue = 1


_NbsSyslogServerAddressType_Type.__name__ = "InetAddressType"
_NbsSyslogServerAddressType_Object = MibTableColumn
nbsSyslogServerAddressType = _NbsSyslogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 3),
    _NbsSyslogServerAddressType_Type()
)
nbsSyslogServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyslogServerAddressType.setStatus("current")
_NbsSyslogServerAddress_Type = InetAddress
_NbsSyslogServerAddress_Object = MibTableColumn
nbsSyslogServerAddress = _NbsSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 4),
    _NbsSyslogServerAddress_Type()
)
nbsSyslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyslogServerAddress.setStatus("current")


class _NbsSyslogServerPort_Type(Unsigned32):
    """Custom type nbsSyslogServerPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbsSyslogServerPort_Type.__name__ = "Unsigned32"
_NbsSyslogServerPort_Object = MibTableColumn
nbsSyslogServerPort = _NbsSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 5),
    _NbsSyslogServerPort_Type()
)
nbsSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyslogServerPort.setStatus("current")


class _NbsSyslogServerLevel_Type(Integer32):
    """Custom type nbsSyslogServerLevel based on Integer32"""
    defaultValue = 6

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("deprecated1", 1),
          ("emerg", 2),
          ("alert", 3),
          ("crit", 4),
          ("error", 5),
          ("warning", 6),
          ("notice", 7),
          ("info", 8),
          ("debug", 9))
    )


_NbsSyslogServerLevel_Type.__name__ = "Integer32"
_NbsSyslogServerLevel_Object = MibTableColumn
nbsSyslogServerLevel = _NbsSyslogServerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 6),
    _NbsSyslogServerLevel_Type()
)
nbsSyslogServerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSyslogServerLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SYSLOG-SERVER-MIB",
    **{"nbsSyslogServerMib": nbsSyslogServerMib,
       "nbsSyslogServerGrp": nbsSyslogServerGrp,
       "nbsSyslogServerTableSize": nbsSyslogServerTableSize,
       "nbsSyslogServerTable": nbsSyslogServerTable,
       "nbsSyslogServerEntry": nbsSyslogServerEntry,
       "nbsSyslogServerIndex": nbsSyslogServerIndex,
       "nbsSyslogServerStatus": nbsSyslogServerStatus,
       "nbsSyslogServerAddressType": nbsSyslogServerAddressType,
       "nbsSyslogServerAddress": nbsSyslogServerAddress,
       "nbsSyslogServerPort": nbsSyslogServerPort,
       "nbsSyslogServerLevel": nbsSyslogServerLevel}
)
