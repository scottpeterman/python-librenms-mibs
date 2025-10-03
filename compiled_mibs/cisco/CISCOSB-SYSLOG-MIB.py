# SNMP MIB module (CISCOSB-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:57 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82)
)
if mibBuilder.loadTexts:
    rlSyslog.setRevisions(
        ("2006-02-12 00:00",
         "2003-09-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSyslogSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7),
          ("notActive", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RlSyslogPrivate_ObjectIdentity = ObjectIdentity
rlSyslogPrivate = _RlSyslogPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2)
)


class _RlSyslogGlobalEnable_Type(TruthValue):
    """Custom type rlSyslogGlobalEnable based on TruthValue"""
    defaultValue = 1


_RlSyslogGlobalEnable_Type.__name__ = "TruthValue"
_RlSyslogGlobalEnable_Object = MibScalar
rlSyslogGlobalEnable = _RlSyslogGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 1),
    _RlSyslogGlobalEnable_Type()
)
rlSyslogGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogGlobalEnable.setStatus("current")


class _RlSyslogMinLogToConsoleSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToConsoleSeverity based on RlSyslogSeverity"""
    defaultValue = 6


_RlSyslogMinLogToConsoleSeverity_Type.__name__ = "RlSyslogSeverity"
_RlSyslogMinLogToConsoleSeverity_Object = MibScalar
rlSyslogMinLogToConsoleSeverity = _RlSyslogMinLogToConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 2),
    _RlSyslogMinLogToConsoleSeverity_Type()
)
rlSyslogMinLogToConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToConsoleSeverity.setStatus("current")


class _RlSyslogMinLogToFileSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToFileSeverity based on RlSyslogSeverity"""
    defaultValue = 3


_RlSyslogMinLogToFileSeverity_Type.__name__ = "RlSyslogSeverity"
_RlSyslogMinLogToFileSeverity_Object = MibScalar
rlSyslogMinLogToFileSeverity = _RlSyslogMinLogToFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 3),
    _RlSyslogMinLogToFileSeverity_Type()
)
rlSyslogMinLogToFileSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToFileSeverity.setStatus("current")


class _RlSyslogMinLogToCacheSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToCacheSeverity based on RlSyslogSeverity"""
    defaultValue = 6


_RlSyslogMinLogToCacheSeverity_Type.__name__ = "RlSyslogSeverity"
_RlSyslogMinLogToCacheSeverity_Object = MibScalar
rlSyslogMinLogToCacheSeverity = _RlSyslogMinLogToCacheSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 4),
    _RlSyslogMinLogToCacheSeverity_Type()
)
rlSyslogMinLogToCacheSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToCacheSeverity.setStatus("current")
_RlSyslogClearLogfile_Type = Unsigned32
_RlSyslogClearLogfile_Object = MibScalar
rlSyslogClearLogfile = _RlSyslogClearLogfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 5),
    _RlSyslogClearLogfile_Type()
)
rlSyslogClearLogfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogClearLogfile.setStatus("current")
_RlSyslogClearCache_Type = Unsigned32
_RlSyslogClearCache_Object = MibScalar
rlSyslogClearCache = _RlSyslogClearCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 6),
    _RlSyslogClearCache_Type()
)
rlSyslogClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogClearCache.setStatus("current")
_RlSyslogMibVersion_Type = Integer32
_RlSyslogMibVersion_Object = MibScalar
rlSyslogMibVersion = _RlSyslogMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 7),
    _RlSyslogMibVersion_Type()
)
rlSyslogMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogMibVersion.setStatus("current")
_RlSyslogLogTable_Object = MibTable
rlSyslogLogTable = _RlSyslogLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8)
)
if mibBuilder.loadTexts:
    rlSyslogLogTable.setStatus("current")
_RlSyslogLogEntry_Object = MibTableRow
rlSyslogLogEntry = _RlSyslogLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1)
)
rlSyslogLogEntry.setIndexNames(
    (0, "CISCOSB-SYSLOG-MIB", "rlSyslogLogCounter"),
)
if mibBuilder.loadTexts:
    rlSyslogLogEntry.setStatus("current")
_RlSyslogLogCounter_Type = Unsigned32
_RlSyslogLogCounter_Object = MibTableColumn
rlSyslogLogCounter = _RlSyslogLogCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 1),
    _RlSyslogLogCounter_Type()
)
rlSyslogLogCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCounter.setStatus("current")


class _RlSyslogLogDateTime_Type(DisplayString):
    """Custom type rlSyslogLogDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogDateTime_Type.__name__ = "DisplayString"
_RlSyslogLogDateTime_Object = MibTableColumn
rlSyslogLogDateTime = _RlSyslogLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 2),
    _RlSyslogLogDateTime_Type()
)
rlSyslogLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogDateTime.setStatus("current")


class _RlSyslogLogAppMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogAppMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSyslogLogAppMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogAppMnemonic_Object = MibTableColumn
rlSyslogLogAppMnemonic = _RlSyslogLogAppMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 3),
    _RlSyslogLogAppMnemonic_Type()
)
rlSyslogLogAppMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogAppMnemonic.setStatus("current")
_RlSyslogLogSeverity_Type = RlSyslogSeverity
_RlSyslogLogSeverity_Object = MibTableColumn
rlSyslogLogSeverity = _RlSyslogLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 4),
    _RlSyslogLogSeverity_Type()
)
rlSyslogLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogSeverity.setStatus("current")


class _RlSyslogLogMessageMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogMessageMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogMessageMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogMessageMnemonic_Object = MibTableColumn
rlSyslogLogMessageMnemonic = _RlSyslogLogMessageMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 5),
    _RlSyslogLogMessageMnemonic_Type()
)
rlSyslogLogMessageMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogMessageMnemonic.setStatus("current")


class _RlSyslogLogText1_Type(DisplayString):
    """Custom type rlSyslogLogText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText1_Type.__name__ = "DisplayString"
_RlSyslogLogText1_Object = MibTableColumn
rlSyslogLogText1 = _RlSyslogLogText1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 6),
    _RlSyslogLogText1_Type()
)
rlSyslogLogText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText1.setStatus("current")


class _RlSyslogLogText2_Type(DisplayString):
    """Custom type rlSyslogLogText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText2_Type.__name__ = "DisplayString"
_RlSyslogLogText2_Object = MibTableColumn
rlSyslogLogText2 = _RlSyslogLogText2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 7),
    _RlSyslogLogText2_Type()
)
rlSyslogLogText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText2.setStatus("current")


class _RlSyslogLogText3_Type(DisplayString):
    """Custom type rlSyslogLogText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText3_Type.__name__ = "DisplayString"
_RlSyslogLogText3_Object = MibTableColumn
rlSyslogLogText3 = _RlSyslogLogText3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 8),
    _RlSyslogLogText3_Type()
)
rlSyslogLogText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText3.setStatus("current")


class _RlSyslogLogText4_Type(DisplayString):
    """Custom type rlSyslogLogText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText4_Type.__name__ = "DisplayString"
_RlSyslogLogText4_Object = MibTableColumn
rlSyslogLogText4 = _RlSyslogLogText4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 9),
    _RlSyslogLogText4_Type()
)
rlSyslogLogText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText4.setStatus("current")
_RlSyslogLogCacheTable_Object = MibTable
rlSyslogLogCacheTable = _RlSyslogLogCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9)
)
if mibBuilder.loadTexts:
    rlSyslogLogCacheTable.setStatus("current")
_RlSyslogLogCacheEntry_Object = MibTableRow
rlSyslogLogCacheEntry = _RlSyslogLogCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1)
)
rlSyslogLogCacheEntry.setIndexNames(
    (0, "CISCOSB-SYSLOG-MIB", "rlSyslogLogCacheCounter"),
)
if mibBuilder.loadTexts:
    rlSyslogLogCacheEntry.setStatus("current")
_RlSyslogLogCacheCounter_Type = Unsigned32
_RlSyslogLogCacheCounter_Object = MibTableColumn
rlSyslogLogCacheCounter = _RlSyslogLogCacheCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 1),
    _RlSyslogLogCacheCounter_Type()
)
rlSyslogLogCacheCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheCounter.setStatus("current")


class _RlSyslogLogCacheDateTime_Type(DisplayString):
    """Custom type rlSyslogLogCacheDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogCacheDateTime_Type.__name__ = "DisplayString"
_RlSyslogLogCacheDateTime_Object = MibTableColumn
rlSyslogLogCacheDateTime = _RlSyslogLogCacheDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 2),
    _RlSyslogLogCacheDateTime_Type()
)
rlSyslogLogCacheDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheDateTime.setStatus("current")


class _RlSyslogLogCacheAppMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogCacheAppMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSyslogLogCacheAppMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogCacheAppMnemonic_Object = MibTableColumn
rlSyslogLogCacheAppMnemonic = _RlSyslogLogCacheAppMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 3),
    _RlSyslogLogCacheAppMnemonic_Type()
)
rlSyslogLogCacheAppMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheAppMnemonic.setStatus("current")
_RlSyslogLogCacheSeverity_Type = RlSyslogSeverity
_RlSyslogLogCacheSeverity_Object = MibTableColumn
rlSyslogLogCacheSeverity = _RlSyslogLogCacheSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 4),
    _RlSyslogLogCacheSeverity_Type()
)
rlSyslogLogCacheSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheSeverity.setStatus("current")


class _RlSyslogLogCacheMessageMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogCacheMessageMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogCacheMessageMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogCacheMessageMnemonic_Object = MibTableColumn
rlSyslogLogCacheMessageMnemonic = _RlSyslogLogCacheMessageMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 5),
    _RlSyslogLogCacheMessageMnemonic_Type()
)
rlSyslogLogCacheMessageMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheMessageMnemonic.setStatus("current")


class _RlSyslogLogCacheText1_Type(DisplayString):
    """Custom type rlSyslogLogCacheText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText1_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText1_Object = MibTableColumn
rlSyslogLogCacheText1 = _RlSyslogLogCacheText1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 6),
    _RlSyslogLogCacheText1_Type()
)
rlSyslogLogCacheText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText1.setStatus("current")


class _RlSyslogLogCacheText2_Type(DisplayString):
    """Custom type rlSyslogLogCacheText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText2_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText2_Object = MibTableColumn
rlSyslogLogCacheText2 = _RlSyslogLogCacheText2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 7),
    _RlSyslogLogCacheText2_Type()
)
rlSyslogLogCacheText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText2.setStatus("current")


class _RlSyslogLogCacheText3_Type(DisplayString):
    """Custom type rlSyslogLogCacheText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText3_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText3_Object = MibTableColumn
rlSyslogLogCacheText3 = _RlSyslogLogCacheText3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 8),
    _RlSyslogLogCacheText3_Type()
)
rlSyslogLogCacheText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText3.setStatus("current")


class _RlSyslogLogCacheText4_Type(DisplayString):
    """Custom type rlSyslogLogCacheText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText4_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText4_Object = MibTableColumn
rlSyslogLogCacheText4 = _RlSyslogLogCacheText4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 9),
    _RlSyslogLogCacheText4_Type()
)
rlSyslogLogCacheText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText4.setStatus("current")
_RlSyslogConsoleMessagesIgnored_Type = Counter32
_RlSyslogConsoleMessagesIgnored_Object = MibScalar
rlSyslogConsoleMessagesIgnored = _RlSyslogConsoleMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 10),
    _RlSyslogConsoleMessagesIgnored_Type()
)
rlSyslogConsoleMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogConsoleMessagesIgnored.setStatus("current")
_RlSyslogFileMessagesIgnored_Type = Counter32
_RlSyslogFileMessagesIgnored_Object = MibScalar
rlSyslogFileMessagesIgnored = _RlSyslogFileMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 11),
    _RlSyslogFileMessagesIgnored_Type()
)
rlSyslogFileMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogFileMessagesIgnored.setStatus("current")
_RlSyslogFileMessagesLogged_Type = Counter32
_RlSyslogFileMessagesLogged_Object = MibScalar
rlSyslogFileMessagesLogged = _RlSyslogFileMessagesLogged_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 12),
    _RlSyslogFileMessagesLogged_Type()
)
rlSyslogFileMessagesLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogFileMessagesLogged.setStatus("current")
_RlSyslogCacheTotalMessages_Type = Counter32
_RlSyslogCacheTotalMessages_Object = MibScalar
rlSyslogCacheTotalMessages = _RlSyslogCacheTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 13),
    _RlSyslogCacheTotalMessages_Type()
)
rlSyslogCacheTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCacheTotalMessages.setStatus("current")
_RlSyslogAggregationEnable_Type = TruthValue
_RlSyslogAggregationEnable_Object = MibScalar
rlSyslogAggregationEnable = _RlSyslogAggregationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 14),
    _RlSyslogAggregationEnable_Type()
)
rlSyslogAggregationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogAggregationEnable.setStatus("current")


class _RlSyslogAggregationAgingTime_Type(Unsigned32):
    """Custom type rlSyslogAggregationAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 3600),
    )


_RlSyslogAggregationAgingTime_Type.__name__ = "Unsigned32"
_RlSyslogAggregationAgingTime_Object = MibScalar
rlSyslogAggregationAgingTime = _RlSyslogAggregationAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 15),
    _RlSyslogAggregationAgingTime_Type()
)
rlSyslogAggregationAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogAggregationAgingTime.setStatus("current")


class _RlSyslogMinLogToWebSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToWebSeverity based on RlSyslogSeverity"""
    defaultValue = 6


_RlSyslogMinLogToWebSeverity_Type.__name__ = "RlSyslogSeverity"
_RlSyslogMinLogToWebSeverity_Object = MibScalar
rlSyslogMinLogToWebSeverity = _RlSyslogMinLogToWebSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 16),
    _RlSyslogMinLogToWebSeverity_Type()
)
rlSyslogMinLogToWebSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToWebSeverity.setStatus("current")


class _RlSyslogAlarmFlag_Type(TruthValue):
    """Custom type rlSyslogAlarmFlag based on TruthValue"""
    defaultValue = 2


_RlSyslogAlarmFlag_Type.__name__ = "TruthValue"
_RlSyslogAlarmFlag_Object = MibScalar
rlSyslogAlarmFlag = _RlSyslogAlarmFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 17),
    _RlSyslogAlarmFlag_Type()
)
rlSyslogAlarmFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogAlarmFlag.setStatus("current")


class _RlSyslogOriginId_Type(Integer32):
    """Custom type rlSyslogOriginId based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("hostname", 2),
          ("ip", 3),
          ("ipv6", 4),
          ("string", 5))
    )


_RlSyslogOriginId_Type.__name__ = "Integer32"
_RlSyslogOriginId_Object = MibScalar
rlSyslogOriginId = _RlSyslogOriginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 18),
    _RlSyslogOriginId_Type()
)
rlSyslogOriginId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogOriginId.setStatus("current")


class _RlSyslogOriginIdString_Type(DisplayString):
    """Custom type rlSyslogOriginIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogOriginIdString_Type.__name__ = "DisplayString"
_RlSyslogOriginIdString_Object = MibScalar
rlSyslogOriginIdString = _RlSyslogOriginIdString_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 19),
    _RlSyslogOriginIdString_Type()
)
rlSyslogOriginIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogOriginIdString.setStatus("current")


class _RlSyslogHeaderSendingEnabled_Type(TruthValue):
    """Custom type rlSyslogHeaderSendingEnabled based on TruthValue"""
    defaultValue = 1


_RlSyslogHeaderSendingEnabled_Type.__name__ = "TruthValue"
_RlSyslogHeaderSendingEnabled_Object = MibScalar
rlSyslogHeaderSendingEnabled = _RlSyslogHeaderSendingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 20),
    _RlSyslogHeaderSendingEnabled_Type()
)
rlSyslogHeaderSendingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogHeaderSendingEnabled.setStatus("current")
_RlSyslogCountersPerSeverityTable_Object = MibTable
rlSyslogCountersPerSeverityTable = _RlSyslogCountersPerSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21)
)
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityTable.setStatus("current")
_RlSyslogCountersPerSeverityEntry_Object = MibTableRow
rlSyslogCountersPerSeverityEntry = _RlSyslogCountersPerSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1)
)
rlSyslogCountersPerSeverityEntry.setIndexNames(
    (0, "CISCOSB-SYSLOG-MIB", "rlSyslogCountersPerSeverityIndex"),
)
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityEntry.setStatus("current")


class _RlSyslogCountersPerSeverityIndex_Type(Integer32):
    """Custom type rlSyslogCountersPerSeverityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlSyslogCountersPerSeverityIndex_Type.__name__ = "Integer32"
_RlSyslogCountersPerSeverityIndex_Object = MibTableColumn
rlSyslogCountersPerSeverityIndex = _RlSyslogCountersPerSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 1),
    _RlSyslogCountersPerSeverityIndex_Type()
)
rlSyslogCountersPerSeverityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityIndex.setStatus("current")
_RlSyslogCountersPerSeverityEmergencyCounter_Type = Counter32
_RlSyslogCountersPerSeverityEmergencyCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityEmergencyCounter = _RlSyslogCountersPerSeverityEmergencyCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 2),
    _RlSyslogCountersPerSeverityEmergencyCounter_Type()
)
rlSyslogCountersPerSeverityEmergencyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityEmergencyCounter.setStatus("current")
_RlSyslogCountersPerSeverityAlertCounter_Type = Counter32
_RlSyslogCountersPerSeverityAlertCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityAlertCounter = _RlSyslogCountersPerSeverityAlertCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 3),
    _RlSyslogCountersPerSeverityAlertCounter_Type()
)
rlSyslogCountersPerSeverityAlertCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityAlertCounter.setStatus("current")
_RlSyslogCountersPerSeverityCriticalCounter_Type = Counter32
_RlSyslogCountersPerSeverityCriticalCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityCriticalCounter = _RlSyslogCountersPerSeverityCriticalCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 4),
    _RlSyslogCountersPerSeverityCriticalCounter_Type()
)
rlSyslogCountersPerSeverityCriticalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityCriticalCounter.setStatus("current")
_RlSyslogCountersPerSeverityErrorCounter_Type = Counter32
_RlSyslogCountersPerSeverityErrorCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityErrorCounter = _RlSyslogCountersPerSeverityErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 5),
    _RlSyslogCountersPerSeverityErrorCounter_Type()
)
rlSyslogCountersPerSeverityErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityErrorCounter.setStatus("current")
_RlSyslogCountersPerSeverityWarningCounter_Type = Counter32
_RlSyslogCountersPerSeverityWarningCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityWarningCounter = _RlSyslogCountersPerSeverityWarningCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 6),
    _RlSyslogCountersPerSeverityWarningCounter_Type()
)
rlSyslogCountersPerSeverityWarningCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityWarningCounter.setStatus("current")
_RlSyslogCountersPerSeverityNoticeCounter_Type = Counter32
_RlSyslogCountersPerSeverityNoticeCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityNoticeCounter = _RlSyslogCountersPerSeverityNoticeCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 7),
    _RlSyslogCountersPerSeverityNoticeCounter_Type()
)
rlSyslogCountersPerSeverityNoticeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityNoticeCounter.setStatus("current")
_RlSyslogCountersPerSeverityInfoCounter_Type = Counter32
_RlSyslogCountersPerSeverityInfoCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityInfoCounter = _RlSyslogCountersPerSeverityInfoCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 8),
    _RlSyslogCountersPerSeverityInfoCounter_Type()
)
rlSyslogCountersPerSeverityInfoCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityInfoCounter.setStatus("current")
_RlSyslogCountersPerSeverityDebugCounter_Type = Counter32
_RlSyslogCountersPerSeverityDebugCounter_Object = MibTableColumn
rlSyslogCountersPerSeverityDebugCounter = _RlSyslogCountersPerSeverityDebugCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 21, 1, 9),
    _RlSyslogCountersPerSeverityDebugCounter_Type()
)
rlSyslogCountersPerSeverityDebugCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCountersPerSeverityDebugCounter.setStatus("current")
_RlsnmpSyslogCollectorTable_Object = MibTable
rlsnmpSyslogCollectorTable = _RlsnmpSyslogCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 22)
)
if mibBuilder.loadTexts:
    rlsnmpSyslogCollectorTable.setStatus("current")
_RlsnmpSyslogCollectorEntry_Object = MibTableRow
rlsnmpSyslogCollectorEntry = _RlsnmpSyslogCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 22, 1)
)
rlsnmpSyslogCollectorEntry.setIndexNames(
    (0, "CISCOSB-SYSLOG-MIB", "rlsnmpSyslogCollectorIndex"),
)
if mibBuilder.loadTexts:
    rlsnmpSyslogCollectorEntry.setStatus("current")


class _RlsnmpSyslogCollectorIndex_Type(Unsigned32):
    """Custom type rlsnmpSyslogCollectorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlsnmpSyslogCollectorIndex_Type.__name__ = "Unsigned32"
_RlsnmpSyslogCollectorIndex_Object = MibTableColumn
rlsnmpSyslogCollectorIndex = _RlsnmpSyslogCollectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 22, 1, 1),
    _RlsnmpSyslogCollectorIndex_Type()
)
rlsnmpSyslogCollectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlsnmpSyslogCollectorIndex.setStatus("current")
_RlsnmpSyslogCollectorAddressType_Type = InetAddressType
_RlsnmpSyslogCollectorAddressType_Object = MibTableColumn
rlsnmpSyslogCollectorAddressType = _RlsnmpSyslogCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 22, 1, 2),
    _RlsnmpSyslogCollectorAddressType_Type()
)
rlsnmpSyslogCollectorAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlsnmpSyslogCollectorAddressType.setStatus("current")
_RlsnmpSyslogCollectorAddress_Type = InetAddress
_RlsnmpSyslogCollectorAddress_Object = MibTableColumn
rlsnmpSyslogCollectorAddress = _RlsnmpSyslogCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 22, 1, 3),
    _RlsnmpSyslogCollectorAddress_Type()
)
rlsnmpSyslogCollectorAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlsnmpSyslogCollectorAddress.setStatus("current")
_RlsnmpSyslogCollectorRowStatus_Type = RowStatus
_RlsnmpSyslogCollectorRowStatus_Object = MibTableColumn
rlsnmpSyslogCollectorRowStatus = _RlsnmpSyslogCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 22, 1, 4),
    _RlsnmpSyslogCollectorRowStatus_Type()
)
rlsnmpSyslogCollectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlsnmpSyslogCollectorRowStatus.setStatus("current")
_RlSyslogLastIndexPerSeverityTable_Object = MibTable
rlSyslogLastIndexPerSeverityTable = _RlSyslogLastIndexPerSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23)
)
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityTable.setStatus("current")
_RlSyslogLastIndexPerSeverityEntry_Object = MibTableRow
rlSyslogLastIndexPerSeverityEntry = _RlSyslogLastIndexPerSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1)
)
rlSyslogLastIndexPerSeverityEntry.setIndexNames(
    (0, "CISCOSB-SYSLOG-MIB", "rlSyslogLastIndexPerSeverityIndex"),
)
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityEntry.setStatus("current")


class _RlSyslogLastIndexPerSeverityIndex_Type(Integer32):
    """Custom type rlSyslogLastIndexPerSeverityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlSyslogLastIndexPerSeverityIndex_Type.__name__ = "Integer32"
_RlSyslogLastIndexPerSeverityIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityIndex = _RlSyslogLastIndexPerSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 1),
    _RlSyslogLastIndexPerSeverityIndex_Type()
)
rlSyslogLastIndexPerSeverityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityEmergencyIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityEmergencyIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityEmergencyIndex = _RlSyslogLastIndexPerSeverityEmergencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 2),
    _RlSyslogLastIndexPerSeverityEmergencyIndex_Type()
)
rlSyslogLastIndexPerSeverityEmergencyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityEmergencyIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityAlertIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityAlertIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityAlertIndex = _RlSyslogLastIndexPerSeverityAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 3),
    _RlSyslogLastIndexPerSeverityAlertIndex_Type()
)
rlSyslogLastIndexPerSeverityAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityAlertIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityCriticalIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityCriticalIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityCriticalIndex = _RlSyslogLastIndexPerSeverityCriticalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 4),
    _RlSyslogLastIndexPerSeverityCriticalIndex_Type()
)
rlSyslogLastIndexPerSeverityCriticalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityCriticalIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityErrorIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityErrorIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityErrorIndex = _RlSyslogLastIndexPerSeverityErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 5),
    _RlSyslogLastIndexPerSeverityErrorIndex_Type()
)
rlSyslogLastIndexPerSeverityErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityErrorIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityWarningIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityWarningIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityWarningIndex = _RlSyslogLastIndexPerSeverityWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 6),
    _RlSyslogLastIndexPerSeverityWarningIndex_Type()
)
rlSyslogLastIndexPerSeverityWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityWarningIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityNoticeIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityNoticeIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityNoticeIndex = _RlSyslogLastIndexPerSeverityNoticeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 7),
    _RlSyslogLastIndexPerSeverityNoticeIndex_Type()
)
rlSyslogLastIndexPerSeverityNoticeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityNoticeIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityInfoIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityInfoIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityInfoIndex = _RlSyslogLastIndexPerSeverityInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 8),
    _RlSyslogLastIndexPerSeverityInfoIndex_Type()
)
rlSyslogLastIndexPerSeverityInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityInfoIndex.setStatus("current")
_RlSyslogLastIndexPerSeverityDebugIndex_Type = Counter32
_RlSyslogLastIndexPerSeverityDebugIndex_Object = MibTableColumn
rlSyslogLastIndexPerSeverityDebugIndex = _RlSyslogLastIndexPerSeverityDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 23, 1, 9),
    _RlSyslogLastIndexPerSeverityDebugIndex_Type()
)
rlSyslogLastIndexPerSeverityDebugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLastIndexPerSeverityDebugIndex.setStatus("current")


class _RlSyslogFindItLogLevel_Type(Integer32):
    """Custom type rlSyslogFindItLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("info", 0),
          ("debug", 1),
          ("warning", 2),
          ("error", 3))
    )


_RlSyslogFindItLogLevel_Type.__name__ = "Integer32"
_RlSyslogFindItLogLevel_Object = MibScalar
rlSyslogFindItLogLevel = _RlSyslogFindItLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 24),
    _RlSyslogFindItLogLevel_Type()
)
rlSyslogFindItLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogFindItLogLevel.setStatus("current")
_RlSyslogFindItLogModule_Type = Unsigned32
_RlSyslogFindItLogModule_Object = MibScalar
rlSyslogFindItLogModule = _RlSyslogFindItLogModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 25),
    _RlSyslogFindItLogModule_Type()
)
rlSyslogFindItLogModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogFindItLogModule.setStatus("current")
_RlSyslogUnexpectedRestartTable_Object = MibTable
rlSyslogUnexpectedRestartTable = _RlSyslogUnexpectedRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26)
)
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartTable.setStatus("current")
_RlSyslogUnexpectedRestartEntry_Object = MibTableRow
rlSyslogUnexpectedRestartEntry = _RlSyslogUnexpectedRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1)
)
rlSyslogUnexpectedRestartEntry.setIndexNames(
    (0, "CISCOSB-SYSLOG-MIB", "rlSyslogUnexpectedRestartCounter"),
)
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartEntry.setStatus("current")
_RlSyslogUnexpectedRestartCounter_Type = Unsigned32
_RlSyslogUnexpectedRestartCounter_Object = MibTableColumn
rlSyslogUnexpectedRestartCounter = _RlSyslogUnexpectedRestartCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 1),
    _RlSyslogUnexpectedRestartCounter_Type()
)
rlSyslogUnexpectedRestartCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartCounter.setStatus("current")


class _RlSyslogUnexpectedRestartDateTime_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogUnexpectedRestartDateTime_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartDateTime_Object = MibTableColumn
rlSyslogUnexpectedRestartDateTime = _RlSyslogUnexpectedRestartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 2),
    _RlSyslogUnexpectedRestartDateTime_Type()
)
rlSyslogUnexpectedRestartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartDateTime.setStatus("current")


class _RlSyslogUnexpectedRestartAppMnemonic_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartAppMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSyslogUnexpectedRestartAppMnemonic_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartAppMnemonic_Object = MibTableColumn
rlSyslogUnexpectedRestartAppMnemonic = _RlSyslogUnexpectedRestartAppMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 3),
    _RlSyslogUnexpectedRestartAppMnemonic_Type()
)
rlSyslogUnexpectedRestartAppMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartAppMnemonic.setStatus("current")
_RlSyslogUnexpectedRestartSeverity_Type = RlSyslogSeverity
_RlSyslogUnexpectedRestartSeverity_Object = MibTableColumn
rlSyslogUnexpectedRestartSeverity = _RlSyslogUnexpectedRestartSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 4),
    _RlSyslogUnexpectedRestartSeverity_Type()
)
rlSyslogUnexpectedRestartSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartSeverity.setStatus("current")


class _RlSyslogUnexpectedRestartMessageMnemonic_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartMessageMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogUnexpectedRestartMessageMnemonic_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartMessageMnemonic_Object = MibTableColumn
rlSyslogUnexpectedRestartMessageMnemonic = _RlSyslogUnexpectedRestartMessageMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 5),
    _RlSyslogUnexpectedRestartMessageMnemonic_Type()
)
rlSyslogUnexpectedRestartMessageMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartMessageMnemonic.setStatus("current")


class _RlSyslogUnexpectedRestartText1_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogUnexpectedRestartText1_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartText1_Object = MibTableColumn
rlSyslogUnexpectedRestartText1 = _RlSyslogUnexpectedRestartText1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 6),
    _RlSyslogUnexpectedRestartText1_Type()
)
rlSyslogUnexpectedRestartText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartText1.setStatus("current")


class _RlSyslogUnexpectedRestartText2_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogUnexpectedRestartText2_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartText2_Object = MibTableColumn
rlSyslogUnexpectedRestartText2 = _RlSyslogUnexpectedRestartText2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 7),
    _RlSyslogUnexpectedRestartText2_Type()
)
rlSyslogUnexpectedRestartText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartText2.setStatus("current")


class _RlSyslogUnexpectedRestartText3_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogUnexpectedRestartText3_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartText3_Object = MibTableColumn
rlSyslogUnexpectedRestartText3 = _RlSyslogUnexpectedRestartText3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 8),
    _RlSyslogUnexpectedRestartText3_Type()
)
rlSyslogUnexpectedRestartText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartText3.setStatus("current")


class _RlSyslogUnexpectedRestartText4_Type(DisplayString):
    """Custom type rlSyslogUnexpectedRestartText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogUnexpectedRestartText4_Type.__name__ = "DisplayString"
_RlSyslogUnexpectedRestartText4_Object = MibTableColumn
rlSyslogUnexpectedRestartText4 = _RlSyslogUnexpectedRestartText4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 26, 1, 9),
    _RlSyslogUnexpectedRestartText4_Type()
)
rlSyslogUnexpectedRestartText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartText4.setStatus("current")


class _RlSyslogUnexpectedRestartOccured_Type(TruthValue):
    """Custom type rlSyslogUnexpectedRestartOccured based on TruthValue"""
    defaultValue = 2


_RlSyslogUnexpectedRestartOccured_Type.__name__ = "TruthValue"
_RlSyslogUnexpectedRestartOccured_Object = MibScalar
rlSyslogUnexpectedRestartOccured = _RlSyslogUnexpectedRestartOccured_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 27),
    _RlSyslogUnexpectedRestartOccured_Type()
)
rlSyslogUnexpectedRestartOccured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartOccured.setStatus("current")
_RlSyslogUnexpectedRestartClear_Type = TruthValue
_RlSyslogUnexpectedRestartClear_Object = MibScalar
rlSyslogUnexpectedRestartClear = _RlSyslogUnexpectedRestartClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 28),
    _RlSyslogUnexpectedRestartClear_Type()
)
rlSyslogUnexpectedRestartClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogUnexpectedRestartClear.setStatus("current")
_RlSyslogPhaseOneTests_ObjectIdentity = ObjectIdentity
rlSyslogPhaseOneTests = _RlSyslogPhaseOneTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 3)
)


class _RlSyslogPhaseOneTestGenerator_Type(Integer32):
    """Custom type rlSyslogPhaseOneTestGenerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              14,
              15,
              16,
              17,
              21,
              22,
              23,
              24,
              25,
              31,
              32,
              33,
              34,
              35,
              36,
              41,
              42,
              43,
              47,
              62)
        )
    )
    namedValues = NamedValues(
        *(("successfulRegistration", 11),
          ("regTheSameComponentTwice", 12),
          ("regWithInvalidComponentID", 13),
          ("regWithInvalidApplicationID", 14),
          ("regWithInvalidMessageString", 15),
          ("regWithInvalidMessageList", 16),
          ("regWithInvalidApplicationList", 17),
          ("successfulLoggingWithNoParams", 21),
          ("logWithUnregisteredComponentID", 22),
          ("logWithInvalidComponentID", 23),
          ("logWithBadApplicationID", 24),
          ("logWithBadMessageID", 25),
          ("paramFormatting", 31),
          ("insufficientParams", 32),
          ("incorrectParams", 33),
          ("tooManyParams", 34),
          ("oversizedParams", 35),
          ("trapParams", 36),
          ("successfulFatalError", 41),
          ("fatalErrorThroughNonFatalInterface", 42),
          ("nonFatalErrorThroughFatalInterface", 43),
          ("nestedFatalErrors", 47),
          ("snmpAccessToLongMessage", 62))
    )


_RlSyslogPhaseOneTestGenerator_Type.__name__ = "Integer32"
_RlSyslogPhaseOneTestGenerator_Object = MibScalar
rlSyslogPhaseOneTestGenerator = _RlSyslogPhaseOneTestGenerator_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 3, 1),
    _RlSyslogPhaseOneTestGenerator_Type()
)
rlSyslogPhaseOneTestGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogPhaseOneTestGenerator.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SYSLOG-MIB",
    **{"RlSyslogSeverity": RlSyslogSeverity,
       "rlSyslog": rlSyslog,
       "rlSyslogPrivate": rlSyslogPrivate,
       "rlSyslogGlobalEnable": rlSyslogGlobalEnable,
       "rlSyslogMinLogToConsoleSeverity": rlSyslogMinLogToConsoleSeverity,
       "rlSyslogMinLogToFileSeverity": rlSyslogMinLogToFileSeverity,
       "rlSyslogMinLogToCacheSeverity": rlSyslogMinLogToCacheSeverity,
       "rlSyslogClearLogfile": rlSyslogClearLogfile,
       "rlSyslogClearCache": rlSyslogClearCache,
       "rlSyslogMibVersion": rlSyslogMibVersion,
       "rlSyslogLogTable": rlSyslogLogTable,
       "rlSyslogLogEntry": rlSyslogLogEntry,
       "rlSyslogLogCounter": rlSyslogLogCounter,
       "rlSyslogLogDateTime": rlSyslogLogDateTime,
       "rlSyslogLogAppMnemonic": rlSyslogLogAppMnemonic,
       "rlSyslogLogSeverity": rlSyslogLogSeverity,
       "rlSyslogLogMessageMnemonic": rlSyslogLogMessageMnemonic,
       "rlSyslogLogText1": rlSyslogLogText1,
       "rlSyslogLogText2": rlSyslogLogText2,
       "rlSyslogLogText3": rlSyslogLogText3,
       "rlSyslogLogText4": rlSyslogLogText4,
       "rlSyslogLogCacheTable": rlSyslogLogCacheTable,
       "rlSyslogLogCacheEntry": rlSyslogLogCacheEntry,
       "rlSyslogLogCacheCounter": rlSyslogLogCacheCounter,
       "rlSyslogLogCacheDateTime": rlSyslogLogCacheDateTime,
       "rlSyslogLogCacheAppMnemonic": rlSyslogLogCacheAppMnemonic,
       "rlSyslogLogCacheSeverity": rlSyslogLogCacheSeverity,
       "rlSyslogLogCacheMessageMnemonic": rlSyslogLogCacheMessageMnemonic,
       "rlSyslogLogCacheText1": rlSyslogLogCacheText1,
       "rlSyslogLogCacheText2": rlSyslogLogCacheText2,
       "rlSyslogLogCacheText3": rlSyslogLogCacheText3,
       "rlSyslogLogCacheText4": rlSyslogLogCacheText4,
       "rlSyslogConsoleMessagesIgnored": rlSyslogConsoleMessagesIgnored,
       "rlSyslogFileMessagesIgnored": rlSyslogFileMessagesIgnored,
       "rlSyslogFileMessagesLogged": rlSyslogFileMessagesLogged,
       "rlSyslogCacheTotalMessages": rlSyslogCacheTotalMessages,
       "rlSyslogAggregationEnable": rlSyslogAggregationEnable,
       "rlSyslogAggregationAgingTime": rlSyslogAggregationAgingTime,
       "rlSyslogMinLogToWebSeverity": rlSyslogMinLogToWebSeverity,
       "rlSyslogAlarmFlag": rlSyslogAlarmFlag,
       "rlSyslogOriginId": rlSyslogOriginId,
       "rlSyslogOriginIdString": rlSyslogOriginIdString,
       "rlSyslogHeaderSendingEnabled": rlSyslogHeaderSendingEnabled,
       "rlSyslogCountersPerSeverityTable": rlSyslogCountersPerSeverityTable,
       "rlSyslogCountersPerSeverityEntry": rlSyslogCountersPerSeverityEntry,
       "rlSyslogCountersPerSeverityIndex": rlSyslogCountersPerSeverityIndex,
       "rlSyslogCountersPerSeverityEmergencyCounter": rlSyslogCountersPerSeverityEmergencyCounter,
       "rlSyslogCountersPerSeverityAlertCounter": rlSyslogCountersPerSeverityAlertCounter,
       "rlSyslogCountersPerSeverityCriticalCounter": rlSyslogCountersPerSeverityCriticalCounter,
       "rlSyslogCountersPerSeverityErrorCounter": rlSyslogCountersPerSeverityErrorCounter,
       "rlSyslogCountersPerSeverityWarningCounter": rlSyslogCountersPerSeverityWarningCounter,
       "rlSyslogCountersPerSeverityNoticeCounter": rlSyslogCountersPerSeverityNoticeCounter,
       "rlSyslogCountersPerSeverityInfoCounter": rlSyslogCountersPerSeverityInfoCounter,
       "rlSyslogCountersPerSeverityDebugCounter": rlSyslogCountersPerSeverityDebugCounter,
       "rlsnmpSyslogCollectorTable": rlsnmpSyslogCollectorTable,
       "rlsnmpSyslogCollectorEntry": rlsnmpSyslogCollectorEntry,
       "rlsnmpSyslogCollectorIndex": rlsnmpSyslogCollectorIndex,
       "rlsnmpSyslogCollectorAddressType": rlsnmpSyslogCollectorAddressType,
       "rlsnmpSyslogCollectorAddress": rlsnmpSyslogCollectorAddress,
       "rlsnmpSyslogCollectorRowStatus": rlsnmpSyslogCollectorRowStatus,
       "rlSyslogLastIndexPerSeverityTable": rlSyslogLastIndexPerSeverityTable,
       "rlSyslogLastIndexPerSeverityEntry": rlSyslogLastIndexPerSeverityEntry,
       "rlSyslogLastIndexPerSeverityIndex": rlSyslogLastIndexPerSeverityIndex,
       "rlSyslogLastIndexPerSeverityEmergencyIndex": rlSyslogLastIndexPerSeverityEmergencyIndex,
       "rlSyslogLastIndexPerSeverityAlertIndex": rlSyslogLastIndexPerSeverityAlertIndex,
       "rlSyslogLastIndexPerSeverityCriticalIndex": rlSyslogLastIndexPerSeverityCriticalIndex,
       "rlSyslogLastIndexPerSeverityErrorIndex": rlSyslogLastIndexPerSeverityErrorIndex,
       "rlSyslogLastIndexPerSeverityWarningIndex": rlSyslogLastIndexPerSeverityWarningIndex,
       "rlSyslogLastIndexPerSeverityNoticeIndex": rlSyslogLastIndexPerSeverityNoticeIndex,
       "rlSyslogLastIndexPerSeverityInfoIndex": rlSyslogLastIndexPerSeverityInfoIndex,
       "rlSyslogLastIndexPerSeverityDebugIndex": rlSyslogLastIndexPerSeverityDebugIndex,
       "rlSyslogFindItLogLevel": rlSyslogFindItLogLevel,
       "rlSyslogFindItLogModule": rlSyslogFindItLogModule,
       "rlSyslogUnexpectedRestartTable": rlSyslogUnexpectedRestartTable,
       "rlSyslogUnexpectedRestartEntry": rlSyslogUnexpectedRestartEntry,
       "rlSyslogUnexpectedRestartCounter": rlSyslogUnexpectedRestartCounter,
       "rlSyslogUnexpectedRestartDateTime": rlSyslogUnexpectedRestartDateTime,
       "rlSyslogUnexpectedRestartAppMnemonic": rlSyslogUnexpectedRestartAppMnemonic,
       "rlSyslogUnexpectedRestartSeverity": rlSyslogUnexpectedRestartSeverity,
       "rlSyslogUnexpectedRestartMessageMnemonic": rlSyslogUnexpectedRestartMessageMnemonic,
       "rlSyslogUnexpectedRestartText1": rlSyslogUnexpectedRestartText1,
       "rlSyslogUnexpectedRestartText2": rlSyslogUnexpectedRestartText2,
       "rlSyslogUnexpectedRestartText3": rlSyslogUnexpectedRestartText3,
       "rlSyslogUnexpectedRestartText4": rlSyslogUnexpectedRestartText4,
       "rlSyslogUnexpectedRestartOccured": rlSyslogUnexpectedRestartOccured,
       "rlSyslogUnexpectedRestartClear": rlSyslogUnexpectedRestartClear,
       "rlSyslogPhaseOneTests": rlSyslogPhaseOneTests,
       "rlSyslogPhaseOneTestGenerator": rlSyslogPhaseOneTestGenerator}
)
